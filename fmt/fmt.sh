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
    echo >&2 "Try running 'bazel run @aspect_rules_fmt//fmt' to fix this."
  fi
}

trap on_exit EXIT

readonly mode="${1:-fix}"

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

files=$(git ls-files '*/BUILD.bazel' '*.bzl' '*.BUILD' 'WORKSPACE' '*.bazel')
bin=$(rlocation buildifier_prebuilt/buildifier/buildifier)
[ -n "$files" ] && [ -n "$bin" ] && {
  echo "Running Buildifier..."
  echo $files | xargs $bin -mode="$mode"
}

files=$(git ls-files '*.js' '*.sh' '*.ts' '*.tsx' '*.json' '*.css' '*.html' '*.md' '*.yaml' '*.yml')
bin=$(rlocation aspect_rules_fmt/fmt/prettier.sh)
[ -n "$files" ] && [ -n "$bin" ] && {
  echo "Running Prettier..."
  echo $files | xargs $bin $prettiermode
}

files=$(git ls-files '*.py' '*.pyi')
bin=$(rlocation aspect_rules_fmt_pypi_black/rules_python_wheel_entry_point_black)
[ -n "$files" ] && [ -n "$bin" ] && {
  echo "Running black..."
  echo $files | xargs $bin $blackmode
}

files=$(git ls-files '*.java')
bin=$(rlocation aspect_rules_fmt/fmt/java-format)
[ -n "$files" ] && [ -n "$bin" ] && {
  echo "Running java-format..."
  # Setting JAVA_RUNFILES to work around https://github.com/bazelbuild/bazel/issues/12348
  echo $files | JAVA_RUNFILES="${RUNFILES_MANIFEST_FILE%_manifest}" xargs $bin $javamode
}

# TODO: don't hardcode "linux"
files=$(git ls-files '*.swift')
bin=$(rlocation swiftformat/swiftformat_linux)
[ -n "$files" ] && [ -n "$bin" ] && {
  # swiftformat itself prints Running SwiftFormat...
  echo $files | xargs $bin $swiftmode
}
