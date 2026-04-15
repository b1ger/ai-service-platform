# Playbook: Reminder Flow

## Goal
Create reminder logic for appointments, estimates, or pending actions.

## Reminder types
- appointment reminder
- payment reminder
- missing information reminder
- quote expiration reminder

## Inputs
- client name
- event type
- relevant date/time
- preferred channel
- required action

## Output
- reminder message
- timing rule
- final escalation note if needed

## Rules
- keep message short
- mention action clearly
- include date/time if relevant
- do not sound aggressive

## Acceptance criteria
- reminder is understandable at a glance
- required action is obvious
- timing is appropriate to event type
