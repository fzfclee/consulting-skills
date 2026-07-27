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

## Adjacent Methods

- `account-plan`: manage the wider account objective, relationships, and growth path.
- `stakeholder-power-map`: diagnose formal power, informal influence, stance, and vetoes.

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
### 1. Deal State
Decision sought:
Value / scope:
Deadline:
Confirmed buying stage:

### 2. Buying Process
| Step | Decision owner | Criteria | Evidence | Blocker |
|---|---|---|---|---|
|  |  |  |  |  |

### 3. Win Themes And Proof
| Buyer need | Win theme | Proof | Competitor risk |
|---|---|---|---|
|  |  |  |  |

### 4. Commitment Plan
| Next commitment | Stakeholder | Owner | Timing | Signal | Fallback |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

### Evidence And Next Decision
- Confirmed facts:
- Assumptions:
- Missing evidence:
- Next action, owner, and timing:
- Expected signal and decision threshold:
```

## Quality Gate

- Produce the method-specific outputs for Deal State, Buying Process, Win Themes And Proof; do not substitute a generic framework summary.
- Tie every material score, causal claim, or stakeholder judgment to evidence or label it as an assumption.
- Include at least one disconfirming check, sensitivity, alternative explanation, or failure condition appropriate to the method.
- Convert the result into a named action or decision with an owner or stakeholder, timing, and observable signal.
- State missing inputs and the smallest validation action instead of inventing precision.
- Keep wording professional and plain enough that a smart non-specialist can use the output directly.
