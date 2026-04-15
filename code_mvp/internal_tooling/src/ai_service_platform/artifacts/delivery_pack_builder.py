from ai_service_platform.schemas import DeliveryPackResult
from ai_service_platform.utils.parsing import extract_sections, extract_bullets

def build_delivery_pack(workflow_text: str, notes_text: str) -> DeliveryPackResult:
    wf_sections = extract_sections(workflow_text)
    notes_sections = extract_sections(notes_text)
    
    return DeliveryPackResult(
        client_business="TBD",
        summary=notes_sections.get("Summary", "Workflow implementation complete."),
        current_issue=extract_bullets(notes_sections.get("Current Issue", "")),
        proposed_workflow=extract_bullets(wf_sections.get("Core steps", "")),
        improvements=extract_bullets(notes_sections.get("Improvements", "")),
        templates_included=extract_bullets(notes_sections.get("Templates", "")),
        how_to_use=extract_bullets(notes_sections.get("How to use", "")),
        exceptions=extract_bullets(wf_sections.get("Exceptions / edge cases", "")),
        next_step=notes_sections.get("Next step", "Schedule a review call.")
    )

def render_delivery_markdown(res: DeliveryPackResult) -> str:
    def list_to_md(l): return "\n".join([f"- {i}" for i in l])
    
    return f"""# Client Delivery Pack

## Summary
{res.summary}

## Current issue
{list_to_md(res.current_issue)}

## Proposed workflow
{list_to_md(res.proposed_workflow)}

## What is improved
{list_to_md(res.improvements)}

## Templates included
{list_to_md(res.templates_included)}

## How to use
{list_to_md(res.how_to_use)}

## Exceptions to watch
{list_to_md(res.exceptions)}

## Recommended next step
{res.next_step}
"""
