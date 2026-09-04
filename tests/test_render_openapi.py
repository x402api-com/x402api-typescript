from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


def _load_renderer():
    path = Path(__file__).parents[1] / "scripts" / "render-openapi.py"
    spec = importlib.util.spec_from_file_location("render_openapi", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("could not load the SDK renderer")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


renderer = _load_renderer()


def _document() -> dict:
    return {
        "openapi": "3.1.0",
        "info": {"version": "1.3.0"},
        "paths": {
            "/v1/facilitator/supported": {
                "get": {"operationId": "facilitator_get_supported"},
            },
            "/v1/payments/{id}/receipt": {
                "get": {
                    "operationId": "payments_retrieve_receipt",
                    "x-speakeasy-group": "payments",
                    "x-speakeasy-name-override": "retrieveReceipt",
                },
            },
            "/dashboard-only": {
                "post": {
                    "operationId": "dashboard_only_mutation",
                    "x-authentication-boundary": (
                        "human-tenant-owner-recent-step-up"
                    ),
                },
            },
        },
        "components": {
            "securitySchemes": {
                "tenantApiKey": {"type": "apiKey"},
                "humanIngressHmac": {"type": "apiKey"},
            },
            "schemas": {
                "NullOnly": {"enum": [None]},
                "Amount": {"type": "string", "format": "decimal"},
                "PendingReceipt": {
                    "oneOf": [
                        {"$ref": "#/components/schemas/NullOnly"},
                        {"$ref": "#/components/schemas/Amount"},
                    ],
                },
            },
        },
    }


class RenderOpenApiTests(unittest.TestCase):
    def test_applies_the_portable_server_sdk_surface(self) -> None:
        rendered = renderer.render(_document())

        self.assertNotIn("humanIngressHmac", rendered["components"]["securitySchemes"])
        self.assertEqual(rendered["security"], [{"tenantApiKey": []}])
        self.assertEqual(
            rendered["paths"]["/v1/facilitator/supported"]["get"]["security"],
            [],
        )
        receipt = rendered["paths"]["/v1/payments/{id}/receipt"]["get"]
        self.assertEqual(receipt["security"], [{"tenantApiKey": []}])
        self.assertEqual(receipt["x-speakeasy-group"], "payments")
        self.assertEqual(receipt["x-speakeasy-name-override"], "retrieveReceipt")
        self.assertNotIn("/dashboard-only", rendered["paths"])

        schemas = rendered["components"]["schemas"]
        self.assertNotIn("NullOnly", schemas)
        self.assertEqual(schemas["Amount"], {"type": "string"})
        self.assertEqual(
            schemas["PendingReceipt"],
            {
                "nullable": True,
                "allOf": [{"$ref": "#/components/schemas/Amount"}],
            },
        )

    def test_rejects_duplicate_operation_ids(self) -> None:
        document = _document()
        document["paths"]["/duplicate"] = {
            "get": {"operationId": "payments_retrieve_receipt"},
        }

        with self.assertRaisesRegex(ValueError, "duplicate operationId"):
            renderer.render(document)

    def test_rejects_an_operation_without_an_id(self) -> None:
        document = _document()
        document["paths"]["/missing"] = {"get": {}}

        with self.assertRaisesRegex(ValueError, "missing operationId"):
            renderer.render(document)


if __name__ == "__main__":
    unittest.main()
