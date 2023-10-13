load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_jar")
load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")
# -- load statements -- #

def _non_module_deps_impl(ctx):
    http_jar(
        name = "scala_reflect",
        integrity = "sha1-lls4LzLZFHFrDGqNBZVqNgCns1o=",
        url = "https://repo1.maven.org/maven2/org/scala-lang/scala-reflect/2.13.11/scala-reflect-2.13.11.jar",
    )
    http_jar(
        name = "scalafmt_cli_2_13",
        integrity = "sha1-tbY3lNIx+JYvDY8GeDgrz+TLRf0=",
        url = "https://repo1.maven.org/maven2/org/scalameta/scalafmt-cli_2.13/3.7.14/scalafmt-cli_2.13-3.7.14.jar",
    )
    http_jar(
        name = "diffutils",
        integrity = "sha1-fgYN1bGUMebRmOkf9nBkQ3L2D70=",
        url = "https://repo1.maven.org/maven2/com/googlecode/java-diff-utils/diffutils/1.3.0/diffutils-1.3.0.jar",
    )
    http_jar(
        name = "scalafmt_config_2_13",
        integrity = "sha1-MbQXYLTpFLvbsxpH3Hu95FcIh+8=",
        url = "https://repo1.maven.org/maven2/org/scalameta/scalafmt-config_2.13/3.7.14/scalafmt-config_2.13-3.7.14.jar",
    )
    http_jar(
        name = "paiges_core_2_13",
        integrity = "sha1-/eB2O8GQfz2+H5BZZGluCTArxkM=",
        url = "https://repo1.maven.org/maven2/org/typelevel/paiges-core_2.13/0.4.2/paiges-core_2.13-0.4.2.jar",
    )
    http_jar(
        name = "scalameta_2_13",
        integrity = "sha1-rM7jsUs8rMEjDaripd/hrfBxvOA=",
        url = "https://repo1.maven.org/maven2/org/scalameta/scalameta_2.13/4.8.10/scalameta_2.13-4.8.10.jar",
    )
    http_jar(
        name = "jline",
        integrity = "sha1-US3ecfG6nLh/MY5OHjrMd9xnpxI=",
        url = "https://repo1.maven.org/maven2/org/jline/jline/3.22.0/jline-3.22.0.jar",
    )
    http_jar(
        name = "sourcecode_2_13",
        integrity = "sha1-lXTaDOmTYHsHH2gq+V9lNeviofE=",
        url = "https://repo1.maven.org/maven2/com/lihaoyi/sourcecode_2.13/0.3.0/sourcecode_2.13-0.3.0.jar",
    )
    http_jar(
        name = "scalap",
        integrity = "sha1-5AM/NkkbNxTAKOjK2i2F/Eq8k+U=",
        url = "https://repo1.maven.org/maven2/org/scala-lang/scalap/2.13.11/scalap-2.13.11.jar",
    )
    http_jar(
        name = "scalafmt_interfaces",
        integrity = "sha1-xA3OqfHmMK99tINLmf1c+3gsxDs=",
        url = "https://repo1.maven.org/maven2/org/scalameta/scalafmt-interfaces/3.7.14/scalafmt-interfaces-3.7.14.jar",
    )
    http_jar(
        name = "scala_compiler",
        integrity = "sha1-MOU8aTaEP29HBhe2JWODFxBI794=",
        url = "https://repo1.maven.org/maven2/org/scala-lang/scala-compiler/2.13.11/scala-compiler-2.13.11.jar",
    )
    http_jar(
        name = "scala_parallel_collections_2_13",
        integrity = "sha1-mEbR7QHyTpDX+UlZhwM7gnSDVDE=",
        url = "https://repo1.maven.org/maven2/org/scala-lang/modules/scala-parallel-collections_2.13/1.0.4/scala-parallel-collections_2.13-1.0.4.jar",
    )
    http_jar(
        name = "java_diff_utils",
        integrity = "sha1-GnEqkTJNVm7vOYF/xcmYDrEMIds=",
        url = "https://repo1.maven.org/maven2/io/github/java-diff-utils/java-diff-utils/4.12/java-diff-utils-4.12.jar",
    )
    http_jar(
        name = "fansi_2_13",
        integrity = "sha1-Qc/9gdauKoyufwstOYpbUIoBGec=",
        url = "https://repo1.maven.org/maven2/com/lihaoyi/fansi_2.13/0.3.0/fansi_2.13-0.3.0.jar",
    )
    http_jar(
        name = "trees_2_13",
        integrity = "sha1-oNzodQ66vRX822yUod+dxMwgh4U=",
        url = "https://repo1.maven.org/maven2/org/scalameta/trees_2.13/4.8.10/trees_2.13-4.8.10.jar",
    )
    http_jar(
        name = "parsers_2_13",
        integrity = "sha1-unzBbLswW3tx1Bo01eDfudx3IKk=",
        url = "https://repo1.maven.org/maven2/org/scalameta/parsers_2.13/4.8.10/parsers_2.13-4.8.10.jar",
    )
    http_jar(
        name = "jna",
        integrity = "sha1-EgDn6+7b4NEAYgk/MpJakSAg50c=",
        url = "https://repo1.maven.org/maven2/net/java/dev/jna/jna/5.13.0/jna-5.13.0.jar",
    )
    http_jar(
        name = "config",
        integrity = "sha1-TECmM+eZTPsDVCRO+20D/LEcPs8=",
        url = "https://repo1.maven.org/maven2/com/typesafe/config/1.4.2/config-1.4.2.jar",
    )
    http_jar(
        name = "scalafmt_core_2_13",
        integrity = "sha1-6YpWD6MOj2V8J626FXmdjJElLaY=",
        url = "https://repo1.maven.org/maven2/org/scalameta/scalafmt-core_2.13/3.7.14/scalafmt-core_2.13-3.7.14.jar",
    )
    http_jar(
        name = "scopt_2_13",
        integrity = "sha1-22cIJsNEtchhYgsOMp2G0vmGgoU=",
        url = "https://repo1.maven.org/maven2/com/github/scopt/scopt_2.13/4.1.0/scopt_2.13-4.1.0.jar",
    )
    http_jar(
        name = "interface",
        integrity = "sha1-iMGIQ7lmc2Th+RloKD8vNIwbINk=",
        url = "https://repo1.maven.org/maven2/io/get-coursier/interface/0.0.17/interface-0.0.17.jar",
    )
    http_jar(
        name = "scalafmt_sysops_2_13",
        integrity = "sha1-Zftlr+872dLsHY4FBjwwFQY4Qdk=",
        url = "https://repo1.maven.org/maven2/org/scalameta/scalafmt-sysops_2.13/3.7.14/scalafmt-sysops_2.13-3.7.14.jar",
    )
    http_jar(
        name = "metaconfig_pprint_2_13",
        integrity = "sha1-Lu7eBd349929+uLiNocg+6/tpWM=",
        url = "https://repo1.maven.org/maven2/com/geirsson/metaconfig-pprint_2.13/0.11.1/metaconfig-pprint_2.13-0.11.1.jar",
    )
    http_jar(
        name = "svm_subs",
        integrity = "sha1-amP3YfwPkgN6A0+T4dUDNQNpR1s=",
        url = "https://repo1.maven.org/maven2/org/scalameta/svm-subs/101.0.0/svm-subs-101.0.0.jar",
    )
    http_jar(
        name = "metaconfig_typesafe_config_2_13",
        integrity = "sha1-PmKhrB+N+TdprsRYTOYjg8V6M+s=",
        url = "https://repo1.maven.org/maven2/com/geirsson/metaconfig-typesafe-config_2.13/0.11.1/metaconfig-typesafe-config_2.13-0.11.1.jar",
    )
    http_jar(
        name = "common_2_13",
        integrity = "sha1-WE49RsSCajNcByq9WVFqPyjI0Mk=",
        url = "https://repo1.maven.org/maven2/org/scalameta/common_2.13/4.8.10/common_2.13-4.8.10.jar",
    )
    http_jar(
        name = "scala_collection_compat_2_13",
        integrity = "sha1-J0UeqJfkHHSYha0gX3uD+nuqfMc=",
        url = "https://repo1.maven.org/maven2/org/scala-lang/modules/scala-collection-compat_2.13/2.5.0/scala-collection-compat_2.13-2.5.0.jar",
    )
    http_jar(
        name = "metaconfig_core_2_13",
        integrity = "sha1-wo9gZZOmp/fR0+DpTNSA3bpeqJw=",
        url = "https://repo1.maven.org/maven2/com/geirsson/metaconfig-core_2.13/0.11.1/metaconfig-core_2.13-0.11.1.jar",
    )
    http_jar(
        name = "scala_library",
        integrity = "sha1-T82C4c5C17FXkUuGhk57NZHh4NI=",
        url = "https://repo1.maven.org/maven2/org/scala-lang/scala-library/2.13.11/scala-library-2.13.11.jar",
    )
    http_jar(
        name = "scalafmt_dynamic_2_13",
        integrity = "sha1-d4+y4XLEnOn0HEgzYgqFhnoRRCk=",
        url = "https://repo1.maven.org/maven2/org/scalameta/scalafmt-dynamic_2.13/3.7.14/scalafmt-dynamic_2.13-3.7.14.jar",
    )
    http_jar(
        name = "nailgun_server",
        integrity = "sha1-1X6gpvbBuxthbFs7MRs3Jsb/Na0=",
        url = "https://repo1.maven.org/maven2/com/martiansoftware/nailgun-server/0.9.1/nailgun-server-0.9.1.jar",
    )
    http_archive(
        name = "buf",
        url = "https://github.com/bufbuild/buf/releases/download/v1.9.0/buf-Linux-x86_64.tar.gz",
        sha256 = "6c1e7258b79273c60085df8825a52a5ee306530e7327942c91ec84545cd2d40a",
        strip_prefix = "buf",
        build_file_content = "exports_files([\"bin/buf\"], visibility = [\"//visibility:public\"])",
    )
    http_archive(
        name = "terraform_linux_x86_64",
        urls = [
            "https://releases.hashicorp.com/terraform/1.4.0/terraform_1.4.0_linux_amd64.zip",
        ],
        sha256 = "5da60da508d6d1941ffa8b9216147456a16bbff6db7622ae9ad01d314cbdd188",
        build_file_content = "exports_files([\"terraform\"])",
    )
    http_archive(
        name = "swiftformat",
        url = "https://github.com/nicklockwood/SwiftFormat/releases/download/0.49.17/swiftformat_linux.zip",
        sha256 = "f62813980c2848cb1941f1456a2a06251c2e2323183623760922058b98c70745",
        patch_cmds = [
            "chmod u+x swiftformat_linux",
        ],
        build_file_content = "filegroup(name = \"swiftformat\", srcs=[\"swiftformat_linux\"], visibility=[\"//visibility:public\"])",
    )
    http_archive(
        name = "jsonnet_linux_x86_64",
        urls = [
            "https://github.com/google/go-jsonnet/releases/download/v0.20.0/go-jsonnet_0.20.0_Linux_x86_64.tar.gz",
        ],
        sha256 = "a137c5e969609c3995c4d05817a247cfef8a92760c5306c3ad7df0355dd62970",
        build_file_content = "exports_files([\"jsonnetfmt\"])",
    )
    http_jar(
        name = "google-java-format",
        sha256 = "33068bbbdce1099982ec1171f5e202898eb35f2919cf486141e439fc6e3a4203",
        url = "https://github.com/google/google-java-format/releases/download/v1.17.0/google-java-format-1.17.0-all-deps.jar",
    )
    http_jar(
        name = "ktfmt",
        url = "https://repo1.maven.org/maven2/com/facebook/ktfmt/0.46/ktfmt-0.46-jar-with-dependencies.jar",
    )

# -- repo definitions -- #

non_module_deps = module_extension(implementation = _non_module_deps_impl)
