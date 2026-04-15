"""Generator for drafting pilot proposals based on discovery summaries."""
from ai_service_platform.schemas import ProposalResult
from ai_service_platform.utils.parsing import extract_sections, extract_bullets, find_value_by_prefix

def generate_proposal(discovery_text: str, workflow_name: str) -> ProposalResult:
    sections = extract_sections(discovery_text)
    prospect_lines = sections.get("Prospect", "").splitlines()
    
    client_name = find_value_by_prefix(prospect_lines, "Name") or "[Not specified]"
    business_name = find_value_by_prefix(prospect_lines, "Business") or "[Not specified]"
    contact = find_value_by_prefix(prospect_lines, "Channel") or "[Not specified]"
    
    request_summary = extract_bullets(sections.get("Request Summary", ""))
    if not request_summary:
        for section in ["Observed pain point", "Current workflow summary", "Repeated tasks", "Strongest pilot candidate"]:
            extracted = extract_bullets(sections.get(section, ""))
            if extracted:
                request_summary.extend(extracted)
            elif sections.get(section):
                request_summary.append(sections[section].strip())
    
    if not request_summary:
        request_summary = ["Client needs automation."]
    
    return ProposalResult(
        client_name=client_name,
        business_name=business_name,
        contact=contact,
        request_summary=request_summary,
        proposed_solution=[f"Implement {workflow_name} to streamline operations."],
        scope_included=[workflow_name, "Template set", "Usage guide"],
        scope_excluded=["Full CRM integration", "Custom software development"],
        workflow_delivery=["Discovery review", "Workflow mapping", "Template delivery"],
        expected_outcome=["Faster response time", "Less manual retyping"],
        next_step="Approve the pilot scope to begin implementation."
    )

def render_proposal_markdown(res: ProposalResult) -> str:
    def list_to_md(l): return "\n".join([f"- {i}" for i in l]) if l else "- [Not specified]"
    def list_to_num_md(l): return "\n".join([f"{i+1}. {v}" for i, v in enumerate(l)]) if l else "1. [Not specified]"
    
    return f"""# Proposal — {res.proposed_solution[0]}

## Client
- Name: {res.client_name}
- Business: {res.business_name}
- Contact: {res.contact}

## Request summary
{list_to_md(res.request_summary)}

## Proposed solution
{list_to_md(res.proposed_solution)}

## Scope
- included:
{list_to_md(res.scope_included)}
- not included:
{list_to_md(res.scope_excluded)}

## Workflow / delivery
{list_to_num_md(res.workflow_delivery)}

## Expected outcome
{list_to_md(res.expected_outcome)}

## Next step
- {res.next_step}
"""
