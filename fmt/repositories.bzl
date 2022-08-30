"""Declare runtime dependencies

These are needed for local dev, and users must install them as well.
See https://docs.bazel.build/versions/main/skylark/deploying.html#dependencies
"""

load("@bazel_tools//tools/build_defs/repo:http.bzl", _http_archive = "http_archive", _http_jar = "http_jar")
load("@bazel_tools//tools/build_defs/repo:utils.bzl", "maybe")

def http_archive(name, **kwargs):
    maybe(_http_archive, name = name, **kwargs)

def http_jar(name, **kwargs):
    maybe(_http_jar, name = name, **kwargs)

# WARNING: any changes in this function may be BREAKING CHANGES for users
# because we'll fetch a dependency which may be different from one that
# they were previously fetching later in their WORKSPACE setup, and now
# ours took precedence. Such breakages are challenging for users, so any
# changes in this function should be marked as BREAKING in the commit message
# and released only in semver majors.
# This is all fixed by bzlmod, so we just tolerate it for now.
def rules_fmt_dependencies():
    "Fetch dependencies"

    # The minimal version of bazel_skylib we require
    http_archive(
        name = "bazel_skylib",
        sha256 = "f7be3474d42aae265405a592bb7da8e171919d74c16f082a5457840f06054728",
        urls = [
            "https://github.com/bazelbuild/bazel-skylib/releases/download/1.2.1/bazel-skylib-1.2.1.tar.gz",
            "https://mirror.bazel.build/github.com/bazelbuild/bazel-skylib/releases/download/1.2.1/bazel-skylib-1.2.1.tar.gz",
        ],
    )

    # TODO: fetch for host platform
    http_archive(
        name = "swiftformat",
        sha256 = "f8ecce65f67cbc4e855d2a508e1282018cd7427f2b6bc33c83a3416c227233b4",
        url = "https://github.com/nicklockwood/SwiftFormat/releases/download/0.49.11/swiftformat_linux.zip",
        patch_cmds = ["chmod u+x swiftformat_linux"],
        build_file_content = "filegroup(name = \"swiftformat\", srcs=[\"swiftformat_linux\"], visibility=[\"//visibility:public\"])",
    )

    http_archive(
        name = "swiftformat_mac",
        sha256 = "978eaffdc3716bbc0859aecee0d83875cf3ab8d8725779448f0035309d9ad9f3",
        url = "https://github.com/nicklockwood/SwiftFormat/releases/download/0.49.17/swiftformat.zip",
        patch_cmds = [
            "xattr -c swiftformat",
            "chmod u+x swiftformat",
        ],
        build_file_content = "filegroup(name = \"swiftformat_mac\", srcs=[\"swiftformat\"], visibility=[\"//visibility:public\"])",
    )

    http_archive(
        name = "buildifier_prebuilt",
        sha256 = "b3fd85ae7e45c2f36bce52cfdbdb6c20261761ea5928d1686edc8873b0d0dad0",
        strip_prefix = "buildifier-prebuilt-5.1.0",
        urls = [
            "http://github.com/keith/buildifier-prebuilt/archive/5.1.0.tar.gz",
        ],
    )

    http_archive(
        name = "rules_nodejs",
        sha256 = "5aef09ed3279aa01d5c928e3beb248f9ad32dde6aafe6373a8c994c3ce643064",
        urls = ["https://github.com/bazelbuild/rules_nodejs/releases/download/5.5.3/rules_nodejs-core-5.5.3.tar.gz"],
    )

    http_archive(
        name = "aspect_rules_js",
        sha256 = "25bcb082d49616ac2da538bf7bdd33a9730c8884edbec787fec83db07e4f7f16",
        strip_prefix = "rules_js-1.1.0",
        url = "https://github.com/aspect-build/rules_js/archive/refs/tags/v1.1.0.tar.gz",
    )

    http_archive(
        name = "aspect_bazel_lib",
        sha256 = "8ea64f13c6db68356355d6a97dced3d149e9cd7ba3ecb4112960586e914e466d",
        strip_prefix = "bazel-lib-1.11.1",
        url = "https://github.com/aspect-build/bazel-lib/archive/refs/tags/v1.11.1.tar.gz",
    )

    http_archive(
        name = "rules_python",
        sha256 = "c03246c11efd49266e8e41e12931090b613e12a59e6f55ba2efd29a7cb8b4258",
        strip_prefix = "rules_python-0.11.0",
        url = "https://github.com/bazelbuild/rules_python/archive/refs/tags/0.11.0.tar.gz",
    )

    http_jar(
        name = "google-java-format",
        sha256 = "a356bb0236b29c57a3ab678f17a7b027aad603b0960c183a18f1fe322e4f38ea",
        url = "https://github.com/google/google-java-format/releases/download/v1.15.0/google-java-format-1.15.0-all-deps.jar",
    )
