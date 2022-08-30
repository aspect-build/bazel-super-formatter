load("@buildifier_prebuilt//:defs.bzl", "buildifier_prebuilt_register_toolchains")
load("@aspect_rules_fmt_pypi//:requirements.bzl", "install_deps")
load("@aspect_rules_fmt_npm//:repositories.bzl", "npm_repositories")

def fmt_register_toolchains():
    buildifier_prebuilt_register_toolchains()

    # Initialize repositories for all packages in requirements_lock.txt.
    install_deps()

    npm_repositories()
