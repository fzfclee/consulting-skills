---
name: win-loss-review
description: Use after a deal, project, pitch, proposal, or client pursuit to learn why the outcome happened. Use when applying the Win Loss Review consulting method and when a user asks for Win Loss Review, method execution, structured diagnosis, or action planning.
license: Apache-2.0
---

# Win Loss Review

Use this skill to run `Win Loss Review` as a practical consulting method, not as a generic framework explanation.

## Method Notes

- Separate factual timeline from interpretation.
- Classify drivers as controllable, influenceable, or external.

## Required Inputs

Collect or infer these inputs before execution:

- opportunity history
- outcome
- buyer feedback
- competitor information
- sales actions

If an input is missing, do not block automatically. Mark it as `missing`, state the assumption used, and add a validation action.

## When Not To Use

Do not use as a blame review. Use it to improve the next pursuit, decision, or operating process.

## Adjacent Methods

- `deal-strategy-map`: plan a live opportunity before the outcome.
- `competitive-positioning`: improve buyer-facing differentiation from repeated decision evidence.

## Step-by-Step Execution

| Step | Required input | How to execute | Output |
|---|---|---|---|
| Reconstruct timeline | Opportunity data, meetings, proposal, feedback, outcome. | Write factual chronology without interpretation. | Win/loss timeline. |
| Map decision drivers | Buyer criteria, stakeholders, competitors, price, proof. | Identify why the buyer chose the outcome. | Decision driver map. |
| Classify drivers | Decision driver map. | Mark each driver as controllable, influenceable, or external. | Controllability view. |
| Extract lessons | Controllability view and future pursuits. | Convert drivers into specific behavior or asset changes. | Lessons learned. |
| Update playbook | Lessons, owners, next opportunities. | Define qualification, messaging, proof, pricing, or relationship changes. | Improvement action plan. |

## Output Template

```markdown
### 1. Decision Timeline
Opportunity:
Outcome:
Buyer decision date:
Sources:

### 2. Decision Drivers
| Driver | Buyer evidence | Our performance | Competitor / alternative |
|---|---|---|---|
|  |  |  |  |

### 3. Controllability
| Factor | Controllable / influenceable / external | Confidence | Lesson |
|---|---|---|---|
|  |  |  |  |

### 4. Playbook Changes
| Change | Owner | Apply when | Success signal |
|---|---|---|---|
|  |  |  |  |

### Evidence And Next Decision
- Confirmed facts:
- Assumptions:
- Missing evidence:
- Next action, owner, and timing:
- Expected signal and decision threshold:
```

## Quality Gate

- Produce the method-specific outputs for Decision Timeline, Decision Drivers, Controllability; do not substitute a generic framework summary.
- Tie every material score, causal claim, or stakeholder judgment to evidence or label it as an assumption.
- Include at least one disconfirming check, sensitivity, alternative explanation, or failure condition appropriate to the method.
- Convert the result into a named action or decision with an owner or stakeholder, timing, and observable signal.
- State missing inputs and the smallest validation action instead of inventing precision.
- Keep wording professional and plain enough that a smart non-specialist can use the output directly.
