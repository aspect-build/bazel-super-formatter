# Bazel rules for formatting source code

Easily ensure your code is always formatted, with consistent tooling across everyone's machines.

Features:

- Don't need to add source files to Bazel library targets, or even adopt Bazel at all.
- Managed, fully hermetic tools and runtimes (except as noted below).
- Honors formatter configuration files.

TODOs:

- Lazy: only fetch tooling needed by languages that are present
- Ship as a pre-commit.com hook

Supported languages:

| Supported | Language                  | Tool                                                           |
| --------- | ------------------------- | -------------------------------------------------------------- |
| ✓         | Starlark (Bazel)          | [Buildifier](https://github.com/keith/buildifier-prebuilt)     |
| ✓         | Swift                     | [SwiftFormat](https://github.com/nicklockwood/SwiftFormat) (1) |
| ✓         | JavaScript/TypeScript/TSX | [Prettier]                                                     |
| ✓         | CSS/HTML                  | [Prettier]                                                     |
| ✓         | JSON/YAML                 | [Prettier]                                                     |
| ✓         | Markdown                  | [Prettier]                                                     |
| ✓         | Bash                      | [prettier-plugin-sh](https://github.com/un-ts/prettier)        |
| ✓         | Python                    | [Black](https://pypi.org/project/black/)                       |
|           | Go                        | [gofmt](https://pkg.go.dev/cmd/gofmt)                          |
|           | C/C++/C#                  | clang-format                                                   |
|           | Rust                      | [rustfmt](https://github.com/rust-lang/rustfmt)                |
| ✓         | Java                      | [google-java-format]                                           |
|           | SQL                       |                                                                |
|           | Objective-C               |                                                                |
|           | Ruby                      |                                                                |
|           | PHP                       |                                                                |
|           | Visual Basic              |                                                                |
|           | Groovy                    |                                                                |
|           | Scala                     |                                                                |
|           | Kotlin                    |                                                                |
|           | Haskell                   |                                                                |
|           | Dart                      |                                                                |
|           | Perl                      |                                                                |
|           | Protobuf                  |                                                                |
|           | Jsonnet                   |                                                                |
|           | Terraform                 |                                                                |

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

💎 One-time re-format all files:

`bazel run @aspect_rules_format//format`

💎 Re-format a specific file:

`bazel run @aspect_rules_format//format some/file.ext`

💎 Install as a git pre-commit hook:

```bash
$ echo "bazel run @aspect_rules_format//format" >> .git/hooks/pre-commit
$ chmod u+x .git/hooks/pre-commit
```

💎 Install under pre-commit.com hook, in your `.pre-commit-config.yaml`:

```yaml
- repo: local
  hooks:
    - id: bazel-super-formatter
      name: Format
      language: system
      entry: bazel run //:format
      files: .*
```

💎 Check that files are already formatted, exit non-zero if formatting is needed:

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
