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
   gofmtmode="-l"
   bufmode="format -d --exit-code"
   tfmode="-check -diff"
   jsonnetmode="--test"
   ;;
 fix)
   swiftmode=""
   prettiermode="--write"
   blackmode=""
   javamode="--replace"
   gofmtmode="-w"
   bufmode="format -w"
   tfmode=""
   jsonnetmode="--in-place"
   ;;
 *) echo >&2 "unknown mode $mode";;
esac

if [ "$#" -eq 0 ]; then
  files=$(git ls-files 'BUILD' '*/BUILD.bazel' '*.bzl' '*.BUILD' 'WORKSPACE' '*.bazel')
else
  files=$(find "$@" -name 'BUILD' -or -name '*.bzl' -or -name '*.BUILD' -or -name 'WORKSPACE' -or -name '*.bazel')
fi
bin=$(rlocation buildifier_prebuilt/buildifier/buildifier)
if [ -n "$files" ] && [ -n "$bin" ]; then
  echo "Running Buildifier..."
  echo "$files" | tr \\n \\0 | xargs -0 $bin -mode="$mode"
fi

if [ "$#" -eq 0 ]; then
  files=$(git ls-files '*.js' '*.cjs' '*.mjs' '*.sh' '*.ts' '*.tsx' '*.mts' '*.cts' '*.json' '*.css' '*.html' '*.md' '*.sql')
else
  files=$(find "$@" -name '*.js' -or -name '*.cjs' -or -name '*.mjs' -or -name '*.sh' -or -name '*.ts' -or -name '*.tsx' -or -name '*.mts' -or -name '*.cts' -or -name '*.json' -or -name '*.css' -or -name '*.html' -or -name '*.md' -or -name '*.sql')
fi
bin=$(rlocation aspect_rules_format/format/prettier.sh)
if [ -n "$files" ] && [ -n "$bin" ]; then
  echo "Running Prettier..."
  echo "$files" | tr \\n \\0 | xargs -0 $bin $prettiermode
fi

if [ "$#" -eq 0 ]; then
  files=$(git ls-files '*.py' '*.pyi')
else
  files=$(find "$@" -name '*.py' -or -name '*.pyi')
fi
bin=$(rlocation aspect_rules_format_pypi_black/rules_python_wheel_entry_point_black)
if [ -n "$files" ] && [ -n "$bin" ]; then
  echo "Running black..."
  echo "$files" | tr \\n \\0 | xargs -0 $bin $blackmode
fi

if [ "$#" -eq 0 ]; then
  files=$(git ls-files '*.tf')
else
  files=$(find "$@" -name '*.tf')
fi
if [[ $OSTYPE == 'darwin'* ]]; then
  if [[ $(uname -p) == 'arm' ]]; then
    bin=$(rlocation terraform_macos_aarch64/terraform)
  else
    bin=$(rlocation terraform_macos_x86_64/terraform)
  fi
else
  bin=$(rlocation terraform_linux_x86_64/terraform)
fi
if [ -n "$files" ] && [ -n "$bin" ]; then
  echo "Running terraform..."
  echo "$files" | tr \\n \\0 | xargs -0 $bin fmt $tfmode
fi

if [ "$#" -eq 0 ]; then
  files=$(git ls-files '*.jsonnet' '*.libsonnet')
else
  files=$(find "$@" -name '*.jsonnet' -or -name '*.libsonnet')
fi
if [[ $OSTYPE == 'darwin'* ]]; then
  if [[ $(uname -p) == 'arm' ]]; then
    bin=$(rlocation jsonnet_macos_aarch64/jsonnetfmt)
  else
    bin=$(rlocation jsonnet_macos_x86_64/jsonnetfmt)
  fi
else
  if [[ $(uname -p) == 'arm' ]]; then
      bin=$(rlocation jsonnet_linux_aarch64/jsonnetfmt)
  else
      bin=$(rlocation jsonnet_linux_x86_64/jsonnetfmt)
  fi
fi
if [ -n "$files" ] && [ -n "$bin" ]; then
  echo "Running jsonnetfmt..."
  echo "$files" | tr \\n \\0 | xargs -0 $bin $jsonnetmode
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
  echo "$files" | tr \\n \\0 | JAVA_RUNFILES="${RUNFILES_MANIFEST_FILE%_manifest}" xargs -0 $bin $javamode
fi

if [ "$#" -eq 0 ]; then
  files=$(git ls-files '*.go')
else
  files=$(find "$@" -name '*.go')
fi
bin=$(rlocation go_sdk/bin/gofmt)
if [ -n "$files" ] && [ -n "$bin" ]; then
  echo "Running gofmt..."
  # gofmt doesn't produce non-zero exit code so we must check for non-empty output
  # https://github.com/golang/go/issues/24230
  if [ "$mode" == "check" ]; then
    NEED_FMT=$(echo "$files" | tr \\n \\0 | xargs -0 $bin $gofmtmode)
    if [ -n "$NEED_FMT" ]; then
       echo "Go files not formatted:"
       echo "$NEED_FMT"
       exit 1
    fi
  else
    echo "$files" | tr \\n \\0 | xargs -0 $bin $gofmtmode
  fi
fi

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
  echo "$files" | tr \\n \\0 | xargs -0 $bin $swiftmode
fi

if [ "$#" -eq 0 ]; then
  files=$(git ls-files '*.proto')
else
  files=$(find "$@" -name '*.proto')
fi
if [[ $OSTYPE == 'darwin'* ]]; then
  bin=$(rlocation buf_mac/bin/buf)
else
  bin=$(rlocation buf/bin/buf)
fi

if [ -n "$files" ] && [ -n "$bin" ]; then
  echo "Running buf..."
  for file in $files; do
    $bin $bufmode $file
  done
fi
