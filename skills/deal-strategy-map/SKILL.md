---
name: deal-strategy-map
description: Use when pursuing a specific opportunity and needing a structured path to win or advance. Use when applying the Deal Strategy Map consulting method and when a user asks for Deal Strategy Map, method execution, structured diagnosis, or action planning.
license: Apache-2.0
---

# Deal Strategy Map

Use this skill to run `Deal Strategy Map` as a practical consulting method, not as a generic framework explanation.

## Method Notes

- Map buying process, stakeholders, win themes, objections, proof, and next commitment.
- The plan must name the next buyer action needed.

## Required Inputs

Collect or infer these inputs before execution:

- opportunity details
- buyer process
- stakeholders
- competitors
- proof and objections

If an input is missing, do not block automatically. Mark it as `missing`, state the assumption used, and add a validation action.

## When Not To Use

Do not use as a sales slogan. Use it to clarify value, buying logic, proof, operating fit, and next commercial action.

## Step-by-Step Execution

| Step | Required input | How to execute | Output |
|---|---|---|---|
| Define deal state | Opportunity, stage, value, deadline, next decision. | State current stage and required next buyer commitment. | Deal frame. |
| Map buying process | Decision steps, criteria, stakeholders, procurement, legal/finance gates. | Lay out how the buyer will decide. | Buying-process map. |
| Assess win themes | Buyer pain, value proof, competitors, objections. | Define why you should win and what could block the deal. | Win/loss driver map. |
| Plan stakeholder moves | Stakeholder influence and relationship access. | Assign message, proof, and ask for each key stakeholder. | Stakeholder pursuit plan. |
| Set next commitment | Deal map, timing, risks. | Define the next meeting, document, pilot, approval, or negotiation move. | Deal action plan. |

## Output Template

```markdown
### 1. Method Frame
- Decision / question:
- Scope:
- Evidence used:
- Key assumptions:

### 2. Working Output
- deal strategy map:
- win themes:
- stakeholder actions:
- next steps and fallbacks:

### 3. Implications
- What this changes:
- What to do first:
- What to watch:

### 4. Open Questions
- Missing evidence:
- Validation step:
- Owner / timing:
```

## Quality Gate

- The output must change a decision, action, prioritization, risk view, or validation plan.
- Every major claim must be tied to evidence or labeled as an assumption.
- Each recommendation must name the action, owner or stakeholder, timing, and expected signal.
- Remove framework filler. Do not explain the method unless the explanation helps the user act.
- Keep wording professional and plain enough that a smart non-specialist can use it without translation.
