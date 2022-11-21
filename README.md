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
| ✓         | JSON                      | [Prettier]                                                     |
| ✓         | Markdown                  | [Prettier]                                                     |
| ✓         | Bash                      | [prettier-plugin-sh](https://github.com/un-ts/prettier)        |
| ✓         | SQL                       | [prettier-plugin-sql](https://github.com/un-ts/prettier)       |
| ✓         | Starlark (Bazel)          | [Buildifier](https://github.com/keith/buildifier-prebuilt)     |
| ✓         | Swift                     | [SwiftFormat](https://github.com/nicklockwood/SwiftFormat) (1) |
| ✓         | Go                        | [gofmt](https://pkg.go.dev/cmd/gofmt)                          |
| ✓         | Protobuf                  | [buf](https://docs.buf.build/format/usage)                     |
|           | C/C++/C#                  | clang-format                                                   |
|           | Rust                      | [rustfmt](https://github.com/rust-lang/rustfmt)                |
|           | YAML                      | [yamlfmt](https://github.com/google/yamlfmt)                   |

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

Otherwise you can just wire directly into the git hook, however
this option will always run the formatter over all files, not just changed files.

```bash
$ echo "bazel run @aspect_rules_format//format" >> .git/hooks/pre-commit
$ chmod u+x .git/hooks/pre-commit
```

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
build --@aspect_rules_format//format:proto_enabled=false
```

### Changing the version of a formatter tool

Look in our `format/repositories.bzl` file and copy the `http_*` rule you want to modify into your WORKSPACE, above the `rules_format_dependencies()` call.

### Ignoring files

We honor the `.gitignore` file. Otherwise use the affordance provided by the formatter tool, for example `.prettierignore` for files to be ignored by Prettier.

Sometimes engineers want to ignore a file with a certain extension because the content isn't actually valid syntax for the corresponding language. For example, you might write a template for YAML and name it `my-template.yaml` even though it needs to have some interpolated values inserted before it's syntactically valid. We recommend instead fixing the file extension. In this example, `my.yaml.tmpl` or `my-template.yaml_` might be better.

### Using from an editor

Some engineers are used to setting up a formatter tool in their editor/IDE. Typically there is an editor extension, for example Prettier documents a number of them on <https://prettier.io/docs/en/editors.html>.

The authors of bazel-super-formatter believe that it's a waste of time for developers to setup their workflow this way.
It's redundant. Since not all engineers will configure their editor, you need to have a pre-commit CI check anyway.
At best, the users are instructed how to carefully reproduce the versions of the tools and their configuration files, so that the format operation
they perform matches what will happen automatically as they send their change off for review.

Not everyone will agree, and it may not be beneficial to convince developers to change their behavior.
Since this tool uses the same configuration files as the tool expects, you can always setup the editor extensions for all the underlying formatters yourself.
Or you could probably configure the editor to always run one of the commands above in the Usage section, any time a file is changed.
The instructions to do this are out-of-scope for this repo, particularly since they have to be formulated and updated for so many editors.

## Design

See https://hackmd.io/0UgIb6gyTvSVX9N2vTPGug

This project just covers the "formatting" use case.
