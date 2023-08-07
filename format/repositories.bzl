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
def rules_format_dependencies():
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

    # TODO: after https://github.com/bazelbuild/rules_swift/issues/864 we should only fetch for host
    http_archive(
        name = "swiftformat",
        sha256 = "f62813980c2848cb1941f1456a2a06251c2e2323183623760922058b98c70745",
        url = "https://github.com/nicklockwood/SwiftFormat/releases/download/0.49.17/swiftformat_linux.zip",
        patch_cmds = ["chmod u+x swiftformat_linux"],
        build_file_content = "filegroup(name = \"swiftformat\", srcs=[\"swiftformat_linux\"], visibility=[\"//visibility:public\"])",
    )

    http_archive(
        name = "swiftformat_mac",
        sha256 = "978eaffdc3716bbc0859aecee0d83875cf3ab8d8725779448f0035309d9ad9f3",
        url = "https://github.com/nicklockwood/SwiftFormat/releases/download/0.49.17/swiftformat.zip",
        patch_cmds = [
            # On MacOS, `xattr -c` clears the "Unknown developer" warning when executing a fetched binary
            "if command -v xattr > /dev/null; then xattr -c swiftformat; fi",
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
        sha256 = "a833b08fc846e27a73ac2b7062e4f48cace0e72a072c6c3fa756847dc44246dd",
        strip_prefix = "rules_nodejs-6.0.0",
        url = "https://github.com/bazelbuild/rules_nodejs/releases/download/v6.0.0/rules_nodejs-v6.0.0.tar.gz",
    )

    http_archive(
        name = "aspect_rules_js",
        sha256 = "7b2a4d1d264e105eae49a27e2e78065b23e2e45724df2251eacdd317e95bfdfd",
        strip_prefix = "rules_js-1.31.0",
        url = "https://github.com/aspect-build/rules_js/archive/refs/tags/v1.31.0.tar.gz",
    )

    http_archive(
        name = "aspect_bazel_lib",
        sha256 = "d488d8ecca98a4042442a4ae5f1ab0b614f896c0ebf6e3eafff363bcc51c6e62",
        strip_prefix = "bazel-lib-1.33.0",
        url = "https://github.com/aspect-build/bazel-lib/releases/download/v1.33.0/bazel-lib-v1.33.0.tar.gz",
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

    http_archive(
        name = "io_bazel_rules_go",
        sha256 = "099a9fb96a376ccbbb7d291ed4ecbdfd42f6bc822ab77ae6f1b5cb9e914e94fa",
        urls = [
            "https://mirror.bazel.build/github.com/bazelbuild/rules_go/releases/download/v0.35.0/rules_go-v0.35.0.zip",
            "https://github.com/bazelbuild/rules_go/releases/download/v0.35.0/rules_go-v0.35.0.zip",
        ],
    )

    http_archive(
        name = "buf",
        sha256 = "6c1e7258b79273c60085df8825a52a5ee306530e7327942c91ec84545cd2d40a",
        url = "https://github.com/bufbuild/buf/releases/download/v1.9.0/buf-Linux-x86_64.tar.gz",
        strip_prefix = "buf",
        build_file_content = """exports_files(["bin/buf"], visibility = ["//visibility:public"])""",
    )

    http_archive(
        name = "buf_mac",
        sha256 = "27ea882bdaf5a4e46410fb3f5ef3507f6ce65cc8e6f4c943c37e89683b2866fb",
        url = "https://github.com/bufbuild/buf/releases/download/v1.9.0/buf-Darwin-x86_64.tar.gz",
        strip_prefix = "buf",
        build_file_content = """exports_files(["bin/buf"], visibility = ["//visibility:public"])""",
    )

    tf_version = "1.4.0"
    http_archive(
        name = "terraform_macos_aarch64",
        build_file_content = "exports_files([\"terraform\"])",
        sha256 = "d4a1e564714c6acf848e86dc020ff182477b49f932e3f550a5d9c8f5da7636fb",
        urls = ["https://releases.hashicorp.com/terraform/{0}/terraform_{0}_darwin_arm64.zip".format(tf_version)],
    )
    http_archive(
        name = "terraform_macos_x86_64",
        build_file_content = "exports_files([\"terraform\"])",
        sha256 = "e897a4217f1c3bfe37c694570dcc6371336fbda698790bb6b0547ec8daf1ffb3",
        urls = ["https://releases.hashicorp.com/terraform/{0}/terraform_{0}_darwin_amd64.zip".format(tf_version)],
    )
    http_archive(
        name = "terraform_linux_x86_64",
        build_file_content = "exports_files([\"terraform\"])",
        sha256 = "5da60da508d6d1941ffa8b9216147456a16bbff6db7622ae9ad01d314cbdd188",
        urls = ["https://releases.hashicorp.com/terraform/{0}/terraform_{0}_linux_amd64.zip".format(tf_version)],
    )
    jsonnet_version = "0.20.0"
    http_archive(
        name = "jsonnet_macos_aarch64",
        build_file_content = "exports_files([\"jsonnetfmt\"])",
        sha256 = "a15a699a58eb172c6d91f4cbddf3681095a649008628e0cfd84f564db4244ee3",
        urls = ["https://github.com/google/go-jsonnet/releases/download/v{0}/go-jsonnet_{0}_Darwin_arm64.tar.gz".format(jsonnet_version)],
    )
    http_archive(
        name = "jsonnet_macos_x86_64",
        build_file_content = "exports_files([\"jsonnetfmt\"])",
        sha256 = "76901637f60589bb9bf91b3481d4aecbc31efcd35ca99ae72bcb510b00270ad9",
        urls = ["https://github.com/google/go-jsonnet/releases/download/v{0}/go-jsonnet_{0}_Darwin_x86_64.tar.gz".format(jsonnet_version)],
    )
    http_archive(
        name = "jsonnet_linux_x86_64",
        build_file_content = "exports_files([\"jsonnetfmt\"])",
        sha256 = "a137c5e969609c3995c4d05817a247cfef8a92760c5306c3ad7df0355dd62970",
        urls = ["https://github.com/google/go-jsonnet/releases/download/v{0}/go-jsonnet_{0}_Linux_x86_64.tar.gz".format(jsonnet_version)],
    )
    http_archive(
        name = "jsonnet_linux_aarch64",
        build_file_content = "exports_files([\"jsonnetfmt\"])",
        sha256 = "49fbc99c91dcd2be53fa856307de3b8708c91dc5c74740714fdf9317957322e0",
        urls = ["https://github.com/google/go-jsonnet/releases/download/v{0}/go-jsonnet_{0}_Linux_arm64.tar.gz".format(jsonnet_version)],
    )
