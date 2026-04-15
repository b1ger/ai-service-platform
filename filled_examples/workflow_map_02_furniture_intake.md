# Workflow Map — Furniture Workshop Intake

## Workflow name
Custom Furniture Request Intake

## Purpose
Create cleaner request briefs and reduce owner time spent on clarification.

## Trigger
A new custom order inquiry arrives through chat.

## Inputs
- request text
- reference photos
- dimensions if available
- material or style hints
- preferred timing

## Core steps
1. collect the incoming request
2. summarize it into a structured brief
3. identify missing dimensions, materials, style, and timing
4. send short clarification message
5. classify as quote-ready / needs details / weak fit
6. add quote-ready requests to owner summary

## Decision points
- If dimensions are missing:
  - ask for key measurements
- If the request is still vague after one clarification:
  - classify as not quote-ready
- If the request fits a common product type:
  - suggest the correct next step

## Outputs
- structured brief
- clarification message
- qualification status
- summary item

## Human-in-the-loop steps
- owner approves quoting
- owner confirms product feasibility

## Exceptions / edge cases
- inspiration-only request
- no dimensions
- unrealistic timing
- materials outside workshop offer

## Success criteria
- cleaner first-pass briefs
- fewer repetitive clarification messages
- easier prioritization of serious leads

## Notes
This is a strong niche for future assistant productization.
