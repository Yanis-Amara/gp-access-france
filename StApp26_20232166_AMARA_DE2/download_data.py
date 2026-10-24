import hashlib
import json
from pathlib import Path

import requests


BASE_DIR = Path(__file__).resolve().parent


def file_hash(path):
    with path.open("rb") as file:
        return hashlib.file_digest(file, "sha256").hexdigest()


def fetch_resource(resource):
    target = BASE_DIR / resource["path"]
    expected_hash = resource["sha256"]

    if target.is_file():
        if file_hash(target) != expected_hash:
            raise ValueError(
                f"Existing file differs from the recorded snapshot: {target}"
            )
        print(f"Using verified cached file: {resource['path']}")
        return

    target.parent.mkdir(parents=True, exist_ok=True)
    response = requests.get(resource["url"], timeout=60)
    response.raise_for_status()

    temporary = target.with_suffix(target.suffix + ".part")
    temporary.write_bytes(response.content)

    if file_hash(temporary) != expected_hash:
        temporary.unlink()
        raise ValueError(
            f"The online resource differs from the recorded snapshot: "
            f"{resource['name']}. Use the submitted snapshot or investigate "
            f"the source update before rebuilding the analysis."
        )

    temporary.replace(target)
    print(f"Downloaded and verified: {resource['path']}")


def main():
    manifest = json.loads(
        (BASE_DIR / "data_sources.json").read_text(encoding="utf-8")
    )
    for resource in manifest["resources"]:
        fetch_resource(resource)


if __name__ == "__main__":
    main()
