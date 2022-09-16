# A tool for formatting source code

Easily ensure your code is always formatted, with consistent tooling across everyone's machines.

bazel-super-formatter is an aggregator tool that runs many formatters, in the spirit of <https://github.com/github/super-linter>.

Features:

- Don't need to add Bazel targets to include the source files, or even adopt Bazel at all.
- Managed, fully hermetic tools and runtimes (except as noted below).
- Honors formatter configuration files.

Supported languages:

| Supported | Language                  | Tool                                                           |
| --------- | ------------------------- | -------------------------------------------------------------- |
| ✓         | Python                    | [Black](https://pypi.org/project/black/)                       |
| ✓         | Java                      | [google-java-format]                                           |
| ✓         | JavaScript/TypeScript/TSX | [Prettier]                                                     |
| ✓         | CSS/HTML                  | [Prettier]                                                     |
| ✓         | JSON/YAML                 | [Prettier]                                                     |
| ✓         | Markdown                  | [Prettier]                                                     |
| ✓         | Bash                      | [prettier-plugin-sh](https://github.com/un-ts/prettier)        |
| ✓         | Starlark (Bazel)          | [Buildifier](https://github.com/keith/buildifier-prebuilt)     |
| ✓         | Swift                     | [SwiftFormat](https://github.com/nicklockwood/SwiftFormat) (1) |
|           | Go                        | [gofmt](https://pkg.go.dev/cmd/gofmt)                          |
|           | C/C++/C#                  | clang-format                                                   |
|           | Rust                      | [rustfmt](https://github.com/rust-lang/rustfmt)                |

More languages TODO: https://github.com/aspect-build/bazel-super-formatter/issues/6

[prettier]: https://prettier.io
[google-java-format]: https://github.com/google/google-java-format

1. Non-hermetic: requires that a swift toolchain is installed on the machine.
   See https://github.com/bazelbuild/rules_swift#1-install-swift

## Installation

Install Bazel: <https://bazel.build/install/bazelisk>

From the release you wish to use:
<https://github.com/aspect-build/bazel-super-formatter/releases>
copy the WORKSPACE snippet into your `WORKSPACE` file.

## Usage

### One-time re-format all files

`bazel run @aspect_rules_format//format`

> Note that mass-reformatting can be disruptive in an active repo.
> You may want to instruct developers with in-flight changes to reformat their branches as well, to avoid merge conflicts.
> Also consider adding your re-format commit to the [`.git-blame-ignore-revs` file](https://docs.github.com/en/repositories/working-with-files/using-files/viewing-a-file#ignore-commits-in-the-blame-view) to avoid polluting the blame layer.

### Re-format specific file(s)

`bazel run @aspect_rules_format//format some/file.md other/file.json`

### Install as a pre-commit hook

If you use [pre-commit.com](https://pre-commit.com/), add this in your `.pre-commit-config.yaml`:

```yaml
- repo: local
  hooks:
    - id: bazel-super-formatter
      name: Format
      language: system
      entry: bazel run @aspect_rules_format//format
      files: .*
```

Otherwise you can just do this simple thing:

```bash
$ echo "bazel run @aspect_rules_format//format" >> .git/hooks/pre-commit
$ chmod u+x .git/hooks/pre-commit
```

> Note that this option will run the formatter over all files, not just changed files.

### Check that files are already formatted

This will exit non-zero if formatting is needed. You would typically run the check mode on CI.

`bazel run @aspect_rules_format//format -- --mode check`

## Configuration

### Disable a formatter for unused language

If you don't use a language in your whole repo, you can turn off fetching the tooling.

Add some of these lines to `.bazelrc`:

```
build --@aspect_rules_format//format:java_enabled=false
build --@aspect_rules_format//format:python_enabled=false
build --@aspect_rules_format//format:swift_enabled=false
```

### Changing the version of a formatter tool

Look in our `format/repositories.bzl` file and copy the `http_*` rule you want to modify into your WORKSPACE, above the `rules_format_dependencies()` call.

### Ignoring files

We honor the `.gitignore` file. Otherwise use the affordance provided by the formatter tool, for example `.prettierignore` for files to be ignored by Prettier.

## Design

See https://hackmd.io/0UgIb6gyTvSVX9N2vTPGug

This project just covers the "formatting" use case.
