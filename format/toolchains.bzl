load("@buildifier_prebuilt//:defs.bzl", "buildifier_prebuilt_register_toolchains")
load("@aspect_rules_format_npm//:repositories.bzl", "npm_repositories")
load("@io_bazel_rules_go//go:deps.bzl", "go_register_toolchains")
load("@rules_jvm_external//:defs.bzl", "maven_install")

# buildifier: disable=function-docstring
def format_register_toolchains():
    buildifier_prebuilt_register_toolchains()

    if "go_sdk" not in native.existing_rules():
        go_register_toolchains(version = "1.19.1")

    # Initialize repositories for all packages in pnpm-lock.yaml.
    npm_repositories()

    maven_install(
        name = "aspect_rules_format_maven",
        artifacts = [
            "org.scalameta:scalafmt-cli_2.13:3.7.14",
        ],
        repositories = [
            "https://maven.google.com",
            "https://repo1.maven.org/maven2",
        ],
    )
