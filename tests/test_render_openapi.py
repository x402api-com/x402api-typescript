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


class RenderOpenApiTests(unittest.TestCase):
    def test_applies_the_reviewed_sdk_surface(self) -> None:
        paths = {
            f"/operation/{index}": {
                "get": {
                    "operationId": operation_id,
                    "security": [
                        {"tenantApiKey": []},
                        {"humanIngressHmac": []},
                    ],
                }
            }
            for index, operation_id in enumerate(renderer.OPERATION_NAMES)
        }
        document = {
            "openapi": "3.0.3",
            "info": {"version": "1.0.0"},
            "servers": [
                {
                    "url": "https://api.x402api.com",
                    "description": "Production",
                }
            ],
            "paths": paths,
            "components": {
                "securitySchemes": {
                    "tenantApiKey": {"type": "apiKey"},
                    "humanIngressHmac": {"type": "apiKey"},
                }
            },
        }

        rendered = renderer.render(document)

        self.assertNotIn("humanIngressHmac", rendered["components"]["securitySchemes"])
        self.assertEqual(rendered["security"], [{"tenantApiKey": []}])
        self.assertEqual(rendered["x-speakeasy-max-method-params"], 0)
        self.assertTrue(rendered["x-speakeasy-retries"]["retryConnectionErrors"])
        for path_item in rendered["paths"].values():
            operation = path_item["get"]
            operation_id = operation["operationId"]
            group, name = renderer.OPERATION_NAMES[operation_id]
            self.assertEqual(operation["x-speakeasy-group"], group)
            self.assertEqual(operation["x-speakeasy-name-override"], name)
            expected_security = (
                []
                if operation_id in renderer.PUBLIC_OPERATIONS
                else [{"tenantApiKey": []}]
            )
            self.assertEqual(operation["security"], expected_security)

        charges = next(
            path_item["get"]
            for path_item in rendered["paths"].values()
            if path_item["get"]["operationId"] == "charges_create"
        )
        self.assertTrue(charges["x-speakeasy-usage-example"])

    def test_rejects_an_unreviewed_operation(self) -> None:
        document = {
            "paths": {"/unexpected": {"get": {"operationId": "unexpected"}}},
            "components": {"securitySchemes": {"tenantApiKey": {}}},
        }

        with self.assertRaisesRegex(ValueError, "unreviewed SDK operation"):
            renderer.render(document)

    def test_prunes_human_step_up_operations_and_empty_paths(self) -> None:
        paths = {
            f"/operation/{index}": {"get": {"operationId": operation_id}}
            for index, operation_id in enumerate(renderer.OPERATION_NAMES)
        }
        paths["/dashboard-only"] = {
            "post": {
                "operationId": "dashboard_only_mutation",
                "x-authentication-boundary": (
                    "human-tenant-owner-recent-step-up"
                ),
            }
        }
        document = {
            "paths": paths,
            "components": {"securitySchemes": {"tenantApiKey": {}}},
        }

        rendered = renderer.render(document)

        self.assertNotIn("/dashboard-only", rendered["paths"])


if __name__ == "__main__":
    unittest.main()
