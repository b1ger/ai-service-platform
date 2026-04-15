from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class IntakeResult:
    client_name: str
    business_name: str
    contact_channel: str
    request_summary: str
    lead_category: str
    missing_information: List[str]
    recommended_next_step: str
    draft_reply: str

@dataclass
class WorkflowResult:
    workflow_name: str
    purpose: str
    trigger: str
    inputs: List[str]
    steps: List[str]
    decision_points: List[str]
    outputs: List[str]
    human_in_the_loop: List[str]
    exceptions: List[str]
    success_criteria: List[str]

@dataclass
class ProposalResult:
    client_name: str
    business_name: str
    contact: str
    request_summary: List[str]
    proposed_solution: List[str]
    scope_included: List[str]
    scope_excluded: List[str]
    workflow_delivery: List[str]
    expected_outcome: List[str]
    next_step: str

@dataclass
class DeliveryPackResult:
    client_business: str
    summary: str
    current_issue: List[str]
    proposed_workflow: List[str]
    improvements: List[str]
    templates_included: List[str]
    how_to_use: List[str]
    exceptions: List[str]
    next_step: str
