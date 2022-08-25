#!/usr/bin/env bash
# TODO:
# - should this program be written in a different language?
# - if bash, we could reuse https://github.com/github/super-linter/blob/main/lib/functions/worker.sh
# - can we detect what version control system is used? (start with git)

if [[ -z "$BUILD_WORKSPACE_DIRECTORY" ]]; then
  echo >&2 "$0: FATAL: This program must be executed under 'bazel run'"
  exit 1
fi

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


# swiftformat itself prints Running SwiftFormat...
# TODO: don't hardcode "linux"

git ls-files '*.swift' \
  | xargs --no-run-if-empty $(rlocation swiftformat/swiftformat_linux) $swiftmode

echo "Running Buildifier..."
git ls-files '*/BUILD.bazel' '*.bzl' '*.BUILD' 'WORKSPACE' '*.bazel' \
  | xargs --no-run-if-empty $(rlocation buildifier_prebuilt/buildifier/buildifier) -mode="$mode"

#set -x
#find . -name "*.sh" | $(rlocation aspect_rules_fmt/fmt/prettier.sh)
echo "Running prettier..."
git ls-files '*.js' '*.sh' '*.ts' '*.tsx' '*.json' '*.css' '*.html' '*.md' '*.yaml' '*.yml' \
  | xargs --no-run-if-empty $(rlocation aspect_rules_fmt/fmt/prettier.sh) $prettiermode

echo "Running black..."
git ls-files '*.py' '*.pyi' \
  | xargs --no-run-if-empty $(rlocation pypi_black/rules_python_wheel_entry_point_black) $blackmode

echo "Running java-format"
git ls-files '*.java' \
  | xargs --no-run-if-empty $(rlocation aspect_rules_fmt/fmt/java-format) $javamode
