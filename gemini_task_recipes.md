# Gemini Task Recipes

## Purpose
Provide repeatable task recipes for Gemini CLI so project work does not depend on ad hoc prompting.

## General usage rule
Always work from repository files first:
- `GEMINI.md`
- `PROJECT_SCOPE.md`
- `TARGET_CLIENTS.md`
- relevant playbooks
- relevant templates
- relevant examples

Do not rely on prior chat context when a file-based source exists.

---

## Recipe 1 — Discovery Summary Generation

### Use when
A prospect conversation, message thread, or call notes need to be converted into structured discovery notes.

### Inputs
- raw notes
- prospect segment
- observed pains
- communication channel
- candidate workflow

### Required outputs
- structured discovery summary
- strongest pilot candidate
- fit assessment
- recommended next step

### Prompting pattern
1. read `templates/discovery_notes_template.md`
2. read one matching example from `filled_examples/`
3. generate a structured discovery summary
4. mark assumptions explicitly
5. do not invent business details

---

## Recipe 2 — Workflow Map Generation

### Use when
A repeated business process needs to be documented as a workflow.

### Inputs
- business segment
- problem summary
- workflow name
- raw process notes

### Required outputs
- workflow purpose
- trigger
- inputs
- steps
- decision points
- outputs
- human review points
- exceptions
- success criteria

### Prompting pattern
1. read `workflow_map_template.md`
2. read matching playbook
3. read matching filled example
4. generate workflow map
5. keep scope narrow

---

## Recipe 3 — Proposal Draft Generation

### Use when
A client or prospect needs a short proposal for a pilot workflow.

### Inputs
- discovery summary
- selected workflow
- scope boundaries
- expected value

### Required outputs
- request summary
- proposed solution
- scope
- delivery steps
- expected outcome
- next step

### Prompting pattern
1. read `templates/proposal_template.md`
2. read a matching proposal example
3. generate proposal
4. avoid vague promises
5. keep scope to one workflow if early-stage

---

## Recipe 4 — Client Delivery Pack Drafting

### Use when
A completed workflow or pilot needs to be packaged for delivery.

### Inputs
- final workflow
- message templates
- usage notes
- exceptions
- next-step recommendation

### Required outputs
- current issue summary
- proposed workflow
- included templates
- usage notes
- exceptions
- next step

### Prompting pattern
1. read `client_delivery_template.md`
2. read related workflow map
3. read `ops/delivery_checklist.md`
4. generate a concise delivery document
5. make it client-sendable

---

## Recipe 5 — Outreach Message Drafting

### Use when
Drafting outreach for a target niche.

### Inputs
- niche
- observed pain point
- desired CTA

### Required outputs
- short outreach message
- no technical jargon
- one clear CTA

### Prompting pattern
1. read `OUTREACH_STRATEGY.md`
2. read `templates/outreach_message_template.md`
3. read a matching filled example
4. generate concise niche-specific message

---

## Recipe 6 — Template Refinement

### Use when
A reusable template needs improvement after pilot feedback.

### Inputs
- current template
- failure points
- user feedback
- desired improvement

### Required outputs
- improved template
- change summary
- note on when to use it

### Prompting pattern
1. read template
2. read pilot feedback
3. revise conservatively
4. preserve reusable structure
