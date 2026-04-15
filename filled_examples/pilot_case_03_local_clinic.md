# Pilot Case — Local Clinic

## Client overview
- Client name: Olena
- Business name: SmileCare Dental
- Segment: private dental clinic
- Team size: 6
- Main contact: administrator
- Contact channel: phone + Instagram

## Current-state problem
- Appointment inquiries come from multiple channels.
- Confirmation and reminders are inconsistent.
- The administrator manually checks who still needs confirmation.
- There is no simple daily pending-action summary.

## Workflow selected for pilot
- Workflow name: appointment reminder and confirmation follow-up
- Why this workflow first: it reduces missed appointments and admin repetition
- Expected business value: fewer no-shows and less manual reminder work

## Inputs
- Source of inbound requests: phone, Instagram
- Current tools used: phone, calendar, chat
- Current communication channels: calls, DMs
- Existing templates or scripts: some reminder wording in old messages

## Proposed automation logic
1. Classify booking status as new, confirmed, pending, or reminder needed.
2. Use one standard reminder message format.
3. Trigger a follow-up if confirmation is missing.
4. Send a short daily pending confirmations summary to admin.

## Deliverables
- reminder template
- confirmation follow-up template
- booking status logic
- pending confirmations summary template
- workflow guide for admin

## Risks / constraints
- missing information: some patients prefer calls only
- limitations: medical topics should not be handled by generic messaging logic
- approval dependencies: sensitive patient communication remains human-managed

## Delivery notes
- what was delivered: reminder structure, follow-up logic, daily summary format
- what required manual editing: tone softened to match clinic brand
- what should be standardized next: inbound FAQ response pack

## Feedback
- client reaction: strong interest because admin time is limited
- useful feedback: keep reminders friendly and simple
- objections: do not over-automate sensitive cases
- follow-up opportunity: FAQ and intake message pack

## Reusable learnings
- repeated pain point: pending confirmations are not visible enough
- reusable template candidate: daily booking status summary
- possible productization signal: appointment workflow assistant
