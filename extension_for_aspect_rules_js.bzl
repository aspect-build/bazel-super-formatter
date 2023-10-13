load("@aspect_rules_js//npm:npm_import.bzl", "npm_translate_lock")
# -- load statements -- #

def _extension_for_aspect_rules_js_impl(ctx):
  npm_translate_lock(
    name = "aspect_rules_format_npm",
    pnpm_lock = "//:pnpm-lock.yaml",
    link_workspace = "aspect_rules_format",
  )
# -- repo definitions -- #

extension_for_aspect_rules_js = module_extension(implementation = _extension_for_aspect_rules_js_impl)
