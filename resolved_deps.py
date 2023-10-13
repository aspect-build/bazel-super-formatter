resolved = [
     {
          "original_rule_class": "local_repository",
          "original_attributes": {
               "name": "bazel_tools",
               "path": "/home/andrzej/.cache/bazel/_bazel_andrzej/install/a09dbb90c658248f08f9aa0eba11997d/embedded_tools"
          },
          "native": "local_repository(name = \"bazel_tools\", path = __embedded_dir__ + \"/\" + \"embedded_tools\")"
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository buildifier_prebuilt instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:6:26: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/repositories.bzl:57:17: in rules_format_dependencies\n  /home/andrzej/code/bazel/bazel-super-formatter/format/repositories.bzl:11:10: in http_archive\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\nRepository rule http_archive defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "buildifier_prebuilt",
               "generator_name": "buildifier_prebuilt",
               "generator_function": "rules_format_dependencies",
               "generator_location": None,
               "urls": [
                    "http://github.com/keith/buildifier-prebuilt/archive/6.3.3.tar.gz"
               ],
               "sha256": "72b5bb0853aac597cce6482ee6c62513318e7f2c0050bc7c319d75d03d8a3875",
               "strip_prefix": "buildifier-prebuilt-6.3.3"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "http://github.com/keith/buildifier-prebuilt/archive/6.3.3.tar.gz"
                         ],
                         "sha256": "72b5bb0853aac597cce6482ee6c62513318e7f2c0050bc7c319d75d03d8a3875",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "buildifier-prebuilt-6.3.3",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "buildifier_prebuilt"
                    },
                    "output_tree_hash": "44a4a4823e1fc5e372043145fa470e38e34b48df95709ba723fd1511fd36f541"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository bazel_skylib instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:6:26: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/repositories.bzl:27:17: in rules_format_dependencies\n  /home/andrzej/code/bazel/bazel-super-formatter/format/repositories.bzl:11:10: in http_archive\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\nRepository rule http_archive defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "bazel_skylib",
               "generator_name": "bazel_skylib",
               "generator_function": "rules_format_dependencies",
               "generator_location": None,
               "urls": [
                    "https://github.com/bazelbuild/bazel-skylib/releases/download/1.2.1/bazel-skylib-1.2.1.tar.gz",
                    "https://mirror.bazel.build/github.com/bazelbuild/bazel-skylib/releases/download/1.2.1/bazel-skylib-1.2.1.tar.gz"
               ],
               "sha256": "f7be3474d42aae265405a592bb7da8e171919d74c16f082a5457840f06054728"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://github.com/bazelbuild/bazel-skylib/releases/download/1.2.1/bazel-skylib-1.2.1.tar.gz",
                              "https://mirror.bazel.build/github.com/bazelbuild/bazel-skylib/releases/download/1.2.1/bazel-skylib-1.2.1.tar.gz"
                         ],
                         "sha256": "f7be3474d42aae265405a592bb7da8e171919d74c16f082a5457840f06054728",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "bazel_skylib"
                    },
                    "output_tree_hash": "b51032127f8b27d13aac4695e5d64ac36c2aa6d0f53aaf68306c32882e84f6cb"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository aspect_rules_js instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:6:26: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/repositories.bzl:72:17: in rules_format_dependencies\n  /home/andrzej/code/bazel/bazel-super-formatter/format/repositories.bzl:11:10: in http_archive\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\nRepository rule http_archive defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "aspect_rules_js",
               "generator_name": "aspect_rules_js",
               "generator_function": "rules_format_dependencies",
               "generator_location": None,
               "url": "https://github.com/aspect-build/rules_js/archive/refs/tags/v1.1.0.tar.gz",
               "sha256": "25bcb082d49616ac2da538bf7bdd33a9730c8884edbec787fec83db07e4f7f16",
               "strip_prefix": "rules_js-1.1.0"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "https://github.com/aspect-build/rules_js/archive/refs/tags/v1.1.0.tar.gz",
                         "urls": [],
                         "sha256": "25bcb082d49616ac2da538bf7bdd33a9730c8884edbec787fec83db07e4f7f16",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "rules_js-1.1.0",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "aspect_rules_js"
                    },
                    "output_tree_hash": "f4818c379883cdc626b5d6ae0103f5933ee60dbef663820d43da8c4d14f4442d"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository rules_nodejs instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:6:26: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/repositories.bzl:66:17: in rules_format_dependencies\n  /home/andrzej/code/bazel/bazel-super-formatter/format/repositories.bzl:11:10: in http_archive\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\nRepository rule http_archive defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "rules_nodejs",
               "generator_name": "rules_nodejs",
               "generator_function": "rules_format_dependencies",
               "generator_location": None,
               "urls": [
                    "https://github.com/bazelbuild/rules_nodejs/releases/download/5.5.3/rules_nodejs-core-5.5.3.tar.gz"
               ],
               "sha256": "5aef09ed3279aa01d5c928e3beb248f9ad32dde6aafe6373a8c994c3ce643064"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://github.com/bazelbuild/rules_nodejs/releases/download/5.5.3/rules_nodejs-core-5.5.3.tar.gz"
                         ],
                         "sha256": "5aef09ed3279aa01d5c928e3beb248f9ad32dde6aafe6373a8c994c3ce643064",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "rules_nodejs"
                    },
                    "output_tree_hash": "52e7c77821a75123d9458febe4538153401d5d24111b9b9716bb05a13728ff7b"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository rules_python instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:6:26: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/repositories.bzl:86:17: in rules_format_dependencies\n  /home/andrzej/code/bazel/bazel-super-formatter/format/repositories.bzl:11:10: in http_archive\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\nRepository rule http_archive defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "rules_python",
               "generator_name": "rules_python",
               "generator_function": "rules_format_dependencies",
               "generator_location": None,
               "url": "https://github.com/bazelbuild/rules_python/archive/refs/tags/0.25.0.tar.gz",
               "sha256": "5868e73107a8e85d8f323806e60cad7283f34b32163ea6ff1020cf27abef6036",
               "strip_prefix": "rules_python-0.25.0"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "https://github.com/bazelbuild/rules_python/archive/refs/tags/0.25.0.tar.gz",
                         "urls": [],
                         "sha256": "5868e73107a8e85d8f323806e60cad7283f34b32163ea6ff1020cf27abef6036",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "rules_python-0.25.0",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "rules_python"
                    },
                    "output_tree_hash": "b85291eaa7b1dd813d46cc1dd41f5f32e08345243a6b093d024ca0c72e513dd4"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository aspect_bazel_lib instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:6:26: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/repositories.bzl:79:17: in rules_format_dependencies\n  /home/andrzej/code/bazel/bazel-super-formatter/format/repositories.bzl:11:10: in http_archive\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\nRepository rule http_archive defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "aspect_bazel_lib",
               "generator_name": "aspect_bazel_lib",
               "generator_function": "rules_format_dependencies",
               "generator_location": None,
               "url": "https://github.com/aspect-build/bazel-lib/archive/refs/tags/v1.11.1.tar.gz",
               "sha256": "8ea64f13c6db68356355d6a97dced3d149e9cd7ba3ecb4112960586e914e466d",
               "strip_prefix": "bazel-lib-1.11.1"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "https://github.com/aspect-build/bazel-lib/archive/refs/tags/v1.11.1.tar.gz",
                         "urls": [],
                         "sha256": "8ea64f13c6db68356355d6a97dced3d149e9cd7ba3ecb4112960586e914e466d",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "bazel-lib-1.11.1",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "aspect_bazel_lib"
                    },
                    "output_tree_hash": "7758921d9d1daaa607a5ef31967d843efe73da2c172d3f46ef7f8f37289c2a2e"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository io_bazel_rules_go instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:6:26: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/repositories.bzl:301:17: in rules_format_dependencies\n  /home/andrzej/code/bazel/bazel-super-formatter/format/repositories.bzl:11:10: in http_archive\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\nRepository rule http_archive defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "io_bazel_rules_go",
               "generator_name": "io_bazel_rules_go",
               "generator_function": "rules_format_dependencies",
               "generator_location": None,
               "urls": [
                    "https://mirror.bazel.build/github.com/bazelbuild/rules_go/releases/download/v0.35.0/rules_go-v0.35.0.zip",
                    "https://github.com/bazelbuild/rules_go/releases/download/v0.35.0/rules_go-v0.35.0.zip"
               ],
               "sha256": "099a9fb96a376ccbbb7d291ed4ecbdfd42f6bc822ab77ae6f1b5cb9e914e94fa"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://mirror.bazel.build/github.com/bazelbuild/rules_go/releases/download/v0.35.0/rules_go-v0.35.0.zip",
                              "https://github.com/bazelbuild/rules_go/releases/download/v0.35.0/rules_go-v0.35.0.zip"
                         ],
                         "sha256": "099a9fb96a376ccbbb7d291ed4ecbdfd42f6bc822ab77ae6f1b5cb9e914e94fa",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "io_bazel_rules_go"
                    },
                    "output_tree_hash": "eadd60a49756d9277fafa988f026c5a753315a3a0f24d4f341e69d3411c9d2a8"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_translate_lock",
          "definition_information": "Repository aspect_rules_format_npm instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:32:19: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/dependencies.bzl:4:23: in parse_dependencies\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:302:24: in npm_translate_lock\nRepository rule _npm_translate_lock defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:33:38: in <toplevel>\n",
          "original_attributes": {
               "name": "aspect_rules_format_npm",
               "generator_name": "aspect_rules_format_npm",
               "generator_function": "parse_dependencies",
               "generator_location": None,
               "pnpm_lock": "//:pnpm-lock.yaml",
               "patches": {},
               "patch_args": {},
               "custom_postinstalls": {},
               "prod": False,
               "public_hoist_packages": {},
               "dev": False,
               "no_optional": False,
               "lifecycle_hooks_exclude": [],
               "run_lifecycle_hooks": True,
               "lifecycle_hooks_envs": {},
               "lifecycle_hooks_execution_requirements": {},
               "bins": {},
               "lifecycle_hooks_no_sandbox": True,
               "warn_on_unqualified_tarball_url": True,
               "link_workspace": "aspect_rules_format"
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_translate_lock",
                    "attributes": {
                         "name": "aspect_rules_format_npm",
                         "generator_name": "aspect_rules_format_npm",
                         "generator_function": "parse_dependencies",
                         "generator_location": None,
                         "pnpm_lock": "//:pnpm-lock.yaml",
                         "patches": {},
                         "patch_args": {},
                         "custom_postinstalls": {},
                         "prod": False,
                         "public_hoist_packages": {},
                         "dev": False,
                         "no_optional": False,
                         "lifecycle_hooks_exclude": [],
                         "run_lifecycle_hooks": True,
                         "lifecycle_hooks_envs": {},
                         "lifecycle_hooks_execution_requirements": {},
                         "bins": {},
                         "lifecycle_hooks_no_sandbox": True,
                         "warn_on_unqualified_tarball_url": True,
                         "link_workspace": "aspect_rules_format"
                    },
                    "output_tree_hash": "01463a701303612560504eb445239bf4f4c2b4831713592f14f54424c0eb26ea"
               }
          ]
     },
     {
          "original_rule_class": "@rules_python//python/private:toolchains_repo.bzl%toolchain_aliases",
          "definition_information": "Repository python3 instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:25:27: in <toplevel>\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/rules_python/python/repositories.bzl:578:22: in python_register_toolchains\nRepository rule toolchain_aliases defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/rules_python/python/private/toolchains_repo.bzl:221:36: in <toplevel>\n",
          "original_attributes": {
               "name": "python3",
               "generator_name": "python3",
               "generator_function": "python_register_toolchains",
               "generator_location": None,
               "python_version": "3.10.12",
               "user_repository_name": "python3"
          },
          "repositories": [
               {
                    "rule_class": "@rules_python//python/private:toolchains_repo.bzl%toolchain_aliases",
                    "attributes": {
                         "name": "python3",
                         "generator_name": "python3",
                         "generator_function": "python_register_toolchains",
                         "generator_location": None,
                         "python_version": "3.10.12",
                         "user_repository_name": "python3"
                    },
                    "output_tree_hash": "09df2f0278b6157396f1427844540726abdc00396f8d850054c4ee5d653a0032"
               }
          ]
     },
     {
          "original_rule_class": "local_config_platform",
          "original_attributes": {
               "name": "local_config_platform"
          },
          "native": "local_config_platform(name = 'local_config_platform')"
     },
     {
          "original_rule_class": "local_repository",
          "original_attributes": {
               "name": "platforms",
               "path": "/home/andrzej/.cache/bazel/_bazel_andrzej/install/a09dbb90c658248f08f9aa0eba11997d/platforms"
          },
          "native": "local_repository(name = \"platforms\", path = __embedded_dir__ + \"/\" + \"platforms\")"
     },
     {
          "original_rule_class": "@io_bazel_rules_go//go/private:sdk.bzl%_go_download_sdk",
          "definition_information": "Repository go_sdk instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:36:27: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/toolchains.bzl:10:31: in format_register_toolchains\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/io_bazel_rules_go/go/private/sdk.bzl:421:28: in go_register_toolchains\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/io_bazel_rules_go/go/private/sdk.bzl:133:21: in go_download_sdk\nRepository rule _go_download_sdk defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/io_bazel_rules_go/go/private/sdk.bzl:120:35: in <toplevel>\n",
          "original_attributes": {
               "name": "go_sdk",
               "generator_name": "go_sdk",
               "generator_function": "format_register_toolchains",
               "generator_location": None,
               "version": "1.19.1"
          },
          "repositories": [
               {
                    "rule_class": "@io_bazel_rules_go//go/private:sdk.bzl%_go_download_sdk",
                    "attributes": {
                         "name": "go_sdk",
                         "generator_name": "go_sdk",
                         "generator_function": "format_register_toolchains",
                         "generator_location": None,
                         "version": "1.19.1"
                    },
                    "output_tree_hash": "e78537e8bf7c53a2ee1c0a23b06a5f9106ef2ce4508fc892454bd931828f54bb"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/sh:sh_configure.bzl%sh_config",
          "definition_information": "Repository local_config_sh instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:526:13: in <toplevel>\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/sh/sh_configure.bzl:83:14: in sh_configure\nRepository rule sh_config defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/sh/sh_configure.bzl:72:28: in <toplevel>\n",
          "original_attributes": {
               "name": "local_config_sh",
               "generator_name": "local_config_sh",
               "generator_function": "sh_configure",
               "generator_location": None
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/sh:sh_configure.bzl%sh_config",
                    "attributes": {
                         "name": "local_config_sh",
                         "generator_name": "local_config_sh",
                         "generator_function": "sh_configure",
                         "generator_location": None
                    },
                    "output_tree_hash": "7bf5ba89669bcdf4526f821bc9f1f9f49409ae9c61c4e8f21c9f17e06c475127"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk11_linux_s390x_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:94:6: in <toplevel>\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/jdk/remote_java_repository.bzl:54:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/jdk/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk11_linux_s390x_toolchain_config_repo",
               "generator_name": "remotejdk11_linux_s390x_toolchain_config_repo",
               "generator_function": "maybe",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:s390x\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_linux_s390x//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk11_linux_s390x_toolchain_config_repo",
                         "generator_name": "remotejdk11_linux_s390x_toolchain_config_repo",
                         "generator_function": "maybe",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:s390x\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_linux_s390x//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "10df692cd4259131687761221fcb989c660f1c6e9376feba066b4fdc80bdc048"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk11_macos_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:110:6: in <toplevel>\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/jdk/remote_java_repository.bzl:54:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/jdk/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk11_macos_toolchain_config_repo",
               "generator_name": "remotejdk11_macos_toolchain_config_repo",
               "generator_function": "maybe",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_macos//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk11_macos_toolchain_config_repo",
                         "generator_name": "remotejdk11_macos_toolchain_config_repo",
                         "generator_function": "maybe",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_macos//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "4b40216fabc2f6c17810749b3bf713065a39e05ff547dac45c395be6391709af"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk11_macos_aarch64_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:126:6: in <toplevel>\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/jdk/remote_java_repository.bzl:54:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/jdk/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk11_macos_aarch64_toolchain_config_repo",
               "generator_name": "remotejdk11_macos_aarch64_toolchain_config_repo",
               "generator_function": "maybe",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_macos_aarch64//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk11_macos_aarch64_toolchain_config_repo",
                         "generator_name": "remotejdk11_macos_aarch64_toolchain_config_repo",
                         "generator_function": "maybe",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_macos_aarch64//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "a762e337f24b8b511c520c1101b81cc02082e3fd25e58140dfa47eb7342161ce"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk11_linux_ppc64le_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:78:6: in <toplevel>\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/jdk/remote_java_repository.bzl:54:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/jdk/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk11_linux_ppc64le_toolchain_config_repo",
               "generator_name": "remotejdk11_linux_ppc64le_toolchain_config_repo",
               "generator_function": "maybe",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:ppc\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_linux_ppc64le//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk11_linux_ppc64le_toolchain_config_repo",
                         "generator_name": "remotejdk11_linux_ppc64le_toolchain_config_repo",
                         "generator_function": "maybe",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:ppc\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_linux_ppc64le//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "b5938368c9f92a6f5045ffca11214afb8ec9256686bec9245714376aa66b67d1"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk11_linux_aarch64_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:62:6: in <toplevel>\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/jdk/remote_java_repository.bzl:54:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/jdk/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk11_linux_aarch64_toolchain_config_repo",
               "generator_name": "remotejdk11_linux_aarch64_toolchain_config_repo",
               "generator_function": "maybe",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_linux_aarch64//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk11_linux_aarch64_toolchain_config_repo",
                         "generator_name": "remotejdk11_linux_aarch64_toolchain_config_repo",
                         "generator_function": "maybe",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_linux_aarch64//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "f817d64408c5484cf564d5fdc24f11c3f601835818645f6de7ab4c56eaf4056f"
               }
          ]
     },
     {
          "original_rule_class": "@rules_python//python/private:toolchains_repo.bzl%toolchains_repo",
          "definition_information": "Repository python3_toolchains instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:25:27: in <toplevel>\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/rules_python/python/repositories.bzl:588:20: in python_register_toolchains\nRepository rule toolchains_repo defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/rules_python/python/private/toolchains_repo.bzl:134:34: in <toplevel>\n",
          "original_attributes": {
               "name": "python3_toolchains",
               "generator_name": "python3_toolchains",
               "generator_function": "python_register_toolchains",
               "generator_location": None,
               "python_version": "3.10.12",
               "set_python_version_constraint": False,
               "user_repository_name": "python3"
          },
          "repositories": [
               {
                    "rule_class": "@rules_python//python/private:toolchains_repo.bzl%toolchains_repo",
                    "attributes": {
                         "name": "python3_toolchains",
                         "generator_name": "python3_toolchains",
                         "generator_function": "python_register_toolchains",
                         "generator_location": None,
                         "python_version": "3.10.12",
                         "set_python_version_constraint": False,
                         "user_repository_name": "python3"
                    },
                    "output_tree_hash": "43d0834147882a911364eb139bbdbcf11f2879b6da06aca2618b25ef840915d8"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk11_win_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:142:6: in <toplevel>\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/jdk/remote_java_repository.bzl:54:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/jdk/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk11_win_toolchain_config_repo",
               "generator_name": "remotejdk11_win_toolchain_config_repo",
               "generator_function": "maybe",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_win//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk11_win_toolchain_config_repo",
                         "generator_name": "remotejdk11_win_toolchain_config_repo",
                         "generator_function": "maybe",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_win//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "f6c7a48666a77c098017285e46d511074ce3de7ff4e9808bc592fd49228681b2"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk11_win_arm64_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:158:6: in <toplevel>\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/jdk/remote_java_repository.bzl:54:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/jdk/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk11_win_arm64_toolchain_config_repo",
               "generator_name": "remotejdk11_win_arm64_toolchain_config_repo",
               "generator_function": "maybe",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:arm64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_win_arm64//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk11_win_arm64_toolchain_config_repo",
                         "generator_name": "remotejdk11_win_arm64_toolchain_config_repo",
                         "generator_function": "maybe",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:arm64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_win_arm64//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "383e78f7a5b828401c8b5a470bc3676797a189fe9641856f243c35e282e4384c"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk11_linux_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:46:6: in <toplevel>\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/jdk/remote_java_repository.bzl:54:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/jdk/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk11_linux_toolchain_config_repo",
               "generator_name": "remotejdk11_linux_toolchain_config_repo",
               "generator_function": "maybe",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_linux//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk11_linux_toolchain_config_repo",
                         "generator_name": "remotejdk11_linux_toolchain_config_repo",
                         "generator_function": "maybe",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_linux//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "8e1033ec85367ff2067aa4aa175c76d9cab0f81b9d0d4f10b7743e953331b892"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk17_linux_aarch64_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:190:6: in <toplevel>\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/jdk/remote_java_repository.bzl:54:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/jdk/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk17_linux_aarch64_toolchain_config_repo",
               "generator_name": "remotejdk17_linux_aarch64_toolchain_config_repo",
               "generator_function": "maybe",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_linux_aarch64//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk17_linux_aarch64_toolchain_config_repo",
                         "generator_name": "remotejdk17_linux_aarch64_toolchain_config_repo",
                         "generator_function": "maybe",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_linux_aarch64//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "57763b4c6342c2729b70ccf1676a75726a4775a6e6468c86462f7247c968ecd7"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk17_macos_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:206:6: in <toplevel>\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/jdk/remote_java_repository.bzl:54:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/jdk/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk17_macos_toolchain_config_repo",
               "generator_name": "remotejdk17_macos_toolchain_config_repo",
               "generator_function": "maybe",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_macos//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk17_macos_toolchain_config_repo",
                         "generator_name": "remotejdk17_macos_toolchain_config_repo",
                         "generator_function": "maybe",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_macos//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "8fc6087c6e654d2ff8ce626db7d0902fcf08d111f3c9f737ab19355b67d59c80"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk17_win_arm64_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:253:6: in <toplevel>\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/jdk/remote_java_repository.bzl:54:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/jdk/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk17_win_arm64_toolchain_config_repo",
               "generator_name": "remotejdk17_win_arm64_toolchain_config_repo",
               "generator_function": "maybe",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:arm64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_win_arm64//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk17_win_arm64_toolchain_config_repo",
                         "generator_name": "remotejdk17_win_arm64_toolchain_config_repo",
                         "generator_function": "maybe",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:arm64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_win_arm64//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "78dfb0f7dab651cbc675d9dfe42e28b363ec26c3e5dc9a57b94833852f91deda"
               }
          ]
     },
     {
          "original_rule_class": "@buildifier_prebuilt//:defs.bzl%_buildifier_toolchain_setup",
          "definition_information": "Repository buildifier_prebuilt_toolchains instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:10:40: in <toplevel>\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/buildifier_prebuilt/defs.bzl:81:32: in buildifier_prebuilt_register_toolchains\nRepository rule _buildifier_toolchain_setup defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/buildifier_prebuilt/defs.bzl:30:46: in <toplevel>\n",
          "original_attributes": {
               "name": "buildifier_prebuilt_toolchains",
               "generator_name": "buildifier_prebuilt_toolchains",
               "generator_function": "buildifier_prebuilt_register_toolchains",
               "generator_location": None,
               "assets_json": "[{\"arch\":\"amd64\",\"name\":\"buildifier\",\"platform\":\"darwin\",\"sha256\":\"3c36a3217bd793815a907a8e5bf81c291e2d35d73c6073914640a5f42e65f73f\",\"version\":\"v6.3.3\"},{\"arch\":\"arm64\",\"name\":\"buildifier\",\"platform\":\"darwin\",\"sha256\":\"9bb366432d515814766afcf6f9010294c13876686fbbe585d5d6b4ff0ca3e982\",\"version\":\"v6.3.3\"},{\"arch\":\"amd64\",\"name\":\"buildifier\",\"platform\":\"linux\",\"sha256\":\"42f798ec532c58e34401985043e660cb19d5ae994e108d19298c7d229547ffca\",\"version\":\"v6.3.3\"},{\"arch\":\"arm64\",\"name\":\"buildifier\",\"platform\":\"linux\",\"sha256\":\"6a03a1cf525045cb686fc67cd5d64cface5092ebefca3c4c93fb6e97c64e07db\",\"version\":\"v6.3.3\"},{\"arch\":\"amd64\",\"name\":\"buildifier\",\"platform\":\"windows\",\"sha256\":\"2761bebc7392d47c2862c43d85201d93efa57249ed09405fd82708867caa787b\",\"version\":\"v6.3.3\"},{\"arch\":\"amd64\",\"name\":\"buildozer\",\"platform\":\"darwin\",\"sha256\":\"9b0bbecb3745250e5ad5a9c36da456699cb55e52999451c3c74047d2b1f0085f\",\"version\":\"v6.3.3\"},{\"arch\":\"arm64\",\"name\":\"buildozer\",\"platform\":\"darwin\",\"sha256\":\"085928dd4deffa1a7fd38c66c4475e37326b2d4942408e8e3d993953ae4c626c\",\"version\":\"v6.3.3\"},{\"arch\":\"amd64\",\"name\":\"buildozer\",\"platform\":\"linux\",\"sha256\":\"1dcdc668d7c775e5bca2d43ac37e036468ca4d139a78fe48ae207d41411c5100\",\"version\":\"v6.3.3\"},{\"arch\":\"arm64\",\"name\":\"buildozer\",\"platform\":\"linux\",\"sha256\":\"94b96d6a3c52d6ef416f0eb96c8a9fe7f6a0757f0458cc8cf190dfc4a5c2d8e7\",\"version\":\"v6.3.3\"},{\"arch\":\"amd64\",\"name\":\"buildozer\",\"platform\":\"windows\",\"sha256\":\"fc1c4f5de391ec6d66f2119c5bd6131d572ae35e92ddffe720e42b619ab158e0\",\"version\":\"v6.3.3\"}]"
          },
          "repositories": [
               {
                    "rule_class": "@buildifier_prebuilt//:defs.bzl%_buildifier_toolchain_setup",
                    "attributes": {
                         "name": "buildifier_prebuilt_toolchains",
                         "generator_name": "buildifier_prebuilt_toolchains",
                         "generator_function": "buildifier_prebuilt_register_toolchains",
                         "generator_location": None,
                         "assets_json": "[{\"arch\":\"amd64\",\"name\":\"buildifier\",\"platform\":\"darwin\",\"sha256\":\"3c36a3217bd793815a907a8e5bf81c291e2d35d73c6073914640a5f42e65f73f\",\"version\":\"v6.3.3\"},{\"arch\":\"arm64\",\"name\":\"buildifier\",\"platform\":\"darwin\",\"sha256\":\"9bb366432d515814766afcf6f9010294c13876686fbbe585d5d6b4ff0ca3e982\",\"version\":\"v6.3.3\"},{\"arch\":\"amd64\",\"name\":\"buildifier\",\"platform\":\"linux\",\"sha256\":\"42f798ec532c58e34401985043e660cb19d5ae994e108d19298c7d229547ffca\",\"version\":\"v6.3.3\"},{\"arch\":\"arm64\",\"name\":\"buildifier\",\"platform\":\"linux\",\"sha256\":\"6a03a1cf525045cb686fc67cd5d64cface5092ebefca3c4c93fb6e97c64e07db\",\"version\":\"v6.3.3\"},{\"arch\":\"amd64\",\"name\":\"buildifier\",\"platform\":\"windows\",\"sha256\":\"2761bebc7392d47c2862c43d85201d93efa57249ed09405fd82708867caa787b\",\"version\":\"v6.3.3\"},{\"arch\":\"amd64\",\"name\":\"buildozer\",\"platform\":\"darwin\",\"sha256\":\"9b0bbecb3745250e5ad5a9c36da456699cb55e52999451c3c74047d2b1f0085f\",\"version\":\"v6.3.3\"},{\"arch\":\"arm64\",\"name\":\"buildozer\",\"platform\":\"darwin\",\"sha256\":\"085928dd4deffa1a7fd38c66c4475e37326b2d4942408e8e3d993953ae4c626c\",\"version\":\"v6.3.3\"},{\"arch\":\"amd64\",\"name\":\"buildozer\",\"platform\":\"linux\",\"sha256\":\"1dcdc668d7c775e5bca2d43ac37e036468ca4d139a78fe48ae207d41411c5100\",\"version\":\"v6.3.3\"},{\"arch\":\"arm64\",\"name\":\"buildozer\",\"platform\":\"linux\",\"sha256\":\"94b96d6a3c52d6ef416f0eb96c8a9fe7f6a0757f0458cc8cf190dfc4a5c2d8e7\",\"version\":\"v6.3.3\"},{\"arch\":\"amd64\",\"name\":\"buildozer\",\"platform\":\"windows\",\"sha256\":\"fc1c4f5de391ec6d66f2119c5bd6131d572ae35e92ddffe720e42b619ab158e0\",\"version\":\"v6.3.3\"}]"
                    },
                    "output_tree_hash": "66566b3c3b08bec407311e0066a9cd9d6731c31ca6f3a95b96455a6cfe220a74"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk17_macos_aarch64_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:222:6: in <toplevel>\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/jdk/remote_java_repository.bzl:54:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/jdk/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk17_macos_aarch64_toolchain_config_repo",
               "generator_name": "remotejdk17_macos_aarch64_toolchain_config_repo",
               "generator_function": "maybe",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_macos_aarch64//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk17_macos_aarch64_toolchain_config_repo",
                         "generator_name": "remotejdk17_macos_aarch64_toolchain_config_repo",
                         "generator_function": "maybe",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_macos_aarch64//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "f698cb98820064a11248ba634c70c6df5b57382ee5f8a1b589007e5b73bfc6f8"
               }
          ]
     },
     {
          "original_rule_class": "@rules_nodejs//nodejs/private:toolchains_repo.bzl%toolchains_repo",
          "definition_information": "Repository nodejs_toolchains instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:18:27: in <toplevel>\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/rules_nodejs/nodejs/repositories.bzl:400:20: in nodejs_register_toolchains\nRepository rule toolchains_repo defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/rules_nodejs/nodejs/private/toolchains_repo.bzl:127:34: in <toplevel>\n",
          "original_attributes": {
               "name": "nodejs_toolchains",
               "generator_name": "nodejs_toolchains",
               "generator_function": "nodejs_register_toolchains",
               "generator_location": None,
               "user_node_repository_name": "nodejs"
          },
          "repositories": [
               {
                    "rule_class": "@rules_nodejs//nodejs/private:toolchains_repo.bzl%toolchains_repo",
                    "attributes": {
                         "name": "nodejs_toolchains",
                         "generator_name": "nodejs_toolchains",
                         "generator_function": "nodejs_register_toolchains",
                         "generator_location": None,
                         "user_node_repository_name": "nodejs"
                    },
                    "output_tree_hash": "8d4f67ce8de75346cd0a4fb362369a0083469c36e34314ef7dfb2c263a58cff2"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk18_macos_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:301:6: in <toplevel>\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/jdk/remote_java_repository.bzl:54:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/jdk/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk18_macos_toolchain_config_repo",
               "generator_name": "remotejdk18_macos_toolchain_config_repo",
               "generator_function": "maybe",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_18\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"18\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk18_macos//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk18_macos_toolchain_config_repo",
                         "generator_name": "remotejdk18_macos_toolchain_config_repo",
                         "generator_function": "maybe",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_18\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"18\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk18_macos//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "195ddef2a390e6ceebe003a0f2ede89a2962723d5e89c88fc6f1203d84eec1c5"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk18_linux_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:269:6: in <toplevel>\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/jdk/remote_java_repository.bzl:54:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/jdk/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk18_linux_toolchain_config_repo",
               "generator_name": "remotejdk18_linux_toolchain_config_repo",
               "generator_function": "maybe",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_18\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"18\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk18_linux//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk18_linux_toolchain_config_repo",
                         "generator_name": "remotejdk18_linux_toolchain_config_repo",
                         "generator_function": "maybe",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_18\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"18\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk18_linux//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "7b4e118acc67f0ab2e764a34c9081459f46ecf83ede0abcb03fdbe4959b9033e"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk18_linux_aarch64_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:285:6: in <toplevel>\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/jdk/remote_java_repository.bzl:54:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/jdk/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk18_linux_aarch64_toolchain_config_repo",
               "generator_name": "remotejdk18_linux_aarch64_toolchain_config_repo",
               "generator_function": "maybe",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_18\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"18\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk18_linux_aarch64//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk18_linux_aarch64_toolchain_config_repo",
                         "generator_name": "remotejdk18_linux_aarch64_toolchain_config_repo",
                         "generator_function": "maybe",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_18\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"18\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk18_linux_aarch64//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "0492adccec49cb7fafa99a8da0a43c1ecf77d62d15c2213ced41f7dd06d2a40f"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk17_win_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:238:6: in <toplevel>\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/jdk/remote_java_repository.bzl:54:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/jdk/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk17_win_toolchain_config_repo",
               "generator_name": "remotejdk17_win_toolchain_config_repo",
               "generator_function": "maybe",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_win//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk17_win_toolchain_config_repo",
                         "generator_name": "remotejdk17_win_toolchain_config_repo",
                         "generator_function": "maybe",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_win//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "224a8c9f9e2f5e5cbb9efff01aa2555019675d3e1c9b93a7b4a83dfd7f5b69d5"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk18_win_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:333:6: in <toplevel>\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/jdk/remote_java_repository.bzl:54:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/jdk/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk18_win_toolchain_config_repo",
               "generator_name": "remotejdk18_win_toolchain_config_repo",
               "generator_function": "maybe",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_18\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"18\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk18_win//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk18_win_toolchain_config_repo",
                         "generator_name": "remotejdk18_win_toolchain_config_repo",
                         "generator_function": "maybe",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_18\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"18\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk18_win//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "0fbe406ef93edfa2dd63ecbec5eb91b55150360ebda0981365494b89015f6d4e"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk18_win_arm64_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:349:6: in <toplevel>\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/jdk/remote_java_repository.bzl:54:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/jdk/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk18_win_arm64_toolchain_config_repo",
               "generator_name": "remotejdk18_win_arm64_toolchain_config_repo",
               "generator_function": "maybe",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_18\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"18\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:arm64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk18_win_arm64//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk18_win_arm64_toolchain_config_repo",
                         "generator_name": "remotejdk18_win_arm64_toolchain_config_repo",
                         "generator_function": "maybe",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_18\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"18\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:arm64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk18_win_arm64//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "bb8b23eb4ea8b42cec8fd2e3752c459811f8944d1b9c66b71d53f693f71c52c7"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk17_linux_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:174:6: in <toplevel>\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/jdk/remote_java_repository.bzl:54:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/jdk/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk17_linux_toolchain_config_repo",
               "generator_name": "remotejdk17_linux_toolchain_config_repo",
               "generator_function": "maybe",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_linux//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk17_linux_toolchain_config_repo",
                         "generator_name": "remotejdk17_linux_toolchain_config_repo",
                         "generator_function": "maybe",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_linux//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "9cd805ebc7702094002f5373bee54fb0b9bba1ece881b83ff48c0586ddaa10d5"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk18_macos_aarch64_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:317:6: in <toplevel>\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/jdk/remote_java_repository.bzl:54:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/jdk/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk18_macos_aarch64_toolchain_config_repo",
               "generator_name": "remotejdk18_macos_aarch64_toolchain_config_repo",
               "generator_function": "maybe",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_18\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"18\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk18_macos_aarch64//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk18_macos_aarch64_toolchain_config_repo",
                         "generator_name": "remotejdk18_macos_aarch64_toolchain_config_repo",
                         "generator_function": "maybe",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_18\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"18\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk18_macos_aarch64//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "d088fdffd2f9c3a6cdefd249980df8b6b1ac0240cb5a1e7c67655ed2f181d0fb"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/cpp:cc_configure.bzl%cc_autoconf_toolchains",
          "definition_information": "Repository local_config_cc_toolchains instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:520:13: in <toplevel>\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/cpp/cc_configure.bzl:183:27: in cc_configure\nRepository rule cc_autoconf_toolchains defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/cpp/cc_configure.bzl:77:41: in <toplevel>\n",
          "original_attributes": {
               "name": "local_config_cc_toolchains",
               "generator_name": "local_config_cc_toolchains",
               "generator_function": "cc_configure",
               "generator_location": None
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/cpp:cc_configure.bzl%cc_autoconf_toolchains",
                    "attributes": {
                         "name": "local_config_cc_toolchains",
                         "generator_name": "local_config_cc_toolchains",
                         "generator_function": "cc_configure",
                         "generator_location": None
                    },
                    "output_tree_hash": "f95f3d84ac75b4a4d9817af803f1d998a755bd9c20c700c79fa82cb159e98cfc"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository swiftformat instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:6:26: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/repositories.bzl:37:17: in rules_format_dependencies\n  /home/andrzej/code/bazel/bazel-super-formatter/format/repositories.bzl:11:10: in http_archive\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\nRepository rule http_archive defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "swiftformat",
               "generator_name": "swiftformat",
               "generator_function": "rules_format_dependencies",
               "generator_location": None,
               "url": "https://github.com/nicklockwood/SwiftFormat/releases/download/0.49.17/swiftformat_linux.zip",
               "sha256": "f62813980c2848cb1941f1456a2a06251c2e2323183623760922058b98c70745",
               "patch_cmds": [
                    "chmod u+x swiftformat_linux"
               ],
               "build_file_content": "filegroup(name = \"swiftformat\", srcs=[\"swiftformat_linux\"], visibility=[\"//visibility:public\"])"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "https://github.com/nicklockwood/SwiftFormat/releases/download/0.49.17/swiftformat_linux.zip",
                         "urls": [],
                         "sha256": "f62813980c2848cb1941f1456a2a06251c2e2323183623760922058b98c70745",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [
                              "chmod u+x swiftformat_linux"
                         ],
                         "patch_cmds_win": [],
                         "build_file_content": "filegroup(name = \"swiftformat\", srcs=[\"swiftformat_linux\"], visibility=[\"//visibility:public\"])",
                         "workspace_file_content": "",
                         "name": "swiftformat"
                    },
                    "output_tree_hash": "8a6fd304f4754f80f1761ba07f63f98363b7ff9ee2e1a7e0a467d0808b34f0e8"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/jdk:local_java_repository.bzl%_local_java_repository_rule",
          "definition_information": "Repository local_jdk instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:32:6: in <toplevel>\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/jdk/local_java_repository.bzl:232:32: in local_java_repository\nRepository rule _local_java_repository_rule defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/jdk/local_java_repository.bzl:201:46: in <toplevel>\n",
          "original_attributes": {
               "name": "local_jdk",
               "generator_name": "local_jdk",
               "generator_function": "maybe",
               "generator_location": None,
               "java_home": "/home/linuxbrew/.linuxbrew/Cellar/openjdk/21/libexec",
               "version": "",
               "build_file_content": "load(\"@rules_java//java:defs.bzl\", \"java_import\", \"java_runtime\")\n\npackage(default_visibility = [\"//visibility:public\"])\n\nexports_files([\"BUILD.bazel\"])\n\nDEPRECATION_MESSAGE = (\"Don't depend on targets in the JDK workspace;\" +\n                       \" use @bazel_tools//tools/jdk:current_java_runtime instead\" +\n                       \" (see https://github.com/bazelbuild/bazel/issues/5594)\")\n\nfilegroup(\n    name = \"jni_header\",\n    srcs = [\"include/jni.h\"],\n    deprecation = DEPRECATION_MESSAGE,\n)\n\nfilegroup(\n    name = \"jni_md_header-darwin\",\n    srcs = [\"include/darwin/jni_md.h\"],\n    deprecation = DEPRECATION_MESSAGE,\n)\n\nfilegroup(\n    name = \"jni_md_header-linux\",\n    srcs = [\"include/linux/jni_md.h\"],\n    deprecation = DEPRECATION_MESSAGE,\n)\n\nfilegroup(\n    name = \"jni_md_header-freebsd\",\n    srcs = [\"include/freebsd/jni_md.h\"],\n    deprecation = DEPRECATION_MESSAGE,\n)\n\nfilegroup(\n    name = \"jni_md_header-openbsd\",\n    srcs = [\"include/openbsd/jni_md.h\"],\n    deprecation = DEPRECATION_MESSAGE,\n)\n\nfilegroup(\n    name = \"jni_md_header-windows\",\n    srcs = [\"include/win32/jni_md.h\"],\n    deprecation = DEPRECATION_MESSAGE,\n)\n\nfilegroup(\n    name = \"java\",\n    srcs = select({\n        \":windows\": [\"bin/java.exe\"],\n        \"//conditions:default\": [\"bin/java\"],\n    }),\n    data = [\":jdk\"],\n    deprecation = DEPRECATION_MESSAGE,\n)\n\nfilegroup(\n    name = \"jar\",\n    srcs = select({\n        \":windows\": [\"bin/jar.exe\"],\n        \"//conditions:default\": [\"bin/jar\"],\n    }),\n    data = [\":jdk\"],\n    deprecation = DEPRECATION_MESSAGE,\n)\n\nfilegroup(\n    name = \"javac\",\n    srcs = select({\n        \":windows\": [\"bin/javac.exe\"],\n        \"//conditions:default\": [\"bin/javac\"],\n    }),\n    data = [\":jdk\"],\n    deprecation = DEPRECATION_MESSAGE,\n)\n\nfilegroup(\n    name = \"javadoc\",\n    srcs = select({\n        \":windows\": [\"bin/javadoc.exe\"],\n        \"//conditions:default\": [\"bin/javadoc\"],\n    }),\n    data = [\":jdk\"],\n    deprecation = DEPRECATION_MESSAGE,\n)\n\nfilegroup(\n    name = \"xjc\",\n    srcs = [\"bin/xjc\"],\n    deprecation = DEPRECATION_MESSAGE,\n)\n\nfilegroup(\n    name = \"wsimport\",\n    srcs = [\"bin/wsimport\"],\n    deprecation = DEPRECATION_MESSAGE,\n)\n\nBOOTCLASS_JARS = [\n    \"rt.jar\",\n    \"resources.jar\",\n    \"jsse.jar\",\n    \"jce.jar\",\n    \"charsets.jar\",\n]\n\n# TODO(cushon): this isn't compatible with JDK 9\nfilegroup(\n    name = \"bootclasspath\",\n    srcs = [\"jre/lib/%s\" % jar for jar in BOOTCLASS_JARS],\n    deprecation = DEPRECATION_MESSAGE,\n)\n\nfilegroup(\n    name = \"jre-bin\",\n    srcs = select({\n        # In some configurations, Java browser plugin is considered harmful and\n        # common antivirus software blocks access to npjp2.dll interfering with Bazel,\n        # so do not include it in JRE on Windows.\n        \":windows\": glob(\n            [\"jre/bin/**\"],\n            allow_empty = True,\n            exclude = [\"jre/bin/plugin2/**\"],\n        ),\n        \"//conditions:default\": glob(\n            [\"jre/bin/**\"],\n            allow_empty = True,\n        ),\n    }),\n    deprecation = DEPRECATION_MESSAGE,\n)\n\nfilegroup(\n    name = \"jre-lib\",\n    srcs = glob(\n        [\"jre/lib/**\"],\n        allow_empty = True,\n    ),\n)\n\nfilegroup(\n    name = \"jre\",\n    srcs = [\":jre-default\"],\n)\n\nfilegroup(\n    name = \"jre-default\",\n    srcs = [\n        \":jre-bin\",\n        \":jre-lib\",\n    ],\n    deprecation = DEPRECATION_MESSAGE,\n)\n\nfilegroup(\n    name = \"jdk-bin\",\n    srcs = glob(\n        [\"bin/**\"],\n        # The JDK on Windows sometimes contains a directory called\n        # \"%systemroot%\", which is not a valid label.\n        exclude = [\"**/*%*/**\"],\n    ),\n)\n\n#This folder holds security policies\nfilegroup(\n    name = \"jdk-conf\",\n    srcs = glob(\n        [\"conf/**\"],\n        allow_empty = True,\n    ),\n)\n\nfilegroup(\n    name = \"jdk-include\",\n    srcs = glob(\n        [\"include/**\"],\n        allow_empty = True,\n    ),\n)\n\nfilegroup(\n    name = \"jdk-lib\",\n    srcs = glob(\n        [\"lib/**\"],\n        allow_empty = True,\n        exclude = [\n            \"lib/missioncontrol/**\",\n            \"lib/visualvm/**\",\n        ],\n    ),\n)\n\njava_runtime(\n    name = \"jdk\",\n    srcs = [\n        \":jdk-bin\",\n        \":jdk-conf\",\n        \":jdk-include\",\n        \":jdk-lib\",\n        \":jre-default\",\n    ],\n    version = ___RUNTIME_VERSION___,\n)\n\nconfig_setting(\n    name = \"windows\",\n    constraint_values = [\"@platforms//os:windows\"],\n    visibility = [\"//visibility:private\"],\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/jdk:local_java_repository.bzl%_local_java_repository_rule",
                    "attributes": {
                         "name": "local_jdk",
                         "generator_name": "local_jdk",
                         "generator_function": "maybe",
                         "generator_location": None,
                         "java_home": "/home/linuxbrew/.linuxbrew/Cellar/openjdk/21/libexec",
                         "version": "",
                         "build_file_content": "load(\"@rules_java//java:defs.bzl\", \"java_import\", \"java_runtime\")\n\npackage(default_visibility = [\"//visibility:public\"])\n\nexports_files([\"BUILD.bazel\"])\n\nDEPRECATION_MESSAGE = (\"Don't depend on targets in the JDK workspace;\" +\n                       \" use @bazel_tools//tools/jdk:current_java_runtime instead\" +\n                       \" (see https://github.com/bazelbuild/bazel/issues/5594)\")\n\nfilegroup(\n    name = \"jni_header\",\n    srcs = [\"include/jni.h\"],\n    deprecation = DEPRECATION_MESSAGE,\n)\n\nfilegroup(\n    name = \"jni_md_header-darwin\",\n    srcs = [\"include/darwin/jni_md.h\"],\n    deprecation = DEPRECATION_MESSAGE,\n)\n\nfilegroup(\n    name = \"jni_md_header-linux\",\n    srcs = [\"include/linux/jni_md.h\"],\n    deprecation = DEPRECATION_MESSAGE,\n)\n\nfilegroup(\n    name = \"jni_md_header-freebsd\",\n    srcs = [\"include/freebsd/jni_md.h\"],\n    deprecation = DEPRECATION_MESSAGE,\n)\n\nfilegroup(\n    name = \"jni_md_header-openbsd\",\n    srcs = [\"include/openbsd/jni_md.h\"],\n    deprecation = DEPRECATION_MESSAGE,\n)\n\nfilegroup(\n    name = \"jni_md_header-windows\",\n    srcs = [\"include/win32/jni_md.h\"],\n    deprecation = DEPRECATION_MESSAGE,\n)\n\nfilegroup(\n    name = \"java\",\n    srcs = select({\n        \":windows\": [\"bin/java.exe\"],\n        \"//conditions:default\": [\"bin/java\"],\n    }),\n    data = [\":jdk\"],\n    deprecation = DEPRECATION_MESSAGE,\n)\n\nfilegroup(\n    name = \"jar\",\n    srcs = select({\n        \":windows\": [\"bin/jar.exe\"],\n        \"//conditions:default\": [\"bin/jar\"],\n    }),\n    data = [\":jdk\"],\n    deprecation = DEPRECATION_MESSAGE,\n)\n\nfilegroup(\n    name = \"javac\",\n    srcs = select({\n        \":windows\": [\"bin/javac.exe\"],\n        \"//conditions:default\": [\"bin/javac\"],\n    }),\n    data = [\":jdk\"],\n    deprecation = DEPRECATION_MESSAGE,\n)\n\nfilegroup(\n    name = \"javadoc\",\n    srcs = select({\n        \":windows\": [\"bin/javadoc.exe\"],\n        \"//conditions:default\": [\"bin/javadoc\"],\n    }),\n    data = [\":jdk\"],\n    deprecation = DEPRECATION_MESSAGE,\n)\n\nfilegroup(\n    name = \"xjc\",\n    srcs = [\"bin/xjc\"],\n    deprecation = DEPRECATION_MESSAGE,\n)\n\nfilegroup(\n    name = \"wsimport\",\n    srcs = [\"bin/wsimport\"],\n    deprecation = DEPRECATION_MESSAGE,\n)\n\nBOOTCLASS_JARS = [\n    \"rt.jar\",\n    \"resources.jar\",\n    \"jsse.jar\",\n    \"jce.jar\",\n    \"charsets.jar\",\n]\n\n# TODO(cushon): this isn't compatible with JDK 9\nfilegroup(\n    name = \"bootclasspath\",\n    srcs = [\"jre/lib/%s\" % jar for jar in BOOTCLASS_JARS],\n    deprecation = DEPRECATION_MESSAGE,\n)\n\nfilegroup(\n    name = \"jre-bin\",\n    srcs = select({\n        # In some configurations, Java browser plugin is considered harmful and\n        # common antivirus software blocks access to npjp2.dll interfering with Bazel,\n        # so do not include it in JRE on Windows.\n        \":windows\": glob(\n            [\"jre/bin/**\"],\n            allow_empty = True,\n            exclude = [\"jre/bin/plugin2/**\"],\n        ),\n        \"//conditions:default\": glob(\n            [\"jre/bin/**\"],\n            allow_empty = True,\n        ),\n    }),\n    deprecation = DEPRECATION_MESSAGE,\n)\n\nfilegroup(\n    name = \"jre-lib\",\n    srcs = glob(\n        [\"jre/lib/**\"],\n        allow_empty = True,\n    ),\n)\n\nfilegroup(\n    name = \"jre\",\n    srcs = [\":jre-default\"],\n)\n\nfilegroup(\n    name = \"jre-default\",\n    srcs = [\n        \":jre-bin\",\n        \":jre-lib\",\n    ],\n    deprecation = DEPRECATION_MESSAGE,\n)\n\nfilegroup(\n    name = \"jdk-bin\",\n    srcs = glob(\n        [\"bin/**\"],\n        # The JDK on Windows sometimes contains a directory called\n        # \"%systemroot%\", which is not a valid label.\n        exclude = [\"**/*%*/**\"],\n    ),\n)\n\n#This folder holds security policies\nfilegroup(\n    name = \"jdk-conf\",\n    srcs = glob(\n        [\"conf/**\"],\n        allow_empty = True,\n    ),\n)\n\nfilegroup(\n    name = \"jdk-include\",\n    srcs = glob(\n        [\"include/**\"],\n        allow_empty = True,\n    ),\n)\n\nfilegroup(\n    name = \"jdk-lib\",\n    srcs = glob(\n        [\"lib/**\"],\n        allow_empty = True,\n        exclude = [\n            \"lib/missioncontrol/**\",\n            \"lib/visualvm/**\",\n        ],\n    ),\n)\n\njava_runtime(\n    name = \"jdk\",\n    srcs = [\n        \":jdk-bin\",\n        \":jdk-conf\",\n        \":jdk-include\",\n        \":jdk-lib\",\n        \":jre-default\",\n    ],\n    version = ___RUNTIME_VERSION___,\n)\n\nconfig_setting(\n    name = \"windows\",\n    constraint_values = [\"@platforms//os:windows\"],\n    visibility = [\"//visibility:private\"],\n)\n"
                    },
                    "output_tree_hash": "4c365352fcd3786cd94c67c73af6e82ac2fc878a6d16fbaa0e83d56d5d23adb0"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository jsonnet_linux_x86_64 instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:6:26: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/repositories.bzl:358:17: in rules_format_dependencies\n  /home/andrzej/code/bazel/bazel-super-formatter/format/repositories.bzl:11:10: in http_archive\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\nRepository rule http_archive defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "jsonnet_linux_x86_64",
               "generator_name": "jsonnet_linux_x86_64",
               "generator_function": "rules_format_dependencies",
               "generator_location": None,
               "urls": [
                    "https://github.com/google/go-jsonnet/releases/download/v0.20.0/go-jsonnet_0.20.0_Linux_x86_64.tar.gz"
               ],
               "sha256": "a137c5e969609c3995c4d05817a247cfef8a92760c5306c3ad7df0355dd62970",
               "build_file_content": "exports_files([\"jsonnetfmt\"])"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://github.com/google/go-jsonnet/releases/download/v0.20.0/go-jsonnet_0.20.0_Linux_x86_64.tar.gz"
                         ],
                         "sha256": "a137c5e969609c3995c4d05817a247cfef8a92760c5306c3ad7df0355dd62970",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "exports_files([\"jsonnetfmt\"])",
                         "workspace_file_content": "",
                         "name": "jsonnet_linux_x86_64"
                    },
                    "output_tree_hash": "8f8ade464f7703f07d92f9d0e4441ea272198f66f48e1b1985d4d0a273528aa9"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository rules_java instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:414:6: in <toplevel>\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\nRepository rule http_archive defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "rules_java",
               "generator_name": "rules_java",
               "generator_function": "maybe",
               "generator_location": None,
               "urls": [
                    "https://mirror.bazel.build/github.com/bazelbuild/rules_java/archive/7cf3cefd652008d0a64a419c34c13bdca6c8f178.zip",
                    "https://github.com/bazelbuild/rules_java/archive/7cf3cefd652008d0a64a419c34c13bdca6c8f178.zip"
               ],
               "sha256": "bc81f1ba47ef5cc68ad32225c3d0e70b8c6f6077663835438da8d5733f917598",
               "strip_prefix": "rules_java-7cf3cefd652008d0a64a419c34c13bdca6c8f178"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://mirror.bazel.build/github.com/bazelbuild/rules_java/archive/7cf3cefd652008d0a64a419c34c13bdca6c8f178.zip",
                              "https://github.com/bazelbuild/rules_java/archive/7cf3cefd652008d0a64a419c34c13bdca6c8f178.zip"
                         ],
                         "sha256": "bc81f1ba47ef5cc68ad32225c3d0e70b8c6f6077663835438da8d5733f917598",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "rules_java-7cf3cefd652008d0a64a419c34c13bdca6c8f178",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "rules_java"
                    },
                    "output_tree_hash": "00a0f1231dacff0b0cea3886200e0158c67a3600068275da14120f5434f83b5e"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_jar",
          "definition_information": "Repository scalafmt_dynamic_2_13 instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:6:26: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/repositories.bzl:257:13: in rules_format_dependencies\n  /home/andrzej/code/bazel/bazel-super-formatter/format/repositories.bzl:14:10: in http_jar\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\nRepository rule http_jar defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/http.bzl:530:27: in <toplevel>\n",
          "original_attributes": {
               "name": "scalafmt_dynamic_2_13",
               "generator_name": "scalafmt_dynamic_2_13",
               "generator_function": "rules_format_dependencies",
               "generator_location": None,
               "integrity": "sha1-d4+y4XLEnOn0HEgzYgqFhnoRRCk=",
               "url": "https://repo1.maven.org/maven2/org/scalameta/scalafmt-dynamic_2.13/3.7.14/scalafmt-dynamic_2.13-3.7.14.jar"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_jar",
                    "attributes": {
                         "sha256": "",
                         "integrity": "sha1-d4+y4XLEnOn0HEgzYgqFhnoRRCk=",
                         "canonical_id": "",
                         "url": "https://repo1.maven.org/maven2/org/scalameta/scalafmt-dynamic_2.13/3.7.14/scalafmt-dynamic_2.13-3.7.14.jar",
                         "urls": [],
                         "netrc": "",
                         "auth_patterns": {},
                         "downloaded_file_name": "downloaded.jar",
                         "name": "scalafmt_dynamic_2_13"
                    },
                    "output_tree_hash": "f7dfc039ec5e429fba5a273dd4488a8160d81584e1675a624af421e7e0a32d81"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_jar",
          "definition_information": "Repository metaconfig_typesafe_config_2_13 instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:6:26: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/repositories.bzl:125:13: in rules_format_dependencies\n  /home/andrzej/code/bazel/bazel-super-formatter/format/repositories.bzl:14:10: in http_jar\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\nRepository rule http_jar defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/http.bzl:530:27: in <toplevel>\n",
          "original_attributes": {
               "name": "metaconfig_typesafe_config_2_13",
               "generator_name": "metaconfig_typesafe_config_2_13",
               "generator_function": "rules_format_dependencies",
               "generator_location": None,
               "integrity": "sha1-PmKhrB+N+TdprsRYTOYjg8V6M+s=",
               "url": "https://repo1.maven.org/maven2/com/geirsson/metaconfig-typesafe-config_2.13/0.11.1/metaconfig-typesafe-config_2.13-0.11.1.jar"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_jar",
                    "attributes": {
                         "sha256": "",
                         "integrity": "sha1-PmKhrB+N+TdprsRYTOYjg8V6M+s=",
                         "canonical_id": "",
                         "url": "https://repo1.maven.org/maven2/com/geirsson/metaconfig-typesafe-config_2.13/0.11.1/metaconfig-typesafe-config_2.13-0.11.1.jar",
                         "urls": [],
                         "netrc": "",
                         "auth_patterns": {},
                         "downloaded_file_name": "downloaded.jar",
                         "name": "metaconfig_typesafe_config_2_13"
                    },
                    "output_tree_hash": "e898e3a410d5dfcad5f1d413f2f4919e9cd838d5860752ae567b91dbe522fd9d"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_jar",
          "definition_information": "Repository common_2_13 instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:6:26: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/repositories.bzl:227:13: in rules_format_dependencies\n  /home/andrzej/code/bazel/bazel-super-formatter/format/repositories.bzl:14:10: in http_jar\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\nRepository rule http_jar defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/http.bzl:530:27: in <toplevel>\n",
          "original_attributes": {
               "name": "common_2_13",
               "generator_name": "common_2_13",
               "generator_function": "rules_format_dependencies",
               "generator_location": None,
               "integrity": "sha1-WE49RsSCajNcByq9WVFqPyjI0Mk=",
               "url": "https://repo1.maven.org/maven2/org/scalameta/common_2.13/4.8.10/common_2.13-4.8.10.jar"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_jar",
                    "attributes": {
                         "sha256": "",
                         "integrity": "sha1-WE49RsSCajNcByq9WVFqPyjI0Mk=",
                         "canonical_id": "",
                         "url": "https://repo1.maven.org/maven2/org/scalameta/common_2.13/4.8.10/common_2.13-4.8.10.jar",
                         "urls": [],
                         "netrc": "",
                         "auth_patterns": {},
                         "downloaded_file_name": "downloaded.jar",
                         "name": "common_2_13"
                    },
                    "output_tree_hash": "0d70ab1f7f223b27cb5692a70bd8fa803cbdbae8f27294464c66e3c07a8b5cff"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_jar",
          "definition_information": "Repository fansi_2_13 instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:6:26: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/repositories.bzl:143:13: in rules_format_dependencies\n  /home/andrzej/code/bazel/bazel-super-formatter/format/repositories.bzl:14:10: in http_jar\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\nRepository rule http_jar defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/http.bzl:530:27: in <toplevel>\n",
          "original_attributes": {
               "name": "fansi_2_13",
               "generator_name": "fansi_2_13",
               "generator_function": "rules_format_dependencies",
               "generator_location": None,
               "integrity": "sha1-Qc/9gdauKoyufwstOYpbUIoBGec=",
               "url": "https://repo1.maven.org/maven2/com/lihaoyi/fansi_2.13/0.3.0/fansi_2.13-0.3.0.jar"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_jar",
                    "attributes": {
                         "sha256": "",
                         "integrity": "sha1-Qc/9gdauKoyufwstOYpbUIoBGec=",
                         "canonical_id": "",
                         "url": "https://repo1.maven.org/maven2/com/lihaoyi/fansi_2.13/0.3.0/fansi_2.13-0.3.0.jar",
                         "urls": [],
                         "netrc": "",
                         "auth_patterns": {},
                         "downloaded_file_name": "downloaded.jar",
                         "name": "fansi_2_13"
                    },
                    "output_tree_hash": "74d4b3da749ebe8292ea24b1f8a8c73581e3307e3ae888e003d0b92e4b1ed864"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_jar",
          "definition_information": "Repository jline instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:6:26: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/repositories.bzl:185:13: in rules_format_dependencies\n  /home/andrzej/code/bazel/bazel-super-formatter/format/repositories.bzl:14:10: in http_jar\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\nRepository rule http_jar defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/http.bzl:530:27: in <toplevel>\n",
          "original_attributes": {
               "name": "jline",
               "generator_name": "jline",
               "generator_function": "rules_format_dependencies",
               "generator_location": None,
               "integrity": "sha1-US3ecfG6nLh/MY5OHjrMd9xnpxI=",
               "url": "https://repo1.maven.org/maven2/org/jline/jline/3.22.0/jline-3.22.0.jar"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_jar",
                    "attributes": {
                         "sha256": "",
                         "integrity": "sha1-US3ecfG6nLh/MY5OHjrMd9xnpxI=",
                         "canonical_id": "",
                         "url": "https://repo1.maven.org/maven2/org/jline/jline/3.22.0/jline-3.22.0.jar",
                         "urls": [],
                         "netrc": "",
                         "auth_patterns": {},
                         "downloaded_file_name": "downloaded.jar",
                         "name": "jline"
                    },
                    "output_tree_hash": "ea50d86b11f9e7d898cc0ca449667e4ae418134f0d19f303594f04b81b244320"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_jar",
          "definition_information": "Repository scopt_2_13 instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:6:26: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/repositories.bzl:131:13: in rules_format_dependencies\n  /home/andrzej/code/bazel/bazel-super-formatter/format/repositories.bzl:14:10: in http_jar\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\nRepository rule http_jar defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/http.bzl:530:27: in <toplevel>\n",
          "original_attributes": {
               "name": "scopt_2_13",
               "generator_name": "scopt_2_13",
               "generator_function": "rules_format_dependencies",
               "generator_location": None,
               "integrity": "sha1-22cIJsNEtchhYgsOMp2G0vmGgoU=",
               "url": "https://repo1.maven.org/maven2/com/github/scopt/scopt_2.13/4.1.0/scopt_2.13-4.1.0.jar"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_jar",
                    "attributes": {
                         "sha256": "",
                         "integrity": "sha1-22cIJsNEtchhYgsOMp2G0vmGgoU=",
                         "canonical_id": "",
                         "url": "https://repo1.maven.org/maven2/com/github/scopt/scopt_2.13/4.1.0/scopt_2.13-4.1.0.jar",
                         "urls": [],
                         "netrc": "",
                         "auth_patterns": {},
                         "downloaded_file_name": "downloaded.jar",
                         "name": "scopt_2_13"
                    },
                    "output_tree_hash": "1d1d141fc15cb35873dbab6bfae8f4c5df3e7fcae6ceffcb7415af2d9511c3ca"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_jar",
          "definition_information": "Repository nailgun_server instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:6:26: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/repositories.bzl:155:13: in rules_format_dependencies\n  /home/andrzej/code/bazel/bazel-super-formatter/format/repositories.bzl:14:10: in http_jar\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\nRepository rule http_jar defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/http.bzl:530:27: in <toplevel>\n",
          "original_attributes": {
               "name": "nailgun_server",
               "generator_name": "nailgun_server",
               "generator_function": "rules_format_dependencies",
               "generator_location": None,
               "integrity": "sha1-1X6gpvbBuxthbFs7MRs3Jsb/Na0=",
               "url": "https://repo1.maven.org/maven2/com/martiansoftware/nailgun-server/0.9.1/nailgun-server-0.9.1.jar"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_jar",
                    "attributes": {
                         "sha256": "",
                         "integrity": "sha1-1X6gpvbBuxthbFs7MRs3Jsb/Na0=",
                         "canonical_id": "",
                         "url": "https://repo1.maven.org/maven2/com/martiansoftware/nailgun-server/0.9.1/nailgun-server-0.9.1.jar",
                         "urls": [],
                         "netrc": "",
                         "auth_patterns": {},
                         "downloaded_file_name": "downloaded.jar",
                         "name": "nailgun_server"
                    },
                    "output_tree_hash": "4d5ede9347c81fc052d1d3d236150ca86fa85e9cceb1c31b10e684c3623e3aa8"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_jar",
          "definition_information": "Repository scalameta_2_13 instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:6:26: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/repositories.bzl:275:13: in rules_format_dependencies\n  /home/andrzej/code/bazel/bazel-super-formatter/format/repositories.bzl:14:10: in http_jar\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\nRepository rule http_jar defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/http.bzl:530:27: in <toplevel>\n",
          "original_attributes": {
               "name": "scalameta_2_13",
               "generator_name": "scalameta_2_13",
               "generator_function": "rules_format_dependencies",
               "generator_location": None,
               "integrity": "sha1-rM7jsUs8rMEjDaripd/hrfBxvOA=",
               "url": "https://repo1.maven.org/maven2/org/scalameta/scalameta_2.13/4.8.10/scalameta_2.13-4.8.10.jar"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_jar",
                    "attributes": {
                         "sha256": "",
                         "integrity": "sha1-rM7jsUs8rMEjDaripd/hrfBxvOA=",
                         "canonical_id": "",
                         "url": "https://repo1.maven.org/maven2/org/scalameta/scalameta_2.13/4.8.10/scalameta_2.13-4.8.10.jar",
                         "urls": [],
                         "netrc": "",
                         "auth_patterns": {},
                         "downloaded_file_name": "downloaded.jar",
                         "name": "scalameta_2_13"
                    },
                    "output_tree_hash": "875fd781b28c29e60414fd80c705ab8aa308bf65a1502792e40df74acf104ffa"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_jar",
          "definition_information": "Repository scala_parallel_collections_2_13 instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:6:26: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/repositories.bzl:221:13: in rules_format_dependencies\n  /home/andrzej/code/bazel/bazel-super-formatter/format/repositories.bzl:14:10: in http_jar\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\nRepository rule http_jar defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/http.bzl:530:27: in <toplevel>\n",
          "original_attributes": {
               "name": "scala_parallel_collections_2_13",
               "generator_name": "scala_parallel_collections_2_13",
               "generator_function": "rules_format_dependencies",
               "generator_location": None,
               "integrity": "sha1-mEbR7QHyTpDX+UlZhwM7gnSDVDE=",
               "url": "https://repo1.maven.org/maven2/org/scala-lang/modules/scala-parallel-collections_2.13/1.0.4/scala-parallel-collections_2.13-1.0.4.jar"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_jar",
                    "attributes": {
                         "sha256": "",
                         "integrity": "sha1-mEbR7QHyTpDX+UlZhwM7gnSDVDE=",
                         "canonical_id": "",
                         "url": "https://repo1.maven.org/maven2/org/scala-lang/modules/scala-parallel-collections_2.13/1.0.4/scala-parallel-collections_2.13-1.0.4.jar",
                         "urls": [],
                         "netrc": "",
                         "auth_patterns": {},
                         "downloaded_file_name": "downloaded.jar",
                         "name": "scala_parallel_collections_2_13"
                    },
                    "output_tree_hash": "d61b2478fe87ebdacdb3b6a4708b0c2f95d414d774dd6ea9ddb8a8fa4262513e"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_jar",
          "definition_information": "Repository scalafmt_sysops_2_13 instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:6:26: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/repositories.bzl:269:13: in rules_format_dependencies\n  /home/andrzej/code/bazel/bazel-super-formatter/format/repositories.bzl:14:10: in http_jar\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\nRepository rule http_jar defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/http.bzl:530:27: in <toplevel>\n",
          "original_attributes": {
               "name": "scalafmt_sysops_2_13",
               "generator_name": "scalafmt_sysops_2_13",
               "generator_function": "rules_format_dependencies",
               "generator_location": None,
               "integrity": "sha1-Zftlr+872dLsHY4FBjwwFQY4Qdk=",
               "url": "https://repo1.maven.org/maven2/org/scalameta/scalafmt-sysops_2.13/3.7.14/scalafmt-sysops_2.13-3.7.14.jar"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_jar",
                    "attributes": {
                         "sha256": "",
                         "integrity": "sha1-Zftlr+872dLsHY4FBjwwFQY4Qdk=",
                         "canonical_id": "",
                         "url": "https://repo1.maven.org/maven2/org/scalameta/scalafmt-sysops_2.13/3.7.14/scalafmt-sysops_2.13-3.7.14.jar",
                         "urls": [],
                         "netrc": "",
                         "auth_patterns": {},
                         "downloaded_file_name": "downloaded.jar",
                         "name": "scalafmt_sysops_2_13"
                    },
                    "output_tree_hash": "78328e121cde4e42695096d6f82156a9deb522f9c50c57341116630ced7e0b89"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_jar",
          "definition_information": "Repository scalafmt_cli_2_13 instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:6:26: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/repositories.bzl:107:13: in rules_format_dependencies\n  /home/andrzej/code/bazel/bazel-super-formatter/format/repositories.bzl:14:10: in http_jar\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\nRepository rule http_jar defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/http.bzl:530:27: in <toplevel>\n",
          "original_attributes": {
               "name": "scalafmt_cli_2_13",
               "generator_name": "scalafmt_cli_2_13",
               "generator_function": "rules_format_dependencies",
               "generator_location": None,
               "integrity": "sha1-tbY3lNIx+JYvDY8GeDgrz+TLRf0=",
               "url": "https://repo1.maven.org/maven2/org/scalameta/scalafmt-cli_2.13/3.7.14/scalafmt-cli_2.13-3.7.14.jar"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_jar",
                    "attributes": {
                         "sha256": "",
                         "integrity": "sha1-tbY3lNIx+JYvDY8GeDgrz+TLRf0=",
                         "canonical_id": "",
                         "url": "https://repo1.maven.org/maven2/org/scalameta/scalafmt-cli_2.13/3.7.14/scalafmt-cli_2.13-3.7.14.jar",
                         "urls": [],
                         "netrc": "",
                         "auth_patterns": {},
                         "downloaded_file_name": "downloaded.jar",
                         "name": "scalafmt_cli_2_13"
                    },
                    "output_tree_hash": "a168f59433b8d4c4e9e156be66692ad8a2da15317bd0379fe867fb7dc35e72e9"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_jar",
          "definition_information": "Repository java_diff_utils instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:6:26: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/repositories.bzl:173:13: in rules_format_dependencies\n  /home/andrzej/code/bazel/bazel-super-formatter/format/repositories.bzl:14:10: in http_jar\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\nRepository rule http_jar defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/http.bzl:530:27: in <toplevel>\n",
          "original_attributes": {
               "name": "java_diff_utils",
               "generator_name": "java_diff_utils",
               "generator_function": "rules_format_dependencies",
               "generator_location": None,
               "integrity": "sha1-GnEqkTJNVm7vOYF/xcmYDrEMIds=",
               "url": "https://repo1.maven.org/maven2/io/github/java-diff-utils/java-diff-utils/4.12/java-diff-utils-4.12.jar"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_jar",
                    "attributes": {
                         "sha256": "",
                         "integrity": "sha1-GnEqkTJNVm7vOYF/xcmYDrEMIds=",
                         "canonical_id": "",
                         "url": "https://repo1.maven.org/maven2/io/github/java-diff-utils/java-diff-utils/4.12/java-diff-utils-4.12.jar",
                         "urls": [],
                         "netrc": "",
                         "auth_patterns": {},
                         "downloaded_file_name": "downloaded.jar",
                         "name": "java_diff_utils"
                    },
                    "output_tree_hash": "4465fc333811324aac634e44d97c197d5221d74e6539d1e9ffcc5a66ea2aa17e"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_jar",
          "definition_information": "Repository parsers_2_13 instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:6:26: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/repositories.bzl:233:13: in rules_format_dependencies\n  /home/andrzej/code/bazel/bazel-super-formatter/format/repositories.bzl:14:10: in http_jar\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\nRepository rule http_jar defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/http.bzl:530:27: in <toplevel>\n",
          "original_attributes": {
               "name": "parsers_2_13",
               "generator_name": "parsers_2_13",
               "generator_function": "rules_format_dependencies",
               "generator_location": None,
               "integrity": "sha1-unzBbLswW3tx1Bo01eDfudx3IKk=",
               "url": "https://repo1.maven.org/maven2/org/scalameta/parsers_2.13/4.8.10/parsers_2.13-4.8.10.jar"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_jar",
                    "attributes": {
                         "sha256": "",
                         "integrity": "sha1-unzBbLswW3tx1Bo01eDfudx3IKk=",
                         "canonical_id": "",
                         "url": "https://repo1.maven.org/maven2/org/scalameta/parsers_2.13/4.8.10/parsers_2.13-4.8.10.jar",
                         "urls": [],
                         "netrc": "",
                         "auth_patterns": {},
                         "downloaded_file_name": "downloaded.jar",
                         "name": "parsers_2_13"
                    },
                    "output_tree_hash": "d902f2a071d5faaed74e3a5c235c1e9f2da582812a2489e9316bfd75685a9b36"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
          "definition_information": "Repository aspect_rules_format_npm__which__2.0.2__links instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:36:27: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/toolchains.bzl:13:21: in format_register_toolchains\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_format_npm/repositories.bzl:728:15: in npm_repositories\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:561:22: in npm_import\nRepository rule _npm_import_links defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:326:36: in <toplevel>\n",
          "original_attributes": {
               "name": "aspect_rules_format_npm__which__2.0.2__links",
               "generator_name": "aspect_rules_format_npm__which__2.0.2__links",
               "generator_function": "format_register_toolchains",
               "generator_location": None,
               "package": "which",
               "version": "2.0.2",
               "root_package": "",
               "link_packages": {},
               "bins": {},
               "deps": {
                    "isexe": "2.0.0"
               },
               "transitive_closure": {
                    "which": [
                         "2.0.2"
                    ],
                    "isexe": [
                         "2.0.0"
                    ]
               },
               "lifecycle_build_target": False,
               "lifecycle_hooks_env": [],
               "lifecycle_hooks_execution_requirements": [],
               "lifecycle_hooks_no_sandbox": True
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
                    "attributes": {
                         "name": "aspect_rules_format_npm__which__2.0.2__links",
                         "generator_name": "aspect_rules_format_npm__which__2.0.2__links",
                         "generator_function": "format_register_toolchains",
                         "generator_location": None,
                         "package": "which",
                         "version": "2.0.2",
                         "root_package": "",
                         "link_packages": {},
                         "bins": {},
                         "deps": {
                              "isexe": "2.0.0"
                         },
                         "transitive_closure": {
                              "which": [
                                   "2.0.2"
                              ],
                              "isexe": [
                                   "2.0.0"
                              ]
                         },
                         "lifecycle_build_target": False,
                         "lifecycle_hooks_env": [],
                         "lifecycle_hooks_execution_requirements": [],
                         "lifecycle_hooks_no_sandbox": True
                    },
                    "output_tree_hash": "8aaeee5fc6a433d54d32c1499cc777879eb9ea1fabb74c195b56f6fa5668b675"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_jar",
          "definition_information": "Repository scala_reflect instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:6:26: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/repositories.bzl:203:13: in rules_format_dependencies\n  /home/andrzej/code/bazel/bazel-super-formatter/format/repositories.bzl:14:10: in http_jar\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\nRepository rule http_jar defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/http.bzl:530:27: in <toplevel>\n",
          "original_attributes": {
               "name": "scala_reflect",
               "generator_name": "scala_reflect",
               "generator_function": "rules_format_dependencies",
               "generator_location": None,
               "integrity": "sha1-lls4LzLZFHFrDGqNBZVqNgCns1o=",
               "url": "https://repo1.maven.org/maven2/org/scala-lang/scala-reflect/2.13.11/scala-reflect-2.13.11.jar"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_jar",
                    "attributes": {
                         "sha256": "",
                         "integrity": "sha1-lls4LzLZFHFrDGqNBZVqNgCns1o=",
                         "canonical_id": "",
                         "url": "https://repo1.maven.org/maven2/org/scala-lang/scala-reflect/2.13.11/scala-reflect-2.13.11.jar",
                         "urls": [],
                         "netrc": "",
                         "auth_patterns": {},
                         "downloaded_file_name": "downloaded.jar",
                         "name": "scala_reflect"
                    },
                    "output_tree_hash": "381dec4808faa2154285e14233120c45e9a3bab21d1f2a1215b20ab750b1ac53"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
          "definition_information": "Repository aspect_rules_format_npm__tslib__2.5.0__links instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:36:27: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/toolchains.bzl:13:21: in format_register_toolchains\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_format_npm/repositories.bzl:714:15: in npm_repositories\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:561:22: in npm_import\nRepository rule _npm_import_links defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:326:36: in <toplevel>\n",
          "original_attributes": {
               "name": "aspect_rules_format_npm__tslib__2.5.0__links",
               "generator_name": "aspect_rules_format_npm__tslib__2.5.0__links",
               "generator_function": "format_register_toolchains",
               "generator_location": None,
               "package": "tslib",
               "version": "2.5.0",
               "root_package": "",
               "link_packages": {},
               "bins": {},
               "deps": {},
               "transitive_closure": {
                    "tslib": [
                         "2.5.0"
                    ]
               },
               "lifecycle_build_target": False,
               "lifecycle_hooks_env": [],
               "lifecycle_hooks_execution_requirements": [],
               "lifecycle_hooks_no_sandbox": True
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
                    "attributes": {
                         "name": "aspect_rules_format_npm__tslib__2.5.0__links",
                         "generator_name": "aspect_rules_format_npm__tslib__2.5.0__links",
                         "generator_function": "format_register_toolchains",
                         "generator_location": None,
                         "package": "tslib",
                         "version": "2.5.0",
                         "root_package": "",
                         "link_packages": {},
                         "bins": {},
                         "deps": {},
                         "transitive_closure": {
                              "tslib": [
                                   "2.5.0"
                              ]
                         },
                         "lifecycle_build_target": False,
                         "lifecycle_hooks_env": [],
                         "lifecycle_hooks_execution_requirements": [],
                         "lifecycle_hooks_no_sandbox": True
                    },
                    "output_tree_hash": "f37372b89267fb5fced2f7d81b56cf75a332b640be80fc712e036e432d3aeb76"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_jar",
          "definition_information": "Repository metaconfig_core_2_13 instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:6:26: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/repositories.bzl:113:13: in rules_format_dependencies\n  /home/andrzej/code/bazel/bazel-super-formatter/format/repositories.bzl:14:10: in http_jar\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\nRepository rule http_jar defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/http.bzl:530:27: in <toplevel>\n",
          "original_attributes": {
               "name": "metaconfig_core_2_13",
               "generator_name": "metaconfig_core_2_13",
               "generator_function": "rules_format_dependencies",
               "generator_location": None,
               "integrity": "sha1-wo9gZZOmp/fR0+DpTNSA3bpeqJw=",
               "url": "https://repo1.maven.org/maven2/com/geirsson/metaconfig-core_2.13/0.11.1/metaconfig-core_2.13-0.11.1.jar"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_jar",
                    "attributes": {
                         "sha256": "",
                         "integrity": "sha1-wo9gZZOmp/fR0+DpTNSA3bpeqJw=",
                         "canonical_id": "",
                         "url": "https://repo1.maven.org/maven2/com/geirsson/metaconfig-core_2.13/0.11.1/metaconfig-core_2.13-0.11.1.jar",
                         "urls": [],
                         "netrc": "",
                         "auth_patterns": {},
                         "downloaded_file_name": "downloaded.jar",
                         "name": "metaconfig_core_2_13"
                    },
                    "output_tree_hash": "6876fed84875a9bf57b968064d0b1bfc8b136e01ad6dac4cc3dc311a6107dcec"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_jar",
          "definition_information": "Repository config instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:6:26: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/repositories.bzl:161:13: in rules_format_dependencies\n  /home/andrzej/code/bazel/bazel-super-formatter/format/repositories.bzl:14:10: in http_jar\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\nRepository rule http_jar defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/http.bzl:530:27: in <toplevel>\n",
          "original_attributes": {
               "name": "config",
               "generator_name": "config",
               "generator_function": "rules_format_dependencies",
               "generator_location": None,
               "integrity": "sha1-TECmM+eZTPsDVCRO+20D/LEcPs8=",
               "url": "https://repo1.maven.org/maven2/com/typesafe/config/1.4.2/config-1.4.2.jar"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_jar",
                    "attributes": {
                         "sha256": "",
                         "integrity": "sha1-TECmM+eZTPsDVCRO+20D/LEcPs8=",
                         "canonical_id": "",
                         "url": "https://repo1.maven.org/maven2/com/typesafe/config/1.4.2/config-1.4.2.jar",
                         "urls": [],
                         "netrc": "",
                         "auth_patterns": {},
                         "downloaded_file_name": "downloaded.jar",
                         "name": "config"
                    },
                    "output_tree_hash": "5c4fe26cc19b70dec630050b4f1bd9f8399cfabe41f5c31917ff6db84bd49c6a"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
          "definition_information": "Repository aspect_rules_format_npm__tiny-glob__0.2.9__links instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:36:27: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/toolchains.bzl:13:21: in format_register_toolchains\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_format_npm/repositories.bzl:694:15: in npm_repositories\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:561:22: in npm_import\nRepository rule _npm_import_links defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:326:36: in <toplevel>\n",
          "original_attributes": {
               "name": "aspect_rules_format_npm__tiny-glob__0.2.9__links",
               "generator_name": "aspect_rules_format_npm__tiny-glob__0.2.9__links",
               "generator_function": "format_register_toolchains",
               "generator_location": None,
               "package": "tiny-glob",
               "version": "0.2.9",
               "root_package": "",
               "link_packages": {},
               "bins": {},
               "deps": {
                    "globalyzer": "0.1.0",
                    "globrex": "0.1.2"
               },
               "transitive_closure": {
                    "tiny-glob": [
                         "0.2.9"
                    ],
                    "globalyzer": [
                         "0.1.0"
                    ],
                    "globrex": [
                         "0.1.2"
                    ]
               },
               "lifecycle_build_target": False,
               "lifecycle_hooks_env": [],
               "lifecycle_hooks_execution_requirements": [],
               "lifecycle_hooks_no_sandbox": True
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
                    "attributes": {
                         "name": "aspect_rules_format_npm__tiny-glob__0.2.9__links",
                         "generator_name": "aspect_rules_format_npm__tiny-glob__0.2.9__links",
                         "generator_function": "format_register_toolchains",
                         "generator_location": None,
                         "package": "tiny-glob",
                         "version": "0.2.9",
                         "root_package": "",
                         "link_packages": {},
                         "bins": {},
                         "deps": {
                              "globalyzer": "0.1.0",
                              "globrex": "0.1.2"
                         },
                         "transitive_closure": {
                              "tiny-glob": [
                                   "0.2.9"
                              ],
                              "globalyzer": [
                                   "0.1.0"
                              ],
                              "globrex": [
                                   "0.1.2"
                              ]
                         },
                         "lifecycle_build_target": False,
                         "lifecycle_hooks_env": [],
                         "lifecycle_hooks_execution_requirements": [],
                         "lifecycle_hooks_no_sandbox": True
                    },
                    "output_tree_hash": "10a209b7611373c98c9cadb4272734f53be59dfe196cfb929ebc01ed310e0a41"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
          "definition_information": "Repository aspect_rules_format_npm__synckit__0.8.5__links instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:36:27: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/toolchains.bzl:13:21: in format_register_toolchains\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_format_npm/repositories.bzl:658:15: in npm_repositories\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:561:22: in npm_import\nRepository rule _npm_import_links defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:326:36: in <toplevel>\n",
          "original_attributes": {
               "name": "aspect_rules_format_npm__synckit__0.8.5__links",
               "generator_name": "aspect_rules_format_npm__synckit__0.8.5__links",
               "generator_function": "format_register_toolchains",
               "generator_location": None,
               "package": "synckit",
               "version": "0.8.5",
               "root_package": "",
               "link_packages": {},
               "bins": {},
               "deps": {
                    "@pkgr/utils": "2.3.1",
                    "tslib": "2.5.0"
               },
               "transitive_closure": {
                    "synckit": [
                         "0.8.5"
                    ],
                    "@pkgr/utils": [
                         "2.3.1"
                    ],
                    "tslib": [
                         "2.5.0"
                    ],
                    "cross-spawn": [
                         "7.0.3"
                    ],
                    "is-glob": [
                         "4.0.3"
                    ],
                    "open": [
                         "8.4.2"
                    ],
                    "picocolors": [
                         "1.0.0"
                    ],
                    "tiny-glob": [
                         "0.2.9"
                    ],
                    "globalyzer": [
                         "0.1.0"
                    ],
                    "globrex": [
                         "0.1.2"
                    ],
                    "define-lazy-prop": [
                         "2.0.0"
                    ],
                    "is-docker": [
                         "2.2.1"
                    ],
                    "is-wsl": [
                         "2.2.0"
                    ],
                    "is-extglob": [
                         "2.1.1"
                    ],
                    "path-key": [
                         "3.1.1"
                    ],
                    "shebang-command": [
                         "2.0.0"
                    ],
                    "which": [
                         "2.0.2"
                    ],
                    "isexe": [
                         "2.0.0"
                    ],
                    "shebang-regex": [
                         "3.0.0"
                    ]
               },
               "lifecycle_build_target": False,
               "lifecycle_hooks_env": [],
               "lifecycle_hooks_execution_requirements": [],
               "lifecycle_hooks_no_sandbox": True
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
                    "attributes": {
                         "name": "aspect_rules_format_npm__synckit__0.8.5__links",
                         "generator_name": "aspect_rules_format_npm__synckit__0.8.5__links",
                         "generator_function": "format_register_toolchains",
                         "generator_location": None,
                         "package": "synckit",
                         "version": "0.8.5",
                         "root_package": "",
                         "link_packages": {},
                         "bins": {},
                         "deps": {
                              "@pkgr/utils": "2.3.1",
                              "tslib": "2.5.0"
                         },
                         "transitive_closure": {
                              "synckit": [
                                   "0.8.5"
                              ],
                              "@pkgr/utils": [
                                   "2.3.1"
                              ],
                              "tslib": [
                                   "2.5.0"
                              ],
                              "cross-spawn": [
                                   "7.0.3"
                              ],
                              "is-glob": [
                                   "4.0.3"
                              ],
                              "open": [
                                   "8.4.2"
                              ],
                              "picocolors": [
                                   "1.0.0"
                              ],
                              "tiny-glob": [
                                   "0.2.9"
                              ],
                              "globalyzer": [
                                   "0.1.0"
                              ],
                              "globrex": [
                                   "0.1.2"
                              ],
                              "define-lazy-prop": [
                                   "2.0.0"
                              ],
                              "is-docker": [
                                   "2.2.1"
                              ],
                              "is-wsl": [
                                   "2.2.0"
                              ],
                              "is-extglob": [
                                   "2.1.1"
                              ],
                              "path-key": [
                                   "3.1.1"
                              ],
                              "shebang-command": [
                                   "2.0.0"
                              ],
                              "which": [
                                   "2.0.2"
                              ],
                              "isexe": [
                                   "2.0.0"
                              ],
                              "shebang-regex": [
                                   "3.0.0"
                              ]
                         },
                         "lifecycle_build_target": False,
                         "lifecycle_hooks_env": [],
                         "lifecycle_hooks_execution_requirements": [],
                         "lifecycle_hooks_no_sandbox": True
                    },
                    "output_tree_hash": "aaf1c13a165eecf90d09cf393ef9b34579ab2c3d8221cfefd0870462200f77a0"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
          "definition_information": "Repository aspect_rules_format_npm__sql-formatter__12.2.0__links instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:36:27: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/toolchains.bzl:13:21: in format_register_toolchains\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_format_npm/repositories.bzl:632:15: in npm_repositories\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:561:22: in npm_import\nRepository rule _npm_import_links defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:326:36: in <toplevel>\n",
          "original_attributes": {
               "name": "aspect_rules_format_npm__sql-formatter__12.2.0__links",
               "generator_name": "aspect_rules_format_npm__sql-formatter__12.2.0__links",
               "generator_function": "format_register_toolchains",
               "generator_location": None,
               "package": "sql-formatter",
               "version": "12.2.0",
               "root_package": "",
               "link_packages": {},
               "bins": {},
               "deps": {
                    "argparse": "2.0.1",
                    "nearley": "2.20.1"
               },
               "transitive_closure": {
                    "sql-formatter": [
                         "12.2.0"
                    ],
                    "argparse": [
                         "2.0.1"
                    ],
                    "nearley": [
                         "2.20.1"
                    ],
                    "commander": [
                         "2.20.3"
                    ],
                    "moo": [
                         "0.5.2"
                    ],
                    "railroad-diagrams": [
                         "1.0.0"
                    ],
                    "randexp": [
                         "0.4.6"
                    ],
                    "discontinuous-range": [
                         "1.0.0"
                    ],
                    "ret": [
                         "0.1.15"
                    ]
               },
               "lifecycle_build_target": False,
               "lifecycle_hooks_env": [],
               "lifecycle_hooks_execution_requirements": [],
               "lifecycle_hooks_no_sandbox": True
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
                    "attributes": {
                         "name": "aspect_rules_format_npm__sql-formatter__12.2.0__links",
                         "generator_name": "aspect_rules_format_npm__sql-formatter__12.2.0__links",
                         "generator_function": "format_register_toolchains",
                         "generator_location": None,
                         "package": "sql-formatter",
                         "version": "12.2.0",
                         "root_package": "",
                         "link_packages": {},
                         "bins": {},
                         "deps": {
                              "argparse": "2.0.1",
                              "nearley": "2.20.1"
                         },
                         "transitive_closure": {
                              "sql-formatter": [
                                   "12.2.0"
                              ],
                              "argparse": [
                                   "2.0.1"
                              ],
                              "nearley": [
                                   "2.20.1"
                              ],
                              "commander": [
                                   "2.20.3"
                              ],
                              "moo": [
                                   "0.5.2"
                              ],
                              "railroad-diagrams": [
                                   "1.0.0"
                              ],
                              "randexp": [
                                   "0.4.6"
                              ],
                              "discontinuous-range": [
                                   "1.0.0"
                              ],
                              "ret": [
                                   "0.1.15"
                              ]
                         },
                         "lifecycle_build_target": False,
                         "lifecycle_hooks_env": [],
                         "lifecycle_hooks_execution_requirements": [],
                         "lifecycle_hooks_no_sandbox": True
                    },
                    "output_tree_hash": "4e26dc6112c9654ce89da0c2d18c06a004ccd01018e17baa9e0ad58affc48570"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
          "definition_information": "Repository aspect_rules_format_npm__shebang-regex__3.0.0__links instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:36:27: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/toolchains.bzl:13:21: in format_register_toolchains\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_format_npm/repositories.bzl:618:15: in npm_repositories\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:561:22: in npm_import\nRepository rule _npm_import_links defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:326:36: in <toplevel>\n",
          "original_attributes": {
               "name": "aspect_rules_format_npm__shebang-regex__3.0.0__links",
               "generator_name": "aspect_rules_format_npm__shebang-regex__3.0.0__links",
               "generator_function": "format_register_toolchains",
               "generator_location": None,
               "package": "shebang-regex",
               "version": "3.0.0",
               "root_package": "",
               "link_packages": {},
               "bins": {},
               "deps": {},
               "transitive_closure": {
                    "shebang-regex": [
                         "3.0.0"
                    ]
               },
               "lifecycle_build_target": False,
               "lifecycle_hooks_env": [],
               "lifecycle_hooks_execution_requirements": [],
               "lifecycle_hooks_no_sandbox": True
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
                    "attributes": {
                         "name": "aspect_rules_format_npm__shebang-regex__3.0.0__links",
                         "generator_name": "aspect_rules_format_npm__shebang-regex__3.0.0__links",
                         "generator_function": "format_register_toolchains",
                         "generator_location": None,
                         "package": "shebang-regex",
                         "version": "3.0.0",
                         "root_package": "",
                         "link_packages": {},
                         "bins": {},
                         "deps": {},
                         "transitive_closure": {
                              "shebang-regex": [
                                   "3.0.0"
                              ]
                         },
                         "lifecycle_build_target": False,
                         "lifecycle_hooks_env": [],
                         "lifecycle_hooks_execution_requirements": [],
                         "lifecycle_hooks_no_sandbox": True
                    },
                    "output_tree_hash": "5a578239e610f7cbcfa08cef91541812062271a9b62104c9fc7a3fb091d1b1f5"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
          "definition_information": "Repository aspect_rules_format_npm__shebang-command__2.0.0__links instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:36:27: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/toolchains.bzl:13:21: in format_register_toolchains\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_format_npm/repositories.bzl:600:15: in npm_repositories\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:561:22: in npm_import\nRepository rule _npm_import_links defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:326:36: in <toplevel>\n",
          "original_attributes": {
               "name": "aspect_rules_format_npm__shebang-command__2.0.0__links",
               "generator_name": "aspect_rules_format_npm__shebang-command__2.0.0__links",
               "generator_function": "format_register_toolchains",
               "generator_location": None,
               "package": "shebang-command",
               "version": "2.0.0",
               "root_package": "",
               "link_packages": {},
               "bins": {},
               "deps": {
                    "shebang-regex": "3.0.0"
               },
               "transitive_closure": {
                    "shebang-command": [
                         "2.0.0"
                    ],
                    "shebang-regex": [
                         "3.0.0"
                    ]
               },
               "lifecycle_build_target": False,
               "lifecycle_hooks_env": [],
               "lifecycle_hooks_execution_requirements": [],
               "lifecycle_hooks_no_sandbox": True
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
                    "attributes": {
                         "name": "aspect_rules_format_npm__shebang-command__2.0.0__links",
                         "generator_name": "aspect_rules_format_npm__shebang-command__2.0.0__links",
                         "generator_function": "format_register_toolchains",
                         "generator_location": None,
                         "package": "shebang-command",
                         "version": "2.0.0",
                         "root_package": "",
                         "link_packages": {},
                         "bins": {},
                         "deps": {
                              "shebang-regex": "3.0.0"
                         },
                         "transitive_closure": {
                              "shebang-command": [
                                   "2.0.0"
                              ],
                              "shebang-regex": [
                                   "3.0.0"
                              ]
                         },
                         "lifecycle_build_target": False,
                         "lifecycle_hooks_env": [],
                         "lifecycle_hooks_execution_requirements": [],
                         "lifecycle_hooks_no_sandbox": True
                    },
                    "output_tree_hash": "c2a03df9edc1a8de16eb27ae6f84cb44cb71d662f52fc2ebf0937d8a3056cf30"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
          "definition_information": "Repository aspect_rules_format_npm__sh-syntax__0.3.7__links instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:36:27: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/toolchains.bzl:13:21: in format_register_toolchains\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_format_npm/repositories.bzl:582:15: in npm_repositories\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:561:22: in npm_import\nRepository rule _npm_import_links defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:326:36: in <toplevel>\n",
          "original_attributes": {
               "name": "aspect_rules_format_npm__sh-syntax__0.3.7__links",
               "generator_name": "aspect_rules_format_npm__sh-syntax__0.3.7__links",
               "generator_function": "format_register_toolchains",
               "generator_location": None,
               "package": "sh-syntax",
               "version": "0.3.7",
               "root_package": "",
               "link_packages": {},
               "bins": {},
               "deps": {
                    "tslib": "2.5.0"
               },
               "transitive_closure": {
                    "sh-syntax": [
                         "0.3.7"
                    ],
                    "tslib": [
                         "2.5.0"
                    ]
               },
               "lifecycle_build_target": False,
               "lifecycle_hooks_env": [],
               "lifecycle_hooks_execution_requirements": [],
               "lifecycle_hooks_no_sandbox": True
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
                    "attributes": {
                         "name": "aspect_rules_format_npm__sh-syntax__0.3.7__links",
                         "generator_name": "aspect_rules_format_npm__sh-syntax__0.3.7__links",
                         "generator_function": "format_register_toolchains",
                         "generator_location": None,
                         "package": "sh-syntax",
                         "version": "0.3.7",
                         "root_package": "",
                         "link_packages": {},
                         "bins": {},
                         "deps": {
                              "tslib": "2.5.0"
                         },
                         "transitive_closure": {
                              "sh-syntax": [
                                   "0.3.7"
                              ],
                              "tslib": [
                                   "2.5.0"
                              ]
                         },
                         "lifecycle_build_target": False,
                         "lifecycle_hooks_env": [],
                         "lifecycle_hooks_execution_requirements": [],
                         "lifecycle_hooks_no_sandbox": True
                    },
                    "output_tree_hash": "ef2ae057f535102b3150aa490011e7a2deb32090958f4d6759bcbc0892c72c23"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
          "definition_information": "Repository aspect_rules_format_npm__ret__0.1.15__links instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:36:27: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/toolchains.bzl:13:21: in format_register_toolchains\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_format_npm/repositories.bzl:568:15: in npm_repositories\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:561:22: in npm_import\nRepository rule _npm_import_links defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:326:36: in <toplevel>\n",
          "original_attributes": {
               "name": "aspect_rules_format_npm__ret__0.1.15__links",
               "generator_name": "aspect_rules_format_npm__ret__0.1.15__links",
               "generator_function": "format_register_toolchains",
               "generator_location": None,
               "package": "ret",
               "version": "0.1.15",
               "root_package": "",
               "link_packages": {},
               "bins": {},
               "deps": {},
               "transitive_closure": {
                    "ret": [
                         "0.1.15"
                    ]
               },
               "lifecycle_build_target": False,
               "lifecycle_hooks_env": [],
               "lifecycle_hooks_execution_requirements": [],
               "lifecycle_hooks_no_sandbox": True
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
                    "attributes": {
                         "name": "aspect_rules_format_npm__ret__0.1.15__links",
                         "generator_name": "aspect_rules_format_npm__ret__0.1.15__links",
                         "generator_function": "format_register_toolchains",
                         "generator_location": None,
                         "package": "ret",
                         "version": "0.1.15",
                         "root_package": "",
                         "link_packages": {},
                         "bins": {},
                         "deps": {},
                         "transitive_closure": {
                              "ret": [
                                   "0.1.15"
                              ]
                         },
                         "lifecycle_build_target": False,
                         "lifecycle_hooks_env": [],
                         "lifecycle_hooks_execution_requirements": [],
                         "lifecycle_hooks_no_sandbox": True
                    },
                    "output_tree_hash": "ba4330bb4373396cae5e98ebc134504f3b1e70a0ea6005a58509715abbdc48a9"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_jar",
          "definition_information": "Repository trees_2_13 instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:6:26: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/repositories.bzl:287:13: in rules_format_dependencies\n  /home/andrzej/code/bazel/bazel-super-formatter/format/repositories.bzl:14:10: in http_jar\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\nRepository rule http_jar defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/http.bzl:530:27: in <toplevel>\n",
          "original_attributes": {
               "name": "trees_2_13",
               "generator_name": "trees_2_13",
               "generator_function": "rules_format_dependencies",
               "generator_location": None,
               "integrity": "sha1-oNzodQ66vRX822yUod+dxMwgh4U=",
               "url": "https://repo1.maven.org/maven2/org/scalameta/trees_2.13/4.8.10/trees_2.13-4.8.10.jar"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_jar",
                    "attributes": {
                         "sha256": "",
                         "integrity": "sha1-oNzodQ66vRX822yUod+dxMwgh4U=",
                         "canonical_id": "",
                         "url": "https://repo1.maven.org/maven2/org/scalameta/trees_2.13/4.8.10/trees_2.13-4.8.10.jar",
                         "urls": [],
                         "netrc": "",
                         "auth_patterns": {},
                         "downloaded_file_name": "downloaded.jar",
                         "name": "trees_2_13"
                    },
                    "output_tree_hash": "8724f3d4173ebbda0e6253fc83013d6365924338a486620587d8070510e152dc"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_jar",
          "definition_information": "Repository scalafmt_interfaces instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:6:26: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/repositories.bzl:263:13: in rules_format_dependencies\n  /home/andrzej/code/bazel/bazel-super-formatter/format/repositories.bzl:14:10: in http_jar\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\nRepository rule http_jar defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/http.bzl:530:27: in <toplevel>\n",
          "original_attributes": {
               "name": "scalafmt_interfaces",
               "generator_name": "scalafmt_interfaces",
               "generator_function": "rules_format_dependencies",
               "generator_location": None,
               "integrity": "sha1-xA3OqfHmMK99tINLmf1c+3gsxDs=",
               "url": "https://repo1.maven.org/maven2/org/scalameta/scalafmt-interfaces/3.7.14/scalafmt-interfaces-3.7.14.jar"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_jar",
                    "attributes": {
                         "sha256": "",
                         "integrity": "sha1-xA3OqfHmMK99tINLmf1c+3gsxDs=",
                         "canonical_id": "",
                         "url": "https://repo1.maven.org/maven2/org/scalameta/scalafmt-interfaces/3.7.14/scalafmt-interfaces-3.7.14.jar",
                         "urls": [],
                         "netrc": "",
                         "auth_patterns": {},
                         "downloaded_file_name": "downloaded.jar",
                         "name": "scalafmt_interfaces"
                    },
                    "output_tree_hash": "71a14943f09eba03d8930855000cb751c6b17a8d829adc6222dbf1e08e692a67"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_jar",
          "definition_information": "Repository scalafmt_core_2_13 instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:6:26: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/repositories.bzl:251:13: in rules_format_dependencies\n  /home/andrzej/code/bazel/bazel-super-formatter/format/repositories.bzl:14:10: in http_jar\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\nRepository rule http_jar defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/http.bzl:530:27: in <toplevel>\n",
          "original_attributes": {
               "name": "scalafmt_core_2_13",
               "generator_name": "scalafmt_core_2_13",
               "generator_function": "rules_format_dependencies",
               "generator_location": None,
               "integrity": "sha1-6YpWD6MOj2V8J626FXmdjJElLaY=",
               "url": "https://repo1.maven.org/maven2/org/scalameta/scalafmt-core_2.13/3.7.14/scalafmt-core_2.13-3.7.14.jar"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_jar",
                    "attributes": {
                         "sha256": "",
                         "integrity": "sha1-6YpWD6MOj2V8J626FXmdjJElLaY=",
                         "canonical_id": "",
                         "url": "https://repo1.maven.org/maven2/org/scalameta/scalafmt-core_2.13/3.7.14/scalafmt-core_2.13-3.7.14.jar",
                         "urls": [],
                         "netrc": "",
                         "auth_patterns": {},
                         "downloaded_file_name": "downloaded.jar",
                         "name": "scalafmt_core_2_13"
                    },
                    "output_tree_hash": "cadf9056ebe4dfbd5f25441e54c402cf660971be3fee96796e5beded72bd56fb"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
          "definition_information": "Repository aspect_rules_format_npm__randexp__0.4.6__links instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:36:27: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/toolchains.bzl:13:21: in format_register_toolchains\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_format_npm/repositories.bzl:548:15: in npm_repositories\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:561:22: in npm_import\nRepository rule _npm_import_links defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:326:36: in <toplevel>\n",
          "original_attributes": {
               "name": "aspect_rules_format_npm__randexp__0.4.6__links",
               "generator_name": "aspect_rules_format_npm__randexp__0.4.6__links",
               "generator_function": "format_register_toolchains",
               "generator_location": None,
               "package": "randexp",
               "version": "0.4.6",
               "root_package": "",
               "link_packages": {},
               "bins": {},
               "deps": {
                    "discontinuous-range": "1.0.0",
                    "ret": "0.1.15"
               },
               "transitive_closure": {
                    "randexp": [
                         "0.4.6"
                    ],
                    "discontinuous-range": [
                         "1.0.0"
                    ],
                    "ret": [
                         "0.1.15"
                    ]
               },
               "lifecycle_build_target": False,
               "lifecycle_hooks_env": [],
               "lifecycle_hooks_execution_requirements": [],
               "lifecycle_hooks_no_sandbox": True
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
                    "attributes": {
                         "name": "aspect_rules_format_npm__randexp__0.4.6__links",
                         "generator_name": "aspect_rules_format_npm__randexp__0.4.6__links",
                         "generator_function": "format_register_toolchains",
                         "generator_location": None,
                         "package": "randexp",
                         "version": "0.4.6",
                         "root_package": "",
                         "link_packages": {},
                         "bins": {},
                         "deps": {
                              "discontinuous-range": "1.0.0",
                              "ret": "0.1.15"
                         },
                         "transitive_closure": {
                              "randexp": [
                                   "0.4.6"
                              ],
                              "discontinuous-range": [
                                   "1.0.0"
                              ],
                              "ret": [
                                   "0.1.15"
                              ]
                         },
                         "lifecycle_build_target": False,
                         "lifecycle_hooks_env": [],
                         "lifecycle_hooks_execution_requirements": [],
                         "lifecycle_hooks_no_sandbox": True
                    },
                    "output_tree_hash": "4a3bd8a6cb8afee1a5fa58760dff135908f590d6ef0f530088d01bc006d44436"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
          "definition_information": "Repository aspect_rules_format_npm__at_pkgr_utils__2.3.1__links instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:36:27: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/toolchains.bzl:13:21: in format_register_toolchains\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_format_npm/repositories.bzl:7:15: in npm_repositories\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:561:22: in npm_import\nRepository rule _npm_import_links defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:326:36: in <toplevel>\n",
          "original_attributes": {
               "name": "aspect_rules_format_npm__at_pkgr_utils__2.3.1__links",
               "generator_name": "aspect_rules_format_npm__at_pkgr_utils__2.3.1__links",
               "generator_function": "format_register_toolchains",
               "generator_location": None,
               "package": "@pkgr/utils",
               "version": "2.3.1",
               "root_package": "",
               "link_packages": {},
               "bins": {},
               "deps": {
                    "cross-spawn": "7.0.3",
                    "is-glob": "4.0.3",
                    "open": "8.4.2",
                    "picocolors": "1.0.0",
                    "tiny-glob": "0.2.9",
                    "tslib": "2.5.0"
               },
               "transitive_closure": {
                    "@pkgr/utils": [
                         "2.3.1"
                    ],
                    "cross-spawn": [
                         "7.0.3"
                    ],
                    "is-glob": [
                         "4.0.3"
                    ],
                    "open": [
                         "8.4.2"
                    ],
                    "picocolors": [
                         "1.0.0"
                    ],
                    "tiny-glob": [
                         "0.2.9"
                    ],
                    "tslib": [
                         "2.5.0"
                    ],
                    "globalyzer": [
                         "0.1.0"
                    ],
                    "globrex": [
                         "0.1.2"
                    ],
                    "define-lazy-prop": [
                         "2.0.0"
                    ],
                    "is-docker": [
                         "2.2.1"
                    ],
                    "is-wsl": [
                         "2.2.0"
                    ],
                    "is-extglob": [
                         "2.1.1"
                    ],
                    "path-key": [
                         "3.1.1"
                    ],
                    "shebang-command": [
                         "2.0.0"
                    ],
                    "which": [
                         "2.0.2"
                    ],
                    "isexe": [
                         "2.0.0"
                    ],
                    "shebang-regex": [
                         "3.0.0"
                    ]
               },
               "lifecycle_build_target": False,
               "lifecycle_hooks_env": [],
               "lifecycle_hooks_execution_requirements": [],
               "lifecycle_hooks_no_sandbox": True
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
                    "attributes": {
                         "name": "aspect_rules_format_npm__at_pkgr_utils__2.3.1__links",
                         "generator_name": "aspect_rules_format_npm__at_pkgr_utils__2.3.1__links",
                         "generator_function": "format_register_toolchains",
                         "generator_location": None,
                         "package": "@pkgr/utils",
                         "version": "2.3.1",
                         "root_package": "",
                         "link_packages": {},
                         "bins": {},
                         "deps": {
                              "cross-spawn": "7.0.3",
                              "is-glob": "4.0.3",
                              "open": "8.4.2",
                              "picocolors": "1.0.0",
                              "tiny-glob": "0.2.9",
                              "tslib": "2.5.0"
                         },
                         "transitive_closure": {
                              "@pkgr/utils": [
                                   "2.3.1"
                              ],
                              "cross-spawn": [
                                   "7.0.3"
                              ],
                              "is-glob": [
                                   "4.0.3"
                              ],
                              "open": [
                                   "8.4.2"
                              ],
                              "picocolors": [
                                   "1.0.0"
                              ],
                              "tiny-glob": [
                                   "0.2.9"
                              ],
                              "tslib": [
                                   "2.5.0"
                              ],
                              "globalyzer": [
                                   "0.1.0"
                              ],
                              "globrex": [
                                   "0.1.2"
                              ],
                              "define-lazy-prop": [
                                   "2.0.0"
                              ],
                              "is-docker": [
                                   "2.2.1"
                              ],
                              "is-wsl": [
                                   "2.2.0"
                              ],
                              "is-extglob": [
                                   "2.1.1"
                              ],
                              "path-key": [
                                   "3.1.1"
                              ],
                              "shebang-command": [
                                   "2.0.0"
                              ],
                              "which": [
                                   "2.0.2"
                              ],
                              "isexe": [
                                   "2.0.0"
                              ],
                              "shebang-regex": [
                                   "3.0.0"
                              ]
                         },
                         "lifecycle_build_target": False,
                         "lifecycle_hooks_env": [],
                         "lifecycle_hooks_execution_requirements": [],
                         "lifecycle_hooks_no_sandbox": True
                    },
                    "output_tree_hash": "202e011cbd8cbd98d6ba1117f0fb0f9ff7e816b28eb179a4604430d0eec55768"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_jar",
          "definition_information": "Repository google-java-format instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:6:26: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/repositories.bzl:93:13: in rules_format_dependencies\n  /home/andrzej/code/bazel/bazel-super-formatter/format/repositories.bzl:14:10: in http_jar\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\nRepository rule http_jar defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/http.bzl:530:27: in <toplevel>\n",
          "original_attributes": {
               "name": "google-java-format",
               "generator_name": "google-java-format",
               "generator_function": "rules_format_dependencies",
               "generator_location": None,
               "sha256": "33068bbbdce1099982ec1171f5e202898eb35f2919cf486141e439fc6e3a4203",
               "url": "https://github.com/google/google-java-format/releases/download/v1.17.0/google-java-format-1.17.0-all-deps.jar"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_jar",
                    "attributes": {
                         "sha256": "33068bbbdce1099982ec1171f5e202898eb35f2919cf486141e439fc6e3a4203",
                         "integrity": "",
                         "canonical_id": "",
                         "url": "https://github.com/google/google-java-format/releases/download/v1.17.0/google-java-format-1.17.0-all-deps.jar",
                         "urls": [],
                         "netrc": "",
                         "auth_patterns": {},
                         "downloaded_file_name": "downloaded.jar",
                         "name": "google-java-format"
                    },
                    "output_tree_hash": "22c94b2fa58f4f21b3750224689b490ba522f06b42a3036c50e53012b34c09b6"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
          "definition_information": "Repository aspect_rules_format_npm__argparse__2.0.1__links instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:36:27: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/toolchains.bzl:13:21: in format_register_toolchains\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_format_npm/repositories.bzl:46:15: in npm_repositories\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:561:22: in npm_import\nRepository rule _npm_import_links defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:326:36: in <toplevel>\n",
          "original_attributes": {
               "name": "aspect_rules_format_npm__argparse__2.0.1__links",
               "generator_name": "aspect_rules_format_npm__argparse__2.0.1__links",
               "generator_function": "format_register_toolchains",
               "generator_location": None,
               "package": "argparse",
               "version": "2.0.1",
               "root_package": "",
               "link_packages": {},
               "bins": {},
               "deps": {},
               "transitive_closure": {
                    "argparse": [
                         "2.0.1"
                    ]
               },
               "lifecycle_build_target": False,
               "lifecycle_hooks_env": [],
               "lifecycle_hooks_execution_requirements": [],
               "lifecycle_hooks_no_sandbox": True
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
                    "attributes": {
                         "name": "aspect_rules_format_npm__argparse__2.0.1__links",
                         "generator_name": "aspect_rules_format_npm__argparse__2.0.1__links",
                         "generator_function": "format_register_toolchains",
                         "generator_location": None,
                         "package": "argparse",
                         "version": "2.0.1",
                         "root_package": "",
                         "link_packages": {},
                         "bins": {},
                         "deps": {},
                         "transitive_closure": {
                              "argparse": [
                                   "2.0.1"
                              ]
                         },
                         "lifecycle_build_target": False,
                         "lifecycle_hooks_env": [],
                         "lifecycle_hooks_execution_requirements": [],
                         "lifecycle_hooks_no_sandbox": True
                    },
                    "output_tree_hash": "667973300af13433e27e1f7fc17bf441df15b150ebd4ffe55bfd02cbfaea4fc3"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
          "definition_information": "Repository aspect_rules_format_npm__commander__2.20.3__links instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:36:27: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/toolchains.bzl:13:21: in format_register_toolchains\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_format_npm/repositories.bzl:74:15: in npm_repositories\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:561:22: in npm_import\nRepository rule _npm_import_links defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:326:36: in <toplevel>\n",
          "original_attributes": {
               "name": "aspect_rules_format_npm__commander__2.20.3__links",
               "generator_name": "aspect_rules_format_npm__commander__2.20.3__links",
               "generator_function": "format_register_toolchains",
               "generator_location": None,
               "package": "commander",
               "version": "2.20.3",
               "root_package": "",
               "link_packages": {},
               "bins": {},
               "deps": {},
               "transitive_closure": {
                    "commander": [
                         "2.20.3"
                    ]
               },
               "lifecycle_build_target": False,
               "lifecycle_hooks_env": [],
               "lifecycle_hooks_execution_requirements": [],
               "lifecycle_hooks_no_sandbox": True
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
                    "attributes": {
                         "name": "aspect_rules_format_npm__commander__2.20.3__links",
                         "generator_name": "aspect_rules_format_npm__commander__2.20.3__links",
                         "generator_function": "format_register_toolchains",
                         "generator_location": None,
                         "package": "commander",
                         "version": "2.20.3",
                         "root_package": "",
                         "link_packages": {},
                         "bins": {},
                         "deps": {},
                         "transitive_closure": {
                              "commander": [
                                   "2.20.3"
                              ]
                         },
                         "lifecycle_build_target": False,
                         "lifecycle_hooks_env": [],
                         "lifecycle_hooks_execution_requirements": [],
                         "lifecycle_hooks_no_sandbox": True
                    },
                    "output_tree_hash": "65869e254b224cb34222a3ab772508c94269fbd5b20e9286eeb3c9d0c64353cd"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
          "definition_information": "Repository aspect_rules_format_npm__railroad-diagrams__1.0.0__links instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:36:27: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/toolchains.bzl:13:21: in format_register_toolchains\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_format_npm/repositories.bzl:534:15: in npm_repositories\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:561:22: in npm_import\nRepository rule _npm_import_links defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:326:36: in <toplevel>\n",
          "original_attributes": {
               "name": "aspect_rules_format_npm__railroad-diagrams__1.0.0__links",
               "generator_name": "aspect_rules_format_npm__railroad-diagrams__1.0.0__links",
               "generator_function": "format_register_toolchains",
               "generator_location": None,
               "package": "railroad-diagrams",
               "version": "1.0.0",
               "root_package": "",
               "link_packages": {},
               "bins": {},
               "deps": {},
               "transitive_closure": {
                    "railroad-diagrams": [
                         "1.0.0"
                    ]
               },
               "lifecycle_build_target": False,
               "lifecycle_hooks_env": [],
               "lifecycle_hooks_execution_requirements": [],
               "lifecycle_hooks_no_sandbox": True
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
                    "attributes": {
                         "name": "aspect_rules_format_npm__railroad-diagrams__1.0.0__links",
                         "generator_name": "aspect_rules_format_npm__railroad-diagrams__1.0.0__links",
                         "generator_function": "format_register_toolchains",
                         "generator_location": None,
                         "package": "railroad-diagrams",
                         "version": "1.0.0",
                         "root_package": "",
                         "link_packages": {},
                         "bins": {},
                         "deps": {},
                         "transitive_closure": {
                              "railroad-diagrams": [
                                   "1.0.0"
                              ]
                         },
                         "lifecycle_build_target": False,
                         "lifecycle_hooks_env": [],
                         "lifecycle_hooks_execution_requirements": [],
                         "lifecycle_hooks_no_sandbox": True
                    },
                    "output_tree_hash": "86ce0aa6b08a7245e968c3c530b53f01b3cb3a18cb598a78f2975a83fdec4d27"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
          "definition_information": "Repository aspect_rules_format_npm__big-integer__1.6.51__links instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:36:27: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/toolchains.bzl:13:21: in format_register_toolchains\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_format_npm/repositories.bzl:60:15: in npm_repositories\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:561:22: in npm_import\nRepository rule _npm_import_links defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:326:36: in <toplevel>\n",
          "original_attributes": {
               "name": "aspect_rules_format_npm__big-integer__1.6.51__links",
               "generator_name": "aspect_rules_format_npm__big-integer__1.6.51__links",
               "generator_function": "format_register_toolchains",
               "generator_location": None,
               "package": "big-integer",
               "version": "1.6.51",
               "root_package": "",
               "link_packages": {},
               "bins": {},
               "deps": {},
               "transitive_closure": {
                    "big-integer": [
                         "1.6.51"
                    ]
               },
               "lifecycle_build_target": False,
               "lifecycle_hooks_env": [],
               "lifecycle_hooks_execution_requirements": [],
               "lifecycle_hooks_no_sandbox": True
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
                    "attributes": {
                         "name": "aspect_rules_format_npm__big-integer__1.6.51__links",
                         "generator_name": "aspect_rules_format_npm__big-integer__1.6.51__links",
                         "generator_function": "format_register_toolchains",
                         "generator_location": None,
                         "package": "big-integer",
                         "version": "1.6.51",
                         "root_package": "",
                         "link_packages": {},
                         "bins": {},
                         "deps": {},
                         "transitive_closure": {
                              "big-integer": [
                                   "1.6.51"
                              ]
                         },
                         "lifecycle_build_target": False,
                         "lifecycle_hooks_env": [],
                         "lifecycle_hooks_execution_requirements": [],
                         "lifecycle_hooks_no_sandbox": True
                    },
                    "output_tree_hash": "14cf2a642a0f3f644b595a0e9752143ee7e8ba59401b114a1133adf732d0ae08"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
          "definition_information": "Repository aspect_rules_format_npm__define-lazy-prop__2.0.0__links instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:36:27: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/toolchains.bzl:13:21: in format_register_toolchains\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_format_npm/repositories.bzl:112:15: in npm_repositories\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:561:22: in npm_import\nRepository rule _npm_import_links defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:326:36: in <toplevel>\n",
          "original_attributes": {
               "name": "aspect_rules_format_npm__define-lazy-prop__2.0.0__links",
               "generator_name": "aspect_rules_format_npm__define-lazy-prop__2.0.0__links",
               "generator_function": "format_register_toolchains",
               "generator_location": None,
               "package": "define-lazy-prop",
               "version": "2.0.0",
               "root_package": "",
               "link_packages": {},
               "bins": {},
               "deps": {},
               "transitive_closure": {
                    "define-lazy-prop": [
                         "2.0.0"
                    ]
               },
               "lifecycle_build_target": False,
               "lifecycle_hooks_env": [],
               "lifecycle_hooks_execution_requirements": [],
               "lifecycle_hooks_no_sandbox": True
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
                    "attributes": {
                         "name": "aspect_rules_format_npm__define-lazy-prop__2.0.0__links",
                         "generator_name": "aspect_rules_format_npm__define-lazy-prop__2.0.0__links",
                         "generator_function": "format_register_toolchains",
                         "generator_location": None,
                         "package": "define-lazy-prop",
                         "version": "2.0.0",
                         "root_package": "",
                         "link_packages": {},
                         "bins": {},
                         "deps": {},
                         "transitive_closure": {
                              "define-lazy-prop": [
                                   "2.0.0"
                              ]
                         },
                         "lifecycle_build_target": False,
                         "lifecycle_hooks_env": [],
                         "lifecycle_hooks_execution_requirements": [],
                         "lifecycle_hooks_no_sandbox": True
                    },
                    "output_tree_hash": "d9f25b092ee92fdedd616211995afc7b7e40280659b65becefc196cdd96600f1"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
          "definition_information": "Repository aspect_rules_format_npm__discontinuous-range__1.0.0__links instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:36:27: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/toolchains.bzl:13:21: in format_register_toolchains\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_format_npm/repositories.bzl:126:15: in npm_repositories\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:561:22: in npm_import\nRepository rule _npm_import_links defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:326:36: in <toplevel>\n",
          "original_attributes": {
               "name": "aspect_rules_format_npm__discontinuous-range__1.0.0__links",
               "generator_name": "aspect_rules_format_npm__discontinuous-range__1.0.0__links",
               "generator_function": "format_register_toolchains",
               "generator_location": None,
               "package": "discontinuous-range",
               "version": "1.0.0",
               "root_package": "",
               "link_packages": {},
               "bins": {},
               "deps": {},
               "transitive_closure": {
                    "discontinuous-range": [
                         "1.0.0"
                    ]
               },
               "lifecycle_build_target": False,
               "lifecycle_hooks_env": [],
               "lifecycle_hooks_execution_requirements": [],
               "lifecycle_hooks_no_sandbox": True
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
                    "attributes": {
                         "name": "aspect_rules_format_npm__discontinuous-range__1.0.0__links",
                         "generator_name": "aspect_rules_format_npm__discontinuous-range__1.0.0__links",
                         "generator_function": "format_register_toolchains",
                         "generator_location": None,
                         "package": "discontinuous-range",
                         "version": "1.0.0",
                         "root_package": "",
                         "link_packages": {},
                         "bins": {},
                         "deps": {},
                         "transitive_closure": {
                              "discontinuous-range": [
                                   "1.0.0"
                              ]
                         },
                         "lifecycle_build_target": False,
                         "lifecycle_hooks_env": [],
                         "lifecycle_hooks_execution_requirements": [],
                         "lifecycle_hooks_no_sandbox": True
                    },
                    "output_tree_hash": "22d02989e179669f78881cb9c418af0b9e7036966cdfd5f02e5ec15da70e9147"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
          "definition_information": "Repository aspect_rules_format_npm__cross-spawn__7.0.3__links instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:36:27: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/toolchains.bzl:13:21: in format_register_toolchains\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_format_npm/repositories.bzl:88:15: in npm_repositories\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:561:22: in npm_import\nRepository rule _npm_import_links defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:326:36: in <toplevel>\n",
          "original_attributes": {
               "name": "aspect_rules_format_npm__cross-spawn__7.0.3__links",
               "generator_name": "aspect_rules_format_npm__cross-spawn__7.0.3__links",
               "generator_function": "format_register_toolchains",
               "generator_location": None,
               "package": "cross-spawn",
               "version": "7.0.3",
               "root_package": "",
               "link_packages": {},
               "bins": {},
               "deps": {
                    "path-key": "3.1.1",
                    "shebang-command": "2.0.0",
                    "which": "2.0.2"
               },
               "transitive_closure": {
                    "cross-spawn": [
                         "7.0.3"
                    ],
                    "path-key": [
                         "3.1.1"
                    ],
                    "shebang-command": [
                         "2.0.0"
                    ],
                    "which": [
                         "2.0.2"
                    ],
                    "isexe": [
                         "2.0.0"
                    ],
                    "shebang-regex": [
                         "3.0.0"
                    ]
               },
               "lifecycle_build_target": False,
               "lifecycle_hooks_env": [],
               "lifecycle_hooks_execution_requirements": [],
               "lifecycle_hooks_no_sandbox": True
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
                    "attributes": {
                         "name": "aspect_rules_format_npm__cross-spawn__7.0.3__links",
                         "generator_name": "aspect_rules_format_npm__cross-spawn__7.0.3__links",
                         "generator_function": "format_register_toolchains",
                         "generator_location": None,
                         "package": "cross-spawn",
                         "version": "7.0.3",
                         "root_package": "",
                         "link_packages": {},
                         "bins": {},
                         "deps": {
                              "path-key": "3.1.1",
                              "shebang-command": "2.0.0",
                              "which": "2.0.2"
                         },
                         "transitive_closure": {
                              "cross-spawn": [
                                   "7.0.3"
                              ],
                              "path-key": [
                                   "3.1.1"
                              ],
                              "shebang-command": [
                                   "2.0.0"
                              ],
                              "which": [
                                   "2.0.2"
                              ],
                              "isexe": [
                                   "2.0.0"
                              ],
                              "shebang-regex": [
                                   "3.0.0"
                              ]
                         },
                         "lifecycle_build_target": False,
                         "lifecycle_hooks_env": [],
                         "lifecycle_hooks_execution_requirements": [],
                         "lifecycle_hooks_no_sandbox": True
                    },
                    "output_tree_hash": "658fb2dbb0cf7b39f898684ac93571d253923e2acccd33e8a556de2831aa8096"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
          "definition_information": "Repository aspect_rules_format_npm__prettier__2.8.7__whkmnyg4gs3djzcukwmxxipg5m__links instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:36:27: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/toolchains.bzl:13:21: in format_register_toolchains\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_format_npm/repositories.bzl:480:15: in npm_repositories\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:561:22: in npm_import\nRepository rule _npm_import_links defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:326:36: in <toplevel>\n",
          "original_attributes": {
               "name": "aspect_rules_format_npm__prettier__2.8.7__whkmnyg4gs3djzcukwmxxipg5m__links",
               "generator_name": "aspect_rules_format_npm__prettier__2.8.7__whkmnyg4gs3djzcukwmxxipg5m__links",
               "generator_function": "format_register_toolchains",
               "generator_location": None,
               "package": "prettier",
               "version": "2.8.7_whkmnyg4gs3djzcukwmxxipg5m",
               "root_package": "",
               "link_packages": {
                    "": [
                         "prettier"
                    ]
               },
               "bins": {},
               "deps": {
                    "prettier-plugin-sh": "0.12.8_prettier@2.8.7",
                    "prettier-plugin-sql": "0.14.0_prettier@2.8.7"
               },
               "transitive_closure": {
                    "prettier": [
                         "2.8.7_whkmnyg4gs3djzcukwmxxipg5m"
                    ],
                    "prettier-plugin-sh": [
                         "0.12.8_prettier@2.8.7"
                    ],
                    "prettier-plugin-sql": [
                         "0.14.0_prettier@2.8.7"
                    ],
                    "node-sql-parser": [
                         "4.6.6"
                    ],
                    "sql-formatter": [
                         "12.2.0"
                    ],
                    "tslib": [
                         "2.5.0"
                    ],
                    "argparse": [
                         "2.0.1"
                    ],
                    "nearley": [
                         "2.20.1"
                    ],
                    "commander": [
                         "2.20.3"
                    ],
                    "moo": [
                         "0.5.2"
                    ],
                    "railroad-diagrams": [
                         "1.0.0"
                    ],
                    "randexp": [
                         "0.4.6"
                    ],
                    "discontinuous-range": [
                         "1.0.0"
                    ],
                    "ret": [
                         "0.1.15"
                    ],
                    "big-integer": [
                         "1.6.51"
                    ],
                    "mvdan-sh": [
                         "0.10.1"
                    ],
                    "sh-syntax": [
                         "0.3.7"
                    ],
                    "synckit": [
                         "0.8.5"
                    ],
                    "@pkgr/utils": [
                         "2.3.1"
                    ],
                    "cross-spawn": [
                         "7.0.3"
                    ],
                    "is-glob": [
                         "4.0.3"
                    ],
                    "open": [
                         "8.4.2"
                    ],
                    "picocolors": [
                         "1.0.0"
                    ],
                    "tiny-glob": [
                         "0.2.9"
                    ],
                    "globalyzer": [
                         "0.1.0"
                    ],
                    "globrex": [
                         "0.1.2"
                    ],
                    "define-lazy-prop": [
                         "2.0.0"
                    ],
                    "is-docker": [
                         "2.2.1"
                    ],
                    "is-wsl": [
                         "2.2.0"
                    ],
                    "is-extglob": [
                         "2.1.1"
                    ],
                    "path-key": [
                         "3.1.1"
                    ],
                    "shebang-command": [
                         "2.0.0"
                    ],
                    "which": [
                         "2.0.2"
                    ],
                    "isexe": [
                         "2.0.0"
                    ],
                    "shebang-regex": [
                         "3.0.0"
                    ]
               },
               "lifecycle_build_target": False,
               "lifecycle_hooks_env": [],
               "lifecycle_hooks_execution_requirements": [],
               "lifecycle_hooks_no_sandbox": True
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
                    "attributes": {
                         "name": "aspect_rules_format_npm__prettier__2.8.7__whkmnyg4gs3djzcukwmxxipg5m__links",
                         "generator_name": "aspect_rules_format_npm__prettier__2.8.7__whkmnyg4gs3djzcukwmxxipg5m__links",
                         "generator_function": "format_register_toolchains",
                         "generator_location": None,
                         "package": "prettier",
                         "version": "2.8.7_whkmnyg4gs3djzcukwmxxipg5m",
                         "root_package": "",
                         "link_packages": {
                              "": [
                                   "prettier"
                              ]
                         },
                         "bins": {},
                         "deps": {
                              "prettier-plugin-sh": "0.12.8_prettier@2.8.7",
                              "prettier-plugin-sql": "0.14.0_prettier@2.8.7"
                         },
                         "transitive_closure": {
                              "prettier": [
                                   "2.8.7_whkmnyg4gs3djzcukwmxxipg5m"
                              ],
                              "prettier-plugin-sh": [
                                   "0.12.8_prettier@2.8.7"
                              ],
                              "prettier-plugin-sql": [
                                   "0.14.0_prettier@2.8.7"
                              ],
                              "node-sql-parser": [
                                   "4.6.6"
                              ],
                              "sql-formatter": [
                                   "12.2.0"
                              ],
                              "tslib": [
                                   "2.5.0"
                              ],
                              "argparse": [
                                   "2.0.1"
                              ],
                              "nearley": [
                                   "2.20.1"
                              ],
                              "commander": [
                                   "2.20.3"
                              ],
                              "moo": [
                                   "0.5.2"
                              ],
                              "railroad-diagrams": [
                                   "1.0.0"
                              ],
                              "randexp": [
                                   "0.4.6"
                              ],
                              "discontinuous-range": [
                                   "1.0.0"
                              ],
                              "ret": [
                                   "0.1.15"
                              ],
                              "big-integer": [
                                   "1.6.51"
                              ],
                              "mvdan-sh": [
                                   "0.10.1"
                              ],
                              "sh-syntax": [
                                   "0.3.7"
                              ],
                              "synckit": [
                                   "0.8.5"
                              ],
                              "@pkgr/utils": [
                                   "2.3.1"
                              ],
                              "cross-spawn": [
                                   "7.0.3"
                              ],
                              "is-glob": [
                                   "4.0.3"
                              ],
                              "open": [
                                   "8.4.2"
                              ],
                              "picocolors": [
                                   "1.0.0"
                              ],
                              "tiny-glob": [
                                   "0.2.9"
                              ],
                              "globalyzer": [
                                   "0.1.0"
                              ],
                              "globrex": [
                                   "0.1.2"
                              ],
                              "define-lazy-prop": [
                                   "2.0.0"
                              ],
                              "is-docker": [
                                   "2.2.1"
                              ],
                              "is-wsl": [
                                   "2.2.0"
                              ],
                              "is-extglob": [
                                   "2.1.1"
                              ],
                              "path-key": [
                                   "3.1.1"
                              ],
                              "shebang-command": [
                                   "2.0.0"
                              ],
                              "which": [
                                   "2.0.2"
                              ],
                              "isexe": [
                                   "2.0.0"
                              ],
                              "shebang-regex": [
                                   "3.0.0"
                              ]
                         },
                         "lifecycle_build_target": False,
                         "lifecycle_hooks_env": [],
                         "lifecycle_hooks_execution_requirements": [],
                         "lifecycle_hooks_no_sandbox": True
                    },
                    "output_tree_hash": "5973370bbb56048cc176a1ea21503feea35fd1894d1d81d80d932ed4d7292f72"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
          "definition_information": "Repository aspect_rules_format_npm__globrex__0.1.2__links instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:36:27: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/toolchains.bzl:13:21: in format_register_toolchains\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_format_npm/repositories.bzl:154:15: in npm_repositories\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:561:22: in npm_import\nRepository rule _npm_import_links defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:326:36: in <toplevel>\n",
          "original_attributes": {
               "name": "aspect_rules_format_npm__globrex__0.1.2__links",
               "generator_name": "aspect_rules_format_npm__globrex__0.1.2__links",
               "generator_function": "format_register_toolchains",
               "generator_location": None,
               "package": "globrex",
               "version": "0.1.2",
               "root_package": "",
               "link_packages": {},
               "bins": {},
               "deps": {},
               "transitive_closure": {
                    "globrex": [
                         "0.1.2"
                    ]
               },
               "lifecycle_build_target": False,
               "lifecycle_hooks_env": [],
               "lifecycle_hooks_execution_requirements": [],
               "lifecycle_hooks_no_sandbox": True
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
                    "attributes": {
                         "name": "aspect_rules_format_npm__globrex__0.1.2__links",
                         "generator_name": "aspect_rules_format_npm__globrex__0.1.2__links",
                         "generator_function": "format_register_toolchains",
                         "generator_location": None,
                         "package": "globrex",
                         "version": "0.1.2",
                         "root_package": "",
                         "link_packages": {},
                         "bins": {},
                         "deps": {},
                         "transitive_closure": {
                              "globrex": [
                                   "0.1.2"
                              ]
                         },
                         "lifecycle_build_target": False,
                         "lifecycle_hooks_env": [],
                         "lifecycle_hooks_execution_requirements": [],
                         "lifecycle_hooks_no_sandbox": True
                    },
                    "output_tree_hash": "49b5bb137fae4e8a3935055da06c7f9b6418440606666f058d40d2278509222f"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
          "definition_information": "Repository aspect_rules_format_npm__globalyzer__0.1.0__links instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:36:27: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/toolchains.bzl:13:21: in format_register_toolchains\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_format_npm/repositories.bzl:140:15: in npm_repositories\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:561:22: in npm_import\nRepository rule _npm_import_links defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:326:36: in <toplevel>\n",
          "original_attributes": {
               "name": "aspect_rules_format_npm__globalyzer__0.1.0__links",
               "generator_name": "aspect_rules_format_npm__globalyzer__0.1.0__links",
               "generator_function": "format_register_toolchains",
               "generator_location": None,
               "package": "globalyzer",
               "version": "0.1.0",
               "root_package": "",
               "link_packages": {},
               "bins": {},
               "deps": {},
               "transitive_closure": {
                    "globalyzer": [
                         "0.1.0"
                    ]
               },
               "lifecycle_build_target": False,
               "lifecycle_hooks_env": [],
               "lifecycle_hooks_execution_requirements": [],
               "lifecycle_hooks_no_sandbox": True
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
                    "attributes": {
                         "name": "aspect_rules_format_npm__globalyzer__0.1.0__links",
                         "generator_name": "aspect_rules_format_npm__globalyzer__0.1.0__links",
                         "generator_function": "format_register_toolchains",
                         "generator_location": None,
                         "package": "globalyzer",
                         "version": "0.1.0",
                         "root_package": "",
                         "link_packages": {},
                         "bins": {},
                         "deps": {},
                         "transitive_closure": {
                              "globalyzer": [
                                   "0.1.0"
                              ]
                         },
                         "lifecycle_build_target": False,
                         "lifecycle_hooks_env": [],
                         "lifecycle_hooks_execution_requirements": [],
                         "lifecycle_hooks_no_sandbox": True
                    },
                    "output_tree_hash": "b5275533549f78978ee2f39d442b3ff51e86751df92cd34196c32f3f846c9cf5"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
          "definition_information": "Repository aspect_rules_format_npm__is-extglob__2.1.1__links instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:36:27: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/toolchains.bzl:13:21: in format_register_toolchains\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_format_npm/repositories.bzl:182:15: in npm_repositories\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:561:22: in npm_import\nRepository rule _npm_import_links defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:326:36: in <toplevel>\n",
          "original_attributes": {
               "name": "aspect_rules_format_npm__is-extglob__2.1.1__links",
               "generator_name": "aspect_rules_format_npm__is-extglob__2.1.1__links",
               "generator_function": "format_register_toolchains",
               "generator_location": None,
               "package": "is-extglob",
               "version": "2.1.1",
               "root_package": "",
               "link_packages": {},
               "bins": {},
               "deps": {},
               "transitive_closure": {
                    "is-extglob": [
                         "2.1.1"
                    ]
               },
               "lifecycle_build_target": False,
               "lifecycle_hooks_env": [],
               "lifecycle_hooks_execution_requirements": [],
               "lifecycle_hooks_no_sandbox": True
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
                    "attributes": {
                         "name": "aspect_rules_format_npm__is-extglob__2.1.1__links",
                         "generator_name": "aspect_rules_format_npm__is-extglob__2.1.1__links",
                         "generator_function": "format_register_toolchains",
                         "generator_location": None,
                         "package": "is-extglob",
                         "version": "2.1.1",
                         "root_package": "",
                         "link_packages": {},
                         "bins": {},
                         "deps": {},
                         "transitive_closure": {
                              "is-extglob": [
                                   "2.1.1"
                              ]
                         },
                         "lifecycle_build_target": False,
                         "lifecycle_hooks_env": [],
                         "lifecycle_hooks_execution_requirements": [],
                         "lifecycle_hooks_no_sandbox": True
                    },
                    "output_tree_hash": "dd3507f834295de81555bd6ceb3931de42adebba15646fc76acf5f3f86199e80"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
          "definition_information": "Repository aspect_rules_format_npm__isexe__2.0.0__links instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:36:27: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/toolchains.bzl:13:21: in format_register_toolchains\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_format_npm/repositories.bzl:232:15: in npm_repositories\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:561:22: in npm_import\nRepository rule _npm_import_links defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:326:36: in <toplevel>\n",
          "original_attributes": {
               "name": "aspect_rules_format_npm__isexe__2.0.0__links",
               "generator_name": "aspect_rules_format_npm__isexe__2.0.0__links",
               "generator_function": "format_register_toolchains",
               "generator_location": None,
               "package": "isexe",
               "version": "2.0.0",
               "root_package": "",
               "link_packages": {},
               "bins": {},
               "deps": {},
               "transitive_closure": {
                    "isexe": [
                         "2.0.0"
                    ]
               },
               "lifecycle_build_target": False,
               "lifecycle_hooks_env": [],
               "lifecycle_hooks_execution_requirements": [],
               "lifecycle_hooks_no_sandbox": True
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
                    "attributes": {
                         "name": "aspect_rules_format_npm__isexe__2.0.0__links",
                         "generator_name": "aspect_rules_format_npm__isexe__2.0.0__links",
                         "generator_function": "format_register_toolchains",
                         "generator_location": None,
                         "package": "isexe",
                         "version": "2.0.0",
                         "root_package": "",
                         "link_packages": {},
                         "bins": {},
                         "deps": {},
                         "transitive_closure": {
                              "isexe": [
                                   "2.0.0"
                              ]
                         },
                         "lifecycle_build_target": False,
                         "lifecycle_hooks_env": [],
                         "lifecycle_hooks_execution_requirements": [],
                         "lifecycle_hooks_no_sandbox": True
                    },
                    "output_tree_hash": "99748060d579dd282c636da12da798839cf19b2051ca51d361329903c850b4e2"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
          "definition_information": "Repository aspect_rules_format_npm__prettier-plugin-sql__0.14.0__prettier_2.8.7__links instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:36:27: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/toolchains.bzl:13:21: in format_register_toolchains\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_format_npm/repositories.bzl:424:15: in npm_repositories\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:561:22: in npm_import\nRepository rule _npm_import_links defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:326:36: in <toplevel>\n",
          "original_attributes": {
               "name": "aspect_rules_format_npm__prettier-plugin-sql__0.14.0__prettier_2.8.7__links",
               "generator_name": "aspect_rules_format_npm__prettier-plugin-sql__0.14.0__prettier_2.8.7__links",
               "generator_function": "format_register_toolchains",
               "generator_location": None,
               "package": "prettier-plugin-sql",
               "version": "0.14.0_prettier@2.8.7",
               "root_package": "",
               "link_packages": {
                    "": [
                         "prettier-plugin-sql"
                    ]
               },
               "bins": {},
               "deps": {
                    "node-sql-parser": "4.6.6",
                    "prettier": "2.8.7_whkmnyg4gs3djzcukwmxxipg5m",
                    "sql-formatter": "12.2.0",
                    "tslib": "2.5.0"
               },
               "transitive_closure": {
                    "prettier-plugin-sql": [
                         "0.14.0_prettier@2.8.7"
                    ],
                    "node-sql-parser": [
                         "4.6.6"
                    ],
                    "prettier": [
                         "2.8.7_whkmnyg4gs3djzcukwmxxipg5m"
                    ],
                    "sql-formatter": [
                         "12.2.0"
                    ],
                    "tslib": [
                         "2.5.0"
                    ],
                    "argparse": [
                         "2.0.1"
                    ],
                    "nearley": [
                         "2.20.1"
                    ],
                    "commander": [
                         "2.20.3"
                    ],
                    "moo": [
                         "0.5.2"
                    ],
                    "railroad-diagrams": [
                         "1.0.0"
                    ],
                    "randexp": [
                         "0.4.6"
                    ],
                    "discontinuous-range": [
                         "1.0.0"
                    ],
                    "ret": [
                         "0.1.15"
                    ],
                    "prettier-plugin-sh": [
                         "0.12.8_prettier@2.8.7"
                    ],
                    "mvdan-sh": [
                         "0.10.1"
                    ],
                    "sh-syntax": [
                         "0.3.7"
                    ],
                    "synckit": [
                         "0.8.5"
                    ],
                    "@pkgr/utils": [
                         "2.3.1"
                    ],
                    "cross-spawn": [
                         "7.0.3"
                    ],
                    "is-glob": [
                         "4.0.3"
                    ],
                    "open": [
                         "8.4.2"
                    ],
                    "picocolors": [
                         "1.0.0"
                    ],
                    "tiny-glob": [
                         "0.2.9"
                    ],
                    "globalyzer": [
                         "0.1.0"
                    ],
                    "globrex": [
                         "0.1.2"
                    ],
                    "define-lazy-prop": [
                         "2.0.0"
                    ],
                    "is-docker": [
                         "2.2.1"
                    ],
                    "is-wsl": [
                         "2.2.0"
                    ],
                    "is-extglob": [
                         "2.1.1"
                    ],
                    "path-key": [
                         "3.1.1"
                    ],
                    "shebang-command": [
                         "2.0.0"
                    ],
                    "which": [
                         "2.0.2"
                    ],
                    "isexe": [
                         "2.0.0"
                    ],
                    "shebang-regex": [
                         "3.0.0"
                    ],
                    "big-integer": [
                         "1.6.51"
                    ]
               },
               "lifecycle_build_target": False,
               "lifecycle_hooks_env": [],
               "lifecycle_hooks_execution_requirements": [],
               "lifecycle_hooks_no_sandbox": True
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
                    "attributes": {
                         "name": "aspect_rules_format_npm__prettier-plugin-sql__0.14.0__prettier_2.8.7__links",
                         "generator_name": "aspect_rules_format_npm__prettier-plugin-sql__0.14.0__prettier_2.8.7__links",
                         "generator_function": "format_register_toolchains",
                         "generator_location": None,
                         "package": "prettier-plugin-sql",
                         "version": "0.14.0_prettier@2.8.7",
                         "root_package": "",
                         "link_packages": {
                              "": [
                                   "prettier-plugin-sql"
                              ]
                         },
                         "bins": {},
                         "deps": {
                              "node-sql-parser": "4.6.6",
                              "prettier": "2.8.7_whkmnyg4gs3djzcukwmxxipg5m",
                              "sql-formatter": "12.2.0",
                              "tslib": "2.5.0"
                         },
                         "transitive_closure": {
                              "prettier-plugin-sql": [
                                   "0.14.0_prettier@2.8.7"
                              ],
                              "node-sql-parser": [
                                   "4.6.6"
                              ],
                              "prettier": [
                                   "2.8.7_whkmnyg4gs3djzcukwmxxipg5m"
                              ],
                              "sql-formatter": [
                                   "12.2.0"
                              ],
                              "tslib": [
                                   "2.5.0"
                              ],
                              "argparse": [
                                   "2.0.1"
                              ],
                              "nearley": [
                                   "2.20.1"
                              ],
                              "commander": [
                                   "2.20.3"
                              ],
                              "moo": [
                                   "0.5.2"
                              ],
                              "railroad-diagrams": [
                                   "1.0.0"
                              ],
                              "randexp": [
                                   "0.4.6"
                              ],
                              "discontinuous-range": [
                                   "1.0.0"
                              ],
                              "ret": [
                                   "0.1.15"
                              ],
                              "prettier-plugin-sh": [
                                   "0.12.8_prettier@2.8.7"
                              ],
                              "mvdan-sh": [
                                   "0.10.1"
                              ],
                              "sh-syntax": [
                                   "0.3.7"
                              ],
                              "synckit": [
                                   "0.8.5"
                              ],
                              "@pkgr/utils": [
                                   "2.3.1"
                              ],
                              "cross-spawn": [
                                   "7.0.3"
                              ],
                              "is-glob": [
                                   "4.0.3"
                              ],
                              "open": [
                                   "8.4.2"
                              ],
                              "picocolors": [
                                   "1.0.0"
                              ],
                              "tiny-glob": [
                                   "0.2.9"
                              ],
                              "globalyzer": [
                                   "0.1.0"
                              ],
                              "globrex": [
                                   "0.1.2"
                              ],
                              "define-lazy-prop": [
                                   "2.0.0"
                              ],
                              "is-docker": [
                                   "2.2.1"
                              ],
                              "is-wsl": [
                                   "2.2.0"
                              ],
                              "is-extglob": [
                                   "2.1.1"
                              ],
                              "path-key": [
                                   "3.1.1"
                              ],
                              "shebang-command": [
                                   "2.0.0"
                              ],
                              "which": [
                                   "2.0.2"
                              ],
                              "isexe": [
                                   "2.0.0"
                              ],
                              "shebang-regex": [
                                   "3.0.0"
                              ],
                              "big-integer": [
                                   "1.6.51"
                              ]
                         },
                         "lifecycle_build_target": False,
                         "lifecycle_hooks_env": [],
                         "lifecycle_hooks_execution_requirements": [],
                         "lifecycle_hooks_no_sandbox": True
                    },
                    "output_tree_hash": "e2ae7de289e86b053f1c87d7ccdbfb8bf7ede961bdb788733da28196139c13bc"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
          "definition_information": "Repository aspect_rules_format_npm__is-wsl__2.2.0__links instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:36:27: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/toolchains.bzl:13:21: in format_register_toolchains\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_format_npm/repositories.bzl:214:15: in npm_repositories\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:561:22: in npm_import\nRepository rule _npm_import_links defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:326:36: in <toplevel>\n",
          "original_attributes": {
               "name": "aspect_rules_format_npm__is-wsl__2.2.0__links",
               "generator_name": "aspect_rules_format_npm__is-wsl__2.2.0__links",
               "generator_function": "format_register_toolchains",
               "generator_location": None,
               "package": "is-wsl",
               "version": "2.2.0",
               "root_package": "",
               "link_packages": {},
               "bins": {},
               "deps": {
                    "is-docker": "2.2.1"
               },
               "transitive_closure": {
                    "is-wsl": [
                         "2.2.0"
                    ],
                    "is-docker": [
                         "2.2.1"
                    ]
               },
               "lifecycle_build_target": False,
               "lifecycle_hooks_env": [],
               "lifecycle_hooks_execution_requirements": [],
               "lifecycle_hooks_no_sandbox": True
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
                    "attributes": {
                         "name": "aspect_rules_format_npm__is-wsl__2.2.0__links",
                         "generator_name": "aspect_rules_format_npm__is-wsl__2.2.0__links",
                         "generator_function": "format_register_toolchains",
                         "generator_location": None,
                         "package": "is-wsl",
                         "version": "2.2.0",
                         "root_package": "",
                         "link_packages": {},
                         "bins": {},
                         "deps": {
                              "is-docker": "2.2.1"
                         },
                         "transitive_closure": {
                              "is-wsl": [
                                   "2.2.0"
                              ],
                              "is-docker": [
                                   "2.2.1"
                              ]
                         },
                         "lifecycle_build_target": False,
                         "lifecycle_hooks_env": [],
                         "lifecycle_hooks_execution_requirements": [],
                         "lifecycle_hooks_no_sandbox": True
                    },
                    "output_tree_hash": "b91b888957bf124d57388c2f36f0dec2d431f2040edb6f2ec6ad8f46183c8f4f"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
          "definition_information": "Repository aspect_rules_format_npm__is-glob__4.0.3__links instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:36:27: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/toolchains.bzl:13:21: in format_register_toolchains\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_format_npm/repositories.bzl:196:15: in npm_repositories\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:561:22: in npm_import\nRepository rule _npm_import_links defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:326:36: in <toplevel>\n",
          "original_attributes": {
               "name": "aspect_rules_format_npm__is-glob__4.0.3__links",
               "generator_name": "aspect_rules_format_npm__is-glob__4.0.3__links",
               "generator_function": "format_register_toolchains",
               "generator_location": None,
               "package": "is-glob",
               "version": "4.0.3",
               "root_package": "",
               "link_packages": {},
               "bins": {},
               "deps": {
                    "is-extglob": "2.1.1"
               },
               "transitive_closure": {
                    "is-glob": [
                         "4.0.3"
                    ],
                    "is-extglob": [
                         "2.1.1"
                    ]
               },
               "lifecycle_build_target": False,
               "lifecycle_hooks_env": [],
               "lifecycle_hooks_execution_requirements": [],
               "lifecycle_hooks_no_sandbox": True
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
                    "attributes": {
                         "name": "aspect_rules_format_npm__is-glob__4.0.3__links",
                         "generator_name": "aspect_rules_format_npm__is-glob__4.0.3__links",
                         "generator_function": "format_register_toolchains",
                         "generator_location": None,
                         "package": "is-glob",
                         "version": "4.0.3",
                         "root_package": "",
                         "link_packages": {},
                         "bins": {},
                         "deps": {
                              "is-extglob": "2.1.1"
                         },
                         "transitive_closure": {
                              "is-glob": [
                                   "4.0.3"
                              ],
                              "is-extglob": [
                                   "2.1.1"
                              ]
                         },
                         "lifecycle_build_target": False,
                         "lifecycle_hooks_env": [],
                         "lifecycle_hooks_execution_requirements": [],
                         "lifecycle_hooks_no_sandbox": True
                    },
                    "output_tree_hash": "033f4406215564532ffe53e5fbe21c0f244f863a44d08eac30b6e01cd3facece"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
          "definition_information": "Repository aspect_rules_format_npm__moo__0.5.2__links instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:36:27: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/toolchains.bzl:13:21: in format_register_toolchains\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_format_npm/repositories.bzl:246:15: in npm_repositories\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:561:22: in npm_import\nRepository rule _npm_import_links defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:326:36: in <toplevel>\n",
          "original_attributes": {
               "name": "aspect_rules_format_npm__moo__0.5.2__links",
               "generator_name": "aspect_rules_format_npm__moo__0.5.2__links",
               "generator_function": "format_register_toolchains",
               "generator_location": None,
               "package": "moo",
               "version": "0.5.2",
               "root_package": "",
               "link_packages": {},
               "bins": {},
               "deps": {},
               "transitive_closure": {
                    "moo": [
                         "0.5.2"
                    ]
               },
               "lifecycle_build_target": False,
               "lifecycle_hooks_env": [],
               "lifecycle_hooks_execution_requirements": [],
               "lifecycle_hooks_no_sandbox": True
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
                    "attributes": {
                         "name": "aspect_rules_format_npm__moo__0.5.2__links",
                         "generator_name": "aspect_rules_format_npm__moo__0.5.2__links",
                         "generator_function": "format_register_toolchains",
                         "generator_location": None,
                         "package": "moo",
                         "version": "0.5.2",
                         "root_package": "",
                         "link_packages": {},
                         "bins": {},
                         "deps": {},
                         "transitive_closure": {
                              "moo": [
                                   "0.5.2"
                              ]
                         },
                         "lifecycle_build_target": False,
                         "lifecycle_hooks_env": [],
                         "lifecycle_hooks_execution_requirements": [],
                         "lifecycle_hooks_no_sandbox": True
                    },
                    "output_tree_hash": "5df5f7305cdf004c4b5a2ba21c798639560af498cd5357ab479d10dcb752d15f"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
          "definition_information": "Repository aspect_rules_format_npm__mvdan-sh__0.10.1__links instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:36:27: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/toolchains.bzl:13:21: in format_register_toolchains\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_format_npm/repositories.bzl:260:15: in npm_repositories\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:561:22: in npm_import\nRepository rule _npm_import_links defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:326:36: in <toplevel>\n",
          "original_attributes": {
               "name": "aspect_rules_format_npm__mvdan-sh__0.10.1__links",
               "generator_name": "aspect_rules_format_npm__mvdan-sh__0.10.1__links",
               "generator_function": "format_register_toolchains",
               "generator_location": None,
               "package": "mvdan-sh",
               "version": "0.10.1",
               "root_package": "",
               "link_packages": {},
               "bins": {},
               "deps": {},
               "transitive_closure": {
                    "mvdan-sh": [
                         "0.10.1"
                    ]
               },
               "lifecycle_build_target": False,
               "lifecycle_hooks_env": [],
               "lifecycle_hooks_execution_requirements": [],
               "lifecycle_hooks_no_sandbox": True
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
                    "attributes": {
                         "name": "aspect_rules_format_npm__mvdan-sh__0.10.1__links",
                         "generator_name": "aspect_rules_format_npm__mvdan-sh__0.10.1__links",
                         "generator_function": "format_register_toolchains",
                         "generator_location": None,
                         "package": "mvdan-sh",
                         "version": "0.10.1",
                         "root_package": "",
                         "link_packages": {},
                         "bins": {},
                         "deps": {},
                         "transitive_closure": {
                              "mvdan-sh": [
                                   "0.10.1"
                              ]
                         },
                         "lifecycle_build_target": False,
                         "lifecycle_hooks_env": [],
                         "lifecycle_hooks_execution_requirements": [],
                         "lifecycle_hooks_no_sandbox": True
                    },
                    "output_tree_hash": "ad6743451f3399d29b2f596bf9d9cc91da15bfcba485b442aaf94913f3520f32"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
          "definition_information": "Repository aspect_rules_format_npm__nearley__2.20.1__links instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:36:27: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/toolchains.bzl:13:21: in format_register_toolchains\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_format_npm/repositories.bzl:274:15: in npm_repositories\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:561:22: in npm_import\nRepository rule _npm_import_links defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:326:36: in <toplevel>\n",
          "original_attributes": {
               "name": "aspect_rules_format_npm__nearley__2.20.1__links",
               "generator_name": "aspect_rules_format_npm__nearley__2.20.1__links",
               "generator_function": "format_register_toolchains",
               "generator_location": None,
               "package": "nearley",
               "version": "2.20.1",
               "root_package": "",
               "link_packages": {},
               "bins": {},
               "deps": {
                    "commander": "2.20.3",
                    "moo": "0.5.2",
                    "railroad-diagrams": "1.0.0",
                    "randexp": "0.4.6"
               },
               "transitive_closure": {
                    "nearley": [
                         "2.20.1"
                    ],
                    "commander": [
                         "2.20.3"
                    ],
                    "moo": [
                         "0.5.2"
                    ],
                    "railroad-diagrams": [
                         "1.0.0"
                    ],
                    "randexp": [
                         "0.4.6"
                    ],
                    "discontinuous-range": [
                         "1.0.0"
                    ],
                    "ret": [
                         "0.1.15"
                    ]
               },
               "lifecycle_build_target": False,
               "lifecycle_hooks_env": [],
               "lifecycle_hooks_execution_requirements": [],
               "lifecycle_hooks_no_sandbox": True
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
                    "attributes": {
                         "name": "aspect_rules_format_npm__nearley__2.20.1__links",
                         "generator_name": "aspect_rules_format_npm__nearley__2.20.1__links",
                         "generator_function": "format_register_toolchains",
                         "generator_location": None,
                         "package": "nearley",
                         "version": "2.20.1",
                         "root_package": "",
                         "link_packages": {},
                         "bins": {},
                         "deps": {
                              "commander": "2.20.3",
                              "moo": "0.5.2",
                              "railroad-diagrams": "1.0.0",
                              "randexp": "0.4.6"
                         },
                         "transitive_closure": {
                              "nearley": [
                                   "2.20.1"
                              ],
                              "commander": [
                                   "2.20.3"
                              ],
                              "moo": [
                                   "0.5.2"
                              ],
                              "railroad-diagrams": [
                                   "1.0.0"
                              ],
                              "randexp": [
                                   "0.4.6"
                              ],
                              "discontinuous-range": [
                                   "1.0.0"
                              ],
                              "ret": [
                                   "0.1.15"
                              ]
                         },
                         "lifecycle_build_target": False,
                         "lifecycle_hooks_env": [],
                         "lifecycle_hooks_execution_requirements": [],
                         "lifecycle_hooks_no_sandbox": True
                    },
                    "output_tree_hash": "340a1818eff666d3c5ef2c078ab9ae63ff5d3d602352dc143f9500eff80b13f4"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
          "definition_information": "Repository aspect_rules_format_npm__prettier-plugin-sh__0.12.8__prettier_2.8.7__links instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:36:27: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/toolchains.bzl:13:21: in format_register_toolchains\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_format_npm/repositories.bzl:368:15: in npm_repositories\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:561:22: in npm_import\nRepository rule _npm_import_links defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:326:36: in <toplevel>\n",
          "original_attributes": {
               "name": "aspect_rules_format_npm__prettier-plugin-sh__0.12.8__prettier_2.8.7__links",
               "generator_name": "aspect_rules_format_npm__prettier-plugin-sh__0.12.8__prettier_2.8.7__links",
               "generator_function": "format_register_toolchains",
               "generator_location": None,
               "package": "prettier-plugin-sh",
               "version": "0.12.8_prettier@2.8.7",
               "root_package": "",
               "link_packages": {
                    "": [
                         "prettier-plugin-sh"
                    ]
               },
               "bins": {},
               "deps": {
                    "mvdan-sh": "0.10.1",
                    "prettier": "2.8.7_whkmnyg4gs3djzcukwmxxipg5m",
                    "sh-syntax": "0.3.7",
                    "synckit": "0.8.5"
               },
               "transitive_closure": {
                    "prettier-plugin-sh": [
                         "0.12.8_prettier@2.8.7"
                    ],
                    "mvdan-sh": [
                         "0.10.1"
                    ],
                    "prettier": [
                         "2.8.7_whkmnyg4gs3djzcukwmxxipg5m"
                    ],
                    "sh-syntax": [
                         "0.3.7"
                    ],
                    "synckit": [
                         "0.8.5"
                    ],
                    "@pkgr/utils": [
                         "2.3.1"
                    ],
                    "tslib": [
                         "2.5.0"
                    ],
                    "cross-spawn": [
                         "7.0.3"
                    ],
                    "is-glob": [
                         "4.0.3"
                    ],
                    "open": [
                         "8.4.2"
                    ],
                    "picocolors": [
                         "1.0.0"
                    ],
                    "tiny-glob": [
                         "0.2.9"
                    ],
                    "globalyzer": [
                         "0.1.0"
                    ],
                    "globrex": [
                         "0.1.2"
                    ],
                    "define-lazy-prop": [
                         "2.0.0"
                    ],
                    "is-docker": [
                         "2.2.1"
                    ],
                    "is-wsl": [
                         "2.2.0"
                    ],
                    "is-extglob": [
                         "2.1.1"
                    ],
                    "path-key": [
                         "3.1.1"
                    ],
                    "shebang-command": [
                         "2.0.0"
                    ],
                    "which": [
                         "2.0.2"
                    ],
                    "isexe": [
                         "2.0.0"
                    ],
                    "shebang-regex": [
                         "3.0.0"
                    ],
                    "prettier-plugin-sql": [
                         "0.14.0_prettier@2.8.7"
                    ],
                    "node-sql-parser": [
                         "4.6.6"
                    ],
                    "sql-formatter": [
                         "12.2.0"
                    ],
                    "argparse": [
                         "2.0.1"
                    ],
                    "nearley": [
                         "2.20.1"
                    ],
                    "commander": [
                         "2.20.3"
                    ],
                    "moo": [
                         "0.5.2"
                    ],
                    "railroad-diagrams": [
                         "1.0.0"
                    ],
                    "randexp": [
                         "0.4.6"
                    ],
                    "discontinuous-range": [
                         "1.0.0"
                    ],
                    "ret": [
                         "0.1.15"
                    ],
                    "big-integer": [
                         "1.6.51"
                    ]
               },
               "lifecycle_build_target": False,
               "lifecycle_hooks_env": [],
               "lifecycle_hooks_execution_requirements": [],
               "lifecycle_hooks_no_sandbox": True
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
                    "attributes": {
                         "name": "aspect_rules_format_npm__prettier-plugin-sh__0.12.8__prettier_2.8.7__links",
                         "generator_name": "aspect_rules_format_npm__prettier-plugin-sh__0.12.8__prettier_2.8.7__links",
                         "generator_function": "format_register_toolchains",
                         "generator_location": None,
                         "package": "prettier-plugin-sh",
                         "version": "0.12.8_prettier@2.8.7",
                         "root_package": "",
                         "link_packages": {
                              "": [
                                   "prettier-plugin-sh"
                              ]
                         },
                         "bins": {},
                         "deps": {
                              "mvdan-sh": "0.10.1",
                              "prettier": "2.8.7_whkmnyg4gs3djzcukwmxxipg5m",
                              "sh-syntax": "0.3.7",
                              "synckit": "0.8.5"
                         },
                         "transitive_closure": {
                              "prettier-plugin-sh": [
                                   "0.12.8_prettier@2.8.7"
                              ],
                              "mvdan-sh": [
                                   "0.10.1"
                              ],
                              "prettier": [
                                   "2.8.7_whkmnyg4gs3djzcukwmxxipg5m"
                              ],
                              "sh-syntax": [
                                   "0.3.7"
                              ],
                              "synckit": [
                                   "0.8.5"
                              ],
                              "@pkgr/utils": [
                                   "2.3.1"
                              ],
                              "tslib": [
                                   "2.5.0"
                              ],
                              "cross-spawn": [
                                   "7.0.3"
                              ],
                              "is-glob": [
                                   "4.0.3"
                              ],
                              "open": [
                                   "8.4.2"
                              ],
                              "picocolors": [
                                   "1.0.0"
                              ],
                              "tiny-glob": [
                                   "0.2.9"
                              ],
                              "globalyzer": [
                                   "0.1.0"
                              ],
                              "globrex": [
                                   "0.1.2"
                              ],
                              "define-lazy-prop": [
                                   "2.0.0"
                              ],
                              "is-docker": [
                                   "2.2.1"
                              ],
                              "is-wsl": [
                                   "2.2.0"
                              ],
                              "is-extglob": [
                                   "2.1.1"
                              ],
                              "path-key": [
                                   "3.1.1"
                              ],
                              "shebang-command": [
                                   "2.0.0"
                              ],
                              "which": [
                                   "2.0.2"
                              ],
                              "isexe": [
                                   "2.0.0"
                              ],
                              "shebang-regex": [
                                   "3.0.0"
                              ],
                              "prettier-plugin-sql": [
                                   "0.14.0_prettier@2.8.7"
                              ],
                              "node-sql-parser": [
                                   "4.6.6"
                              ],
                              "sql-formatter": [
                                   "12.2.0"
                              ],
                              "argparse": [
                                   "2.0.1"
                              ],
                              "nearley": [
                                   "2.20.1"
                              ],
                              "commander": [
                                   "2.20.3"
                              ],
                              "moo": [
                                   "0.5.2"
                              ],
                              "railroad-diagrams": [
                                   "1.0.0"
                              ],
                              "randexp": [
                                   "0.4.6"
                              ],
                              "discontinuous-range": [
                                   "1.0.0"
                              ],
                              "ret": [
                                   "0.1.15"
                              ],
                              "big-integer": [
                                   "1.6.51"
                              ]
                         },
                         "lifecycle_build_target": False,
                         "lifecycle_hooks_env": [],
                         "lifecycle_hooks_execution_requirements": [],
                         "lifecycle_hooks_no_sandbox": True
                    },
                    "output_tree_hash": "d6f89c566f3589c368a4c93110b3bdc81ba66c52d3693abac2c78ce4a3bd2fc7"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
          "definition_information": "Repository aspect_rules_format_npm__is-docker__2.2.1__links instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:36:27: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/toolchains.bzl:13:21: in format_register_toolchains\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_format_npm/repositories.bzl:168:15: in npm_repositories\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:561:22: in npm_import\nRepository rule _npm_import_links defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:326:36: in <toplevel>\n",
          "original_attributes": {
               "name": "aspect_rules_format_npm__is-docker__2.2.1__links",
               "generator_name": "aspect_rules_format_npm__is-docker__2.2.1__links",
               "generator_function": "format_register_toolchains",
               "generator_location": None,
               "package": "is-docker",
               "version": "2.2.1",
               "root_package": "",
               "link_packages": {},
               "bins": {},
               "deps": {},
               "transitive_closure": {
                    "is-docker": [
                         "2.2.1"
                    ]
               },
               "lifecycle_build_target": False,
               "lifecycle_hooks_env": [],
               "lifecycle_hooks_execution_requirements": [],
               "lifecycle_hooks_no_sandbox": True
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
                    "attributes": {
                         "name": "aspect_rules_format_npm__is-docker__2.2.1__links",
                         "generator_name": "aspect_rules_format_npm__is-docker__2.2.1__links",
                         "generator_function": "format_register_toolchains",
                         "generator_location": None,
                         "package": "is-docker",
                         "version": "2.2.1",
                         "root_package": "",
                         "link_packages": {},
                         "bins": {},
                         "deps": {},
                         "transitive_closure": {
                              "is-docker": [
                                   "2.2.1"
                              ]
                         },
                         "lifecycle_build_target": False,
                         "lifecycle_hooks_env": [],
                         "lifecycle_hooks_execution_requirements": [],
                         "lifecycle_hooks_no_sandbox": True
                    },
                    "output_tree_hash": "078e7d8d14012f630ea3dec0ea4e5815351463ef3071a4aa393a377fad616a0a"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
          "definition_information": "Repository aspect_rules_format_npm__node-sql-parser__4.6.6__links instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:36:27: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/toolchains.bzl:13:21: in format_register_toolchains\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_format_npm/repositories.bzl:300:15: in npm_repositories\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:561:22: in npm_import\nRepository rule _npm_import_links defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:326:36: in <toplevel>\n",
          "original_attributes": {
               "name": "aspect_rules_format_npm__node-sql-parser__4.6.6__links",
               "generator_name": "aspect_rules_format_npm__node-sql-parser__4.6.6__links",
               "generator_function": "format_register_toolchains",
               "generator_location": None,
               "package": "node-sql-parser",
               "version": "4.6.6",
               "root_package": "",
               "link_packages": {},
               "bins": {},
               "deps": {
                    "big-integer": "1.6.51"
               },
               "transitive_closure": {
                    "node-sql-parser": [
                         "4.6.6"
                    ],
                    "big-integer": [
                         "1.6.51"
                    ]
               },
               "lifecycle_build_target": False,
               "lifecycle_hooks_env": [],
               "lifecycle_hooks_execution_requirements": [],
               "lifecycle_hooks_no_sandbox": True
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
                    "attributes": {
                         "name": "aspect_rules_format_npm__node-sql-parser__4.6.6__links",
                         "generator_name": "aspect_rules_format_npm__node-sql-parser__4.6.6__links",
                         "generator_function": "format_register_toolchains",
                         "generator_location": None,
                         "package": "node-sql-parser",
                         "version": "4.6.6",
                         "root_package": "",
                         "link_packages": {},
                         "bins": {},
                         "deps": {
                              "big-integer": "1.6.51"
                         },
                         "transitive_closure": {
                              "node-sql-parser": [
                                   "4.6.6"
                              ],
                              "big-integer": [
                                   "1.6.51"
                              ]
                         },
                         "lifecycle_build_target": False,
                         "lifecycle_hooks_env": [],
                         "lifecycle_hooks_execution_requirements": [],
                         "lifecycle_hooks_no_sandbox": True
                    },
                    "output_tree_hash": "79e01d93a534d09c9e840eab503172a258b660681be22921807f00c1ee20ab4b"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
          "definition_information": "Repository aspect_rules_format_npm__path-key__3.1.1__links instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:36:27: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/toolchains.bzl:13:21: in format_register_toolchains\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_format_npm/repositories.bzl:340:15: in npm_repositories\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:561:22: in npm_import\nRepository rule _npm_import_links defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:326:36: in <toplevel>\n",
          "original_attributes": {
               "name": "aspect_rules_format_npm__path-key__3.1.1__links",
               "generator_name": "aspect_rules_format_npm__path-key__3.1.1__links",
               "generator_function": "format_register_toolchains",
               "generator_location": None,
               "package": "path-key",
               "version": "3.1.1",
               "root_package": "",
               "link_packages": {},
               "bins": {},
               "deps": {},
               "transitive_closure": {
                    "path-key": [
                         "3.1.1"
                    ]
               },
               "lifecycle_build_target": False,
               "lifecycle_hooks_env": [],
               "lifecycle_hooks_execution_requirements": [],
               "lifecycle_hooks_no_sandbox": True
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
                    "attributes": {
                         "name": "aspect_rules_format_npm__path-key__3.1.1__links",
                         "generator_name": "aspect_rules_format_npm__path-key__3.1.1__links",
                         "generator_function": "format_register_toolchains",
                         "generator_location": None,
                         "package": "path-key",
                         "version": "3.1.1",
                         "root_package": "",
                         "link_packages": {},
                         "bins": {},
                         "deps": {},
                         "transitive_closure": {
                              "path-key": [
                                   "3.1.1"
                              ]
                         },
                         "lifecycle_build_target": False,
                         "lifecycle_hooks_env": [],
                         "lifecycle_hooks_execution_requirements": [],
                         "lifecycle_hooks_no_sandbox": True
                    },
                    "output_tree_hash": "7d349a3212c0ed359224a64a5e9e108f2da66d94e65d82e4310531ae21763b13"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
          "definition_information": "Repository aspect_rules_format_npm__picocolors__1.0.0__links instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:36:27: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/toolchains.bzl:13:21: in format_register_toolchains\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_format_npm/repositories.bzl:354:15: in npm_repositories\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:561:22: in npm_import\nRepository rule _npm_import_links defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:326:36: in <toplevel>\n",
          "original_attributes": {
               "name": "aspect_rules_format_npm__picocolors__1.0.0__links",
               "generator_name": "aspect_rules_format_npm__picocolors__1.0.0__links",
               "generator_function": "format_register_toolchains",
               "generator_location": None,
               "package": "picocolors",
               "version": "1.0.0",
               "root_package": "",
               "link_packages": {},
               "bins": {},
               "deps": {},
               "transitive_closure": {
                    "picocolors": [
                         "1.0.0"
                    ]
               },
               "lifecycle_build_target": False,
               "lifecycle_hooks_env": [],
               "lifecycle_hooks_execution_requirements": [],
               "lifecycle_hooks_no_sandbox": True
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
                    "attributes": {
                         "name": "aspect_rules_format_npm__picocolors__1.0.0__links",
                         "generator_name": "aspect_rules_format_npm__picocolors__1.0.0__links",
                         "generator_function": "format_register_toolchains",
                         "generator_location": None,
                         "package": "picocolors",
                         "version": "1.0.0",
                         "root_package": "",
                         "link_packages": {},
                         "bins": {},
                         "deps": {},
                         "transitive_closure": {
                              "picocolors": [
                                   "1.0.0"
                              ]
                         },
                         "lifecycle_build_target": False,
                         "lifecycle_hooks_env": [],
                         "lifecycle_hooks_execution_requirements": [],
                         "lifecycle_hooks_no_sandbox": True
                    },
                    "output_tree_hash": "18df4509faabe7a2c029c70e8339fc6eddcd57b35447a1a841b54598c5ba85fb"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_file",
          "definition_information": "Repository buildifier_linux_amd64 instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:10:40: in <toplevel>\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/buildifier_prebuilt/defs.bzl:74:18: in buildifier_prebuilt_register_toolchains\nRepository rule http_file defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/http.bzl:466:28: in <toplevel>\n",
          "original_attributes": {
               "name": "buildifier_linux_amd64",
               "generator_name": "buildifier_linux_amd64",
               "generator_function": "buildifier_prebuilt_register_toolchains",
               "generator_location": None,
               "executable": True,
               "downloaded_file_path": "buildifier",
               "sha256": "42f798ec532c58e34401985043e660cb19d5ae994e108d19298c7d229547ffca",
               "urls": [
                    "https://github.com/bazelbuild/buildtools/releases/download/v6.3.3/buildifier-linux-amd64"
               ]
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_file",
                    "attributes": {
                         "executable": True,
                         "downloaded_file_path": "buildifier",
                         "sha256": "42f798ec532c58e34401985043e660cb19d5ae994e108d19298c7d229547ffca",
                         "integrity": "",
                         "canonical_id": "",
                         "url": "",
                         "urls": [
                              "https://github.com/bazelbuild/buildtools/releases/download/v6.3.3/buildifier-linux-amd64"
                         ],
                         "netrc": "",
                         "auth_patterns": {},
                         "name": "buildifier_linux_amd64"
                    },
                    "output_tree_hash": "659b8ed2e7ffbe70d45736f9fadb8e9c4eaeb508e321773f58f7f423d78c0e29"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
          "definition_information": "Repository aspect_rules_format_npm__open__8.4.2__links instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:36:27: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/toolchains.bzl:13:21: in format_register_toolchains\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_format_npm/repositories.bzl:318:15: in npm_repositories\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:561:22: in npm_import\nRepository rule _npm_import_links defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:326:36: in <toplevel>\n",
          "original_attributes": {
               "name": "aspect_rules_format_npm__open__8.4.2__links",
               "generator_name": "aspect_rules_format_npm__open__8.4.2__links",
               "generator_function": "format_register_toolchains",
               "generator_location": None,
               "package": "open",
               "version": "8.4.2",
               "root_package": "",
               "link_packages": {},
               "bins": {},
               "deps": {
                    "define-lazy-prop": "2.0.0",
                    "is-docker": "2.2.1",
                    "is-wsl": "2.2.0"
               },
               "transitive_closure": {
                    "open": [
                         "8.4.2"
                    ],
                    "define-lazy-prop": [
                         "2.0.0"
                    ],
                    "is-docker": [
                         "2.2.1"
                    ],
                    "is-wsl": [
                         "2.2.0"
                    ]
               },
               "lifecycle_build_target": False,
               "lifecycle_hooks_env": [],
               "lifecycle_hooks_execution_requirements": [],
               "lifecycle_hooks_no_sandbox": True
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import_links",
                    "attributes": {
                         "name": "aspect_rules_format_npm__open__8.4.2__links",
                         "generator_name": "aspect_rules_format_npm__open__8.4.2__links",
                         "generator_function": "format_register_toolchains",
                         "generator_location": None,
                         "package": "open",
                         "version": "8.4.2",
                         "root_package": "",
                         "link_packages": {},
                         "bins": {},
                         "deps": {
                              "define-lazy-prop": "2.0.0",
                              "is-docker": "2.2.1",
                              "is-wsl": "2.2.0"
                         },
                         "transitive_closure": {
                              "open": [
                                   "8.4.2"
                              ],
                              "define-lazy-prop": [
                                   "2.0.0"
                              ],
                              "is-docker": [
                                   "2.2.1"
                              ],
                              "is-wsl": [
                                   "2.2.0"
                              ]
                         },
                         "lifecycle_build_target": False,
                         "lifecycle_hooks_env": [],
                         "lifecycle_hooks_execution_requirements": [],
                         "lifecycle_hooks_no_sandbox": True
                    },
                    "output_tree_hash": "c2464bd42ba0b341291879deb28b475173caba89431a46de0f8923d9965d51d3"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository buf instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:6:26: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/repositories.bzl:310:17: in rules_format_dependencies\n  /home/andrzej/code/bazel/bazel-super-formatter/format/repositories.bzl:11:10: in http_archive\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\nRepository rule http_archive defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "buf",
               "generator_name": "buf",
               "generator_function": "rules_format_dependencies",
               "generator_location": None,
               "url": "https://github.com/bufbuild/buf/releases/download/v1.9.0/buf-Linux-x86_64.tar.gz",
               "sha256": "6c1e7258b79273c60085df8825a52a5ee306530e7327942c91ec84545cd2d40a",
               "strip_prefix": "buf",
               "build_file_content": "exports_files([\"bin/buf\"], visibility = [\"//visibility:public\"])"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "https://github.com/bufbuild/buf/releases/download/v1.9.0/buf-Linux-x86_64.tar.gz",
                         "urls": [],
                         "sha256": "6c1e7258b79273c60085df8825a52a5ee306530e7327942c91ec84545cd2d40a",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "buf",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "exports_files([\"bin/buf\"], visibility = [\"//visibility:public\"])",
                         "workspace_file_content": "",
                         "name": "buf"
                    },
                    "output_tree_hash": "058857dbe3441034765407f3696fa7ffe72f454d7fde0cb34e172c92dd7e3468"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_jar",
          "definition_information": "Repository sourcecode_2_13 instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:6:26: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/repositories.bzl:149:13: in rules_format_dependencies\n  /home/andrzej/code/bazel/bazel-super-formatter/format/repositories.bzl:14:10: in http_jar\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\nRepository rule http_jar defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/http.bzl:530:27: in <toplevel>\n",
          "original_attributes": {
               "name": "sourcecode_2_13",
               "generator_name": "sourcecode_2_13",
               "generator_function": "rules_format_dependencies",
               "generator_location": None,
               "integrity": "sha1-lXTaDOmTYHsHH2gq+V9lNeviofE=",
               "url": "https://repo1.maven.org/maven2/com/lihaoyi/sourcecode_2.13/0.3.0/sourcecode_2.13-0.3.0.jar"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_jar",
                    "attributes": {
                         "sha256": "",
                         "integrity": "sha1-lXTaDOmTYHsHH2gq+V9lNeviofE=",
                         "canonical_id": "",
                         "url": "https://repo1.maven.org/maven2/com/lihaoyi/sourcecode_2.13/0.3.0/sourcecode_2.13-0.3.0.jar",
                         "urls": [],
                         "netrc": "",
                         "auth_patterns": {},
                         "downloaded_file_name": "downloaded.jar",
                         "name": "sourcecode_2_13"
                    },
                    "output_tree_hash": "65b02966d5f8ba8b11e7245191c5915199ce8124f3cfe74afecdff96af004850"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_jar",
          "definition_information": "Repository paiges_core_2_13 instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:6:26: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/repositories.bzl:293:13: in rules_format_dependencies\n  /home/andrzej/code/bazel/bazel-super-formatter/format/repositories.bzl:14:10: in http_jar\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\nRepository rule http_jar defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/http.bzl:530:27: in <toplevel>\n",
          "original_attributes": {
               "name": "paiges_core_2_13",
               "generator_name": "paiges_core_2_13",
               "generator_function": "rules_format_dependencies",
               "generator_location": None,
               "integrity": "sha1-/eB2O8GQfz2+H5BZZGluCTArxkM=",
               "url": "https://repo1.maven.org/maven2/org/typelevel/paiges-core_2.13/0.4.2/paiges-core_2.13-0.4.2.jar"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_jar",
                    "attributes": {
                         "sha256": "",
                         "integrity": "sha1-/eB2O8GQfz2+H5BZZGluCTArxkM=",
                         "canonical_id": "",
                         "url": "https://repo1.maven.org/maven2/org/typelevel/paiges-core_2.13/0.4.2/paiges-core_2.13-0.4.2.jar",
                         "urls": [],
                         "netrc": "",
                         "auth_patterns": {},
                         "downloaded_file_name": "downloaded.jar",
                         "name": "paiges_core_2_13"
                    },
                    "output_tree_hash": "45362d39daa72c24202ae24b0d696970f2a2fc02d3a3f809f813c2d1e04a9389"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_jar",
          "definition_information": "Repository interface instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:6:26: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/repositories.bzl:167:13: in rules_format_dependencies\n  /home/andrzej/code/bazel/bazel-super-formatter/format/repositories.bzl:14:10: in http_jar\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\nRepository rule http_jar defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/http.bzl:530:27: in <toplevel>\n",
          "original_attributes": {
               "name": "interface",
               "generator_name": "interface",
               "generator_function": "rules_format_dependencies",
               "generator_location": None,
               "integrity": "sha1-iMGIQ7lmc2Th+RloKD8vNIwbINk=",
               "url": "https://repo1.maven.org/maven2/io/get-coursier/interface/0.0.17/interface-0.0.17.jar"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_jar",
                    "attributes": {
                         "sha256": "",
                         "integrity": "sha1-iMGIQ7lmc2Th+RloKD8vNIwbINk=",
                         "canonical_id": "",
                         "url": "https://repo1.maven.org/maven2/io/get-coursier/interface/0.0.17/interface-0.0.17.jar",
                         "urls": [],
                         "netrc": "",
                         "auth_patterns": {},
                         "downloaded_file_name": "downloaded.jar",
                         "name": "interface"
                    },
                    "output_tree_hash": "83b9979d07965356cc7101b8f65595d5f786feac636cf97b98325c9e9de6c978"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_jar",
          "definition_information": "Repository jna instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:6:26: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/repositories.bzl:179:13: in rules_format_dependencies\n  /home/andrzej/code/bazel/bazel-super-formatter/format/repositories.bzl:14:10: in http_jar\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\nRepository rule http_jar defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/http.bzl:530:27: in <toplevel>\n",
          "original_attributes": {
               "name": "jna",
               "generator_name": "jna",
               "generator_function": "rules_format_dependencies",
               "generator_location": None,
               "integrity": "sha1-EgDn6+7b4NEAYgk/MpJakSAg50c=",
               "url": "https://repo1.maven.org/maven2/net/java/dev/jna/jna/5.13.0/jna-5.13.0.jar"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_jar",
                    "attributes": {
                         "sha256": "",
                         "integrity": "sha1-EgDn6+7b4NEAYgk/MpJakSAg50c=",
                         "canonical_id": "",
                         "url": "https://repo1.maven.org/maven2/net/java/dev/jna/jna/5.13.0/jna-5.13.0.jar",
                         "urls": [],
                         "netrc": "",
                         "auth_patterns": {},
                         "downloaded_file_name": "downloaded.jar",
                         "name": "jna"
                    },
                    "output_tree_hash": "9a66c30e4d462ddd9e7f15dfbd166422ce4edb720c80d799e1738ed2d0f4a1d5"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_jar",
          "definition_information": "Repository scala_compiler instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:6:26: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/repositories.bzl:191:13: in rules_format_dependencies\n  /home/andrzej/code/bazel/bazel-super-formatter/format/repositories.bzl:14:10: in http_jar\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\nRepository rule http_jar defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/http.bzl:530:27: in <toplevel>\n",
          "original_attributes": {
               "name": "scala_compiler",
               "generator_name": "scala_compiler",
               "generator_function": "rules_format_dependencies",
               "generator_location": None,
               "integrity": "sha1-MOU8aTaEP29HBhe2JWODFxBI794=",
               "url": "https://repo1.maven.org/maven2/org/scala-lang/scala-compiler/2.13.11/scala-compiler-2.13.11.jar"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_jar",
                    "attributes": {
                         "sha256": "",
                         "integrity": "sha1-MOU8aTaEP29HBhe2JWODFxBI794=",
                         "canonical_id": "",
                         "url": "https://repo1.maven.org/maven2/org/scala-lang/scala-compiler/2.13.11/scala-compiler-2.13.11.jar",
                         "urls": [],
                         "netrc": "",
                         "auth_patterns": {},
                         "downloaded_file_name": "downloaded.jar",
                         "name": "scala_compiler"
                    },
                    "output_tree_hash": "44c96e9783cce1e61299770a30c30276e998c9b8a3186684759429d8548141a6"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_jar",
          "definition_information": "Repository scalap instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:6:26: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/repositories.bzl:209:13: in rules_format_dependencies\n  /home/andrzej/code/bazel/bazel-super-formatter/format/repositories.bzl:14:10: in http_jar\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\nRepository rule http_jar defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/http.bzl:530:27: in <toplevel>\n",
          "original_attributes": {
               "name": "scalap",
               "generator_name": "scalap",
               "generator_function": "rules_format_dependencies",
               "generator_location": None,
               "integrity": "sha1-5AM/NkkbNxTAKOjK2i2F/Eq8k+U=",
               "url": "https://repo1.maven.org/maven2/org/scala-lang/scalap/2.13.11/scalap-2.13.11.jar"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_jar",
                    "attributes": {
                         "sha256": "",
                         "integrity": "sha1-5AM/NkkbNxTAKOjK2i2F/Eq8k+U=",
                         "canonical_id": "",
                         "url": "https://repo1.maven.org/maven2/org/scala-lang/scalap/2.13.11/scalap-2.13.11.jar",
                         "urls": [],
                         "netrc": "",
                         "auth_patterns": {},
                         "downloaded_file_name": "downloaded.jar",
                         "name": "scalap"
                    },
                    "output_tree_hash": "9771c36212773a98e4f6d7511787d21f1002fbcfdc365717c913e0ee0590898b"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_jar",
          "definition_information": "Repository scala_library instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:6:26: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/repositories.bzl:197:13: in rules_format_dependencies\n  /home/andrzej/code/bazel/bazel-super-formatter/format/repositories.bzl:14:10: in http_jar\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\nRepository rule http_jar defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/http.bzl:530:27: in <toplevel>\n",
          "original_attributes": {
               "name": "scala_library",
               "generator_name": "scala_library",
               "generator_function": "rules_format_dependencies",
               "generator_location": None,
               "integrity": "sha1-T82C4c5C17FXkUuGhk57NZHh4NI=",
               "url": "https://repo1.maven.org/maven2/org/scala-lang/scala-library/2.13.11/scala-library-2.13.11.jar"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_jar",
                    "attributes": {
                         "sha256": "",
                         "integrity": "sha1-T82C4c5C17FXkUuGhk57NZHh4NI=",
                         "canonical_id": "",
                         "url": "https://repo1.maven.org/maven2/org/scala-lang/scala-library/2.13.11/scala-library-2.13.11.jar",
                         "urls": [],
                         "netrc": "",
                         "auth_patterns": {},
                         "downloaded_file_name": "downloaded.jar",
                         "name": "scala_library"
                    },
                    "output_tree_hash": "e2cd360cfbecfc9f0695b924cd52ec9c9796ad44de2d878f72b7b47d1309c67c"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_jar",
          "definition_information": "Repository metaconfig_pprint_2_13 instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:6:26: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/repositories.bzl:119:13: in rules_format_dependencies\n  /home/andrzej/code/bazel/bazel-super-formatter/format/repositories.bzl:14:10: in http_jar\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\nRepository rule http_jar defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/http.bzl:530:27: in <toplevel>\n",
          "original_attributes": {
               "name": "metaconfig_pprint_2_13",
               "generator_name": "metaconfig_pprint_2_13",
               "generator_function": "rules_format_dependencies",
               "generator_location": None,
               "integrity": "sha1-Lu7eBd349929+uLiNocg+6/tpWM=",
               "url": "https://repo1.maven.org/maven2/com/geirsson/metaconfig-pprint_2.13/0.11.1/metaconfig-pprint_2.13-0.11.1.jar"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_jar",
                    "attributes": {
                         "sha256": "",
                         "integrity": "sha1-Lu7eBd349929+uLiNocg+6/tpWM=",
                         "canonical_id": "",
                         "url": "https://repo1.maven.org/maven2/com/geirsson/metaconfig-pprint_2.13/0.11.1/metaconfig-pprint_2.13-0.11.1.jar",
                         "urls": [],
                         "netrc": "",
                         "auth_patterns": {},
                         "downloaded_file_name": "downloaded.jar",
                         "name": "metaconfig_pprint_2_13"
                    },
                    "output_tree_hash": "73b5dd877f6ed6fd7ad1927968a14d25c26b16b930c819980892cce78202388b"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_jar",
          "definition_information": "Repository scala_collection_compat_2_13 instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:6:26: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/repositories.bzl:215:13: in rules_format_dependencies\n  /home/andrzej/code/bazel/bazel-super-formatter/format/repositories.bzl:14:10: in http_jar\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\nRepository rule http_jar defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/http.bzl:530:27: in <toplevel>\n",
          "original_attributes": {
               "name": "scala_collection_compat_2_13",
               "generator_name": "scala_collection_compat_2_13",
               "generator_function": "rules_format_dependencies",
               "generator_location": None,
               "integrity": "sha1-J0UeqJfkHHSYha0gX3uD+nuqfMc=",
               "url": "https://repo1.maven.org/maven2/org/scala-lang/modules/scala-collection-compat_2.13/2.5.0/scala-collection-compat_2.13-2.5.0.jar"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_jar",
                    "attributes": {
                         "sha256": "",
                         "integrity": "sha1-J0UeqJfkHHSYha0gX3uD+nuqfMc=",
                         "canonical_id": "",
                         "url": "https://repo1.maven.org/maven2/org/scala-lang/modules/scala-collection-compat_2.13/2.5.0/scala-collection-compat_2.13-2.5.0.jar",
                         "urls": [],
                         "netrc": "",
                         "auth_patterns": {},
                         "downloaded_file_name": "downloaded.jar",
                         "name": "scala_collection_compat_2_13"
                    },
                    "output_tree_hash": "a7adcf2b8f6fce02e52b6d8feb3df3d1d20c8e2b0faac632bef2254c6043ddaa"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_jar",
          "definition_information": "Repository scalafmt_config_2_13 instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:6:26: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/repositories.bzl:245:13: in rules_format_dependencies\n  /home/andrzej/code/bazel/bazel-super-formatter/format/repositories.bzl:14:10: in http_jar\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\nRepository rule http_jar defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/http.bzl:530:27: in <toplevel>\n",
          "original_attributes": {
               "name": "scalafmt_config_2_13",
               "generator_name": "scalafmt_config_2_13",
               "generator_function": "rules_format_dependencies",
               "generator_location": None,
               "integrity": "sha1-MbQXYLTpFLvbsxpH3Hu95FcIh+8=",
               "url": "https://repo1.maven.org/maven2/org/scalameta/scalafmt-config_2.13/3.7.14/scalafmt-config_2.13-3.7.14.jar"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_jar",
                    "attributes": {
                         "sha256": "",
                         "integrity": "sha1-MbQXYLTpFLvbsxpH3Hu95FcIh+8=",
                         "canonical_id": "",
                         "url": "https://repo1.maven.org/maven2/org/scalameta/scalafmt-config_2.13/3.7.14/scalafmt-config_2.13-3.7.14.jar",
                         "urls": [],
                         "netrc": "",
                         "auth_patterns": {},
                         "downloaded_file_name": "downloaded.jar",
                         "name": "scalafmt_config_2_13"
                    },
                    "output_tree_hash": "11444dd638d2b5901a426b89d416e567fe0528384b35330f0d6c545812d7036b"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_jar",
          "definition_information": "Repository diffutils instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:6:26: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/repositories.bzl:137:13: in rules_format_dependencies\n  /home/andrzej/code/bazel/bazel-super-formatter/format/repositories.bzl:14:10: in http_jar\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\nRepository rule http_jar defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/http.bzl:530:27: in <toplevel>\n",
          "original_attributes": {
               "name": "diffutils",
               "generator_name": "diffutils",
               "generator_function": "rules_format_dependencies",
               "generator_location": None,
               "integrity": "sha1-fgYN1bGUMebRmOkf9nBkQ3L2D70=",
               "url": "https://repo1.maven.org/maven2/com/googlecode/java-diff-utils/diffutils/1.3.0/diffutils-1.3.0.jar"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_jar",
                    "attributes": {
                         "sha256": "",
                         "integrity": "sha1-fgYN1bGUMebRmOkf9nBkQ3L2D70=",
                         "canonical_id": "",
                         "url": "https://repo1.maven.org/maven2/com/googlecode/java-diff-utils/diffutils/1.3.0/diffutils-1.3.0.jar",
                         "urls": [],
                         "netrc": "",
                         "auth_patterns": {},
                         "downloaded_file_name": "downloaded.jar",
                         "name": "diffutils"
                    },
                    "output_tree_hash": "5c0cca751fcd70c1c6e69edb0eee8a99c97ccef7cfdc65032061b0b232df7a30"
               }
          ]
     },
     {
          "original_rule_class": "@rules_python//python:repositories.bzl%python_repository",
          "definition_information": "Repository python3_x86_64-unknown-linux-gnu instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:25:27: in <toplevel>\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/rules_python/python/repositories.bzl:555:26: in python_register_toolchains\nRepository rule python_repository defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/rules_python/python/repositories.bzl:384:36: in <toplevel>\n",
          "original_attributes": {
               "name": "python3_x86_64-unknown-linux-gnu",
               "generator_name": "python3_x86_64-unknown-linux-gnu",
               "generator_function": "python_register_toolchains",
               "generator_location": None,
               "patches": [],
               "platform": "x86_64-unknown-linux-gnu",
               "python_version": "3.10.12",
               "release_filename": "20230726/cpython-3.10.12+20230726-x86_64-unknown-linux-gnu-install_only.tar.gz",
               "sha256": "a476dbca9184df9fc69fe6309cda5ebaf031d27ca9e529852437c94ec1bc43d3",
               "strip_prefix": "python",
               "urls": [
                    "https://github.com/indygreg/python-build-standalone/releases/download/20230726/cpython-3.10.12+20230726-x86_64-unknown-linux-gnu-install_only.tar.gz"
               ]
          },
          "repositories": [
               {
                    "rule_class": "@rules_python//python:repositories.bzl%python_repository",
                    "attributes": {
                         "coverage_tool": "",
                         "distutils": None,
                         "distutils_content": "",
                         "ignore_root_user_error": False,
                         "name": "python3_x86_64-unknown-linux-gnu",
                         "patches": [],
                         "platform": "x86_64-unknown-linux-gnu",
                         "python_version": "3.10.12",
                         "release_filename": "20230726/cpython-3.10.12+20230726-x86_64-unknown-linux-gnu-install_only.tar.gz",
                         "sha256": "a476dbca9184df9fc69fe6309cda5ebaf031d27ca9e529852437c94ec1bc43d3",
                         "strip_prefix": "python",
                         "urls": [
                              "https://github.com/indygreg/python-build-standalone/releases/download/20230726/cpython-3.10.12+20230726-x86_64-unknown-linux-gnu-install_only.tar.gz"
                         ]
                    },
                    "output_tree_hash": "d0c6b872cf1e81be99dff8fa148a47e2ad11bb0f1966bcf82cd732d793da7a81"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository terraform_linux_x86_64 instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:6:26: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/repositories.bzl:339:17: in rules_format_dependencies\n  /home/andrzej/code/bazel/bazel-super-formatter/format/repositories.bzl:11:10: in http_archive\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\nRepository rule http_archive defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "terraform_linux_x86_64",
               "generator_name": "terraform_linux_x86_64",
               "generator_function": "rules_format_dependencies",
               "generator_location": None,
               "urls": [
                    "https://releases.hashicorp.com/terraform/1.4.0/terraform_1.4.0_linux_amd64.zip"
               ],
               "sha256": "5da60da508d6d1941ffa8b9216147456a16bbff6db7622ae9ad01d314cbdd188",
               "build_file_content": "exports_files([\"terraform\"])"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://releases.hashicorp.com/terraform/1.4.0/terraform_1.4.0_linux_amd64.zip"
                         ],
                         "sha256": "5da60da508d6d1941ffa8b9216147456a16bbff6db7622ae9ad01d314cbdd188",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "exports_files([\"terraform\"])",
                         "workspace_file_content": "",
                         "name": "terraform_linux_x86_64"
                    },
                    "output_tree_hash": "37251c50ea8f6c71e91911aa9b22bbdd37338683d445c383321c4f18c13c8830"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository pypi__build instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:41:10: in <toplevel>\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/rules_python/python/pip.bzl:150:29: in pip_parse\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/rules_python/python/pip_install/repositories.bzl:143:14: in pip_install_dependencies\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\nRepository rule http_archive defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "pypi__build",
               "generator_name": "pypi__build",
               "generator_function": "pip_parse",
               "generator_location": None,
               "url": "https://files.pythonhosted.org/packages/03/97/f58c723ff036a8d8b4d3115377c0a37ed05c1f68dd9a0d66dab5e82c5c1c/build-0.9.0-py3-none-any.whl",
               "sha256": "38a7a2b7a0bdc61a42a0a67509d88c71ecfc37b393baba770fae34e20929ff69",
               "type": "zip",
               "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude in /python/pip_install/tools/bazel.py\n        # to avoid non-determinism following pip install's behavior.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/* *\",\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ]),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "https://files.pythonhosted.org/packages/03/97/f58c723ff036a8d8b4d3115377c0a37ed05c1f68dd9a0d66dab5e82c5c1c/build-0.9.0-py3-none-any.whl",
                         "urls": [],
                         "sha256": "38a7a2b7a0bdc61a42a0a67509d88c71ecfc37b393baba770fae34e20929ff69",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "zip",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude in /python/pip_install/tools/bazel.py\n        # to avoid non-determinism following pip install's behavior.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/* *\",\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ]),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n",
                         "workspace_file_content": "",
                         "name": "pypi__build"
                    },
                    "output_tree_hash": "73799e69bfa8d8b02d4267d54c53224b83eeb5e9702602e988c8db9af5d46c8a"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/cpp:cc_configure.bzl%cc_autoconf",
          "definition_information": "Repository local_config_cc instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:520:13: in <toplevel>\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/cpp/cc_configure.bzl:184:16: in cc_configure\nRepository rule cc_autoconf defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/cpp/cc_configure.bzl:143:30: in <toplevel>\n",
          "original_attributes": {
               "name": "local_config_cc",
               "generator_name": "local_config_cc",
               "generator_function": "cc_configure",
               "generator_location": None
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/cpp:cc_configure.bzl%cc_autoconf",
                    "attributes": {
                         "name": "local_config_cc",
                         "generator_name": "local_config_cc",
                         "generator_function": "cc_configure",
                         "generator_location": None
                    },
                    "output_tree_hash": "ab1a5c7b34faab68e6d54cdd66bb53f8d41ed834d1e72c5b46ef8a160da42d98"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_jar",
          "definition_information": "Repository svm_subs instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:6:26: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/repositories.bzl:281:13: in rules_format_dependencies\n  /home/andrzej/code/bazel/bazel-super-formatter/format/repositories.bzl:14:10: in http_jar\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\nRepository rule http_jar defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/http.bzl:530:27: in <toplevel>\n",
          "original_attributes": {
               "name": "svm_subs",
               "generator_name": "svm_subs",
               "generator_function": "rules_format_dependencies",
               "generator_location": None,
               "integrity": "sha1-amP3YfwPkgN6A0+T4dUDNQNpR1s=",
               "url": "https://repo1.maven.org/maven2/org/scalameta/svm-subs/101.0.0/svm-subs-101.0.0.jar"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_jar",
                    "attributes": {
                         "sha256": "",
                         "integrity": "sha1-amP3YfwPkgN6A0+T4dUDNQNpR1s=",
                         "canonical_id": "",
                         "url": "https://repo1.maven.org/maven2/org/scalameta/svm-subs/101.0.0/svm-subs-101.0.0.jar",
                         "urls": [],
                         "netrc": "",
                         "auth_patterns": {},
                         "downloaded_file_name": "downloaded.jar",
                         "name": "svm_subs"
                    },
                    "output_tree_hash": "4c351596277dc56c2547394e31a3d69a8aad9e98e98b1a65ba64d958988045c7"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository rules_cc instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:425:6: in <toplevel>\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\nRepository rule http_archive defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "rules_cc",
               "generator_name": "rules_cc",
               "generator_function": "maybe",
               "generator_location": None,
               "urls": [
                    "https://github.com/bazelbuild/rules_cc/releases/download/0.0.2/rules_cc-0.0.2.tar.gz"
               ],
               "sha256": "58bff40957ace85c2de21ebfc72e53ed3a0d33af8cc20abd0ceec55c63be7de2"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://github.com/bazelbuild/rules_cc/releases/download/0.0.2/rules_cc-0.0.2.tar.gz"
                         ],
                         "sha256": "58bff40957ace85c2de21ebfc72e53ed3a0d33af8cc20abd0ceec55c63be7de2",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "rules_cc"
                    },
                    "output_tree_hash": "d1aae5466714ed8166cc876175f2ed95ce245b5318420f9ecba8201cbb68ff26"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository pypi__click instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:41:10: in <toplevel>\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/rules_python/python/pip.bzl:150:29: in pip_parse\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/rules_python/python/pip_install/repositories.bzl:143:14: in pip_install_dependencies\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\nRepository rule http_archive defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "pypi__click",
               "generator_name": "pypi__click",
               "generator_function": "pip_parse",
               "generator_location": None,
               "url": "https://files.pythonhosted.org/packages/76/0a/b6c5f311e32aeb3b406e03c079ade51e905ea630fc19d1262a46249c1c86/click-8.0.1-py3-none-any.whl",
               "sha256": "fba402a4a47334742d782209a7c79bc448911afe1149d07bdabdf480b3e2f4b6",
               "type": "zip",
               "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude in /python/pip_install/tools/bazel.py\n        # to avoid non-determinism following pip install's behavior.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/* *\",\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ]),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "https://files.pythonhosted.org/packages/76/0a/b6c5f311e32aeb3b406e03c079ade51e905ea630fc19d1262a46249c1c86/click-8.0.1-py3-none-any.whl",
                         "urls": [],
                         "sha256": "fba402a4a47334742d782209a7c79bc448911afe1149d07bdabdf480b3e2f4b6",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "zip",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude in /python/pip_install/tools/bazel.py\n        # to avoid non-determinism following pip install's behavior.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/* *\",\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ]),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n",
                         "workspace_file_content": "",
                         "name": "pypi__click"
                    },
                    "output_tree_hash": "a06ff9e9d9469babaa56cf1663c1dad09408a8bf1df29447f189aef657408e6f"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository pypi__colorama instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:41:10: in <toplevel>\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/rules_python/python/pip.bzl:150:29: in pip_parse\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/rules_python/python/pip_install/repositories.bzl:143:14: in pip_install_dependencies\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\nRepository rule http_archive defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "pypi__colorama",
               "generator_name": "pypi__colorama",
               "generator_function": "pip_parse",
               "generator_location": None,
               "url": "https://files.pythonhosted.org/packages/d1/d6/3965ed04c63042e047cb6a3e6ed1a63a35087b6a609aa3a15ed8ac56c221/colorama-0.4.6-py2.py3-none-any.whl",
               "sha256": "4f1d9991f5acc0ca119f9d443620b77f9d6b33703e51011c16baf57afb285fc6",
               "type": "zip",
               "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude in /python/pip_install/tools/bazel.py\n        # to avoid non-determinism following pip install's behavior.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/* *\",\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ]),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "https://files.pythonhosted.org/packages/d1/d6/3965ed04c63042e047cb6a3e6ed1a63a35087b6a609aa3a15ed8ac56c221/colorama-0.4.6-py2.py3-none-any.whl",
                         "urls": [],
                         "sha256": "4f1d9991f5acc0ca119f9d443620b77f9d6b33703e51011c16baf57afb285fc6",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "zip",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude in /python/pip_install/tools/bazel.py\n        # to avoid non-determinism following pip install's behavior.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/* *\",\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ]),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n",
                         "workspace_file_content": "",
                         "name": "pypi__colorama"
                    },
                    "output_tree_hash": "b4b748db844b7bd5ddd33b18b4c247920bee533f0c9317770ff8af88bd2e0b68"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository pypi__importlib_metadata instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:41:10: in <toplevel>\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/rules_python/python/pip.bzl:150:29: in pip_parse\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/rules_python/python/pip_install/repositories.bzl:143:14: in pip_install_dependencies\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\nRepository rule http_archive defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "pypi__importlib_metadata",
               "generator_name": "pypi__importlib_metadata",
               "generator_function": "pip_parse",
               "generator_location": None,
               "url": "https://files.pythonhosted.org/packages/d7/31/74dcb59a601b95fce3b0334e8fc9db758f78e43075f22aeb3677dfb19f4c/importlib_metadata-1.4.0-py2.py3-none-any.whl",
               "sha256": "bdd9b7c397c273bcc9a11d6629a38487cd07154fa255a467bf704cd2c258e359",
               "type": "zip",
               "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude in /python/pip_install/tools/bazel.py\n        # to avoid non-determinism following pip install's behavior.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/* *\",\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ]),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "https://files.pythonhosted.org/packages/d7/31/74dcb59a601b95fce3b0334e8fc9db758f78e43075f22aeb3677dfb19f4c/importlib_metadata-1.4.0-py2.py3-none-any.whl",
                         "urls": [],
                         "sha256": "bdd9b7c397c273bcc9a11d6629a38487cd07154fa255a467bf704cd2c258e359",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "zip",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude in /python/pip_install/tools/bazel.py\n        # to avoid non-determinism following pip install's behavior.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/* *\",\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ]),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n",
                         "workspace_file_content": "",
                         "name": "pypi__importlib_metadata"
                    },
                    "output_tree_hash": "c8c48d09f914e5c792d6bc475351bda0e594a6f5c8b9c5dc56eb71159e6efba2"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository pypi__installer instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:41:10: in <toplevel>\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/rules_python/python/pip.bzl:150:29: in pip_parse\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/rules_python/python/pip_install/repositories.bzl:143:14: in pip_install_dependencies\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\nRepository rule http_archive defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "pypi__installer",
               "generator_name": "pypi__installer",
               "generator_function": "pip_parse",
               "generator_location": None,
               "url": "https://files.pythonhosted.org/packages/e5/ca/1172b6638d52f2d6caa2dd262ec4c811ba59eee96d54a7701930726bce18/installer-0.7.0-py3-none-any.whl",
               "sha256": "05d1933f0a5ba7d8d6296bb6d5018e7c94fa473ceb10cf198a92ccea19c27b53",
               "type": "zip",
               "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude in /python/pip_install/tools/bazel.py\n        # to avoid non-determinism following pip install's behavior.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/* *\",\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ]),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "https://files.pythonhosted.org/packages/e5/ca/1172b6638d52f2d6caa2dd262ec4c811ba59eee96d54a7701930726bce18/installer-0.7.0-py3-none-any.whl",
                         "urls": [],
                         "sha256": "05d1933f0a5ba7d8d6296bb6d5018e7c94fa473ceb10cf198a92ccea19c27b53",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "zip",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude in /python/pip_install/tools/bazel.py\n        # to avoid non-determinism following pip install's behavior.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/* *\",\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ]),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n",
                         "workspace_file_content": "",
                         "name": "pypi__installer"
                    },
                    "output_tree_hash": "4384d89d32a9ff4be9389762f11abe965b5d381906a1e3e3f76983907a3c908e"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository pypi__more_itertools instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:41:10: in <toplevel>\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/rules_python/python/pip.bzl:150:29: in pip_parse\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/rules_python/python/pip_install/repositories.bzl:143:14: in pip_install_dependencies\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\nRepository rule http_archive defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "pypi__more_itertools",
               "generator_name": "pypi__more_itertools",
               "generator_function": "pip_parse",
               "generator_location": None,
               "url": "https://files.pythonhosted.org/packages/bd/3f/c4b3dbd315e248f84c388bd4a72b131a29f123ecacc37ffb2b3834546e42/more_itertools-8.13.0-py3-none-any.whl",
               "sha256": "c5122bffc5f104d37c1626b8615b511f3427aa5389b94d61e5ef8236bfbc3ddb",
               "type": "zip",
               "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude in /python/pip_install/tools/bazel.py\n        # to avoid non-determinism following pip install's behavior.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/* *\",\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ]),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "https://files.pythonhosted.org/packages/bd/3f/c4b3dbd315e248f84c388bd4a72b131a29f123ecacc37ffb2b3834546e42/more_itertools-8.13.0-py3-none-any.whl",
                         "urls": [],
                         "sha256": "c5122bffc5f104d37c1626b8615b511f3427aa5389b94d61e5ef8236bfbc3ddb",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "zip",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude in /python/pip_install/tools/bazel.py\n        # to avoid non-determinism following pip install's behavior.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/* *\",\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ]),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n",
                         "workspace_file_content": "",
                         "name": "pypi__more_itertools"
                    },
                    "output_tree_hash": "8916c5cd60c889d19628ebe1f5328a7fc7ba1d7ab6f4d6a08fb080b74b5a8024"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository pypi__packaging instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:41:10: in <toplevel>\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/rules_python/python/pip.bzl:150:29: in pip_parse\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/rules_python/python/pip_install/repositories.bzl:143:14: in pip_install_dependencies\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\nRepository rule http_archive defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "pypi__packaging",
               "generator_name": "pypi__packaging",
               "generator_function": "pip_parse",
               "generator_location": None,
               "url": "https://files.pythonhosted.org/packages/8f/7b/42582927d281d7cb035609cd3a543ffac89b74f3f4ee8e1c50914bcb57eb/packaging-22.0-py3-none-any.whl",
               "sha256": "957e2148ba0e1a3b282772e791ef1d8083648bc131c8ab0c1feba110ce1146c3",
               "type": "zip",
               "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude in /python/pip_install/tools/bazel.py\n        # to avoid non-determinism following pip install's behavior.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/* *\",\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ]),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "https://files.pythonhosted.org/packages/8f/7b/42582927d281d7cb035609cd3a543ffac89b74f3f4ee8e1c50914bcb57eb/packaging-22.0-py3-none-any.whl",
                         "urls": [],
                         "sha256": "957e2148ba0e1a3b282772e791ef1d8083648bc131c8ab0c1feba110ce1146c3",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "zip",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude in /python/pip_install/tools/bazel.py\n        # to avoid non-determinism following pip install's behavior.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/* *\",\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ]),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n",
                         "workspace_file_content": "",
                         "name": "pypi__packaging"
                    },
                    "output_tree_hash": "406a9804521709bebb7c8714915f10f94ae4b36ad55eb30163ec31fbf2ee1891"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository pypi__pep517 instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:41:10: in <toplevel>\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/rules_python/python/pip.bzl:150:29: in pip_parse\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/rules_python/python/pip_install/repositories.bzl:143:14: in pip_install_dependencies\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\nRepository rule http_archive defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "pypi__pep517",
               "generator_name": "pypi__pep517",
               "generator_function": "pip_parse",
               "generator_location": None,
               "url": "https://files.pythonhosted.org/packages/ee/2f/ef63e64e9429111e73d3d6cbee80591672d16f2725e648ebc52096f3d323/pep517-0.13.0-py3-none-any.whl",
               "sha256": "4ba4446d80aed5b5eac6509ade100bff3e7943a8489de249654a5ae9b33ee35b",
               "type": "zip",
               "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude in /python/pip_install/tools/bazel.py\n        # to avoid non-determinism following pip install's behavior.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/* *\",\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ]),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "https://files.pythonhosted.org/packages/ee/2f/ef63e64e9429111e73d3d6cbee80591672d16f2725e648ebc52096f3d323/pep517-0.13.0-py3-none-any.whl",
                         "urls": [],
                         "sha256": "4ba4446d80aed5b5eac6509ade100bff3e7943a8489de249654a5ae9b33ee35b",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "zip",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude in /python/pip_install/tools/bazel.py\n        # to avoid non-determinism following pip install's behavior.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/* *\",\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ]),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n",
                         "workspace_file_content": "",
                         "name": "pypi__pep517"
                    },
                    "output_tree_hash": "1363a557a4f8c410257bdcdd71176a058f243bd04cf881bc3a3028439e2f31e3"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository remote_java_tools instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:364:6: in <toplevel>\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\nRepository rule http_archive defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "remote_java_tools",
               "generator_name": "remote_java_tools",
               "generator_function": "maybe",
               "generator_location": None,
               "urls": [
                    "https://mirror.bazel.build/bazel_java_tools/releases/java/v12.6/java_tools-v12.6.zip",
                    "https://github.com/bazelbuild/java_tools/releases/download/java_v12.6/java_tools-v12.6.zip"
               ],
               "sha256": "f58a358ca694a41416a9b6a92b852935ad301d8882e5d22f4f11134f035317d5"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://mirror.bazel.build/bazel_java_tools/releases/java/v12.6/java_tools-v12.6.zip",
                              "https://github.com/bazelbuild/java_tools/releases/download/java_v12.6/java_tools-v12.6.zip"
                         ],
                         "sha256": "f58a358ca694a41416a9b6a92b852935ad301d8882e5d22f4f11134f035317d5",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "remote_java_tools"
                    },
                    "output_tree_hash": "d0318a0b45e1984647f426e4d46fde87aec93eb36897e706ad4cc3db6d096493"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository pypi__pip instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:41:10: in <toplevel>\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/rules_python/python/pip.bzl:150:29: in pip_parse\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/rules_python/python/pip_install/repositories.bzl:143:14: in pip_install_dependencies\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\nRepository rule http_archive defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "pypi__pip",
               "generator_name": "pypi__pip",
               "generator_function": "pip_parse",
               "generator_location": None,
               "url": "https://files.pythonhosted.org/packages/09/bd/2410905c76ee14c62baf69e3f4aa780226c1bbfc9485731ad018e35b0cb5/pip-22.3.1-py3-none-any.whl",
               "sha256": "908c78e6bc29b676ede1c4d57981d490cb892eb45cd8c214ab6298125119e077",
               "type": "zip",
               "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude in /python/pip_install/tools/bazel.py\n        # to avoid non-determinism following pip install's behavior.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/* *\",\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ]),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "https://files.pythonhosted.org/packages/09/bd/2410905c76ee14c62baf69e3f4aa780226c1bbfc9485731ad018e35b0cb5/pip-22.3.1-py3-none-any.whl",
                         "urls": [],
                         "sha256": "908c78e6bc29b676ede1c4d57981d490cb892eb45cd8c214ab6298125119e077",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "zip",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude in /python/pip_install/tools/bazel.py\n        # to avoid non-determinism following pip install's behavior.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/* *\",\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ]),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n",
                         "workspace_file_content": "",
                         "name": "pypi__pip"
                    },
                    "output_tree_hash": "29a8f69f6cebdbcb5a784d361bd5fff7a81285f8ac7126f59f5cdf9078398024"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository rules_proto instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:436:6: in <toplevel>\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\nRepository rule http_archive defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "rules_proto",
               "generator_name": "rules_proto",
               "generator_function": "maybe",
               "generator_location": None,
               "urls": [
                    "https://mirror.bazel.build/github.com/bazelbuild/rules_proto/archive/7e4afce6fe62dbff0a4a03450143146f9f2d7488.tar.gz",
                    "https://github.com/bazelbuild/rules_proto/archive/7e4afce6fe62dbff0a4a03450143146f9f2d7488.tar.gz"
               ],
               "sha256": "8e7d59a5b12b233be5652e3d29f42fba01c7cbab09f6b3a8d0a57ed6d1e9a0da",
               "strip_prefix": "rules_proto-7e4afce6fe62dbff0a4a03450143146f9f2d7488"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://mirror.bazel.build/github.com/bazelbuild/rules_proto/archive/7e4afce6fe62dbff0a4a03450143146f9f2d7488.tar.gz",
                              "https://github.com/bazelbuild/rules_proto/archive/7e4afce6fe62dbff0a4a03450143146f9f2d7488.tar.gz"
                         ],
                         "sha256": "8e7d59a5b12b233be5652e3d29f42fba01c7cbab09f6b3a8d0a57ed6d1e9a0da",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "rules_proto-7e4afce6fe62dbff0a4a03450143146f9f2d7488",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "rules_proto"
                    },
                    "output_tree_hash": "949d4de46aa6da1c096c0c7d833e9495fa4775950870c8d844b7dba6e0e03a97"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository remote_java_tools_linux instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:374:6: in <toplevel>\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\nRepository rule http_archive defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "remote_java_tools_linux",
               "generator_name": "remote_java_tools_linux",
               "generator_function": "maybe",
               "generator_location": None,
               "urls": [
                    "https://mirror.bazel.build/bazel_java_tools/releases/java/v12.6/java_tools_linux-v12.6.zip",
                    "https://github.com/bazelbuild/java_tools/releases/download/java_v12.6/java_tools_linux-v12.6.zip"
               ],
               "sha256": "64294e91fe940c77e6d35818b4c3a1f07d78e33add01e330188d907032687066"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://mirror.bazel.build/bazel_java_tools/releases/java/v12.6/java_tools_linux-v12.6.zip",
                              "https://github.com/bazelbuild/java_tools/releases/download/java_v12.6/java_tools_linux-v12.6.zip"
                         ],
                         "sha256": "64294e91fe940c77e6d35818b4c3a1f07d78e33add01e330188d907032687066",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "remote_java_tools_linux"
                    },
                    "output_tree_hash": "0cbec48340ba55c02dbc8dafccc776c4957ebb327e00afef877416cd035cfa91"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository pypi__pip_tools instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:41:10: in <toplevel>\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/rules_python/python/pip.bzl:150:29: in pip_parse\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/rules_python/python/pip_install/repositories.bzl:143:14: in pip_install_dependencies\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\nRepository rule http_archive defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "pypi__pip_tools",
               "generator_name": "pypi__pip_tools",
               "generator_function": "pip_parse",
               "generator_location": None,
               "url": "https://files.pythonhosted.org/packages/5e/e8/f6d7d1847c7351048da870417724ace5c4506e816b38db02f4d7c675c189/pip_tools-6.12.1-py3-none-any.whl",
               "sha256": "f0c0c0ec57b58250afce458e2e6058b1f30a4263db895b7d72fd6311bf1dc6f7",
               "type": "zip",
               "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude in /python/pip_install/tools/bazel.py\n        # to avoid non-determinism following pip install's behavior.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/* *\",\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ]),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "https://files.pythonhosted.org/packages/5e/e8/f6d7d1847c7351048da870417724ace5c4506e816b38db02f4d7c675c189/pip_tools-6.12.1-py3-none-any.whl",
                         "urls": [],
                         "sha256": "f0c0c0ec57b58250afce458e2e6058b1f30a4263db895b7d72fd6311bf1dc6f7",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "zip",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude in /python/pip_install/tools/bazel.py\n        # to avoid non-determinism following pip install's behavior.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/* *\",\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ]),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n",
                         "workspace_file_content": "",
                         "name": "pypi__pip_tools"
                    },
                    "output_tree_hash": "85a3a499c07c52d0270ac0e216a171369dfbb55e32fd598e75b1030ebb4067c4"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository pypi__setuptools instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:41:10: in <toplevel>\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/rules_python/python/pip.bzl:150:29: in pip_parse\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/rules_python/python/pip_install/repositories.bzl:143:14: in pip_install_dependencies\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\nRepository rule http_archive defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "pypi__setuptools",
               "generator_name": "pypi__setuptools",
               "generator_function": "pip_parse",
               "generator_location": None,
               "url": "https://files.pythonhosted.org/packages/7c/5b/3d92b9f0f7ca1645cba48c080b54fe7d8b1033a4e5720091d1631c4266db/setuptools-60.10.0-py3-none-any.whl",
               "sha256": "782ef48d58982ddb49920c11a0c5c9c0b02e7d7d1c2ad0aa44e1a1e133051c96",
               "type": "zip",
               "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude in /python/pip_install/tools/bazel.py\n        # to avoid non-determinism following pip install's behavior.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/* *\",\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ]),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "https://files.pythonhosted.org/packages/7c/5b/3d92b9f0f7ca1645cba48c080b54fe7d8b1033a4e5720091d1631c4266db/setuptools-60.10.0-py3-none-any.whl",
                         "urls": [],
                         "sha256": "782ef48d58982ddb49920c11a0c5c9c0b02e7d7d1c2ad0aa44e1a1e133051c96",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "zip",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude in /python/pip_install/tools/bazel.py\n        # to avoid non-determinism following pip install's behavior.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/* *\",\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ]),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n",
                         "workspace_file_content": "",
                         "name": "pypi__setuptools"
                    },
                    "output_tree_hash": "ffc3fd2dd2576e1b41a287055ec54f39b3def9fa5c085b744a2dc74ca3b53e0d"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository pypi__tomli instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:41:10: in <toplevel>\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/rules_python/python/pip.bzl:150:29: in pip_parse\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/rules_python/python/pip_install/repositories.bzl:143:14: in pip_install_dependencies\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\nRepository rule http_archive defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "pypi__tomli",
               "generator_name": "pypi__tomli",
               "generator_function": "pip_parse",
               "generator_location": None,
               "url": "https://files.pythonhosted.org/packages/97/75/10a9ebee3fd790d20926a90a2547f0bf78f371b2f13aa822c759680ca7b9/tomli-2.0.1-py3-none-any.whl",
               "sha256": "939de3e7a6161af0c887ef91b7d41a53e7c5a1ca976325f429cb46ea9bc30ecc",
               "type": "zip",
               "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude in /python/pip_install/tools/bazel.py\n        # to avoid non-determinism following pip install's behavior.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/* *\",\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ]),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "https://files.pythonhosted.org/packages/97/75/10a9ebee3fd790d20926a90a2547f0bf78f371b2f13aa822c759680ca7b9/tomli-2.0.1-py3-none-any.whl",
                         "urls": [],
                         "sha256": "939de3e7a6161af0c887ef91b7d41a53e7c5a1ca976325f429cb46ea9bc30ecc",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "zip",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude in /python/pip_install/tools/bazel.py\n        # to avoid non-determinism following pip install's behavior.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/* *\",\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ]),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n",
                         "workspace_file_content": "",
                         "name": "pypi__tomli"
                    },
                    "output_tree_hash": "f9a1c7504cb442c93fd0ba6fad73302a929d58fa4ec63d9e58722761310453f6"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository pypi__wheel instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:41:10: in <toplevel>\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/rules_python/python/pip.bzl:150:29: in pip_parse\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/rules_python/python/pip_install/repositories.bzl:143:14: in pip_install_dependencies\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\nRepository rule http_archive defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "pypi__wheel",
               "generator_name": "pypi__wheel",
               "generator_function": "pip_parse",
               "generator_location": None,
               "url": "https://files.pythonhosted.org/packages/bd/7c/d38a0b30ce22fc26ed7dbc087c6d00851fb3395e9d0dac40bec1f905030c/wheel-0.38.4-py3-none-any.whl",
               "sha256": "b60533f3f5d530e971d6737ca6d58681ee434818fab630c83a734bb10c083ce8",
               "type": "zip",
               "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude in /python/pip_install/tools/bazel.py\n        # to avoid non-determinism following pip install's behavior.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/* *\",\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ]),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "https://files.pythonhosted.org/packages/bd/7c/d38a0b30ce22fc26ed7dbc087c6d00851fb3395e9d0dac40bec1f905030c/wheel-0.38.4-py3-none-any.whl",
                         "urls": [],
                         "sha256": "b60533f3f5d530e971d6737ca6d58681ee434818fab630c83a734bb10c083ce8",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "zip",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude in /python/pip_install/tools/bazel.py\n        # to avoid non-determinism following pip install's behavior.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/* *\",\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ]),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n",
                         "workspace_file_content": "",
                         "name": "pypi__wheel"
                    },
                    "output_tree_hash": "91027a1210b7bfa0eeb8de51e7fba85271509fa81116287f5bcd39b6172f4aac"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository pypi__zipp instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:41:10: in <toplevel>\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/rules_python/python/pip.bzl:150:29: in pip_parse\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/rules_python/python/pip_install/repositories.bzl:143:14: in pip_install_dependencies\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\nRepository rule http_archive defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "pypi__zipp",
               "generator_name": "pypi__zipp",
               "generator_function": "pip_parse",
               "generator_location": None,
               "url": "https://files.pythonhosted.org/packages/f4/50/cc72c5bcd48f6e98219fc4a88a5227e9e28b81637a99c49feba1d51f4d50/zipp-1.0.0-py2.py3-none-any.whl",
               "sha256": "8dda78f06bd1674bd8720df8a50bb47b6e1233c503a4eed8e7810686bde37656",
               "type": "zip",
               "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude in /python/pip_install/tools/bazel.py\n        # to avoid non-determinism following pip install's behavior.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/* *\",\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ]),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "https://files.pythonhosted.org/packages/f4/50/cc72c5bcd48f6e98219fc4a88a5227e9e28b81637a99c49feba1d51f4d50/zipp-1.0.0-py2.py3-none-any.whl",
                         "urls": [],
                         "sha256": "8dda78f06bd1674bd8720df8a50bb47b6e1233c503a4eed8e7810686bde37656",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "zip",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude in /python/pip_install/tools/bazel.py\n        # to avoid non-determinism following pip install's behavior.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/* *\",\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ]),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n",
                         "workspace_file_content": "",
                         "name": "pypi__zipp"
                    },
                    "output_tree_hash": "b3422ec36f3599644d4180eb467482299741d5ae4c5a609fda2f6d830cda5939"
               }
          ]
     },
     {
          "original_rule_class": "@rules_nodejs//nodejs:repositories.bzl%node_repositories",
          "definition_information": "Repository nodejs_linux_amd64 instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:18:27: in <toplevel>\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/rules_nodejs/nodejs/repositories.bzl:385:26: in nodejs_register_toolchains\nRepository rule node_repositories defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/rules_nodejs/nodejs/repositories.bzl:359:36: in <toplevel>\n",
          "original_attributes": {
               "name": "nodejs_linux_amd64",
               "generator_name": "nodejs_linux_amd64",
               "generator_function": "nodejs_register_toolchains",
               "generator_location": None,
               "node_version": "16.9.0",
               "platform": "linux_amd64"
          },
          "repositories": [
               {
                    "rule_class": "@rules_nodejs//nodejs:repositories.bzl%node_repositories",
                    "attributes": {
                         "name": "nodejs_linux_amd64",
                         "generator_name": "nodejs_linux_amd64",
                         "generator_function": "nodejs_register_toolchains",
                         "generator_location": None,
                         "node_version": "16.9.0",
                         "platform": "linux_amd64"
                    },
                    "output_tree_hash": "edde6b95bc5fdb32e848a90010946c1129a1683fefa76fe03e7ae2d31d516dc0"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
          "definition_information": "Repository aspect_rules_format_npm__moo__0.5.2 instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:36:27: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/toolchains.bzl:13:21: in format_register_toolchains\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_format_npm/repositories.bzl:246:15: in npm_repositories\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:544:16: in npm_import\nRepository rule _npm_import defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:331:30: in <toplevel>\n",
          "original_attributes": {
               "name": "aspect_rules_format_npm__moo__0.5.2",
               "generator_name": "aspect_rules_format_npm__moo__0.5.2",
               "generator_function": "format_register_toolchains",
               "generator_location": None,
               "package": "moo",
               "version": "0.5.2",
               "root_package": "",
               "link_packages": {},
               "integrity": "sha512-iSAJLHYKnX41mKcJKjqvnAN9sf0LMDTXDEvFv+ffuRR9a1MIuXLjMNL6EsnDHSkKLTWNqQQ5uo61P4EbU4NU+Q==",
               "patch_args": [
                    "-p0"
               ],
               "patches": [],
               "run_lifecycle_hooks": False,
               "custom_postinstall": "",
               "link_workspace": "aspect_rules_format",
               "url": ""
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
                    "attributes": {
                         "name": "aspect_rules_format_npm__moo__0.5.2",
                         "generator_name": "aspect_rules_format_npm__moo__0.5.2",
                         "generator_function": "format_register_toolchains",
                         "generator_location": None,
                         "package": "moo",
                         "version": "0.5.2",
                         "root_package": "",
                         "link_packages": {},
                         "integrity": "sha512-iSAJLHYKnX41mKcJKjqvnAN9sf0LMDTXDEvFv+ffuRR9a1MIuXLjMNL6EsnDHSkKLTWNqQQ5uo61P4EbU4NU+Q==",
                         "patch_args": [
                              "-p0"
                         ],
                         "patches": [],
                         "run_lifecycle_hooks": False,
                         "custom_postinstall": "",
                         "link_workspace": "aspect_rules_format",
                         "url": ""
                    },
                    "output_tree_hash": "a9eea176fef1498835680866a0a59973640320861343a9e83e0db0b3cd367b73"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
          "definition_information": "Repository aspect_rules_format_npm__is-glob__4.0.3 instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:36:27: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/toolchains.bzl:13:21: in format_register_toolchains\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_format_npm/repositories.bzl:196:15: in npm_repositories\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:544:16: in npm_import\nRepository rule _npm_import defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:331:30: in <toplevel>\n",
          "original_attributes": {
               "name": "aspect_rules_format_npm__is-glob__4.0.3",
               "generator_name": "aspect_rules_format_npm__is-glob__4.0.3",
               "generator_function": "format_register_toolchains",
               "generator_location": None,
               "package": "is-glob",
               "version": "4.0.3",
               "root_package": "",
               "link_packages": {},
               "integrity": "sha512-xelSayHH36ZgE7ZWhli7pW34hNbNl8Ojv5KVmkJD4hBdD3th8Tfk9vYasLM+mXWOZhFkgZfxhLSnrwRr4elSSg==",
               "patch_args": [
                    "-p0"
               ],
               "patches": [],
               "run_lifecycle_hooks": False,
               "custom_postinstall": "",
               "link_workspace": "aspect_rules_format",
               "url": ""
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
                    "attributes": {
                         "name": "aspect_rules_format_npm__is-glob__4.0.3",
                         "generator_name": "aspect_rules_format_npm__is-glob__4.0.3",
                         "generator_function": "format_register_toolchains",
                         "generator_location": None,
                         "package": "is-glob",
                         "version": "4.0.3",
                         "root_package": "",
                         "link_packages": {},
                         "integrity": "sha512-xelSayHH36ZgE7ZWhli7pW34hNbNl8Ojv5KVmkJD4hBdD3th8Tfk9vYasLM+mXWOZhFkgZfxhLSnrwRr4elSSg==",
                         "patch_args": [
                              "-p0"
                         ],
                         "patches": [],
                         "run_lifecycle_hooks": False,
                         "custom_postinstall": "",
                         "link_workspace": "aspect_rules_format",
                         "url": ""
                    },
                    "output_tree_hash": "55b8d575595ff362af2c7c0705bd624d38fdb9b106de9bb63bc1e5e500193bfa"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
          "definition_information": "Repository aspect_rules_format_npm__argparse__2.0.1 instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:36:27: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/toolchains.bzl:13:21: in format_register_toolchains\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_format_npm/repositories.bzl:46:15: in npm_repositories\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:544:16: in npm_import\nRepository rule _npm_import defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:331:30: in <toplevel>\n",
          "original_attributes": {
               "name": "aspect_rules_format_npm__argparse__2.0.1",
               "generator_name": "aspect_rules_format_npm__argparse__2.0.1",
               "generator_function": "format_register_toolchains",
               "generator_location": None,
               "package": "argparse",
               "version": "2.0.1",
               "root_package": "",
               "link_packages": {},
               "integrity": "sha512-8+9WqebbFzpX9OR+Wa6O29asIogeRMzcGtAINdpMHHyAg10f05aSFVBbcEqGf/PXw1EjAZ+q2/bEBg3DvurK3Q==",
               "patch_args": [
                    "-p0"
               ],
               "patches": [],
               "run_lifecycle_hooks": False,
               "custom_postinstall": "",
               "link_workspace": "aspect_rules_format",
               "url": ""
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
                    "attributes": {
                         "name": "aspect_rules_format_npm__argparse__2.0.1",
                         "generator_name": "aspect_rules_format_npm__argparse__2.0.1",
                         "generator_function": "format_register_toolchains",
                         "generator_location": None,
                         "package": "argparse",
                         "version": "2.0.1",
                         "root_package": "",
                         "link_packages": {},
                         "integrity": "sha512-8+9WqebbFzpX9OR+Wa6O29asIogeRMzcGtAINdpMHHyAg10f05aSFVBbcEqGf/PXw1EjAZ+q2/bEBg3DvurK3Q==",
                         "patch_args": [
                              "-p0"
                         ],
                         "patches": [],
                         "run_lifecycle_hooks": False,
                         "custom_postinstall": "",
                         "link_workspace": "aspect_rules_format",
                         "url": ""
                    },
                    "output_tree_hash": "9bcef81284fde9c067f7ecd4494b1c98d45ac99a4cd840cf6e46255659a97c92"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
          "definition_information": "Repository aspect_rules_format_npm__commander__2.20.3 instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:36:27: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/toolchains.bzl:13:21: in format_register_toolchains\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_format_npm/repositories.bzl:74:15: in npm_repositories\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:544:16: in npm_import\nRepository rule _npm_import defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:331:30: in <toplevel>\n",
          "original_attributes": {
               "name": "aspect_rules_format_npm__commander__2.20.3",
               "generator_name": "aspect_rules_format_npm__commander__2.20.3",
               "generator_function": "format_register_toolchains",
               "generator_location": None,
               "package": "commander",
               "version": "2.20.3",
               "root_package": "",
               "link_packages": {},
               "integrity": "sha512-GpVkmM8vF2vQUkj2LvZmD35JxeJOLCwJ9cUkugyk2nuhbv3+mJvpLYYt+0+USMxE+oj+ey/lJEnhZw75x/OMcQ==",
               "patch_args": [
                    "-p0"
               ],
               "patches": [],
               "run_lifecycle_hooks": False,
               "custom_postinstall": "",
               "link_workspace": "aspect_rules_format",
               "url": ""
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
                    "attributes": {
                         "name": "aspect_rules_format_npm__commander__2.20.3",
                         "generator_name": "aspect_rules_format_npm__commander__2.20.3",
                         "generator_function": "format_register_toolchains",
                         "generator_location": None,
                         "package": "commander",
                         "version": "2.20.3",
                         "root_package": "",
                         "link_packages": {},
                         "integrity": "sha512-GpVkmM8vF2vQUkj2LvZmD35JxeJOLCwJ9cUkugyk2nuhbv3+mJvpLYYt+0+USMxE+oj+ey/lJEnhZw75x/OMcQ==",
                         "patch_args": [
                              "-p0"
                         ],
                         "patches": [],
                         "run_lifecycle_hooks": False,
                         "custom_postinstall": "",
                         "link_workspace": "aspect_rules_format",
                         "url": ""
                    },
                    "output_tree_hash": "d4168b9f89f3db737aea4ec3b3f0bae4e5308025080a336c2e2c5e87e055b100"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
          "definition_information": "Repository aspect_rules_format_npm__tiny-glob__0.2.9 instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:36:27: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/toolchains.bzl:13:21: in format_register_toolchains\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_format_npm/repositories.bzl:694:15: in npm_repositories\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:544:16: in npm_import\nRepository rule _npm_import defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:331:30: in <toplevel>\n",
          "original_attributes": {
               "name": "aspect_rules_format_npm__tiny-glob__0.2.9",
               "generator_name": "aspect_rules_format_npm__tiny-glob__0.2.9",
               "generator_function": "format_register_toolchains",
               "generator_location": None,
               "package": "tiny-glob",
               "version": "0.2.9",
               "root_package": "",
               "link_packages": {},
               "integrity": "sha512-g/55ssRPUjShh+xkfx9UPDXqhckHEsHr4Vd9zX55oSdGZc/MD0m3sferOkwWtp98bv+kcVfEHtRJgBVJzelrzg==",
               "patch_args": [
                    "-p0"
               ],
               "patches": [],
               "run_lifecycle_hooks": False,
               "custom_postinstall": "",
               "link_workspace": "aspect_rules_format",
               "url": ""
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
                    "attributes": {
                         "name": "aspect_rules_format_npm__tiny-glob__0.2.9",
                         "generator_name": "aspect_rules_format_npm__tiny-glob__0.2.9",
                         "generator_function": "format_register_toolchains",
                         "generator_location": None,
                         "package": "tiny-glob",
                         "version": "0.2.9",
                         "root_package": "",
                         "link_packages": {},
                         "integrity": "sha512-g/55ssRPUjShh+xkfx9UPDXqhckHEsHr4Vd9zX55oSdGZc/MD0m3sferOkwWtp98bv+kcVfEHtRJgBVJzelrzg==",
                         "patch_args": [
                              "-p0"
                         ],
                         "patches": [],
                         "run_lifecycle_hooks": False,
                         "custom_postinstall": "",
                         "link_workspace": "aspect_rules_format",
                         "url": ""
                    },
                    "output_tree_hash": "e0f98f7396167648073a4b562e5f0b1231d7f28f708013d44da3a360bf41242d"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
          "definition_information": "Repository aspect_rules_format_npm__prettier-plugin-sql__0.14.0__prettier_2.8.7 instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:36:27: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/toolchains.bzl:13:21: in format_register_toolchains\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_format_npm/repositories.bzl:424:15: in npm_repositories\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:544:16: in npm_import\nRepository rule _npm_import defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:331:30: in <toplevel>\n",
          "original_attributes": {
               "name": "aspect_rules_format_npm__prettier-plugin-sql__0.14.0__prettier_2.8.7",
               "generator_name": "aspect_rules_format_npm__prettier-plugin-sql__0.14.0__prettier_2.8.7",
               "generator_function": "format_register_toolchains",
               "generator_location": None,
               "package": "prettier-plugin-sql",
               "version": "0.14.0_prettier@2.8.7",
               "root_package": "",
               "link_packages": {
                    "": [
                         "prettier-plugin-sql"
                    ]
               },
               "integrity": "sha512-dRgINgNd3ZhBDuO/+EFalJjSlAqNXvXv9XDtSCeMufXaP6O64HHLBo1Szo+l+cfvXFxwvkTSGrS+sjpEpSchNA==",
               "patch_args": [
                    "-p0"
               ],
               "patches": [],
               "run_lifecycle_hooks": False,
               "custom_postinstall": "",
               "link_workspace": "aspect_rules_format",
               "url": ""
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
                    "attributes": {
                         "name": "aspect_rules_format_npm__prettier-plugin-sql__0.14.0__prettier_2.8.7",
                         "generator_name": "aspect_rules_format_npm__prettier-plugin-sql__0.14.0__prettier_2.8.7",
                         "generator_function": "format_register_toolchains",
                         "generator_location": None,
                         "package": "prettier-plugin-sql",
                         "version": "0.14.0_prettier@2.8.7",
                         "root_package": "",
                         "link_packages": {
                              "": [
                                   "prettier-plugin-sql"
                              ]
                         },
                         "integrity": "sha512-dRgINgNd3ZhBDuO/+EFalJjSlAqNXvXv9XDtSCeMufXaP6O64HHLBo1Szo+l+cfvXFxwvkTSGrS+sjpEpSchNA==",
                         "patch_args": [
                              "-p0"
                         ],
                         "patches": [],
                         "run_lifecycle_hooks": False,
                         "custom_postinstall": "",
                         "link_workspace": "aspect_rules_format",
                         "url": ""
                    },
                    "output_tree_hash": "202a0aa69f9f51308eb653af553eb24ea17c7b4791f1f0a3ad03584fdfd105f9"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
          "definition_information": "Repository aspect_rules_format_npm__tslib__2.5.0 instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:36:27: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/toolchains.bzl:13:21: in format_register_toolchains\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_format_npm/repositories.bzl:714:15: in npm_repositories\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:544:16: in npm_import\nRepository rule _npm_import defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:331:30: in <toplevel>\n",
          "original_attributes": {
               "name": "aspect_rules_format_npm__tslib__2.5.0",
               "generator_name": "aspect_rules_format_npm__tslib__2.5.0",
               "generator_function": "format_register_toolchains",
               "generator_location": None,
               "package": "tslib",
               "version": "2.5.0",
               "root_package": "",
               "link_packages": {},
               "integrity": "sha512-336iVw3rtn2BUK7ORdIAHTyxHGRIHVReokCR3XjbckJMK7ms8FysBfhLR8IXnAgy7T0PTPNBWKiH514FOW/WSg==",
               "patch_args": [
                    "-p0"
               ],
               "patches": [],
               "run_lifecycle_hooks": False,
               "custom_postinstall": "",
               "link_workspace": "aspect_rules_format",
               "url": ""
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
                    "attributes": {
                         "name": "aspect_rules_format_npm__tslib__2.5.0",
                         "generator_name": "aspect_rules_format_npm__tslib__2.5.0",
                         "generator_function": "format_register_toolchains",
                         "generator_location": None,
                         "package": "tslib",
                         "version": "2.5.0",
                         "root_package": "",
                         "link_packages": {},
                         "integrity": "sha512-336iVw3rtn2BUK7ORdIAHTyxHGRIHVReokCR3XjbckJMK7ms8FysBfhLR8IXnAgy7T0PTPNBWKiH514FOW/WSg==",
                         "patch_args": [
                              "-p0"
                         ],
                         "patches": [],
                         "run_lifecycle_hooks": False,
                         "custom_postinstall": "",
                         "link_workspace": "aspect_rules_format",
                         "url": ""
                    },
                    "output_tree_hash": "61882fe8cc32e533394f014a7d34197e57c637e078c765ab0e81a2143cd0a279"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
          "definition_information": "Repository aspect_rules_format_npm__sql-formatter__12.2.0 instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:36:27: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/toolchains.bzl:13:21: in format_register_toolchains\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_format_npm/repositories.bzl:632:15: in npm_repositories\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:544:16: in npm_import\nRepository rule _npm_import defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:331:30: in <toplevel>\n",
          "original_attributes": {
               "name": "aspect_rules_format_npm__sql-formatter__12.2.0",
               "generator_name": "aspect_rules_format_npm__sql-formatter__12.2.0",
               "generator_function": "format_register_toolchains",
               "generator_location": None,
               "package": "sql-formatter",
               "version": "12.2.0",
               "root_package": "",
               "link_packages": {},
               "integrity": "sha512-wNsPUdOD6nnN9RUgHlNprQtm+iLW5LTOy/T0/2DDr2UeWSP8mvlQHrx6TY+IG1nfu5Kipq9GaOtS9SVq8s0Vig==",
               "patch_args": [
                    "-p0"
               ],
               "patches": [],
               "run_lifecycle_hooks": False,
               "custom_postinstall": "",
               "link_workspace": "aspect_rules_format",
               "url": ""
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
                    "attributes": {
                         "name": "aspect_rules_format_npm__sql-formatter__12.2.0",
                         "generator_name": "aspect_rules_format_npm__sql-formatter__12.2.0",
                         "generator_function": "format_register_toolchains",
                         "generator_location": None,
                         "package": "sql-formatter",
                         "version": "12.2.0",
                         "root_package": "",
                         "link_packages": {},
                         "integrity": "sha512-wNsPUdOD6nnN9RUgHlNprQtm+iLW5LTOy/T0/2DDr2UeWSP8mvlQHrx6TY+IG1nfu5Kipq9GaOtS9SVq8s0Vig==",
                         "patch_args": [
                              "-p0"
                         ],
                         "patches": [],
                         "run_lifecycle_hooks": False,
                         "custom_postinstall": "",
                         "link_workspace": "aspect_rules_format",
                         "url": ""
                    },
                    "output_tree_hash": "b0dd1a959e9e07fd06a2ab7a89393f7a1eae3a39fc210344e103c629554698fd"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
          "definition_information": "Repository aspect_rules_format_npm__big-integer__1.6.51 instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:36:27: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/toolchains.bzl:13:21: in format_register_toolchains\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_format_npm/repositories.bzl:60:15: in npm_repositories\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:544:16: in npm_import\nRepository rule _npm_import defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:331:30: in <toplevel>\n",
          "original_attributes": {
               "name": "aspect_rules_format_npm__big-integer__1.6.51",
               "generator_name": "aspect_rules_format_npm__big-integer__1.6.51",
               "generator_function": "format_register_toolchains",
               "generator_location": None,
               "package": "big-integer",
               "version": "1.6.51",
               "root_package": "",
               "link_packages": {},
               "integrity": "sha512-GPEid2Y9QU1Exl1rpO9B2IPJGHPSupF5GnVIP0blYvNOMer2bTvSWs1jGOUg04hTmu67nmLsQ9TBo1puaotBHg==",
               "patch_args": [
                    "-p0"
               ],
               "patches": [],
               "run_lifecycle_hooks": False,
               "custom_postinstall": "",
               "link_workspace": "aspect_rules_format",
               "url": ""
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
                    "attributes": {
                         "name": "aspect_rules_format_npm__big-integer__1.6.51",
                         "generator_name": "aspect_rules_format_npm__big-integer__1.6.51",
                         "generator_function": "format_register_toolchains",
                         "generator_location": None,
                         "package": "big-integer",
                         "version": "1.6.51",
                         "root_package": "",
                         "link_packages": {},
                         "integrity": "sha512-GPEid2Y9QU1Exl1rpO9B2IPJGHPSupF5GnVIP0blYvNOMer2bTvSWs1jGOUg04hTmu67nmLsQ9TBo1puaotBHg==",
                         "patch_args": [
                              "-p0"
                         ],
                         "patches": [],
                         "run_lifecycle_hooks": False,
                         "custom_postinstall": "",
                         "link_workspace": "aspect_rules_format",
                         "url": ""
                    },
                    "output_tree_hash": "981f2bc0d96243b5d5f8e88146da877a5739bd74efbbc4b190a318280d2d0c99"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
          "definition_information": "Repository aspect_rules_format_npm__mvdan-sh__0.10.1 instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:36:27: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/toolchains.bzl:13:21: in format_register_toolchains\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_format_npm/repositories.bzl:260:15: in npm_repositories\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:544:16: in npm_import\nRepository rule _npm_import defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:331:30: in <toplevel>\n",
          "original_attributes": {
               "name": "aspect_rules_format_npm__mvdan-sh__0.10.1",
               "generator_name": "aspect_rules_format_npm__mvdan-sh__0.10.1",
               "generator_function": "format_register_toolchains",
               "generator_location": None,
               "package": "mvdan-sh",
               "version": "0.10.1",
               "root_package": "",
               "link_packages": {},
               "integrity": "sha512-kMbrH0EObaKmK3nVRKUIIya1dpASHIEusM13S4V1ViHFuxuNxCo+arxoa6j/dbV22YBGjl7UKJm9QQKJ2Crzhg==",
               "patch_args": [
                    "-p0"
               ],
               "patches": [],
               "run_lifecycle_hooks": False,
               "custom_postinstall": "",
               "link_workspace": "aspect_rules_format",
               "url": ""
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
                    "attributes": {
                         "name": "aspect_rules_format_npm__mvdan-sh__0.10.1",
                         "generator_name": "aspect_rules_format_npm__mvdan-sh__0.10.1",
                         "generator_function": "format_register_toolchains",
                         "generator_location": None,
                         "package": "mvdan-sh",
                         "version": "0.10.1",
                         "root_package": "",
                         "link_packages": {},
                         "integrity": "sha512-kMbrH0EObaKmK3nVRKUIIya1dpASHIEusM13S4V1ViHFuxuNxCo+arxoa6j/dbV22YBGjl7UKJm9QQKJ2Crzhg==",
                         "patch_args": [
                              "-p0"
                         ],
                         "patches": [],
                         "run_lifecycle_hooks": False,
                         "custom_postinstall": "",
                         "link_workspace": "aspect_rules_format",
                         "url": ""
                    },
                    "output_tree_hash": "923916c1333e8fe537136b25330d2b85cd504e477731dd43eb92c30c91655800"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
          "definition_information": "Repository aspect_rules_format_npm__prettier-plugin-sh__0.12.8__prettier_2.8.7 instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:36:27: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/toolchains.bzl:13:21: in format_register_toolchains\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_format_npm/repositories.bzl:368:15: in npm_repositories\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:544:16: in npm_import\nRepository rule _npm_import defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:331:30: in <toplevel>\n",
          "original_attributes": {
               "name": "aspect_rules_format_npm__prettier-plugin-sh__0.12.8__prettier_2.8.7",
               "generator_name": "aspect_rules_format_npm__prettier-plugin-sh__0.12.8__prettier_2.8.7",
               "generator_function": "format_register_toolchains",
               "generator_location": None,
               "package": "prettier-plugin-sh",
               "version": "0.12.8_prettier@2.8.7",
               "root_package": "",
               "link_packages": {
                    "": [
                         "prettier-plugin-sh"
                    ]
               },
               "integrity": "sha512-VOq8h2Gn5UzrCIKm4p/nAScXJbN09HdyFDknAcxt6Qu/tv/juu9bahxSrcnM9XWYA+Spz1F1ANJ4LhfwB7+Q1Q==",
               "patch_args": [
                    "-p0"
               ],
               "patches": [],
               "run_lifecycle_hooks": False,
               "custom_postinstall": "",
               "link_workspace": "aspect_rules_format",
               "url": ""
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
                    "attributes": {
                         "name": "aspect_rules_format_npm__prettier-plugin-sh__0.12.8__prettier_2.8.7",
                         "generator_name": "aspect_rules_format_npm__prettier-plugin-sh__0.12.8__prettier_2.8.7",
                         "generator_function": "format_register_toolchains",
                         "generator_location": None,
                         "package": "prettier-plugin-sh",
                         "version": "0.12.8_prettier@2.8.7",
                         "root_package": "",
                         "link_packages": {
                              "": [
                                   "prettier-plugin-sh"
                              ]
                         },
                         "integrity": "sha512-VOq8h2Gn5UzrCIKm4p/nAScXJbN09HdyFDknAcxt6Qu/tv/juu9bahxSrcnM9XWYA+Spz1F1ANJ4LhfwB7+Q1Q==",
                         "patch_args": [
                              "-p0"
                         ],
                         "patches": [],
                         "run_lifecycle_hooks": False,
                         "custom_postinstall": "",
                         "link_workspace": "aspect_rules_format",
                         "url": ""
                    },
                    "output_tree_hash": "21c2bdf2a46445c90d08554d70b4c5a0d3a318baddb953c8635bea064dae2392"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
          "definition_information": "Repository aspect_rules_format_npm__sh-syntax__0.3.7 instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:36:27: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/toolchains.bzl:13:21: in format_register_toolchains\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_format_npm/repositories.bzl:582:15: in npm_repositories\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:544:16: in npm_import\nRepository rule _npm_import defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:331:30: in <toplevel>\n",
          "original_attributes": {
               "name": "aspect_rules_format_npm__sh-syntax__0.3.7",
               "generator_name": "aspect_rules_format_npm__sh-syntax__0.3.7",
               "generator_function": "format_register_toolchains",
               "generator_location": None,
               "package": "sh-syntax",
               "version": "0.3.7",
               "root_package": "",
               "link_packages": {},
               "integrity": "sha512-xIB/uRniZ9urxAuXp1Ouh/BKSI1VK8RSqfwGj7cV57HvGrFo3vHdJfv8Tdp/cVcxJgXQTkmHr5mG5rqJW8r4wQ==",
               "patch_args": [
                    "-p0"
               ],
               "patches": [],
               "run_lifecycle_hooks": False,
               "custom_postinstall": "",
               "link_workspace": "aspect_rules_format",
               "url": ""
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
                    "attributes": {
                         "name": "aspect_rules_format_npm__sh-syntax__0.3.7",
                         "generator_name": "aspect_rules_format_npm__sh-syntax__0.3.7",
                         "generator_function": "format_register_toolchains",
                         "generator_location": None,
                         "package": "sh-syntax",
                         "version": "0.3.7",
                         "root_package": "",
                         "link_packages": {},
                         "integrity": "sha512-xIB/uRniZ9urxAuXp1Ouh/BKSI1VK8RSqfwGj7cV57HvGrFo3vHdJfv8Tdp/cVcxJgXQTkmHr5mG5rqJW8r4wQ==",
                         "patch_args": [
                              "-p0"
                         ],
                         "patches": [],
                         "run_lifecycle_hooks": False,
                         "custom_postinstall": "",
                         "link_workspace": "aspect_rules_format",
                         "url": ""
                    },
                    "output_tree_hash": "8db0d716e77927b922a424ddfe17c5c63e295889862824dbfae14ddeec0de7ae"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
          "definition_information": "Repository aspect_rules_format_npm__railroad-diagrams__1.0.0 instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:36:27: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/toolchains.bzl:13:21: in format_register_toolchains\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_format_npm/repositories.bzl:534:15: in npm_repositories\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:544:16: in npm_import\nRepository rule _npm_import defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:331:30: in <toplevel>\n",
          "original_attributes": {
               "name": "aspect_rules_format_npm__railroad-diagrams__1.0.0",
               "generator_name": "aspect_rules_format_npm__railroad-diagrams__1.0.0",
               "generator_function": "format_register_toolchains",
               "generator_location": None,
               "package": "railroad-diagrams",
               "version": "1.0.0",
               "root_package": "",
               "link_packages": {},
               "integrity": "sha512-cz93DjNeLY0idrCNOH6PviZGRN9GJhsdm9hpn1YCS879fj4W+x5IFJhhkRZcwVgMmFF7R82UA/7Oh+R8lLZg6A==",
               "patch_args": [
                    "-p0"
               ],
               "patches": [],
               "run_lifecycle_hooks": False,
               "custom_postinstall": "",
               "link_workspace": "aspect_rules_format",
               "url": ""
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
                    "attributes": {
                         "name": "aspect_rules_format_npm__railroad-diagrams__1.0.0",
                         "generator_name": "aspect_rules_format_npm__railroad-diagrams__1.0.0",
                         "generator_function": "format_register_toolchains",
                         "generator_location": None,
                         "package": "railroad-diagrams",
                         "version": "1.0.0",
                         "root_package": "",
                         "link_packages": {},
                         "integrity": "sha512-cz93DjNeLY0idrCNOH6PviZGRN9GJhsdm9hpn1YCS879fj4W+x5IFJhhkRZcwVgMmFF7R82UA/7Oh+R8lLZg6A==",
                         "patch_args": [
                              "-p0"
                         ],
                         "patches": [],
                         "run_lifecycle_hooks": False,
                         "custom_postinstall": "",
                         "link_workspace": "aspect_rules_format",
                         "url": ""
                    },
                    "output_tree_hash": "93cecc80ab2757334648ec3f4fb6a4701a9b6e91e87edd64bd584b9d335d6e3a"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
          "definition_information": "Repository aspect_rules_format_npm__is-extglob__2.1.1 instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:36:27: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/toolchains.bzl:13:21: in format_register_toolchains\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_format_npm/repositories.bzl:182:15: in npm_repositories\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:544:16: in npm_import\nRepository rule _npm_import defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:331:30: in <toplevel>\n",
          "original_attributes": {
               "name": "aspect_rules_format_npm__is-extglob__2.1.1",
               "generator_name": "aspect_rules_format_npm__is-extglob__2.1.1",
               "generator_function": "format_register_toolchains",
               "generator_location": None,
               "package": "is-extglob",
               "version": "2.1.1",
               "root_package": "",
               "link_packages": {},
               "integrity": "sha512-SbKbANkN603Vi4jEZv49LeVJMn4yGwsbzZworEoyEiutsN3nJYdbO36zfhGJ6QEDpOZIFkDtnq5JRxmvl3jsoQ==",
               "patch_args": [
                    "-p0"
               ],
               "patches": [],
               "run_lifecycle_hooks": False,
               "custom_postinstall": "",
               "link_workspace": "aspect_rules_format",
               "url": ""
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
                    "attributes": {
                         "name": "aspect_rules_format_npm__is-extglob__2.1.1",
                         "generator_name": "aspect_rules_format_npm__is-extglob__2.1.1",
                         "generator_function": "format_register_toolchains",
                         "generator_location": None,
                         "package": "is-extglob",
                         "version": "2.1.1",
                         "root_package": "",
                         "link_packages": {},
                         "integrity": "sha512-SbKbANkN603Vi4jEZv49LeVJMn4yGwsbzZworEoyEiutsN3nJYdbO36zfhGJ6QEDpOZIFkDtnq5JRxmvl3jsoQ==",
                         "patch_args": [
                              "-p0"
                         ],
                         "patches": [],
                         "run_lifecycle_hooks": False,
                         "custom_postinstall": "",
                         "link_workspace": "aspect_rules_format",
                         "url": ""
                    },
                    "output_tree_hash": "42a40a4f1b5c0a488d1495930027afbad008d2e5cffb08f38b41881a2aaf4175"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
          "definition_information": "Repository aspect_rules_format_npm__randexp__0.4.6 instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:36:27: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/toolchains.bzl:13:21: in format_register_toolchains\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_format_npm/repositories.bzl:548:15: in npm_repositories\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:544:16: in npm_import\nRepository rule _npm_import defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:331:30: in <toplevel>\n",
          "original_attributes": {
               "name": "aspect_rules_format_npm__randexp__0.4.6",
               "generator_name": "aspect_rules_format_npm__randexp__0.4.6",
               "generator_function": "format_register_toolchains",
               "generator_location": None,
               "package": "randexp",
               "version": "0.4.6",
               "root_package": "",
               "link_packages": {},
               "integrity": "sha512-80WNmd9DA0tmZrw9qQa62GPPWfuXJknrmVmLcxvq4uZBdYqb1wYoKTmnlGUchvVWe0XiLupYkBoXVOxz3C8DYQ==",
               "patch_args": [
                    "-p0"
               ],
               "patches": [],
               "run_lifecycle_hooks": False,
               "custom_postinstall": "",
               "link_workspace": "aspect_rules_format",
               "url": ""
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
                    "attributes": {
                         "name": "aspect_rules_format_npm__randexp__0.4.6",
                         "generator_name": "aspect_rules_format_npm__randexp__0.4.6",
                         "generator_function": "format_register_toolchains",
                         "generator_location": None,
                         "package": "randexp",
                         "version": "0.4.6",
                         "root_package": "",
                         "link_packages": {},
                         "integrity": "sha512-80WNmd9DA0tmZrw9qQa62GPPWfuXJknrmVmLcxvq4uZBdYqb1wYoKTmnlGUchvVWe0XiLupYkBoXVOxz3C8DYQ==",
                         "patch_args": [
                              "-p0"
                         ],
                         "patches": [],
                         "run_lifecycle_hooks": False,
                         "custom_postinstall": "",
                         "link_workspace": "aspect_rules_format",
                         "url": ""
                    },
                    "output_tree_hash": "165e9b43b9984553e2902a9ba50ac73b055d45a73ab61db68f66f0ec02d94c8a"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
          "definition_information": "Repository aspect_rules_format_npm__shebang-regex__3.0.0 instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:36:27: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/toolchains.bzl:13:21: in format_register_toolchains\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_format_npm/repositories.bzl:618:15: in npm_repositories\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:544:16: in npm_import\nRepository rule _npm_import defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:331:30: in <toplevel>\n",
          "original_attributes": {
               "name": "aspect_rules_format_npm__shebang-regex__3.0.0",
               "generator_name": "aspect_rules_format_npm__shebang-regex__3.0.0",
               "generator_function": "format_register_toolchains",
               "generator_location": None,
               "package": "shebang-regex",
               "version": "3.0.0",
               "root_package": "",
               "link_packages": {},
               "integrity": "sha512-7++dFhtcx3353uBaq8DDR4NuxBetBzC7ZQOhmTQInHEd6bSrXdiEyzCvG07Z44UYdLShWUyXt5M/yhz8ekcb1A==",
               "patch_args": [
                    "-p0"
               ],
               "patches": [],
               "run_lifecycle_hooks": False,
               "custom_postinstall": "",
               "link_workspace": "aspect_rules_format",
               "url": ""
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
                    "attributes": {
                         "name": "aspect_rules_format_npm__shebang-regex__3.0.0",
                         "generator_name": "aspect_rules_format_npm__shebang-regex__3.0.0",
                         "generator_function": "format_register_toolchains",
                         "generator_location": None,
                         "package": "shebang-regex",
                         "version": "3.0.0",
                         "root_package": "",
                         "link_packages": {},
                         "integrity": "sha512-7++dFhtcx3353uBaq8DDR4NuxBetBzC7ZQOhmTQInHEd6bSrXdiEyzCvG07Z44UYdLShWUyXt5M/yhz8ekcb1A==",
                         "patch_args": [
                              "-p0"
                         ],
                         "patches": [],
                         "run_lifecycle_hooks": False,
                         "custom_postinstall": "",
                         "link_workspace": "aspect_rules_format",
                         "url": ""
                    },
                    "output_tree_hash": "aacf4aa387cd621d6b8d920eb2741fb25ee01dac085bf838070db6cf7337d725"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
          "definition_information": "Repository aspect_rules_format_npm__ret__0.1.15 instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:36:27: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/toolchains.bzl:13:21: in format_register_toolchains\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_format_npm/repositories.bzl:568:15: in npm_repositories\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:544:16: in npm_import\nRepository rule _npm_import defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:331:30: in <toplevel>\n",
          "original_attributes": {
               "name": "aspect_rules_format_npm__ret__0.1.15",
               "generator_name": "aspect_rules_format_npm__ret__0.1.15",
               "generator_function": "format_register_toolchains",
               "generator_location": None,
               "package": "ret",
               "version": "0.1.15",
               "root_package": "",
               "link_packages": {},
               "integrity": "sha512-TTlYpa+OL+vMMNG24xSlQGEJ3B/RzEfUlLct7b5G/ytav+wPrplCpVMFuwzXbkecJrb6IYo1iFb0S9v37754mg==",
               "patch_args": [
                    "-p0"
               ],
               "patches": [],
               "run_lifecycle_hooks": False,
               "custom_postinstall": "",
               "link_workspace": "aspect_rules_format",
               "url": ""
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
                    "attributes": {
                         "name": "aspect_rules_format_npm__ret__0.1.15",
                         "generator_name": "aspect_rules_format_npm__ret__0.1.15",
                         "generator_function": "format_register_toolchains",
                         "generator_location": None,
                         "package": "ret",
                         "version": "0.1.15",
                         "root_package": "",
                         "link_packages": {},
                         "integrity": "sha512-TTlYpa+OL+vMMNG24xSlQGEJ3B/RzEfUlLct7b5G/ytav+wPrplCpVMFuwzXbkecJrb6IYo1iFb0S9v37754mg==",
                         "patch_args": [
                              "-p0"
                         ],
                         "patches": [],
                         "run_lifecycle_hooks": False,
                         "custom_postinstall": "",
                         "link_workspace": "aspect_rules_format",
                         "url": ""
                    },
                    "output_tree_hash": "2274b8e41dc6d82753287128393a3d1a0e3fb31158408e040ca8b870ec44b9c2"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
          "definition_information": "Repository aspect_rules_format_npm__discontinuous-range__1.0.0 instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:36:27: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/toolchains.bzl:13:21: in format_register_toolchains\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_format_npm/repositories.bzl:126:15: in npm_repositories\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:544:16: in npm_import\nRepository rule _npm_import defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:331:30: in <toplevel>\n",
          "original_attributes": {
               "name": "aspect_rules_format_npm__discontinuous-range__1.0.0",
               "generator_name": "aspect_rules_format_npm__discontinuous-range__1.0.0",
               "generator_function": "format_register_toolchains",
               "generator_location": None,
               "package": "discontinuous-range",
               "version": "1.0.0",
               "root_package": "",
               "link_packages": {},
               "integrity": "sha512-c68LpLbO+7kP/b1Hr1qs8/BJ09F5khZGTxqxZuhzxpmwJKOgRFHJWIb9/KmqnqHhLdO55aOxFH/EGBvUQbL/RQ==",
               "patch_args": [
                    "-p0"
               ],
               "patches": [],
               "run_lifecycle_hooks": False,
               "custom_postinstall": "",
               "link_workspace": "aspect_rules_format",
               "url": ""
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
                    "attributes": {
                         "name": "aspect_rules_format_npm__discontinuous-range__1.0.0",
                         "generator_name": "aspect_rules_format_npm__discontinuous-range__1.0.0",
                         "generator_function": "format_register_toolchains",
                         "generator_location": None,
                         "package": "discontinuous-range",
                         "version": "1.0.0",
                         "root_package": "",
                         "link_packages": {},
                         "integrity": "sha512-c68LpLbO+7kP/b1Hr1qs8/BJ09F5khZGTxqxZuhzxpmwJKOgRFHJWIb9/KmqnqHhLdO55aOxFH/EGBvUQbL/RQ==",
                         "patch_args": [
                              "-p0"
                         ],
                         "patches": [],
                         "run_lifecycle_hooks": False,
                         "custom_postinstall": "",
                         "link_workspace": "aspect_rules_format",
                         "url": ""
                    },
                    "output_tree_hash": "e6ae5a038fa38605c165750a15a1d3337e9ecdf30ef01ce24a8b44ffec85595b"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
          "definition_information": "Repository aspect_rules_format_npm__nearley__2.20.1 instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:36:27: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/toolchains.bzl:13:21: in format_register_toolchains\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_format_npm/repositories.bzl:274:15: in npm_repositories\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:544:16: in npm_import\nRepository rule _npm_import defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:331:30: in <toplevel>\n",
          "original_attributes": {
               "name": "aspect_rules_format_npm__nearley__2.20.1",
               "generator_name": "aspect_rules_format_npm__nearley__2.20.1",
               "generator_function": "format_register_toolchains",
               "generator_location": None,
               "package": "nearley",
               "version": "2.20.1",
               "root_package": "",
               "link_packages": {},
               "integrity": "sha512-+Mc8UaAebFzgV+KpI5n7DasuuQCHA89dmwm7JXw3TV43ukfNQ9DnBH3Mdb2g/I4Fdxc26pwimBWvjIw0UAILSQ==",
               "patch_args": [
                    "-p0"
               ],
               "patches": [],
               "run_lifecycle_hooks": False,
               "custom_postinstall": "",
               "link_workspace": "aspect_rules_format",
               "url": ""
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
                    "attributes": {
                         "name": "aspect_rules_format_npm__nearley__2.20.1",
                         "generator_name": "aspect_rules_format_npm__nearley__2.20.1",
                         "generator_function": "format_register_toolchains",
                         "generator_location": None,
                         "package": "nearley",
                         "version": "2.20.1",
                         "root_package": "",
                         "link_packages": {},
                         "integrity": "sha512-+Mc8UaAebFzgV+KpI5n7DasuuQCHA89dmwm7JXw3TV43ukfNQ9DnBH3Mdb2g/I4Fdxc26pwimBWvjIw0UAILSQ==",
                         "patch_args": [
                              "-p0"
                         ],
                         "patches": [],
                         "run_lifecycle_hooks": False,
                         "custom_postinstall": "",
                         "link_workspace": "aspect_rules_format",
                         "url": ""
                    },
                    "output_tree_hash": "5f6a405e508f5b06406f76649e5920779180db8f5a1ebb44cc4872549ace2dfd"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
          "definition_information": "Repository aspect_rules_format_npm__open__8.4.2 instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:36:27: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/toolchains.bzl:13:21: in format_register_toolchains\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_format_npm/repositories.bzl:318:15: in npm_repositories\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:544:16: in npm_import\nRepository rule _npm_import defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:331:30: in <toplevel>\n",
          "original_attributes": {
               "name": "aspect_rules_format_npm__open__8.4.2",
               "generator_name": "aspect_rules_format_npm__open__8.4.2",
               "generator_function": "format_register_toolchains",
               "generator_location": None,
               "package": "open",
               "version": "8.4.2",
               "root_package": "",
               "link_packages": {},
               "integrity": "sha512-7x81NCL719oNbsq/3mh+hVrAWmFuEYUqrq/Iw3kUzH8ReypT9QQ0BLoJS7/G9k6N81XjW4qHWtjWwe/9eLy1EQ==",
               "patch_args": [
                    "-p0"
               ],
               "patches": [],
               "run_lifecycle_hooks": False,
               "custom_postinstall": "",
               "link_workspace": "aspect_rules_format",
               "url": ""
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
                    "attributes": {
                         "name": "aspect_rules_format_npm__open__8.4.2",
                         "generator_name": "aspect_rules_format_npm__open__8.4.2",
                         "generator_function": "format_register_toolchains",
                         "generator_location": None,
                         "package": "open",
                         "version": "8.4.2",
                         "root_package": "",
                         "link_packages": {},
                         "integrity": "sha512-7x81NCL719oNbsq/3mh+hVrAWmFuEYUqrq/Iw3kUzH8ReypT9QQ0BLoJS7/G9k6N81XjW4qHWtjWwe/9eLy1EQ==",
                         "patch_args": [
                              "-p0"
                         ],
                         "patches": [],
                         "run_lifecycle_hooks": False,
                         "custom_postinstall": "",
                         "link_workspace": "aspect_rules_format",
                         "url": ""
                    },
                    "output_tree_hash": "a739e3c4b2bd1c47567d5e38926ab9be185a46bddaab2d34ef7ae894e837eaf8"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
          "definition_information": "Repository aspect_rules_format_npm__at_pkgr_utils__2.3.1 instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:36:27: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/toolchains.bzl:13:21: in format_register_toolchains\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_format_npm/repositories.bzl:7:15: in npm_repositories\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:544:16: in npm_import\nRepository rule _npm_import defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:331:30: in <toplevel>\n",
          "original_attributes": {
               "name": "aspect_rules_format_npm__at_pkgr_utils__2.3.1",
               "generator_name": "aspect_rules_format_npm__at_pkgr_utils__2.3.1",
               "generator_function": "format_register_toolchains",
               "generator_location": None,
               "package": "@pkgr/utils",
               "version": "2.3.1",
               "root_package": "",
               "link_packages": {},
               "integrity": "sha512-wfzX8kc1PMyUILA+1Z/EqoE4UCXGy0iRGMhPwdfae1+f0OXlLqCk+By+aMzgJBzR9AzS4CDizioG6Ss1gvAFJw==",
               "patch_args": [
                    "-p0"
               ],
               "patches": [],
               "run_lifecycle_hooks": False,
               "custom_postinstall": "",
               "link_workspace": "aspect_rules_format",
               "url": ""
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
                    "attributes": {
                         "name": "aspect_rules_format_npm__at_pkgr_utils__2.3.1",
                         "generator_name": "aspect_rules_format_npm__at_pkgr_utils__2.3.1",
                         "generator_function": "format_register_toolchains",
                         "generator_location": None,
                         "package": "@pkgr/utils",
                         "version": "2.3.1",
                         "root_package": "",
                         "link_packages": {},
                         "integrity": "sha512-wfzX8kc1PMyUILA+1Z/EqoE4UCXGy0iRGMhPwdfae1+f0OXlLqCk+By+aMzgJBzR9AzS4CDizioG6Ss1gvAFJw==",
                         "patch_args": [
                              "-p0"
                         ],
                         "patches": [],
                         "run_lifecycle_hooks": False,
                         "custom_postinstall": "",
                         "link_workspace": "aspect_rules_format",
                         "url": ""
                    },
                    "output_tree_hash": "2b401f7e20fd945973a6c8b3715402d19cc2fdd91e241922660f89dce93858f5"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
          "definition_information": "Repository aspect_rules_format_npm__cross-spawn__7.0.3 instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:36:27: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/toolchains.bzl:13:21: in format_register_toolchains\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_format_npm/repositories.bzl:88:15: in npm_repositories\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:544:16: in npm_import\nRepository rule _npm_import defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:331:30: in <toplevel>\n",
          "original_attributes": {
               "name": "aspect_rules_format_npm__cross-spawn__7.0.3",
               "generator_name": "aspect_rules_format_npm__cross-spawn__7.0.3",
               "generator_function": "format_register_toolchains",
               "generator_location": None,
               "package": "cross-spawn",
               "version": "7.0.3",
               "root_package": "",
               "link_packages": {},
               "integrity": "sha512-iRDPJKUPVEND7dHPO8rkbOnPpyDygcDFtWjpeWNCgy8WP2rXcxXL8TskReQl6OrB2G7+UJrags1q15Fudc7G6w==",
               "patch_args": [
                    "-p0"
               ],
               "patches": [],
               "run_lifecycle_hooks": False,
               "custom_postinstall": "",
               "link_workspace": "aspect_rules_format",
               "url": ""
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
                    "attributes": {
                         "name": "aspect_rules_format_npm__cross-spawn__7.0.3",
                         "generator_name": "aspect_rules_format_npm__cross-spawn__7.0.3",
                         "generator_function": "format_register_toolchains",
                         "generator_location": None,
                         "package": "cross-spawn",
                         "version": "7.0.3",
                         "root_package": "",
                         "link_packages": {},
                         "integrity": "sha512-iRDPJKUPVEND7dHPO8rkbOnPpyDygcDFtWjpeWNCgy8WP2rXcxXL8TskReQl6OrB2G7+UJrags1q15Fudc7G6w==",
                         "patch_args": [
                              "-p0"
                         ],
                         "patches": [],
                         "run_lifecycle_hooks": False,
                         "custom_postinstall": "",
                         "link_workspace": "aspect_rules_format",
                         "url": ""
                    },
                    "output_tree_hash": "5d5e833b543981b0f13ef3c4172efa167a1647cb8656b2ea52ac2aff3d1b02b7"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
          "definition_information": "Repository aspect_rules_format_npm__globalyzer__0.1.0 instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:36:27: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/toolchains.bzl:13:21: in format_register_toolchains\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_format_npm/repositories.bzl:140:15: in npm_repositories\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:544:16: in npm_import\nRepository rule _npm_import defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:331:30: in <toplevel>\n",
          "original_attributes": {
               "name": "aspect_rules_format_npm__globalyzer__0.1.0",
               "generator_name": "aspect_rules_format_npm__globalyzer__0.1.0",
               "generator_function": "format_register_toolchains",
               "generator_location": None,
               "package": "globalyzer",
               "version": "0.1.0",
               "root_package": "",
               "link_packages": {},
               "integrity": "sha512-40oNTM9UfG6aBmuKxk/giHn5nQ8RVz/SS4Ir6zgzOv9/qC3kKZ9v4etGTcJbEl/NyVQH7FGU7d+X1egr57Md2Q==",
               "patch_args": [
                    "-p0"
               ],
               "patches": [],
               "run_lifecycle_hooks": False,
               "custom_postinstall": "",
               "link_workspace": "aspect_rules_format",
               "url": ""
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
                    "attributes": {
                         "name": "aspect_rules_format_npm__globalyzer__0.1.0",
                         "generator_name": "aspect_rules_format_npm__globalyzer__0.1.0",
                         "generator_function": "format_register_toolchains",
                         "generator_location": None,
                         "package": "globalyzer",
                         "version": "0.1.0",
                         "root_package": "",
                         "link_packages": {},
                         "integrity": "sha512-40oNTM9UfG6aBmuKxk/giHn5nQ8RVz/SS4Ir6zgzOv9/qC3kKZ9v4etGTcJbEl/NyVQH7FGU7d+X1egr57Md2Q==",
                         "patch_args": [
                              "-p0"
                         ],
                         "patches": [],
                         "run_lifecycle_hooks": False,
                         "custom_postinstall": "",
                         "link_workspace": "aspect_rules_format",
                         "url": ""
                    },
                    "output_tree_hash": "b0b709d65e2918a2b75fe97ed13a7be7b08ee684b78858c9ea08e2585e998800"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
          "definition_information": "Repository aspect_rules_format_npm__is-docker__2.2.1 instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:36:27: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/toolchains.bzl:13:21: in format_register_toolchains\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_format_npm/repositories.bzl:168:15: in npm_repositories\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:544:16: in npm_import\nRepository rule _npm_import defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:331:30: in <toplevel>\n",
          "original_attributes": {
               "name": "aspect_rules_format_npm__is-docker__2.2.1",
               "generator_name": "aspect_rules_format_npm__is-docker__2.2.1",
               "generator_function": "format_register_toolchains",
               "generator_location": None,
               "package": "is-docker",
               "version": "2.2.1",
               "root_package": "",
               "link_packages": {},
               "integrity": "sha512-F+i2BKsFrH66iaUFc0woD8sLy8getkwTwtOBjvs56Cx4CgJDeKQeqfz8wAYiSb8JOprWhHH5p77PbmYCvvUuXQ==",
               "patch_args": [
                    "-p0"
               ],
               "patches": [],
               "run_lifecycle_hooks": False,
               "custom_postinstall": "",
               "link_workspace": "aspect_rules_format",
               "url": ""
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
                    "attributes": {
                         "name": "aspect_rules_format_npm__is-docker__2.2.1",
                         "generator_name": "aspect_rules_format_npm__is-docker__2.2.1",
                         "generator_function": "format_register_toolchains",
                         "generator_location": None,
                         "package": "is-docker",
                         "version": "2.2.1",
                         "root_package": "",
                         "link_packages": {},
                         "integrity": "sha512-F+i2BKsFrH66iaUFc0woD8sLy8getkwTwtOBjvs56Cx4CgJDeKQeqfz8wAYiSb8JOprWhHH5p77PbmYCvvUuXQ==",
                         "patch_args": [
                              "-p0"
                         ],
                         "patches": [],
                         "run_lifecycle_hooks": False,
                         "custom_postinstall": "",
                         "link_workspace": "aspect_rules_format",
                         "url": ""
                    },
                    "output_tree_hash": "186d38061ac3a3043d703ded37db96f2de896a384065f842d8eca6cac45a4a6b"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
          "definition_information": "Repository aspect_rules_format_npm__isexe__2.0.0 instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:36:27: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/toolchains.bzl:13:21: in format_register_toolchains\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_format_npm/repositories.bzl:232:15: in npm_repositories\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:544:16: in npm_import\nRepository rule _npm_import defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:331:30: in <toplevel>\n",
          "original_attributes": {
               "name": "aspect_rules_format_npm__isexe__2.0.0",
               "generator_name": "aspect_rules_format_npm__isexe__2.0.0",
               "generator_function": "format_register_toolchains",
               "generator_location": None,
               "package": "isexe",
               "version": "2.0.0",
               "root_package": "",
               "link_packages": {},
               "integrity": "sha512-RHxMLp9lnKHGHRng9QFhRCMbYAcVpn69smSGcq3f36xjgVVWThj4qqLbTLlq7Ssj8B+fIQ1EuCEGI2lKsyQeIw==",
               "patch_args": [
                    "-p0"
               ],
               "patches": [],
               "run_lifecycle_hooks": False,
               "custom_postinstall": "",
               "link_workspace": "aspect_rules_format",
               "url": ""
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
                    "attributes": {
                         "name": "aspect_rules_format_npm__isexe__2.0.0",
                         "generator_name": "aspect_rules_format_npm__isexe__2.0.0",
                         "generator_function": "format_register_toolchains",
                         "generator_location": None,
                         "package": "isexe",
                         "version": "2.0.0",
                         "root_package": "",
                         "link_packages": {},
                         "integrity": "sha512-RHxMLp9lnKHGHRng9QFhRCMbYAcVpn69smSGcq3f36xjgVVWThj4qqLbTLlq7Ssj8B+fIQ1EuCEGI2lKsyQeIw==",
                         "patch_args": [
                              "-p0"
                         ],
                         "patches": [],
                         "run_lifecycle_hooks": False,
                         "custom_postinstall": "",
                         "link_workspace": "aspect_rules_format",
                         "url": ""
                    },
                    "output_tree_hash": "a0af737c8b532855d1d08ff942822829dd7e3f64926520248195938b3993522d"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
          "definition_information": "Repository aspect_rules_format_npm__synckit__0.8.5 instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:36:27: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/toolchains.bzl:13:21: in format_register_toolchains\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_format_npm/repositories.bzl:658:15: in npm_repositories\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:544:16: in npm_import\nRepository rule _npm_import defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:331:30: in <toplevel>\n",
          "original_attributes": {
               "name": "aspect_rules_format_npm__synckit__0.8.5",
               "generator_name": "aspect_rules_format_npm__synckit__0.8.5",
               "generator_function": "format_register_toolchains",
               "generator_location": None,
               "package": "synckit",
               "version": "0.8.5",
               "root_package": "",
               "link_packages": {},
               "integrity": "sha512-L1dapNV6vu2s/4Sputv8xGsCdAVlb5nRDMFU/E27D44l5U6cw1g0dGd45uLc+OXjNMmF4ntiMdCimzcjFKQI8Q==",
               "patch_args": [
                    "-p0"
               ],
               "patches": [],
               "run_lifecycle_hooks": False,
               "custom_postinstall": "",
               "link_workspace": "aspect_rules_format",
               "url": ""
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
                    "attributes": {
                         "name": "aspect_rules_format_npm__synckit__0.8.5",
                         "generator_name": "aspect_rules_format_npm__synckit__0.8.5",
                         "generator_function": "format_register_toolchains",
                         "generator_location": None,
                         "package": "synckit",
                         "version": "0.8.5",
                         "root_package": "",
                         "link_packages": {},
                         "integrity": "sha512-L1dapNV6vu2s/4Sputv8xGsCdAVlb5nRDMFU/E27D44l5U6cw1g0dGd45uLc+OXjNMmF4ntiMdCimzcjFKQI8Q==",
                         "patch_args": [
                              "-p0"
                         ],
                         "patches": [],
                         "run_lifecycle_hooks": False,
                         "custom_postinstall": "",
                         "link_workspace": "aspect_rules_format",
                         "url": ""
                    },
                    "output_tree_hash": "0217cbc6afe0cfd16329d82238520a8d9535f2146e62263635d2bf5819b82d60"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
          "definition_information": "Repository aspect_rules_format_npm__is-wsl__2.2.0 instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:36:27: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/toolchains.bzl:13:21: in format_register_toolchains\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_format_npm/repositories.bzl:214:15: in npm_repositories\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:544:16: in npm_import\nRepository rule _npm_import defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:331:30: in <toplevel>\n",
          "original_attributes": {
               "name": "aspect_rules_format_npm__is-wsl__2.2.0",
               "generator_name": "aspect_rules_format_npm__is-wsl__2.2.0",
               "generator_function": "format_register_toolchains",
               "generator_location": None,
               "package": "is-wsl",
               "version": "2.2.0",
               "root_package": "",
               "link_packages": {},
               "integrity": "sha512-fKzAra0rGJUUBwGBgNkHZuToZcn+TtXHpeCgmkMJMMYx1sQDYaCSyjJBSCa2nH1DGm7s3n1oBnohoVTBaN7Lww==",
               "patch_args": [
                    "-p0"
               ],
               "patches": [],
               "run_lifecycle_hooks": False,
               "custom_postinstall": "",
               "link_workspace": "aspect_rules_format",
               "url": ""
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
                    "attributes": {
                         "name": "aspect_rules_format_npm__is-wsl__2.2.0",
                         "generator_name": "aspect_rules_format_npm__is-wsl__2.2.0",
                         "generator_function": "format_register_toolchains",
                         "generator_location": None,
                         "package": "is-wsl",
                         "version": "2.2.0",
                         "root_package": "",
                         "link_packages": {},
                         "integrity": "sha512-fKzAra0rGJUUBwGBgNkHZuToZcn+TtXHpeCgmkMJMMYx1sQDYaCSyjJBSCa2nH1DGm7s3n1oBnohoVTBaN7Lww==",
                         "patch_args": [
                              "-p0"
                         ],
                         "patches": [],
                         "run_lifecycle_hooks": False,
                         "custom_postinstall": "",
                         "link_workspace": "aspect_rules_format",
                         "url": ""
                    },
                    "output_tree_hash": "f22fdabe8da99fea64bec1100e5e350a260a440b6dac9ac1570e870eaf773fd3"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
          "definition_information": "Repository aspect_rules_format_npm__path-key__3.1.1 instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:36:27: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/toolchains.bzl:13:21: in format_register_toolchains\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_format_npm/repositories.bzl:340:15: in npm_repositories\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:544:16: in npm_import\nRepository rule _npm_import defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:331:30: in <toplevel>\n",
          "original_attributes": {
               "name": "aspect_rules_format_npm__path-key__3.1.1",
               "generator_name": "aspect_rules_format_npm__path-key__3.1.1",
               "generator_function": "format_register_toolchains",
               "generator_location": None,
               "package": "path-key",
               "version": "3.1.1",
               "root_package": "",
               "link_packages": {},
               "integrity": "sha512-ojmeN0qd+y0jszEtoY48r0Peq5dwMEkIlCOu6Q5f41lfkswXuKtYrhgoTpLnyIcHm24Uhqx+5Tqm2InSwLhE6Q==",
               "patch_args": [
                    "-p0"
               ],
               "patches": [],
               "run_lifecycle_hooks": False,
               "custom_postinstall": "",
               "link_workspace": "aspect_rules_format",
               "url": ""
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
                    "attributes": {
                         "name": "aspect_rules_format_npm__path-key__3.1.1",
                         "generator_name": "aspect_rules_format_npm__path-key__3.1.1",
                         "generator_function": "format_register_toolchains",
                         "generator_location": None,
                         "package": "path-key",
                         "version": "3.1.1",
                         "root_package": "",
                         "link_packages": {},
                         "integrity": "sha512-ojmeN0qd+y0jszEtoY48r0Peq5dwMEkIlCOu6Q5f41lfkswXuKtYrhgoTpLnyIcHm24Uhqx+5Tqm2InSwLhE6Q==",
                         "patch_args": [
                              "-p0"
                         ],
                         "patches": [],
                         "run_lifecycle_hooks": False,
                         "custom_postinstall": "",
                         "link_workspace": "aspect_rules_format",
                         "url": ""
                    },
                    "output_tree_hash": "89b0c5255aba4158c250ba1fe068200e9ab345a6e15b0d0b01a3c75cc53ada51"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
          "definition_information": "Repository aspect_rules_format_npm__globrex__0.1.2 instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:36:27: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/toolchains.bzl:13:21: in format_register_toolchains\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_format_npm/repositories.bzl:154:15: in npm_repositories\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:544:16: in npm_import\nRepository rule _npm_import defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:331:30: in <toplevel>\n",
          "original_attributes": {
               "name": "aspect_rules_format_npm__globrex__0.1.2",
               "generator_name": "aspect_rules_format_npm__globrex__0.1.2",
               "generator_function": "format_register_toolchains",
               "generator_location": None,
               "package": "globrex",
               "version": "0.1.2",
               "root_package": "",
               "link_packages": {},
               "integrity": "sha512-uHJgbwAMwNFf5mLst7IWLNg14x1CkeqglJb/K3doi4dw6q2IvAAmM/Y81kevy83wP+Sst+nutFTYOGg3d1lsxg==",
               "patch_args": [
                    "-p0"
               ],
               "patches": [],
               "run_lifecycle_hooks": False,
               "custom_postinstall": "",
               "link_workspace": "aspect_rules_format",
               "url": ""
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
                    "attributes": {
                         "name": "aspect_rules_format_npm__globrex__0.1.2",
                         "generator_name": "aspect_rules_format_npm__globrex__0.1.2",
                         "generator_function": "format_register_toolchains",
                         "generator_location": None,
                         "package": "globrex",
                         "version": "0.1.2",
                         "root_package": "",
                         "link_packages": {},
                         "integrity": "sha512-uHJgbwAMwNFf5mLst7IWLNg14x1CkeqglJb/K3doi4dw6q2IvAAmM/Y81kevy83wP+Sst+nutFTYOGg3d1lsxg==",
                         "patch_args": [
                              "-p0"
                         ],
                         "patches": [],
                         "run_lifecycle_hooks": False,
                         "custom_postinstall": "",
                         "link_workspace": "aspect_rules_format",
                         "url": ""
                    },
                    "output_tree_hash": "9a6a461c0b1d776aa8018f77da5fa8d91e130ce4f5137129e08408e4acd79460"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
          "definition_information": "Repository aspect_rules_format_npm__which__2.0.2 instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:36:27: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/toolchains.bzl:13:21: in format_register_toolchains\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_format_npm/repositories.bzl:728:15: in npm_repositories\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:544:16: in npm_import\nRepository rule _npm_import defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:331:30: in <toplevel>\n",
          "original_attributes": {
               "name": "aspect_rules_format_npm__which__2.0.2",
               "generator_name": "aspect_rules_format_npm__which__2.0.2",
               "generator_function": "format_register_toolchains",
               "generator_location": None,
               "package": "which",
               "version": "2.0.2",
               "root_package": "",
               "link_packages": {},
               "integrity": "sha512-BLI3Tl1TW3Pvl70l3yq3Y64i+awpwXqsGBYWkkqMtnbXgrMD+yj7rhW0kuEDxzJaYXGjEW5ogapKNMEKNMjibA==",
               "patch_args": [
                    "-p0"
               ],
               "patches": [],
               "run_lifecycle_hooks": False,
               "custom_postinstall": "",
               "link_workspace": "aspect_rules_format",
               "url": ""
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
                    "attributes": {
                         "name": "aspect_rules_format_npm__which__2.0.2",
                         "generator_name": "aspect_rules_format_npm__which__2.0.2",
                         "generator_function": "format_register_toolchains",
                         "generator_location": None,
                         "package": "which",
                         "version": "2.0.2",
                         "root_package": "",
                         "link_packages": {},
                         "integrity": "sha512-BLI3Tl1TW3Pvl70l3yq3Y64i+awpwXqsGBYWkkqMtnbXgrMD+yj7rhW0kuEDxzJaYXGjEW5ogapKNMEKNMjibA==",
                         "patch_args": [
                              "-p0"
                         ],
                         "patches": [],
                         "run_lifecycle_hooks": False,
                         "custom_postinstall": "",
                         "link_workspace": "aspect_rules_format",
                         "url": ""
                    },
                    "output_tree_hash": "1b9a32f039a0591061bea226cdc126c2e9cdd0aae5ed508a93492401a1bf5cbe"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
          "definition_information": "Repository aspect_rules_format_npm__shebang-command__2.0.0 instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:36:27: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/toolchains.bzl:13:21: in format_register_toolchains\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_format_npm/repositories.bzl:600:15: in npm_repositories\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:544:16: in npm_import\nRepository rule _npm_import defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:331:30: in <toplevel>\n",
          "original_attributes": {
               "name": "aspect_rules_format_npm__shebang-command__2.0.0",
               "generator_name": "aspect_rules_format_npm__shebang-command__2.0.0",
               "generator_function": "format_register_toolchains",
               "generator_location": None,
               "package": "shebang-command",
               "version": "2.0.0",
               "root_package": "",
               "link_packages": {},
               "integrity": "sha512-kHxr2zZpYtdmrN1qDjrrX/Z1rR1kG8Dx+gkpK1G4eXmvXswmcE1hTWBWYUzlraYw1/yZp6YuDY77YtvbN0dmDA==",
               "patch_args": [
                    "-p0"
               ],
               "patches": [],
               "run_lifecycle_hooks": False,
               "custom_postinstall": "",
               "link_workspace": "aspect_rules_format",
               "url": ""
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
                    "attributes": {
                         "name": "aspect_rules_format_npm__shebang-command__2.0.0",
                         "generator_name": "aspect_rules_format_npm__shebang-command__2.0.0",
                         "generator_function": "format_register_toolchains",
                         "generator_location": None,
                         "package": "shebang-command",
                         "version": "2.0.0",
                         "root_package": "",
                         "link_packages": {},
                         "integrity": "sha512-kHxr2zZpYtdmrN1qDjrrX/Z1rR1kG8Dx+gkpK1G4eXmvXswmcE1hTWBWYUzlraYw1/yZp6YuDY77YtvbN0dmDA==",
                         "patch_args": [
                              "-p0"
                         ],
                         "patches": [],
                         "run_lifecycle_hooks": False,
                         "custom_postinstall": "",
                         "link_workspace": "aspect_rules_format",
                         "url": ""
                    },
                    "output_tree_hash": "c757b35964a134ac207a5d09a31c2bfa68c173f1d081409a4675d82eb7b932c5"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
          "definition_information": "Repository aspect_rules_format_npm__define-lazy-prop__2.0.0 instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:36:27: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/toolchains.bzl:13:21: in format_register_toolchains\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_format_npm/repositories.bzl:112:15: in npm_repositories\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:544:16: in npm_import\nRepository rule _npm_import defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:331:30: in <toplevel>\n",
          "original_attributes": {
               "name": "aspect_rules_format_npm__define-lazy-prop__2.0.0",
               "generator_name": "aspect_rules_format_npm__define-lazy-prop__2.0.0",
               "generator_function": "format_register_toolchains",
               "generator_location": None,
               "package": "define-lazy-prop",
               "version": "2.0.0",
               "root_package": "",
               "link_packages": {},
               "integrity": "sha512-Ds09qNh8yw3khSjiJjiUInaGX9xlqZDY7JVryGxdxV7NPeuqQfplOpQ66yJFZut3jLa5zOwkXw1g9EI2uKh4Og==",
               "patch_args": [
                    "-p0"
               ],
               "patches": [],
               "run_lifecycle_hooks": False,
               "custom_postinstall": "",
               "link_workspace": "aspect_rules_format",
               "url": ""
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
                    "attributes": {
                         "name": "aspect_rules_format_npm__define-lazy-prop__2.0.0",
                         "generator_name": "aspect_rules_format_npm__define-lazy-prop__2.0.0",
                         "generator_function": "format_register_toolchains",
                         "generator_location": None,
                         "package": "define-lazy-prop",
                         "version": "2.0.0",
                         "root_package": "",
                         "link_packages": {},
                         "integrity": "sha512-Ds09qNh8yw3khSjiJjiUInaGX9xlqZDY7JVryGxdxV7NPeuqQfplOpQ66yJFZut3jLa5zOwkXw1g9EI2uKh4Og==",
                         "patch_args": [
                              "-p0"
                         ],
                         "patches": [],
                         "run_lifecycle_hooks": False,
                         "custom_postinstall": "",
                         "link_workspace": "aspect_rules_format",
                         "url": ""
                    },
                    "output_tree_hash": "055f95f9c81e421e740e4932d0a7ec8a6b5e305a32f630d5d4e1c7d92b6ecf1c"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
          "definition_information": "Repository aspect_rules_format_npm__picocolors__1.0.0 instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:36:27: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/toolchains.bzl:13:21: in format_register_toolchains\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_format_npm/repositories.bzl:354:15: in npm_repositories\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:544:16: in npm_import\nRepository rule _npm_import defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:331:30: in <toplevel>\n",
          "original_attributes": {
               "name": "aspect_rules_format_npm__picocolors__1.0.0",
               "generator_name": "aspect_rules_format_npm__picocolors__1.0.0",
               "generator_function": "format_register_toolchains",
               "generator_location": None,
               "package": "picocolors",
               "version": "1.0.0",
               "root_package": "",
               "link_packages": {},
               "integrity": "sha512-1fygroTLlHu66zi26VoTDv8yRgm0Fccecssto+MhsZ0D/DGW2sm8E8AjW7NU5VVTRt5GxbeZ5qBuJr+HyLYkjQ==",
               "patch_args": [
                    "-p0"
               ],
               "patches": [],
               "run_lifecycle_hooks": False,
               "custom_postinstall": "",
               "link_workspace": "aspect_rules_format",
               "url": ""
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
                    "attributes": {
                         "name": "aspect_rules_format_npm__picocolors__1.0.0",
                         "generator_name": "aspect_rules_format_npm__picocolors__1.0.0",
                         "generator_function": "format_register_toolchains",
                         "generator_location": None,
                         "package": "picocolors",
                         "version": "1.0.0",
                         "root_package": "",
                         "link_packages": {},
                         "integrity": "sha512-1fygroTLlHu66zi26VoTDv8yRgm0Fccecssto+MhsZ0D/DGW2sm8E8AjW7NU5VVTRt5GxbeZ5qBuJr+HyLYkjQ==",
                         "patch_args": [
                              "-p0"
                         ],
                         "patches": [],
                         "run_lifecycle_hooks": False,
                         "custom_postinstall": "",
                         "link_workspace": "aspect_rules_format",
                         "url": ""
                    },
                    "output_tree_hash": "7995bed5b84cb653f0045da90711c98bebdd9d76bf7d036b2081a80aa468764f"
               }
          ]
     },
     {
          "original_rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
          "definition_information": "Repository aspect_rules_format_npm__node-sql-parser__4.6.6 instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:36:27: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/toolchains.bzl:13:21: in format_register_toolchains\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_format_npm/repositories.bzl:300:15: in npm_repositories\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:544:16: in npm_import\nRepository rule _npm_import defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/aspect_rules_js/npm/npm_import.bzl:331:30: in <toplevel>\n",
          "original_attributes": {
               "name": "aspect_rules_format_npm__node-sql-parser__4.6.6",
               "generator_name": "aspect_rules_format_npm__node-sql-parser__4.6.6",
               "generator_function": "format_register_toolchains",
               "generator_location": None,
               "package": "node-sql-parser",
               "version": "4.6.6",
               "root_package": "",
               "link_packages": {},
               "integrity": "sha512-zpash5xnRY6+0C9HFru32iRJV1LTkwtrVpO90i385tYVF6efyXK/B3Nsq/15Fuv2utxrqHNjKtL55OHb8sl+eQ==",
               "patch_args": [
                    "-p0"
               ],
               "patches": [],
               "run_lifecycle_hooks": False,
               "custom_postinstall": "",
               "link_workspace": "aspect_rules_format",
               "url": ""
          },
          "repositories": [
               {
                    "rule_class": "@aspect_rules_js//npm:npm_import.bzl%_npm_import",
                    "attributes": {
                         "name": "aspect_rules_format_npm__node-sql-parser__4.6.6",
                         "generator_name": "aspect_rules_format_npm__node-sql-parser__4.6.6",
                         "generator_function": "format_register_toolchains",
                         "generator_location": None,
                         "package": "node-sql-parser",
                         "version": "4.6.6",
                         "root_package": "",
                         "link_packages": {},
                         "integrity": "sha512-zpash5xnRY6+0C9HFru32iRJV1LTkwtrVpO90i385tYVF6efyXK/B3Nsq/15Fuv2utxrqHNjKtL55OHb8sl+eQ==",
                         "patch_args": [
                              "-p0"
                         ],
                         "patches": [],
                         "run_lifecycle_hooks": False,
                         "custom_postinstall": "",
                         "link_workspace": "aspect_rules_format",
                         "url": ""
                    },
                    "output_tree_hash": "123b00bce5c855d7f4562ccd8ebb292c9d78a583eab2b434460785c155698df9"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository remotejdk11_linux instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:46:6: in <toplevel>\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/jdk/remote_java_repository.bzl:49:17: in remote_java_repository\nRepository rule http_archive defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk11_linux",
               "generator_name": "remotejdk11_linux",
               "generator_function": "maybe",
               "generator_location": None,
               "urls": [
                    "https://mirror.bazel.build/cdn.azul.com/zulu/bin/zulu11.56.19-ca-jdk11.0.15-linux_x64.tar.gz",
                    "https://cdn.azul.com/zulu/bin/zulu11.56.19-ca-jdk11.0.15-linux_x64.tar.gz"
               ],
               "sha256": "e064b61d93304012351242bf0823c6a2e41d9e28add7ea7f05378b7243d34247",
               "strip_prefix": "zulu11.56.19-ca-jdk11.0.15-linux_x64",
               "build_file_content": "load(\"@rules_java//java:defs.bzl\", \"java_import\", \"java_runtime\")\n\npackage(default_visibility = [\"//visibility:public\"])\n\nexports_files([\"BUILD.bazel\"])\n\nDEPRECATION_MESSAGE = (\"Don't depend on targets in the JDK workspace;\" +\n                       \" use @bazel_tools//tools/jdk:current_java_runtime instead\" +\n                       \" (see https://github.com/bazelbuild/bazel/issues/5594)\")\n\nfilegroup(\n    name = \"jni_header\",\n    srcs = [\"include/jni.h\"],\n    deprecation = DEPRECATION_MESSAGE,\n)\n\nfilegroup(\n    name = \"jni_md_header-darwin\",\n    srcs = [\"include/darwin/jni_md.h\"],\n    deprecation = DEPRECATION_MESSAGE,\n)\n\nfilegroup(\n    name = \"jni_md_header-linux\",\n    srcs = [\"include/linux/jni_md.h\"],\n    deprecation = DEPRECATION_MESSAGE,\n)\n\nfilegroup(\n    name = \"jni_md_header-freebsd\",\n    srcs = [\"include/freebsd/jni_md.h\"],\n    deprecation = DEPRECATION_MESSAGE,\n)\n\nfilegroup(\n    name = \"jni_md_header-openbsd\",\n    srcs = [\"include/openbsd/jni_md.h\"],\n    deprecation = DEPRECATION_MESSAGE,\n)\n\nfilegroup(\n    name = \"jni_md_header-windows\",\n    srcs = [\"include/win32/jni_md.h\"],\n    deprecation = DEPRECATION_MESSAGE,\n)\n\nfilegroup(\n    name = \"java\",\n    srcs = select({\n        \":windows\": [\"bin/java.exe\"],\n        \"//conditions:default\": [\"bin/java\"],\n    }),\n    data = [\":jdk\"],\n    deprecation = DEPRECATION_MESSAGE,\n)\n\nfilegroup(\n    name = \"jar\",\n    srcs = select({\n        \":windows\": [\"bin/jar.exe\"],\n        \"//conditions:default\": [\"bin/jar\"],\n    }),\n    data = [\":jdk\"],\n    deprecation = DEPRECATION_MESSAGE,\n)\n\nfilegroup(\n    name = \"javac\",\n    srcs = select({\n        \":windows\": [\"bin/javac.exe\"],\n        \"//conditions:default\": [\"bin/javac\"],\n    }),\n    data = [\":jdk\"],\n    deprecation = DEPRECATION_MESSAGE,\n)\n\nfilegroup(\n    name = \"javadoc\",\n    srcs = select({\n        \":windows\": [\"bin/javadoc.exe\"],\n        \"//conditions:default\": [\"bin/javadoc\"],\n    }),\n    data = [\":jdk\"],\n    deprecation = DEPRECATION_MESSAGE,\n)\n\nfilegroup(\n    name = \"xjc\",\n    srcs = [\"bin/xjc\"],\n    deprecation = DEPRECATION_MESSAGE,\n)\n\nfilegroup(\n    name = \"wsimport\",\n    srcs = [\"bin/wsimport\"],\n    deprecation = DEPRECATION_MESSAGE,\n)\n\nBOOTCLASS_JARS = [\n    \"rt.jar\",\n    \"resources.jar\",\n    \"jsse.jar\",\n    \"jce.jar\",\n    \"charsets.jar\",\n]\n\n# TODO(cushon): this isn't compatible with JDK 9\nfilegroup(\n    name = \"bootclasspath\",\n    srcs = [\"jre/lib/%s\" % jar for jar in BOOTCLASS_JARS],\n    deprecation = DEPRECATION_MESSAGE,\n)\n\nfilegroup(\n    name = \"jre-bin\",\n    srcs = select({\n        # In some configurations, Java browser plugin is considered harmful and\n        # common antivirus software blocks access to npjp2.dll interfering with Bazel,\n        # so do not include it in JRE on Windows.\n        \":windows\": glob(\n            [\"jre/bin/**\"],\n            allow_empty = True,\n            exclude = [\"jre/bin/plugin2/**\"],\n        ),\n        \"//conditions:default\": glob(\n            [\"jre/bin/**\"],\n            allow_empty = True,\n        ),\n    }),\n    deprecation = DEPRECATION_MESSAGE,\n)\n\nfilegroup(\n    name = \"jre-lib\",\n    srcs = glob(\n        [\"jre/lib/**\"],\n        allow_empty = True,\n    ),\n)\n\nfilegroup(\n    name = \"jre\",\n    srcs = [\":jre-default\"],\n)\n\nfilegroup(\n    name = \"jre-default\",\n    srcs = [\n        \":jre-bin\",\n        \":jre-lib\",\n    ],\n    deprecation = DEPRECATION_MESSAGE,\n)\n\nfilegroup(\n    name = \"jdk-bin\",\n    srcs = glob(\n        [\"bin/**\"],\n        # The JDK on Windows sometimes contains a directory called\n        # \"%systemroot%\", which is not a valid label.\n        exclude = [\"**/*%*/**\"],\n    ),\n)\n\n#This folder holds security policies\nfilegroup(\n    name = \"jdk-conf\",\n    srcs = glob(\n        [\"conf/**\"],\n        allow_empty = True,\n    ),\n)\n\nfilegroup(\n    name = \"jdk-include\",\n    srcs = glob(\n        [\"include/**\"],\n        allow_empty = True,\n    ),\n)\n\nfilegroup(\n    name = \"jdk-lib\",\n    srcs = glob(\n        [\"lib/**\"],\n        allow_empty = True,\n        exclude = [\n            \"lib/missioncontrol/**\",\n            \"lib/visualvm/**\",\n        ],\n    ),\n)\n\njava_runtime(\n    name = \"jdk\",\n    srcs = [\n        \":jdk-bin\",\n        \":jdk-conf\",\n        \":jdk-include\",\n        \":jdk-lib\",\n        \":jre-default\",\n    ],\n    version = 11,\n)\n\nconfig_setting(\n    name = \"windows\",\n    constraint_values = [\"@platforms//os:windows\"],\n    visibility = [\"//visibility:private\"],\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://mirror.bazel.build/cdn.azul.com/zulu/bin/zulu11.56.19-ca-jdk11.0.15-linux_x64.tar.gz",
                              "https://cdn.azul.com/zulu/bin/zulu11.56.19-ca-jdk11.0.15-linux_x64.tar.gz"
                         ],
                         "sha256": "e064b61d93304012351242bf0823c6a2e41d9e28add7ea7f05378b7243d34247",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "zulu11.56.19-ca-jdk11.0.15-linux_x64",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "load(\"@rules_java//java:defs.bzl\", \"java_import\", \"java_runtime\")\n\npackage(default_visibility = [\"//visibility:public\"])\n\nexports_files([\"BUILD.bazel\"])\n\nDEPRECATION_MESSAGE = (\"Don't depend on targets in the JDK workspace;\" +\n                       \" use @bazel_tools//tools/jdk:current_java_runtime instead\" +\n                       \" (see https://github.com/bazelbuild/bazel/issues/5594)\")\n\nfilegroup(\n    name = \"jni_header\",\n    srcs = [\"include/jni.h\"],\n    deprecation = DEPRECATION_MESSAGE,\n)\n\nfilegroup(\n    name = \"jni_md_header-darwin\",\n    srcs = [\"include/darwin/jni_md.h\"],\n    deprecation = DEPRECATION_MESSAGE,\n)\n\nfilegroup(\n    name = \"jni_md_header-linux\",\n    srcs = [\"include/linux/jni_md.h\"],\n    deprecation = DEPRECATION_MESSAGE,\n)\n\nfilegroup(\n    name = \"jni_md_header-freebsd\",\n    srcs = [\"include/freebsd/jni_md.h\"],\n    deprecation = DEPRECATION_MESSAGE,\n)\n\nfilegroup(\n    name = \"jni_md_header-openbsd\",\n    srcs = [\"include/openbsd/jni_md.h\"],\n    deprecation = DEPRECATION_MESSAGE,\n)\n\nfilegroup(\n    name = \"jni_md_header-windows\",\n    srcs = [\"include/win32/jni_md.h\"],\n    deprecation = DEPRECATION_MESSAGE,\n)\n\nfilegroup(\n    name = \"java\",\n    srcs = select({\n        \":windows\": [\"bin/java.exe\"],\n        \"//conditions:default\": [\"bin/java\"],\n    }),\n    data = [\":jdk\"],\n    deprecation = DEPRECATION_MESSAGE,\n)\n\nfilegroup(\n    name = \"jar\",\n    srcs = select({\n        \":windows\": [\"bin/jar.exe\"],\n        \"//conditions:default\": [\"bin/jar\"],\n    }),\n    data = [\":jdk\"],\n    deprecation = DEPRECATION_MESSAGE,\n)\n\nfilegroup(\n    name = \"javac\",\n    srcs = select({\n        \":windows\": [\"bin/javac.exe\"],\n        \"//conditions:default\": [\"bin/javac\"],\n    }),\n    data = [\":jdk\"],\n    deprecation = DEPRECATION_MESSAGE,\n)\n\nfilegroup(\n    name = \"javadoc\",\n    srcs = select({\n        \":windows\": [\"bin/javadoc.exe\"],\n        \"//conditions:default\": [\"bin/javadoc\"],\n    }),\n    data = [\":jdk\"],\n    deprecation = DEPRECATION_MESSAGE,\n)\n\nfilegroup(\n    name = \"xjc\",\n    srcs = [\"bin/xjc\"],\n    deprecation = DEPRECATION_MESSAGE,\n)\n\nfilegroup(\n    name = \"wsimport\",\n    srcs = [\"bin/wsimport\"],\n    deprecation = DEPRECATION_MESSAGE,\n)\n\nBOOTCLASS_JARS = [\n    \"rt.jar\",\n    \"resources.jar\",\n    \"jsse.jar\",\n    \"jce.jar\",\n    \"charsets.jar\",\n]\n\n# TODO(cushon): this isn't compatible with JDK 9\nfilegroup(\n    name = \"bootclasspath\",\n    srcs = [\"jre/lib/%s\" % jar for jar in BOOTCLASS_JARS],\n    deprecation = DEPRECATION_MESSAGE,\n)\n\nfilegroup(\n    name = \"jre-bin\",\n    srcs = select({\n        # In some configurations, Java browser plugin is considered harmful and\n        # common antivirus software blocks access to npjp2.dll interfering with Bazel,\n        # so do not include it in JRE on Windows.\n        \":windows\": glob(\n            [\"jre/bin/**\"],\n            allow_empty = True,\n            exclude = [\"jre/bin/plugin2/**\"],\n        ),\n        \"//conditions:default\": glob(\n            [\"jre/bin/**\"],\n            allow_empty = True,\n        ),\n    }),\n    deprecation = DEPRECATION_MESSAGE,\n)\n\nfilegroup(\n    name = \"jre-lib\",\n    srcs = glob(\n        [\"jre/lib/**\"],\n        allow_empty = True,\n    ),\n)\n\nfilegroup(\n    name = \"jre\",\n    srcs = [\":jre-default\"],\n)\n\nfilegroup(\n    name = \"jre-default\",\n    srcs = [\n        \":jre-bin\",\n        \":jre-lib\",\n    ],\n    deprecation = DEPRECATION_MESSAGE,\n)\n\nfilegroup(\n    name = \"jdk-bin\",\n    srcs = glob(\n        [\"bin/**\"],\n        # The JDK on Windows sometimes contains a directory called\n        # \"%systemroot%\", which is not a valid label.\n        exclude = [\"**/*%*/**\"],\n    ),\n)\n\n#This folder holds security policies\nfilegroup(\n    name = \"jdk-conf\",\n    srcs = glob(\n        [\"conf/**\"],\n        allow_empty = True,\n    ),\n)\n\nfilegroup(\n    name = \"jdk-include\",\n    srcs = glob(\n        [\"include/**\"],\n        allow_empty = True,\n    ),\n)\n\nfilegroup(\n    name = \"jdk-lib\",\n    srcs = glob(\n        [\"lib/**\"],\n        allow_empty = True,\n        exclude = [\n            \"lib/missioncontrol/**\",\n            \"lib/visualvm/**\",\n        ],\n    ),\n)\n\njava_runtime(\n    name = \"jdk\",\n    srcs = [\n        \":jdk-bin\",\n        \":jdk-conf\",\n        \":jdk-include\",\n        \":jdk-lib\",\n        \":jre-default\",\n    ],\n    version = 11,\n)\n\nconfig_setting(\n    name = \"windows\",\n    constraint_values = [\"@platforms//os:windows\"],\n    visibility = [\"//visibility:private\"],\n)\n",
                         "workspace_file_content": "",
                         "name": "remotejdk11_linux"
                    },
                    "output_tree_hash": "089393550c7741e76a520e84fad53f254f5f3c896288452516baa7b0686d9dc8"
               }
          ]
     },
     {
          "original_rule_class": "@rules_python//python/pip_install:pip_repository.bzl%whl_library",
          "definition_information": "Repository aspect_rules_format_pypi_black instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:49:14: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/requirements.bzl:50:20: in install_deps\nRepository rule whl_library defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/rules_python/python/pip_install/pip_repository.bzl:727:30: in <toplevel>\n",
          "original_attributes": {
               "name": "aspect_rules_format_pypi_black",
               "generator_name": "aspect_rules_format_pypi_black",
               "generator_function": "install_deps",
               "generator_location": None,
               "repo": "aspect_rules_format_pypi",
               "requirement": "black==22.6.0     --hash=sha256:074458dc2f6e0d3dab7928d4417bb6957bb834434516f21514138437accdbe90     --hash=sha256:187d96c5e713f441a5829e77120c269b6514418f4513a390b0499b0987f2ff1c     --hash=sha256:2ea29072e954a4d55a2ff58971b83365eba5d3d357352a07a7a4df0d95f51c78     --hash=sha256:4af5bc0e1f96be5ae9bd7aaec219c901a94d6caa2484c21983d043371c733fc4     --hash=sha256:560558527e52ce8afba936fcce93a7411ab40c7d5fe8c2463e279e843c0328ee     --hash=sha256:568ac3c465b1c8b34b61cd7a4e349e93f91abf0f9371eda1cf87194663ab684e     --hash=sha256:6797f58943fceb1c461fb572edbe828d811e719c24e03375fd25170ada53825e     --hash=sha256:6c1734ab264b8f7929cef8ae5f900b85d579e6cbfde09d7387da8f04771b51c6     --hash=sha256:6c6d39e28aed379aec40da1c65434c77d75e65bb59a1e1c283de545fb4e7c6c9     --hash=sha256:7ba9be198ecca5031cd78745780d65a3f75a34b2ff9be5837045dce55db83d1c     --hash=sha256:94783f636bca89f11eb5d50437e8e17fbc6a929a628d82304c80fa9cd945f256     --hash=sha256:a218d7e5856f91d20f04e931b6f16d15356db1c846ee55f01bac297a705ca24f     --hash=sha256:a3db5b6409b96d9bd543323b23ef32a1a2b06416d525d27e0f67e74f1446c8f2     --hash=sha256:ac609cf8ef5e7115ddd07d85d988d074ed00e10fbc3445aee393e70164a2219c     --hash=sha256:b154e6bbde1e79ea3260c4b40c0b7b3109ffcdf7bc4ebf8859169a6af72cd70b     --hash=sha256:b270a168d69edb8b7ed32c193ef10fd27844e5c60852039599f9184460ce0807     --hash=sha256:b9fd45787ba8aa3f5e0a0a98920c1012c884622c6c920dbe98dbd05bc7c70fbf     --hash=sha256:c85928b9d5f83b23cee7d0efcb310172412fbf7cb9d9ce963bd67fd141781def     --hash=sha256:c9a3ac16efe9ec7d7381ddebcc022119794872abce99475345c5a61aa18c45ad     --hash=sha256:cfaf3895a9634e882bf9d2363fed5af8888802d670f58b279b0bece00e9a872d     --hash=sha256:e439798f819d49ba1c0bd9664427a05aab79bfba777a6db94fd4e56fae0cb849     --hash=sha256:f586c26118bc6e714ec58c09df0157fe2d9ee195c764f630eb0d8e7ccce72e69     --hash=sha256:f6fe02afde060bbeef044af7996f335fbe90b039ccf3f5eb8f16df8b20f77666",
               "download_only": False,
               "enable_implicit_namespace_pkgs": False,
               "environment": {},
               "extra_pip_args": [],
               "isolated": True,
               "pip_data_exclude": [],
               "python_interpreter": "python3",
               "python_interpreter_target": "@python3_x86_64-unknown-linux-gnu//:bin/python3",
               "quiet": True,
               "repo_prefix": "aspect_rules_format_pypi_",
               "timeout": 600
          },
          "repositories": [
               {
                    "rule_class": "@rules_python//python/pip_install:pip_repository.bzl%whl_library",
                    "attributes": {
                         "name": "aspect_rules_format_pypi_black",
                         "generator_name": "aspect_rules_format_pypi_black",
                         "generator_function": "install_deps",
                         "generator_location": None,
                         "repo": "aspect_rules_format_pypi",
                         "requirement": "black==22.6.0     --hash=sha256:074458dc2f6e0d3dab7928d4417bb6957bb834434516f21514138437accdbe90     --hash=sha256:187d96c5e713f441a5829e77120c269b6514418f4513a390b0499b0987f2ff1c     --hash=sha256:2ea29072e954a4d55a2ff58971b83365eba5d3d357352a07a7a4df0d95f51c78     --hash=sha256:4af5bc0e1f96be5ae9bd7aaec219c901a94d6caa2484c21983d043371c733fc4     --hash=sha256:560558527e52ce8afba936fcce93a7411ab40c7d5fe8c2463e279e843c0328ee     --hash=sha256:568ac3c465b1c8b34b61cd7a4e349e93f91abf0f9371eda1cf87194663ab684e     --hash=sha256:6797f58943fceb1c461fb572edbe828d811e719c24e03375fd25170ada53825e     --hash=sha256:6c1734ab264b8f7929cef8ae5f900b85d579e6cbfde09d7387da8f04771b51c6     --hash=sha256:6c6d39e28aed379aec40da1c65434c77d75e65bb59a1e1c283de545fb4e7c6c9     --hash=sha256:7ba9be198ecca5031cd78745780d65a3f75a34b2ff9be5837045dce55db83d1c     --hash=sha256:94783f636bca89f11eb5d50437e8e17fbc6a929a628d82304c80fa9cd945f256     --hash=sha256:a218d7e5856f91d20f04e931b6f16d15356db1c846ee55f01bac297a705ca24f     --hash=sha256:a3db5b6409b96d9bd543323b23ef32a1a2b06416d525d27e0f67e74f1446c8f2     --hash=sha256:ac609cf8ef5e7115ddd07d85d988d074ed00e10fbc3445aee393e70164a2219c     --hash=sha256:b154e6bbde1e79ea3260c4b40c0b7b3109ffcdf7bc4ebf8859169a6af72cd70b     --hash=sha256:b270a168d69edb8b7ed32c193ef10fd27844e5c60852039599f9184460ce0807     --hash=sha256:b9fd45787ba8aa3f5e0a0a98920c1012c884622c6c920dbe98dbd05bc7c70fbf     --hash=sha256:c85928b9d5f83b23cee7d0efcb310172412fbf7cb9d9ce963bd67fd141781def     --hash=sha256:c9a3ac16efe9ec7d7381ddebcc022119794872abce99475345c5a61aa18c45ad     --hash=sha256:cfaf3895a9634e882bf9d2363fed5af8888802d670f58b279b0bece00e9a872d     --hash=sha256:e439798f819d49ba1c0bd9664427a05aab79bfba777a6db94fd4e56fae0cb849     --hash=sha256:f586c26118bc6e714ec58c09df0157fe2d9ee195c764f630eb0d8e7ccce72e69     --hash=sha256:f6fe02afde060bbeef044af7996f335fbe90b039ccf3f5eb8f16df8b20f77666",
                         "download_only": False,
                         "enable_implicit_namespace_pkgs": False,
                         "environment": {},
                         "extra_pip_args": [],
                         "isolated": True,
                         "pip_data_exclude": [],
                         "python_interpreter": "python3",
                         "python_interpreter_target": "@python3_x86_64-unknown-linux-gnu//:bin/python3",
                         "quiet": True,
                         "repo_prefix": "aspect_rules_format_pypi_",
                         "timeout": 600
                    },
                    "output_tree_hash": "4824ee83b528ca11af6071ac0c572d5b32f850ce8959b770bcc948db0c8b6967"
               }
          ]
     },
     {
          "original_rule_class": "@rules_python//python/pip_install:pip_repository.bzl%whl_library",
          "definition_information": "Repository aspect_rules_format_pypi_tomli instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:49:14: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/requirements.bzl:50:20: in install_deps\nRepository rule whl_library defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/rules_python/python/pip_install/pip_repository.bzl:727:30: in <toplevel>\n",
          "original_attributes": {
               "name": "aspect_rules_format_pypi_tomli",
               "generator_name": "aspect_rules_format_pypi_tomli",
               "generator_function": "install_deps",
               "generator_location": None,
               "repo": "aspect_rules_format_pypi",
               "requirement": "tomli==2.0.1     --hash=sha256:939de3e7a6161af0c887ef91b7d41a53e7c5a1ca976325f429cb46ea9bc30ecc     --hash=sha256:de526c12914f0c550d15924c62d72abc48d6fe7364aa87328337a31007fe8a4f",
               "download_only": False,
               "enable_implicit_namespace_pkgs": False,
               "environment": {},
               "extra_pip_args": [],
               "isolated": True,
               "pip_data_exclude": [],
               "python_interpreter": "python3",
               "python_interpreter_target": "@python3_x86_64-unknown-linux-gnu//:bin/python3",
               "quiet": True,
               "repo_prefix": "aspect_rules_format_pypi_",
               "timeout": 600
          },
          "repositories": [
               {
                    "rule_class": "@rules_python//python/pip_install:pip_repository.bzl%whl_library",
                    "attributes": {
                         "name": "aspect_rules_format_pypi_tomli",
                         "generator_name": "aspect_rules_format_pypi_tomli",
                         "generator_function": "install_deps",
                         "generator_location": None,
                         "repo": "aspect_rules_format_pypi",
                         "requirement": "tomli==2.0.1     --hash=sha256:939de3e7a6161af0c887ef91b7d41a53e7c5a1ca976325f429cb46ea9bc30ecc     --hash=sha256:de526c12914f0c550d15924c62d72abc48d6fe7364aa87328337a31007fe8a4f",
                         "download_only": False,
                         "enable_implicit_namespace_pkgs": False,
                         "environment": {},
                         "extra_pip_args": [],
                         "isolated": True,
                         "pip_data_exclude": [],
                         "python_interpreter": "python3",
                         "python_interpreter_target": "@python3_x86_64-unknown-linux-gnu//:bin/python3",
                         "quiet": True,
                         "repo_prefix": "aspect_rules_format_pypi_",
                         "timeout": 600
                    },
                    "output_tree_hash": "9c265e973ac3d3b56a3074d6314797029b97ffc5c8c744486248e6b2d9904e69"
               }
          ]
     },
     {
          "original_rule_class": "@rules_python//python/pip_install:pip_repository.bzl%whl_library",
          "definition_information": "Repository aspect_rules_format_pypi_platformdirs instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:49:14: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/requirements.bzl:50:20: in install_deps\nRepository rule whl_library defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/rules_python/python/pip_install/pip_repository.bzl:727:30: in <toplevel>\n",
          "original_attributes": {
               "name": "aspect_rules_format_pypi_platformdirs",
               "generator_name": "aspect_rules_format_pypi_platformdirs",
               "generator_function": "install_deps",
               "generator_location": None,
               "repo": "aspect_rules_format_pypi",
               "requirement": "platformdirs==2.5.2     --hash=sha256:027d8e83a2d7de06bbac4e5ef7e023c02b863d7ea5d079477e722bb41ab25788     --hash=sha256:58c8abb07dcb441e6ee4b11d8df0ac856038f944ab98b7be6b27b2a3c7feef19",
               "download_only": False,
               "enable_implicit_namespace_pkgs": False,
               "environment": {},
               "extra_pip_args": [],
               "isolated": True,
               "pip_data_exclude": [],
               "python_interpreter": "python3",
               "python_interpreter_target": "@python3_x86_64-unknown-linux-gnu//:bin/python3",
               "quiet": True,
               "repo_prefix": "aspect_rules_format_pypi_",
               "timeout": 600
          },
          "repositories": [
               {
                    "rule_class": "@rules_python//python/pip_install:pip_repository.bzl%whl_library",
                    "attributes": {
                         "name": "aspect_rules_format_pypi_platformdirs",
                         "generator_name": "aspect_rules_format_pypi_platformdirs",
                         "generator_function": "install_deps",
                         "generator_location": None,
                         "repo": "aspect_rules_format_pypi",
                         "requirement": "platformdirs==2.5.2     --hash=sha256:027d8e83a2d7de06bbac4e5ef7e023c02b863d7ea5d079477e722bb41ab25788     --hash=sha256:58c8abb07dcb441e6ee4b11d8df0ac856038f944ab98b7be6b27b2a3c7feef19",
                         "download_only": False,
                         "enable_implicit_namespace_pkgs": False,
                         "environment": {},
                         "extra_pip_args": [],
                         "isolated": True,
                         "pip_data_exclude": [],
                         "python_interpreter": "python3",
                         "python_interpreter_target": "@python3_x86_64-unknown-linux-gnu//:bin/python3",
                         "quiet": True,
                         "repo_prefix": "aspect_rules_format_pypi_",
                         "timeout": 600
                    },
                    "output_tree_hash": "dc0a799e14e579b4de1b1bd67c5639f473cef703e42e5201927092b031e5ffb3"
               }
          ]
     },
     {
          "original_rule_class": "@rules_python//python/pip_install:pip_repository.bzl%whl_library",
          "definition_information": "Repository aspect_rules_format_pypi_mypy_extensions instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:49:14: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/requirements.bzl:50:20: in install_deps\nRepository rule whl_library defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/rules_python/python/pip_install/pip_repository.bzl:727:30: in <toplevel>\n",
          "original_attributes": {
               "name": "aspect_rules_format_pypi_mypy_extensions",
               "generator_name": "aspect_rules_format_pypi_mypy_extensions",
               "generator_function": "install_deps",
               "generator_location": None,
               "repo": "aspect_rules_format_pypi",
               "requirement": "mypy-extensions==0.4.3     --hash=sha256:090fedd75945a69ae91ce1303b5824f428daf5a028d2f6ab8a299250a846f15d     --hash=sha256:2d82818f5bb3e369420cb3c4060a7970edba416647068eb4c5343488a6c604a8",
               "download_only": False,
               "enable_implicit_namespace_pkgs": False,
               "environment": {},
               "extra_pip_args": [],
               "isolated": True,
               "pip_data_exclude": [],
               "python_interpreter": "python3",
               "python_interpreter_target": "@python3_x86_64-unknown-linux-gnu//:bin/python3",
               "quiet": True,
               "repo_prefix": "aspect_rules_format_pypi_",
               "timeout": 600
          },
          "repositories": [
               {
                    "rule_class": "@rules_python//python/pip_install:pip_repository.bzl%whl_library",
                    "attributes": {
                         "name": "aspect_rules_format_pypi_mypy_extensions",
                         "generator_name": "aspect_rules_format_pypi_mypy_extensions",
                         "generator_function": "install_deps",
                         "generator_location": None,
                         "repo": "aspect_rules_format_pypi",
                         "requirement": "mypy-extensions==0.4.3     --hash=sha256:090fedd75945a69ae91ce1303b5824f428daf5a028d2f6ab8a299250a846f15d     --hash=sha256:2d82818f5bb3e369420cb3c4060a7970edba416647068eb4c5343488a6c604a8",
                         "download_only": False,
                         "enable_implicit_namespace_pkgs": False,
                         "environment": {},
                         "extra_pip_args": [],
                         "isolated": True,
                         "pip_data_exclude": [],
                         "python_interpreter": "python3",
                         "python_interpreter_target": "@python3_x86_64-unknown-linux-gnu//:bin/python3",
                         "quiet": True,
                         "repo_prefix": "aspect_rules_format_pypi_",
                         "timeout": 600
                    },
                    "output_tree_hash": "55c3ff314bd96f3485c6943471773026c2c2f8efb8084c376756ae8a82f4091a"
               }
          ]
     },
     {
          "original_rule_class": "@rules_python//python/pip_install:pip_repository.bzl%whl_library",
          "definition_information": "Repository aspect_rules_format_pypi_click instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:49:14: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/requirements.bzl:50:20: in install_deps\nRepository rule whl_library defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/rules_python/python/pip_install/pip_repository.bzl:727:30: in <toplevel>\n",
          "original_attributes": {
               "name": "aspect_rules_format_pypi_click",
               "generator_name": "aspect_rules_format_pypi_click",
               "generator_function": "install_deps",
               "generator_location": None,
               "repo": "aspect_rules_format_pypi",
               "requirement": "click==8.1.3     --hash=sha256:7682dc8afb30297001674575ea00d1814d808d6a36af415a82bd481d37ba7b8e     --hash=sha256:bb4d8133cb15a609f44e8213d9b391b0809795062913b383c62be0ee95b1db48",
               "download_only": False,
               "enable_implicit_namespace_pkgs": False,
               "environment": {},
               "extra_pip_args": [],
               "isolated": True,
               "pip_data_exclude": [],
               "python_interpreter": "python3",
               "python_interpreter_target": "@python3_x86_64-unknown-linux-gnu//:bin/python3",
               "quiet": True,
               "repo_prefix": "aspect_rules_format_pypi_",
               "timeout": 600
          },
          "repositories": [
               {
                    "rule_class": "@rules_python//python/pip_install:pip_repository.bzl%whl_library",
                    "attributes": {
                         "name": "aspect_rules_format_pypi_click",
                         "generator_name": "aspect_rules_format_pypi_click",
                         "generator_function": "install_deps",
                         "generator_location": None,
                         "repo": "aspect_rules_format_pypi",
                         "requirement": "click==8.1.3     --hash=sha256:7682dc8afb30297001674575ea00d1814d808d6a36af415a82bd481d37ba7b8e     --hash=sha256:bb4d8133cb15a609f44e8213d9b391b0809795062913b383c62be0ee95b1db48",
                         "download_only": False,
                         "enable_implicit_namespace_pkgs": False,
                         "environment": {},
                         "extra_pip_args": [],
                         "isolated": True,
                         "pip_data_exclude": [],
                         "python_interpreter": "python3",
                         "python_interpreter_target": "@python3_x86_64-unknown-linux-gnu//:bin/python3",
                         "quiet": True,
                         "repo_prefix": "aspect_rules_format_pypi_",
                         "timeout": 600
                    },
                    "output_tree_hash": "c120be1fd0fe7857de84d44222b0b60727afad4ce9a135eba6e314b15a5eff2f"
               }
          ]
     },
     {
          "original_rule_class": "@rules_python//python/pip_install:pip_repository.bzl%whl_library",
          "definition_information": "Repository aspect_rules_format_pypi_pathspec instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:49:14: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/requirements.bzl:50:20: in install_deps\nRepository rule whl_library defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/rules_python/python/pip_install/pip_repository.bzl:727:30: in <toplevel>\n",
          "original_attributes": {
               "name": "aspect_rules_format_pypi_pathspec",
               "generator_name": "aspect_rules_format_pypi_pathspec",
               "generator_function": "install_deps",
               "generator_location": None,
               "repo": "aspect_rules_format_pypi",
               "requirement": "pathspec==0.9.0     --hash=sha256:7d15c4ddb0b5c802d161efc417ec1a2558ea2653c2e8ad9c19098201dc1c993a     --hash=sha256:e564499435a2673d586f6b2130bb5b95f04a3ba06f81b8f895b651a3c76aabb1",
               "download_only": False,
               "enable_implicit_namespace_pkgs": False,
               "environment": {},
               "extra_pip_args": [],
               "isolated": True,
               "pip_data_exclude": [],
               "python_interpreter": "python3",
               "python_interpreter_target": "@python3_x86_64-unknown-linux-gnu//:bin/python3",
               "quiet": True,
               "repo_prefix": "aspect_rules_format_pypi_",
               "timeout": 600
          },
          "repositories": [
               {
                    "rule_class": "@rules_python//python/pip_install:pip_repository.bzl%whl_library",
                    "attributes": {
                         "name": "aspect_rules_format_pypi_pathspec",
                         "generator_name": "aspect_rules_format_pypi_pathspec",
                         "generator_function": "install_deps",
                         "generator_location": None,
                         "repo": "aspect_rules_format_pypi",
                         "requirement": "pathspec==0.9.0     --hash=sha256:7d15c4ddb0b5c802d161efc417ec1a2558ea2653c2e8ad9c19098201dc1c993a     --hash=sha256:e564499435a2673d586f6b2130bb5b95f04a3ba06f81b8f895b651a3c76aabb1",
                         "download_only": False,
                         "enable_implicit_namespace_pkgs": False,
                         "environment": {},
                         "extra_pip_args": [],
                         "isolated": True,
                         "pip_data_exclude": [],
                         "python_interpreter": "python3",
                         "python_interpreter_target": "@python3_x86_64-unknown-linux-gnu//:bin/python3",
                         "quiet": True,
                         "repo_prefix": "aspect_rules_format_pypi_",
                         "timeout": 600
                    },
                    "output_tree_hash": "ffc6bb6a4233975deb8e5842e700e821301d84e0ec095b4ce474e8428e76ef60"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_jar",
          "definition_information": "Repository ktfmt instantiated at:\n  /home/andrzej/code/bazel/bazel-super-formatter/WORKSPACE:6:26: in <toplevel>\n  /home/andrzej/code/bazel/bazel-super-formatter/format/repositories.bzl:99:13: in rules_format_dependencies\n  /home/andrzej/code/bazel/bazel-super-formatter/format/repositories.bzl:14:10: in http_jar\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\nRepository rule http_jar defined at:\n  /home/andrzej/.cache/bazel/_bazel_andrzej/e16ab79167a03e69f53e4f66b414037d/external/bazel_tools/tools/build_defs/repo/http.bzl:530:27: in <toplevel>\n",
          "original_attributes": {
               "name": "ktfmt",
               "generator_name": "ktfmt",
               "generator_function": "rules_format_dependencies",
               "generator_location": None,
               "url": "https://repo1.maven.org/maven2/com/facebook/ktfmt/0.46/ktfmt-0.46-jar-with-dependencies.jar"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_jar",
                    "attributes": {
                         "sha256": "97fc7fbd194d01a9fa45d8147c0552403003d55bac4ab89d84d7bb4d5e3f48de",
                         "integrity": "",
                         "canonical_id": "",
                         "url": "https://repo1.maven.org/maven2/com/facebook/ktfmt/0.46/ktfmt-0.46-jar-with-dependencies.jar",
                         "urls": [],
                         "netrc": "",
                         "auth_patterns": {},
                         "downloaded_file_name": "downloaded.jar",
                         "name": "ktfmt"
                    },
                    "output_tree_hash": "40b518de00c07086d428db06f94e47433cd1eac8d0af32d59e51f4baed864ef8"
               }
          ]
     }
]