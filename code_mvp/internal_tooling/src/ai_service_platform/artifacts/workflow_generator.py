from ai_service_platform.schemas import WorkflowResult
from ai_service_platform.utils.parsing import extract_bullets, extract_sections

def generate_workflow(notes: str, name: str, segment: str) -> WorkflowResult:
    sections = extract_sections(notes)
    
    return WorkflowResult(
        workflow_name=name,
        purpose=sections.get("Purpose", "Automate routine communication."),
        trigger=sections.get("Trigger", "New inbound inquiry."),
        inputs=extract_bullets(sections.get("Inputs", "")),
        steps=extract_bullets(sections.get("Steps", "")),
        decision_points=extract_bullets(sections.get("Decision Points", "")),
        outputs=extract_bullets(sections.get("Outputs", "")),
        human_in_the_loop=extract_bullets(sections.get("Human Review", "")),
        exceptions=extract_bullets(sections.get("Exceptions", "")),
        success_criteria=extract_bullets(sections.get("Success Criteria", ""))
    )

def render_workflow_markdown(res: WorkflowResult) -> str:
    def list_to_md(l): return "\n".join([f"- {i}" for i in l]) if l else "- TBD"
    def list_to_num_md(l): return "\n".join([f"{i+1}. {v}" for i, v in enumerate(l)]) if l else "1. TBD"
    
    return f"""# Workflow Map — {res.workflow_name}

## Purpose
{res.purpose}

## Trigger
{res.trigger}

## Inputs
{list_to_md(res.inputs)}

## Core steps
{list_to_num_md(res.steps)}

## Decision points
{list_to_md(res.decision_points)}

## Outputs
{list_to_md(res.outputs)}

## Human-in-the-loop steps
{list_to_md(res.human_in_the_loop)}

## Exceptions / edge cases
{list_to_md(res.exceptions)}

## Success criteria
{list_to_md(res.success_criteria)}
"""
