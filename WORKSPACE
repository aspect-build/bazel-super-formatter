workspace(name = "aspect_rules_format")

load("//format:repositories.bzl", "rules_format_dependencies")

# Fetch dependencies which users need as well
rules_format_dependencies()

load("@buildifier_prebuilt//:defs.bzl", "buildifier_prebuilt_register_toolchains")

buildifier_prebuilt_register_toolchains()

load("@aspect_rules_js//js:repositories.bzl", "rules_js_dependencies")

rules_js_dependencies()

load("@rules_nodejs//nodejs:repositories.bzl", "nodejs_register_toolchains")

nodejs_register_toolchains(
    name = "nodejs",
    node_version = "16.9.0",
)

load("@rules_python//python:repositories.bzl", "python_register_toolchains")

python_register_toolchains(
    name = "python3",
    python_version = "3.10",
)

load("@aspect_rules_format//format:dependencies.bzl", "parse_dependencies")

parse_dependencies()

load("//format:toolchains.bzl", "format_register_toolchains")

format_register_toolchains()
