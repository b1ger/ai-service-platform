import unittest
from ai_service_platform.artifacts.intake_processor import process_intake
from ai_service_platform.utils.parsing import extract_bullets, extract_sections

class TestLogic(unittest.TestCase):
    def test_extract_bullets(self):
        text = "- Step 1\n- Step 2\nSome text\n* Step 3"
        bullets = extract_bullets(text)
        self.assertEqual(bullets, ["Step 1", "Step 2", "Step 3"])

    def test_extract_sections(self):
        text = "# Section 1\nContent 1\n## Section 2\nContent 2"
        sections = extract_sections(text)
        self.assertIn("Section 1", sections)
        self.assertIn("Section 2", sections)
        self.assertEqual(sections["Section 1"], "Content 1")

    def test_process_intake_contractor_missing(self):
        raw = "From: Serhii\nI need a contractor."
        result = process_intake(raw, "contractor")
        self.assertEqual(result.client_name, "Serhii")
        self.assertIn("Job location", result.missing_information)
        self.assertIn("Photos of the area", result.missing_information)

    def test_process_intake_contractor_found(self):
        raw = "From: Serhii\nI need a contractor. We are in Lviv. I have photos."
        result = process_intake(raw, "contractor")
        self.assertEqual(result.missing_information, [])
        
        raw2 = "From: Alex\nI need a contractor in Kyiv with some images."
        result2 = process_intake(raw2, "contractor")
        self.assertEqual(result2.missing_information, [])

    def test_workflow_markdown_shape(self):
        from ai_service_platform.artifacts.workflow_generator import generate_workflow, render_workflow_markdown
        notes = "# Purpose\nTest purpose\n# Steps\n- Step 1"
        res = generate_workflow(notes, "Test WF", "test")
        md = render_workflow_markdown(res)
        self.assertIn("# Workflow Map — Test WF", md)
        self.assertIn("## Workflow name", md)
        self.assertIn("## Purpose", md)
        self.assertIn("## Core steps", md)
        self.assertIn("## Human-in-the-loop steps", md)

    def test_proposal_markdown_shape(self):
        from ai_service_platform.artifacts.proposal_generator import generate_proposal, render_proposal_markdown
        discovery = "# Prospect\nName: Serhii\nBusiness: RenovPro\n# Request Summary\n- Problem 1"
        res = generate_proposal(discovery, "Test Pilot")
        md = render_proposal_markdown(res)
        self.assertIn("# Proposal — Implement Test Pilot", md)
        self.assertIn("## Client", md)
        self.assertIn("- Name: Serhii", md)
        self.assertIn("- Business: RenovPro", md)
        self.assertIn("## Request summary", md)
        self.assertIn("- Problem 1", md)
        self.assertIn("## Scope", md)
        self.assertIn("- included:", md)
        self.assertIn("- not included:", md)
        self.assertIn("1. Discovery review", md) # checking numbered list formatting

    def test_proposal_fallback_logic(self):
        from ai_service_platform.artifacts.proposal_generator import generate_proposal
        discovery_no_summary = "# Observed pain point\n- Lots of manual typing"
        res = generate_proposal(discovery_no_summary, "Test Pilot")
        self.assertIn("Lots of manual typing", res.request_summary)

        discovery_text_pain = "# Observed pain point\nOwner feels overwhelmed."
        res2 = generate_proposal(discovery_text_pain, "Test Pilot")
        self.assertIn("Owner feels overwhelmed.", res2.request_summary)

    def test_delivery_markdown_shape(self):
        from ai_service_platform.artifacts.delivery_pack_builder import build_delivery_pack, render_delivery_markdown
        wf = "# Core steps\n- Step 1\n# Exceptions / edge cases\n- Edge 1"
        notes = "# Summary\nDone\n# Current Issue\n- Issue 1\n# Templates\n- Template 1"
        res = build_delivery_pack(wf, notes)
        md = render_delivery_markdown(res)
        self.assertIn("# Client Delivery Pack", md)
        self.assertIn("## Summary", md)
        self.assertIn("## Current issue", md)
        self.assertIn("## Proposed workflow", md)
        self.assertIn("## What is improved", md)
        self.assertIn("## Templates included", md)
        self.assertIn("## Exceptions to watch", md)
        self.assertIn("## Recommended next step", md)

    def test_empty_fallback_rendering(self):
        from ai_service_platform.artifacts.workflow_generator import generate_workflow, render_workflow_markdown
        res = generate_workflow("", "Empty WF", "none")
        md = render_workflow_markdown(res)
        self.assertIn("[Not specified]", md)
        self.assertNotIn("TBD", md)

if __name__ == "__main__":
    unittest.main()
