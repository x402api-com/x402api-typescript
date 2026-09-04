from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).parents[1]


class GenerationWorkflowTests(unittest.TestCase):
    def test_generated_version_fields_are_not_persistently_merged(self) -> None:
        config = (ROOT / ".speakeasy" / "gen.yaml").read_text()
        self.assertIn('persistentEdits:\n    enabled: "false"', config)

    def test_preview_is_tested_and_bound_to_provenance_before_success(self) -> None:
        workflow = (ROOT / ".github" / "workflows" / "sdk_generation.yaml").read_text()
        self.assertIn("Mint a one-repository preview token", workflow)
        self.assertIn("repositories: x402api-typescript", workflow)
        self.assertIn(
            "github_access_token: ${{ steps.app-token.outputs.token }}", workflow
        )
        self.assertNotIn("pull_request_target:", workflow)
        self.assertIn("finalize-preview:", workflow)
        self.assertIn("needs: [validate-inputs, preview]", workflow)
        self.assertIn("scripts/write-release-manifest.py", workflow)
        self.assertIn("Unresolved generated-source conflict", workflow)
        self.assertIn("npm pack --dry-run", workflow)

    def test_preview_stages_only_normalized_files_before_clean_tree_gate(self) -> None:
        workflow = (ROOT / ".github" / "workflows" / "sdk_generation.yaml").read_text()
        normalize = workflow.index("python scripts/normalize-generated.py --stage")
        cached_check = workflow.index("git diff --cached --check")
        clean_tree = workflow.index(
            "git diff --exit-code -- . ':(exclude).x402api/release.json'"
        )
        manifest_stage = workflow.index("git add .x402api/release.json")

        self.assertLess(normalize, cached_check)
        self.assertLess(cached_check, clean_tree)
        self.assertLess(clean_tree, manifest_stage)
        self.assertNotIn("git add --update", workflow)


if __name__ == "__main__":
    unittest.main()
