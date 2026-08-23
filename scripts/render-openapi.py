#!/usr/bin/env python3
"""Render the public contract with the reviewed TypeScript SDK overlay."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

HTTP_METHODS = frozenset({"delete", "get", "head", "options", "patch", "post", "put"})
SEMVER = re.compile(r"^(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)$")
OPERATION_NAMES = {
    "charges_create": ("charges", "create"),
    "charges_retrieve": ("charges", "retrieve"),
    "facilitator_get_supported": ("facilitator", "getSupported"),
    "idempotency_get_outcome": ("idempotency", "getOutcome"),
    "network_fees_create_quote": ("networkFees", "createQuote"),
    "orders_list": ("orders", "list"),
    "orders_retrieve": ("orders", "retrieve"),
    "payment_readiness_retrieve": ("paymentReadiness", "retrieve"),
    "receipt_verification_keys_retrieve": ("receiptVerificationKeys", "retrieve"),
    "payments_list": ("payments", "list"),
    "payments_retrieve": ("payments", "retrieve"),
    "payments_list_observations": ("payments", "listObservations"),
    "payments_retrieve_receipt": ("payments", "retrieveReceipt"),
    "receiving_addresses_get_control_capabilities": (
        "receivingAddresses",
        "getControlCapabilities",
    ),
    "receiving_addresses_create_control_challenge": (
        "receivingAddresses",
        "createControlChallenge",
    ),
    "receiving_addresses_list": ("receivingAddresses", "list"),
    "receiving_addresses_register": ("receivingAddresses", "register"),
    "receiving_addresses_activate": ("receivingAddresses", "activate"),
    "receiving_addresses_refresh_readiness": (
        "receivingAddresses",
        "refreshReadiness",
    ),
    "receiving_addresses_rotate": ("receivingAddresses", "rotate"),
    "resources_list": ("resources", "list"),
    "resources_create": ("resources", "create"),
    "resources_list_versions": ("resources", "listVersions"),
    "resources_create_version": ("resources", "createVersion"),
    "resources_activate_version": ("resources", "activateVersion"),
    "resources_retire_version": ("resources", "retireVersion"),
    "wallets_retrieve_balance": ("wallets", "retrieveBalance"),
}
PUBLIC_OPERATIONS = {
    "facilitator_get_supported",
    "receipt_verification_keys_retrieve",
}


def _load(path: Path) -> dict[str, Any]:
    document = json.loads(path.read_text())
    if not isinstance(document, dict):
        raise ValueError("OpenAPI document must be a JSON object")
    if document.get("openapi") != "3.0.3":
        raise ValueError("OpenAPI 3.0.3 is required")
    version = document.get("info", {}).get("version")
    if not isinstance(version, str) or not SEMVER.fullmatch(version):
        raise ValueError("info.version must be stable SemVer")
    if document.get("servers") != [
        {"url": "https://api.x402api.com", "description": "Production"}
    ]:
        raise ValueError("the SDK contract must target only the production API")
    return document


def render(document: dict[str, Any]) -> dict[str, Any]:
    components = document.get("components")
    if not isinstance(components, dict):
        raise ValueError("components object is required")
    schemes = components.get("securitySchemes")
    if not isinstance(schemes, dict) or "tenantApiKey" not in schemes:
        raise ValueError("tenantApiKey security scheme is required")
    schemes.pop("humanIngressHmac", None)

    tenant_security = [{"tenantApiKey": []}]
    document["x-speakeasy-max-method-params"] = 0
    document["security"] = tenant_security
    document["x-speakeasy-errors"] = {
        "statusCodes": ["4XX", "5XX", "default"],
    }
    document["x-speakeasy-retries"] = {
        "strategy": "backoff",
        "backoff": {
            "initialInterval": 500,
            "maxInterval": 1000,
            "maxElapsedTime": 1500,
            "exponent": 2,
        },
        "statusCodes": [408, 429, 500, 502, 503, 504],
        "retryConnectionErrors": True,
    }

    paths = document.get("paths")
    if not isinstance(paths, dict):
        raise ValueError("paths object is required")
    observed: set[str] = set()
    for path_item in paths.values():
        if not isinstance(path_item, dict):
            continue
        for method, operation in path_item.items():
            if method not in HTTP_METHODS or not isinstance(operation, dict):
                continue
            operation_id = operation.get("operationId")
            if not isinstance(operation_id, str) or operation_id not in OPERATION_NAMES:
                raise ValueError(f"unreviewed SDK operation: {operation_id!r}")
            if operation_id in observed:
                raise ValueError(f"duplicate operationId: {operation_id}")
            observed.add(operation_id)
            group, name = OPERATION_NAMES[operation_id]
            operation["x-speakeasy-group"] = group
            operation["x-speakeasy-name-override"] = name
            if operation_id == "charges_create":
                operation["x-speakeasy-usage-example"] = True
            operation["security"] = (
                [] if operation_id in PUBLIC_OPERATIONS else tenant_security
            )

    if observed != set(OPERATION_NAMES):
        raise ValueError(
            f"SDK operation set is incomplete: {set(OPERATION_NAMES) - observed}"
        )
    return document


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(render(_load(args.input)), indent=2) + "\n")


if __name__ == "__main__":
    main()
