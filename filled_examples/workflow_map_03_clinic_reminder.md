# Workflow Map — Clinic Reminder Flow

## Workflow name
Appointment Reminder and Confirmation Workflow

## Purpose
Reduce admin repetition and improve visibility of unconfirmed appointments.

## Trigger
An upcoming appointment needs confirmation.

## Inputs
- patient name
- appointment date/time
- service type if relevant
- contact channel
- confirmation status

## Core steps
1. identify pending appointment
2. generate reminder message
3. request confirmation
4. flag non-response for follow-up
5. add pending items to daily admin summary

## Decision points
- If confirmation is received:
  - mark as confirmed
- If no reply after reminder:
  - send follow-up or flag for manual call
- If the case is sensitive:
  - keep it manual

## Outputs
- reminder message
- follow-up flag
- daily pending summary
- booking status note

## Human-in-the-loop steps
- admin reviews special or sensitive cases
- admin makes phone calls when needed

## Exceptions / edge cases
- patient prefers calls only
- late reschedule request
- unclear appointment details
- sensitive procedure communication

## Success criteria
- fewer missed reminders
- less admin checking
- clearer pending confirmations list

## Notes
Healthcare communication requires tighter human review boundaries.
