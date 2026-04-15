"""Processor for generating client intake summaries from raw notes."""
from ai_service_platform.schemas import IntakeResult
import re

def process_intake(raw_text: str, segment: str) -> IntakeResult:
    lines = raw_text.splitlines()
    
    # Heuristic: first line often contains name if it's "From: Name"
    client_name = "Unknown"
    for line in lines[:5]:
        if "from:" in line.lower():
            client_name = line.split(":", 1)[1].strip()
            break
            
    # Heuristic: category based on keywords
    category = "standard inquiry"
    text_lower = raw_text.lower()
    if any(k in text_lower for k in ["urgent", "asap", "emergency"]):
        category = "hot lead"
    elif any(k in text_lower for k in ["price", "cost", "quote", "estimate"]):
        category = "estimate request"
        
    # Heuristic: missing info by segment
    missing = []
    if segment == "contractor":
        has_location = any(k in text_lower for k in ["location", "address", "city", "we are in", "based in"])
        if not has_location and re.search(r'\bin [A-Z]', raw_text):
            has_location = True
            
        if not has_location:
            missing.append("Job location")
            
        if not any(k in text_lower for k in ["photo", "image", "picture"]): missing.append("Photos of the area")
    elif segment == "furniture":
        if "dimension" not in text_lower and "size" not in text_lower: missing.append("Dimensions")
        if "material" not in text_lower: missing.append("Preferred materials")
        
    return IntakeResult(
        client_name=client_name,
        business_name="[Not specified]",
        contact_channel="[Not specified]",
        request_summary=lines[0] if lines else "Empty inquiry",
        lead_category=category,
        missing_information=missing,
        recommended_next_step="Send clarification request for missing details." if missing else "Prepare estimate.",
        draft_reply=f"Hi {client_name}, thanks for reaching out. To give you an accurate estimate, could you provide: " + ", ".join(missing) if missing else f"Hi {client_name}, thanks for your inquiry. I'll get back to you with an estimate shortly."
    )

def render_intake_markdown(result: IntakeResult) -> str:
    missing_md = "\n".join([f"- {m}" for m in result.missing_information]) if result.missing_information else "- [None identified]"
    return f"""# Client Intake Summary

## Client
- Name: {result.client_name}
- Business: {result.business_name}
- Contact channel: {result.contact_channel}

## Request
- Requested service: {result.request_summary}
- Main pain point: {result.lead_category}
- Urgency: {"Urgent" if "hot" in result.lead_category.lower() else "Standard"}
- Timing: [Not specified]

## Important details
- Budget: [Not specified]
- Location: [Not specified]
- Constraints: [Not specified]
- Supporting materials: [Not specified]

## Missing information
{missing_md}

## Recommended next step
- {result.recommended_next_step}

## Draft reply
- {result.draft_reply}
"""
