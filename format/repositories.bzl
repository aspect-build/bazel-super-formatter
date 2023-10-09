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
        sha256 = "72b5bb0853aac597cce6482ee6c62513318e7f2c0050bc7c319d75d03d8a3875",
        strip_prefix = "buildifier-prebuilt-6.3.3",
        urls = [
            "http://github.com/keith/buildifier-prebuilt/archive/6.3.3.tar.gz",
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
        sha256 = "5868e73107a8e85d8f323806e60cad7283f34b32163ea6ff1020cf27abef6036",
        strip_prefix = "rules_python-0.25.0",
        url = "https://github.com/bazelbuild/rules_python/archive/refs/tags/0.25.0.tar.gz",
    )

    http_jar(
        name = "google-java-format",
        sha256 = "33068bbbdce1099982ec1171f5e202898eb35f2919cf486141e439fc6e3a4203",
        url = "https://github.com/google/google-java-format/releases/download/v1.17.0/google-java-format-1.17.0-all-deps.jar",
    )

    # GENERATED DEPS FOR org.scalameta:scalafmt-cli_2.13:3.7.14

    http_jar(
        name = "scalafmt_cli_2_13",
        url = "https://repo1.maven.org/maven2/org/scalameta/scalafmt-cli_2.13/3.7.14/scalafmt-cli_2.13-3.7.14.jar",
        sha256 = "5cb41b84a7c23bd02f03de2aefe4859cb6ce9b20523d072d3bab852c976e0aab",
    )

    http_jar(
        name = "metaconfig_core_2_13",
        url = "https://repo1.maven.org/maven2/com/geirsson/metaconfig-core_2.13/0.11.1/metaconfig-core_2.13-0.11.1.jar",
        sha256 = "26a731767c34ccf165ec86984c9e349d382a85ceaddd44bb438ac4970f89e0cb",
    )

    http_jar(
        name = "metaconfig_pprint_2_13",
        url = "https://repo1.maven.org/maven2/com/geirsson/metaconfig-pprint_2.13/0.11.1/metaconfig-pprint_2.13-0.11.1.jar",
        sha256 = "1df65fcac6437d2dd7bf244061b252e168bad49ee066bb4ddd17062a47ac0d6b",
    )

    http_jar(
        name = "metaconfig_typesafe_config_2_13",
        url = "https://repo1.maven.org/maven2/com/geirsson/metaconfig-typesafe-config_2.13/0.11.1/metaconfig-typesafe-config_2.13-0.11.1.jar",
        sha256 = "d1c823e1eb7f794b49b36f2340994b56c5dcdd6d3e689ab536c07212c7f88d49",
    )

    http_jar(
        name = "scopt_2_13",
        url = "https://repo1.maven.org/maven2/com/github/scopt/scopt_2.13/4.1.0/scopt_2.13-4.1.0.jar",
        sha256 = "2e5037bda974630b046794274e344273919abf4727acfcd86352617dce68f82b",
    )

    http_jar(
        name = "diffutils",
        url = "https://repo1.maven.org/maven2/com/googlecode/java-diff-utils/diffutils/1.3.0/diffutils-1.3.0.jar",
        sha256 = "61ba4dc49adca95243beaa0569adc2a23aedb5292ae78aa01186fa782ebdc5c2",
    )

    http_jar(
        name = "fansi_2_13",
        url = "https://repo1.maven.org/maven2/com/lihaoyi/fansi_2.13/0.3.0/fansi_2.13-0.3.0.jar",
        sha256 = "2f1d4cdd8971ef2cca8c37da8a04cb0ecf94bc89e59c6383185e88cde21f2e86",
    )

    http_jar(
        name = "sourcecode_2_13",
        url = "https://repo1.maven.org/maven2/com/lihaoyi/sourcecode_2.13/0.3.0/sourcecode_2.13-0.3.0.jar",
        sha256 = "6e5b2d55e942b450a222bfd3ebc23e99ca03716e42da25af1b2c8cde038100f5",
    )

    http_jar(
        name = "nailgun_server",
        url = "https://repo1.maven.org/maven2/com/martiansoftware/nailgun-server/0.9.1/nailgun-server-0.9.1.jar",
        sha256 = "4518faa6bf4bd26fccdc4d85e1625dc679381a08d56872d8ad12151dda9cef25",
    )

    http_jar(
        name = "config",
        url = "https://repo1.maven.org/maven2/com/typesafe/config/1.4.2/config-1.4.2.jar",
        sha256 = "0076c249b4387d8369146528fd5dacb3efba098dc02ecf9ac81debdfc2e12fd5",
    )

    http_jar(
        name = "interface",
        url = "https://repo1.maven.org/maven2/io/get-coursier/interface/0.0.17/interface-0.0.17.jar",
        sha256 = "b3987e8c02441e82d88ab8727acd64eabf3a35217ffedba904b125e06a722a77",
    )

    http_jar(
        name = "java_diff_utils",
        url = "https://repo1.maven.org/maven2/io/github/java-diff-utils/java-diff-utils/4.12/java-diff-utils-4.12.jar",
        sha256 = "9990a2039778f6b4cc94790141c2868864eacee0620c6c459451121a901cd5b5",
    )

    http_jar(
        name = "jna",
        url = "https://repo1.maven.org/maven2/net/java/dev/jna/jna/5.13.0/jna-5.13.0.jar",
        sha256 = "66d4f819a062a51a1d5627bffc23fac55d1677f0e0a1feba144aabdd670a64bb",
    )

    http_jar(
        name = "jline",
        url = "https://repo1.maven.org/maven2/org/jline/jline/3.22.0/jline-3.22.0.jar",
        sha256 = "7c3ec8d2c5815188bbaefa4c7c42bc9b8ec172382ca026a4b4f3d113c0b5c3e3",
    )

    http_jar(
        name = "scala_compiler",
        url = "https://repo1.maven.org/maven2/org/scala-lang/scala-compiler/2.13.11/scala-compiler-2.13.11.jar",
        sha256 = "c5a14770370e73a69367b131da1533890200b1e2aa70643b73f9ff31ef2e69ec",
    )

    http_jar(
        name = "scala_library",
        url = "https://repo1.maven.org/maven2/org/scala-lang/scala-library/2.13.11/scala-library-2.13.11.jar",
        sha256 = "71853291f61bda32786a866533361cae474344f5b2772a379179b02112444ed3",
    )

    http_jar(
        name = "scala_reflect",
        url = "https://repo1.maven.org/maven2/org/scala-lang/scala-reflect/2.13.11/scala-reflect-2.13.11.jar",
        sha256 = "6a46ed9b333857e8b5ea668bb254ed8e47dacd1116bf53ade9467aa4ae8f1818",
    )

    http_jar(
        name = "scalap",
        url = "https://repo1.maven.org/maven2/org/scala-lang/scalap/2.13.11/scalap-2.13.11.jar",
        sha256 = "ac358699f40002fb4f32ad77531765fce23425d0e83c51854d1635118ab285ea",
    )

    http_jar(
        name = "scala_collection_compat_2_13",
        url = "https://repo1.maven.org/maven2/org/scala-lang/modules/scala-collection-compat_2.13/2.5.0/scala-collection-compat_2.13-2.5.0.jar",
        sha256 = "93f8bf202ac28c4ca13562e31f6881a7770768e12b056b568139f37c025a3841",
    )

    http_jar(
        name = "scala_parallel_collections_2_13",
        url = "https://repo1.maven.org/maven2/org/scala-lang/modules/scala-parallel-collections_2.13/1.0.4/scala-parallel-collections_2.13-1.0.4.jar",
        sha256 = "68f266c4fa37cb20a76e905ad940e241190ce288b7e4a9877f1dd1261cd1a9a7",
    )

    http_jar(
        name = "common_2_13",
        url = "https://repo1.maven.org/maven2/org/scalameta/common_2.13/4.8.10/common_2.13-4.8.10.jar",
        sha256 = "137d07baa33d8fb5243f1e399b4d210b929ce8a5d3b9ec70c9de8e875265d0d4",
    )

    http_jar(
        name = "parsers_2_13",
        url = "https://repo1.maven.org/maven2/org/scalameta/parsers_2.13/4.8.10/parsers_2.13-4.8.10.jar",
        sha256 = "27dc6e6da71938717df932236a6301bb98dd1f13f93adaee169ea5408e8f780b",
    )

    http_jar(
        name = "scalafmt_cli_2_13",
        url = "https://repo1.maven.org/maven2/org/scalameta/scalafmt-cli_2.13/3.7.14/scalafmt-cli_2.13-3.7.14.jar",
        sha256 = "5cb41b84a7c23bd02f03de2aefe4859cb6ce9b20523d072d3bab852c976e0aab",
    )

    http_jar(
        name = "scalafmt_config_2_13",
        url = "https://repo1.maven.org/maven2/org/scalameta/scalafmt-config_2.13/3.7.14/scalafmt-config_2.13-3.7.14.jar",
        sha256 = "e6ce13331421f12f25822702321543a4f236d74764074e47c55135792f5ba87d",
    )

    http_jar(
        name = "scalafmt_core_2_13",
        url = "https://repo1.maven.org/maven2/org/scalameta/scalafmt-core_2.13/3.7.14/scalafmt-core_2.13-3.7.14.jar",
        sha256 = "9815741de95769ccd9ac6c05defcbcc939293245a6b00ea02faa0c9e8bbf3c67",
    )

    http_jar(
        name = "scalafmt_dynamic_2_13",
        url = "https://repo1.maven.org/maven2/org/scalameta/scalafmt-dynamic_2.13/3.7.14/scalafmt-dynamic_2.13-3.7.14.jar",
        sha256 = "92764f8d856e45a32aeaa1ea85d9bb9bf0615372992f90f10bb74ea414b618df",
    )

    http_jar(
        name = "scalafmt_interfaces",
        url = "https://repo1.maven.org/maven2/org/scalameta/scalafmt-interfaces/3.7.14/scalafmt-interfaces-3.7.14.jar",
        sha256 = "fd76f128868e3070e3fb9eb13d4377051874a64729590040fcac1da4a7021585",
    )

    http_jar(
        name = "scalafmt_sysops_2_13",
        url = "https://repo1.maven.org/maven2/org/scalameta/scalafmt-sysops_2.13/3.7.14/scalafmt-sysops_2.13-3.7.14.jar",
        sha256 = "92968b494703f385f8bd4351e95b5c400c0efbef4ce3f04f8dbfd73b7dceb083",
    )

    http_jar(
        name = "scalameta_2_13",
        url = "https://repo1.maven.org/maven2/org/scalameta/scalameta_2.13/4.8.10/scalameta_2.13-4.8.10.jar",
        sha256 = "482bc472be542a43badc1d19b54bedaf2bfc258a433ac6a4c53dd31baa16eb5f",
    )

    http_jar(
        name = "svm_subs",
        url = "https://repo1.maven.org/maven2/org/scalameta/svm-subs/101.0.0/svm-subs-101.0.0.jar",
        sha256 = "b31eb8ef90bec4c22a8ec858f5bd007bd46ce80c3dcef9dce238c6f9dd15c1a4",
    )

    http_jar(
        name = "trees_2_13",
        url = "https://repo1.maven.org/maven2/org/scalameta/trees_2.13/4.8.10/trees_2.13-4.8.10.jar",
        sha256 = "998c9104557d13de9ac1011545c7f958383574f4adde02f0a5ad2f6da3774159",
    )

    http_jar(
        name = "paiges_core_2_13",
        url = "https://repo1.maven.org/maven2/org/typelevel/paiges-core_2.13/0.4.2/paiges-core_2.13-0.4.2.jar",
        sha256 = "9484ac95856510459d1bd52a77a6b93cdd641560decdf9910395ee4d17e88163",
    )

    # END GENERATED DEPS FOR org.scalameta:scalafmt-cli_2.13:3.7.14

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
