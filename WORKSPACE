workspace(name = "aspect_rules_fmt")

load("//fmt:repositories.bzl", "rules_fmt_dependencies")

# Fetch dependencies which users need as well
rules_fmt_dependencies()

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

load("@aspect_rules_fmt//fmt:dependencies.bzl", "parse_dependencies")

parse_dependencies()

load("//fmt:toolchains.bzl", "fmt_register_toolchains")

fmt_register_toolchains()
