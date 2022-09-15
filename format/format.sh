#!/usr/bin/env bash
# TODO:
# - should this program be written in a different language?
# - if bash, we could reuse https://github.com/github/super-linter/blob/main/lib/functions/worker.sh
# - can we detect what version control system is used? (start with git)

if [[ -z "$BUILD_WORKSPACE_DIRECTORY" ]]; then
  echo >&2 "$0: FATAL: This program must be executed under 'bazel run'"
  exit 1
fi

function on_exit {
  code=$?
  if [[ $code != 0 ]]; then
    echo >&2 "FAILED: A formatter tool exited with code $code"
    echo >&2 "Try running 'bazel run @aspect_rules_format//format' to fix this."
  fi
}

trap on_exit EXIT

mode=fix
if [ "$1" == "--mode" ]; then
  readonly mode=$2
  shift 2
fi

# --- begin runfiles.bash initialization v2 ---
# Copy-pasted from the Bazel Bash runfiles library v2:
# https://github.com/bazelbuild/bazel/blob/master/tools/bash/runfiles/runfiles.bash
set -o nounset -o pipefail
f=bazel_tools/tools/bash/runfiles/runfiles.bash
source "${RUNFILES_DIR:-/dev/null}/$f" 2> /dev/null \
  || source "$(grep -sm1 "^$f " "${RUNFILES_MANIFEST_FILE:-/dev/null}" | cut -f2- -d' ')" 2> /dev/null \
  || source "$0.runfiles/$f" 2> /dev/null \
  || source "$(grep -sm1 "^$f " "$0.runfiles_manifest" | cut -f2- -d' ')" 2> /dev/null \
  || source "$(grep -sm1 "^$f " "$0.exe.runfiles_manifest" | cut -f2- -d' ')" 2> /dev/null \
  || {
    echo >&2 "ERROR: cannot find $f"
    exit 1
  }
f=
set -o errexit
# --- end runfiles.bash initialization v2 ---

cd $BUILD_WORKSPACE_DIRECTORY

# NOTE: we need to honor .gitignore, so we use git ls-files below
# TODO: talk to version control to determine which staged changes we should format
# TODO: avoid formatting unstaged changes
# TODO: try to format only regions where supported
# TODO: run them concurrently, not serial

case "$mode" in
 check)
   swiftmode="--lint"
   prettiermode="--check"
   blackmode="--check"
   javamode="--set-exit-if-changed --dry-run"
   ;;
 fix)
   swiftmode=""
   prettiermode="--write"
   blackmode=""
   javamode="--replace"
   ;;
 *) echo >&2 "unknown mode $mode";;
esac

if [ "$#" -eq 0 ]; then
  files=$(git ls-files '*/BUILD.bazel' '*.bzl' '*.BUILD' 'WORKSPACE' '*.bazel')
else
  files=$(find "$@" -name '*/BUILD.bazel' -or -name '*.bzl' -or -name '*.BUILD' -or -name 'WORKSPACE' -or -name '*.bazel')
fi
bin=$(rlocation buildifier_prebuilt/buildifier/buildifier)
if [ -n "$files" ] && [ -n "$bin" ]; then
  echo "Running Buildifier..."
  echo $files | xargs $bin -mode="$mode"
fi

if [ "$#" -eq 0 ]; then
  files=$(git ls-files '*.js' '*.sh' '*.ts' '*.tsx' '*.json' '*.css' '*.html' '*.md' '*.yaml' '*.yml')
else
  files=$(find "$@" -name '*.js' -or -name '*.sh' -or -name '*.ts' -or -name '*.tsx' -or -name '*.json' -or -name '*.css' -or -name '*.html' -or -name '*.md' -or -name '*.yaml' -or -name '*.yml')
fi
bin=$(rlocation aspect_rules_format/format/prettier.sh)
if [ -n "$files" ] && [ -n "$bin" ]; then
  echo "Running Prettier..."
  echo $files | xargs $bin $prettiermode
fi

if [ "$#" -eq 0 ]; then
  files=$(git ls-files '*.py' '*.pyi')
else
  files=$(find "$@" -name '*.py' -or -name '*.pyi')
fi
bin=$(rlocation aspect_rules_format_pypi_black/rules_python_wheel_entry_point_black)
if [ -n "$files" ] && [ -n "$bin" ]; then
  echo "Running black..."
  echo $files | xargs $bin $blackmode
fi

if [ "$#" -eq 0 ]; then
  files=$(git ls-files '*.java')
else
  files=$(find "$@" -name '*.java')
fi
bin=$(rlocation aspect_rules_format/format/java-format)
if [ -n "$files" ] && [ -n "$bin" ]; then
  echo "Running java-format..."
  # Setting JAVA_RUNFILES to work around https://github.com/bazelbuild/bazel/issues/12348
  echo $files | JAVA_RUNFILES="${RUNFILES_MANIFEST_FILE%_manifest}" xargs $bin $javamode
fi

# TODO: don't hardcode "linux"
if [ "$#" -eq 0 ]; then
  files=$(git ls-files '*.swift')
else
  files=$(find "$@" -name '*.swift')
fi
if [[ $OSTYPE == 'darwin'* ]]; then
  bin=$(rlocation swiftformat_mac/swiftformat)
else
  bin=$(rlocation swiftformat/swiftformat_linux)
fi

if [ -n "$files" ] && [ -n "$bin" ]; then
  # swiftformat itself prints Running SwiftFormat...
  echo $files | xargs $bin $swiftmode
fi
