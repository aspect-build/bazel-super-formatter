load("@io_bazel_rules_go//go/private:sdk.bzl", "go_download_sdk")
# -- load statements -- #

def _extension_for_io_bazel_rules_go_impl(ctx):
  go_download_sdk(
    name = "go_sdk",
    version = "1.19.1",
  )
# -- repo definitions -- #

extension_for_io_bazel_rules_go = module_extension(implementation = _extension_for_io_bazel_rules_go_impl)
