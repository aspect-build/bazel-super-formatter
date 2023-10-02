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

load("@python3//:defs.bzl", "interpreter")
load("@rules_python//python:pip.bzl", "pip_parse")

pip_parse(
    name = "aspect_rules_format_pypi",
    python_interpreter_target = interpreter,
    requirements_lock = "//:requirements_lock.txt",
)

load("//:requirements.bzl", install_black = "install_deps")

install_black()

load("@rules_jvm_external//:repositories.bzl", "rules_jvm_external_deps")

rules_jvm_external_deps()

load("@rules_jvm_external//:setup.bzl", "rules_jvm_external_setup")

rules_jvm_external_setup()

load("@rules_jvm_external//:defs.bzl", "maven_install")

maven_install(
    artifacts = [
        "org.scalameta:scalafmt-cli_2.13:3.7.14",
    ],
    repositories = [
        "https://maven.google.com",
        "https://repo1.maven.org/maven2",
    ],
)

