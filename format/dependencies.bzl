load("@aspect_rules_js//npm:npm_import.bzl", "npm_translate_lock")
load("@rules_jvm_external//:defs.bzl", "maven_install")

def parse_dependencies():
    npm_translate_lock(
        name = "aspect_rules_format_npm",
        link_workspace = "aspect_rules_format",
        pnpm_lock = "@aspect_rules_format//:pnpm-lock.yaml",
    )

def rules_format_setup():
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
