# Gemini CLI Working Conventions

## Purpose
Standardize how Gemini CLI should be used inside this repository.

## Session start convention
At the beginning of a task:
1. identify the artifact type
2. read the matching template
3. read the matching playbook
4. read one matching example if available
5. generate only the requested artifact

## File update convention
When refining a deliverable:
- update the artifact first
- then update the source template only if the issue is reusable
- then update `BAD_CASES.md` or `EDGE_CASES.md` if needed

## Naming convention
Use descriptive file names:
- `discovery_summary_[client].md`
- `workflow_map_[workflow].md`
- `proposal_[client]_[workflow].md`
- `delivery_[client]_[workflow].md`

## Review convention
Before finalizing:
- run through `ACCEPTANCE_CRITERIA.md`
- run through `ops/artifact_qa_matrix.md`
- check `ops/revision_rules.md`

## Anti-patterns
- generating proposals without discovery notes
- generating workflow maps without a named workflow
- skipping scope exclusions
- writing delivery docs in internal language
