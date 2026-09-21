#!/usr/bin/env python3
from __future__ import annotations

from hashlib import sha1
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "catalog.json"
EXPECTED_REPOSITORY = "GoreeCloud/branding-assets"
GIT_BLOB = re.compile(r"^[0-9a-f]{40}$")
EXPECTED_SYSTEM_CENTERS = {
    "privacy-shield": "Privacy Center",
    "wardveil-security": "Security Center",
    "everkeep": "Continuity Center",
    "glaze-ui": "Design Center",
    "goreecloud-mesh": "Mesh Center",
    "goreecloud-policy": "Policy Center",
}


def fail(message: str) -> None:
    raise ValueError(message)


def git_blob_id(raw: bytes) -> str:
    return sha1(f"blob {len(raw)}\0".encode("ascii") + raw).hexdigest()


def require_pinned_file(relative: str, expected_blob: str, label: str) -> None:
    path = ROOT / relative
    if not path.is_file() or path.is_symlink():
        fail(f"{label} is not a regular canonical file: {relative}")
    if not GIT_BLOB.fullmatch(expected_blob):
        fail(f"{label} has invalid pinned Git blob: {expected_blob!r}")
    actual = git_blob_id(path.read_bytes())
    if actual != expected_blob:
        fail(f"{label} changed without catalog approval: {relative}; expected {expected_blob}, got {actual}")


def main() -> int:
    try:
        data = json.loads(CATALOG.read_text(encoding="utf-8"))

        if data.get("schema_version") != 1:
            fail("catalog schema_version must be 1")
        if data.get("canonical_repository") != EXPECTED_REPOSITORY:
            fail("catalog canonical_repository drifted")

        policy = data.get("policy") or {}
        for key in (
            "canonical_first",
            "consumer_copies_are_derivatives",
            "new_branding_must_originate_here",
        ):
            if policy.get(key) is not True:
                fail(f"catalog policy must keep {key}=true")
        if policy.get("branding_creates_technical_authority") is not False:
            fail("branding must never create technical authority")

        platform = data.get("platform") or {}
        if platform.get("status") != "approved":
            fail("platform branding status must remain approved")
        require_pinned_file(
            str(platform.get("canonical_asset", "")),
            str(platform.get("git_blob", "")),
            "platform asset",
        )

        system_ids: set[str] = set()
        system_paths: set[str] = set()
        classified_repositories: set[str] = set()
        for system in data.get("systems", []):
            system_id = system.get("id")
            if not system_id or system_id in system_ids:
                fail(f"duplicate or missing system id: {system_id!r}")
            system_ids.add(system_id)

            expected_center = EXPECTED_SYSTEM_CENTERS.get(system_id)
            if expected_center is None:
                fail(f"unrecognized GoreeCloud platform system: {system_id}")
            if system.get("center") != expected_center:
                fail(f"system center drift for {system_id}: expected {expected_center!r}")

            status = system.get("status")
            asset = system.get("canonical_asset")
            blob = system.get("git_blob")
            if status in {"approved", "review-candidate"}:
                if not asset:
                    fail(f"approved system lacks canonical asset: {system_id}")
                if asset in system_paths:
                    fail(f"duplicate system canonical asset: {asset}")
                system_paths.add(asset)
                require_pinned_file(str(asset), str(blob or ""), f"system {system_id}")
            elif status == "text-only-pending-approved-artwork":
                if asset is not None or blob is not None:
                    fail(f"pending text-only system must not claim artwork or blob: {system_id}")
            else:
                fail(f"unsupported system branding status for {system_id}: {status!r}")

            repo = system.get("consumer_repository")
            if repo is not None:
                if not str(repo).startswith("GoreeCloud/"):
                    fail(f"invalid system consumer repository: {repo!r}")
                if repo in classified_repositories:
                    fail(f"consumer repository classified more than once: {repo}")
                classified_repositories.add(repo)

        if system_ids != set(EXPECTED_SYSTEM_CENTERS):
            fail(
                "platform-system catalog drift: expected "
                f"{sorted(EXPECTED_SYSTEM_CENTERS)}, got {sorted(system_ids)}"
            )

        product_ids: set[str] = set()
        product_paths: set[str] = set()
        for product in data.get("products", []):
            product_id = product.get("id")
            if not product_id or product_id in product_ids:
                fail(f"duplicate or missing product id: {product_id!r}")
            product_ids.add(product_id)

            asset = product.get("canonical_asset")
            expected = f"products/{product_id}/app-icon.svg"
            if asset != expected:
                fail(f"product canonical path drift for {product_id}: expected {expected!r}, got {asset!r}")
            if asset in product_paths:
                fail(f"duplicate product canonical asset: {asset}")
            product_paths.add(asset)
            require_pinned_file(str(asset), str(product.get("git_blob", "")), f"product {product_id}")

            repo = product.get("consumer_repository")
            if repo is not None:
                if not str(repo).startswith("GoreeCloud/"):
                    fail(f"invalid product consumer repository: {repo!r}")
                if repo in classified_repositories:
                    fail(f"consumer repository classified more than once: {repo}")
                classified_repositories.add(repo)

        other_repositories: set[str] = set()
        for consumer in data.get("other_consumers", []):
            repo = consumer.get("repository")
            contract = consumer.get("branding_contract")
            relationship = consumer.get("relationship")
            if not repo or not str(repo).startswith("GoreeCloud/"):
                fail(f"invalid additional consumer repository: {repo!r}")
            if repo in other_repositories or repo in classified_repositories:
                fail(f"consumer repository classified more than once: {repo}")
            other_repositories.add(repo)
            classified_repositories.add(repo)
            if contract != "BRANDING.md":
                fail(f"additional consumer must use BRANDING.md contract: {repo}")
            if not relationship:
                fail(f"additional consumer lacks relationship: {repo}")

        if not product_ids:
            fail("catalog contains no product branding records")
        if not system_ids:
            fail("catalog contains no platform-system branding records")

    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"Branding catalog validation failed: {exc}", file=sys.stderr)
        return 1

    print(
        f"Branding catalog validation passed: {len(product_ids)} products, "
        f"{len(system_ids)} platform systems, {len(other_repositories)} additional consumers, "
        "all pinned canonical blobs match."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
