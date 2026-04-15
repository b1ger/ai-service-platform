# Playbook: New Lead Flow

## Goal
Create a clear workflow for handling a new inbound inquiry.

## Inputs
- source channel
- client message
- contact details if available
- service request type
- urgency if stated

## Steps
1. capture the inquiry
2. normalize the message into a structured summary
3. classify the lead type
4. generate a first-response draft
5. identify missing information
6. prepare follow-up questions
7. store summary for daily reporting

## Outputs
- lead summary
- lead category
- response draft
- clarification questions
- next action

## Example lead categories
- hot lead
- standard inquiry
- info request
- unqualified
- spam / irrelevant

## Edge cases
- missing contact details
- vague service request
- duplicate inquiry
- urgent request outside working hours

## Acceptance criteria
- every new inquiry gets a category
- every qualified inquiry gets a response draft
- every vague inquiry gets clarification questions
- every inquiry appears in summary output
