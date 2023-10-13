load("@aspect_rules_js//npm:npm_import.bzl", "npm_translate_lock")

def parse_dependencies():
    npm_translate_lock(
        name = "aspect_rules_format_npm",
        link_workspace = "aspect_rules_format",
        pnpm_lock = "//:pnpm-lock.yaml",
    )
