from ai_service_platform.schemas import ProposalResult
from ai_service_platform.utils.parsing import extract_sections, extract_bullets

def generate_proposal(discovery_text: str, workflow_name: str) -> ProposalResult:
    sections = extract_sections(discovery_text)
    
    return ProposalResult(
        client_name="TBD",
        business_name="TBD",
        contact="TBD",
        request_summary=extract_bullets(sections.get("Request Summary", "Client needs automation.")),
        proposed_solution=[f"Implement {workflow_name} to streamline operations."],
        scope_included=[workflow_name, "Template set", "Usage guide"],
        scope_excluded=["Full CRM integration", "Custom software development"],
        workflow_delivery=["Discovery review", "Workflow mapping", "Template delivery"],
        expected_outcome=["Faster response time", "Less manual retyping"],
        next_step="Approve the pilot scope to begin implementation."
    )

def render_proposal_markdown(res: ProposalResult) -> str:
    def list_to_md(l): return "\n".join([f"- {i}" for i in l])
    
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
### Included:
{list_to_md(res.scope_included)}
### Excluded:
{list_to_md(res.scope_excluded)}

## Workflow / delivery
{list_to_md(res.workflow_delivery)}

## Expected outcome
{list_to_md(res.expected_outcome)}

## Next step
{res.next_step}
"""
