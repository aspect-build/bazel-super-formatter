# Bazel rules for formatting source code

Easily ensure your code is always formatted, with consistent tooling across everyone's machines.

Features:

- Don't need to add source files to Bazel library targets, or even adopt Bazel at all.
- Managed, fully hermetic tools and runtimes (except as noted below).
- Honors formatter configuration files.

TODOs:

- Lazy: only fetch tooling needed by languages that are present

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
|           | C/C++                     | clang-format                                                   |
|           | C#                        | clang-format                                                   |

[prettier]: https://prettier.io

1. Non-hermetic: requires that a swift toolchain is installed on the machine.
   See https://github.com/bazelbuild/rules_swift#1-install-swift

## Installation

Install Bazel: <https://bazel.build/install/bazelisk>

From the release you wish to use:
<https://github.com/aspect-build/rules_fmt/releases>
copy the WORKSPACE snippet into your `WORKSPACE` file.

## Usage

One-time re-format all files:

`bazel run @aspect_rules_fmt//fmt`

Install as a git pre-commit hook:

```bash
$ echo "bazel run @aspect_rules_fmt//fmt" >> .git/hooks/pre-commit
$ chmod u+x .git/hooks/pre-commit
```

## Design

See https://hackmd.io/0UgIb6gyTvSVX9N2vTPGug

This project just covers the "formatting" use case.
