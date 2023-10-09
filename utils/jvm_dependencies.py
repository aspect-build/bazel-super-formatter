import os
import sys
import tempfile
import requests
import hashlib
import subprocess
from dataclasses import dataclass


@dataclass
class Artifact:
    group: str
    name: str
    version: str
    url: str
    bazelized_name: str


def parse_line(line: str) -> Artifact:
    parts = line.strip().split(':')
    if len(parts) == 4:
        group, name, version, _ = parts
        group_path = group.replace('.', '/')
        jar_name = f"{name}-{version}.jar"
        url = f"https://repo1.maven.org/maven2/{group_path}/{name}/{version}/{jar_name}"
        bazelized_name = name.replace('-', '_').replace('.', '_')
        return Artifact(group, name, version, url, bazelized_name)


def download_and_compute_sha256(artifact: Artifact) -> str:
    # Create a temporary directory for the downloaded file
    temp_dir = tempfile.mkdtemp()
    file_path = os.path.join(temp_dir, artifact.name + '.jar')

    try:
        # Download the artifact
        response = requests.get(artifact.url)
        response.raise_for_status()

        # Save the downloaded file
        with open(file_path, 'wb') as file:
            file.write(response.content)

        # Compute the SHA-256 hash
        sha256_hash = hashlib.sha256()
        with open(file_path, 'rb') as file:
            while True:
                data = file.read(65536)  # Read in 64k chunks
                if not data:
                    break
                sha256_hash.update(data)

        print(f"Downloaded {artifact.name}", file=sys.stderr)

        sha256 = sha256_hash.hexdigest()
        os.remove(file_path)

        return sha256

    except requests.exceptions.RequestException as e:
        print(f"Error downloading artifact: {e}")
        return None

    finally:
        # Clean up temporary files
        if os.path.exists(file_path):
            os.remove(file_path)
        if os.path.exists(temp_dir):
            os.rmdir(temp_dir)

def resolve_and_parse(artifact_str: str) -> list[Artifact]:
    try:
        # Run the external process using coursier resolve
        command = ["coursier", "resolve", artifact_str]
        output = subprocess.check_output(command, text=True)

        # Split the output into lines and parse each line
        lines = output.strip().split('\n')
        parsed_artifacts = [parse_line(line) for line in lines if line.strip()]

        return parsed_artifacts

    except subprocess.CalledProcessError as e:
        print(f"Error running 'coursier resolve': {e}")
        return []


def to_bazel_target(artifact: Artifact) -> str:
    return f"""
    http_jar(
        name = "{artifact.bazelized_name}",
        url = "{artifact.url}",
        sha256 = "{download_and_compute_sha256(artifact)}",
    )
    """

def parse_requested_artifact(artifact_str: str) -> Artifact:
    artifact_str = artifact_str + ":default"
    return parse_line(artifact_str)

def requested_to_bazel_target(artifact: Artifact, deps: list[Artifact]) -> str:
    deps_to_bazel_targets = [f"{to_bazel_target(dep)}" for dep in deps]

    return f"""
java_binary(
    name = "{artifact.bazelized_name}",
    main_class = (FILL IN),
    runtime_deps = [{", ".join([f'"@{dep.bazelized_name}//jar"' for dep in deps])}],
)


# GENERATED DEPS FOR {artifact.group}:{artifact.name}:{artifact.version}

http_jar(
    name = "{artifact.bazelized_name}",
    url = "{artifact.url}",
    sha256 = "{download_and_compute_sha256(artifact)}",
)

{"".join(deps_to_bazel_targets)}

# END GENERATED DEPS FOR {artifact.group}:{artifact.name}:{artifact.version}
"""

def main(requested_artifact_str: str):
    requested_artifact = parse_requested_artifact(requested_artifact_str)
    deps = resolve_and_parse(requested_artifact_str)
    print(requested_to_bazel_target(requested_artifact, deps))

artifact_str = "org.scalameta:scalafmt-cli_2.13:3.7.14"
main(artifact_str)
