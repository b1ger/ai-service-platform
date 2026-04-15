# Internal Tooling MVP

Internal operator-facing CLI tool to generate Phase 1 markdown artifacts.

## Setup
```bash
python3 -m venv venv
source venv/bin/activate
pip install -e .
```

## Commands
### Intake Generator
```bash
asp-tool intake --input examples/inputs/raw_intake.txt --segment contractor --output examples/outputs/intake_summary.md
```

### Workflow Generator
```bash
asp-tool workflow --input examples/inputs/workflow_notes.txt --name "New Inquiry Flow" --segment contractor --output examples/outputs/workflow_map.md
```

### Proposal Generator
```bash
asp-tool proposal --input examples/outputs/intake_summary.md --name "Contractor Inquiry Pilot" --output examples/outputs/proposal_draft.md
```

### Delivery Pack Generator
```bash
asp-tool delivery --workflow examples/outputs/workflow_map.md --notes examples/inputs/delivery_notes.txt --output examples/outputs/delivery_pack.md
```
