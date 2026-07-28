---
name: power-interest-grid
description: Use when stakeholders need to be grouped into manage closely, keep satisfied, keep informed, or monitor categories. Use when applying the Power Interest Grid consulting method and when a user asks for Power Interest Grid, method execution, structured diagnosis, or action planning.
license: Apache-2.0
---

# Power Interest Grid

Use this skill to run `Power Interest Grid` as a practical consulting method, not as a generic framework explanation.

## Method Notes

- Use four cells: manage closely, keep satisfied, keep informed, monitor.
- Power means ability to change the outcome; interest means concern about the outcome.

## Required Inputs

Collect or infer these inputs before execution:

- stakeholder list
- decision context
- power evidence
- interest evidence

If an input is missing, do not block automatically. Mark it as `missing`, state the assumption used, and add a validation action.

## When Not To Use

Do not use when informal influence, stakeholder stance, or relationship networks require a more detailed map. The grid is a coarse engagement triage, not proof of motives or support.

## Adjacent Methods

- `stakeholder-power-map`: add stance, incentives, confidence, informal influence, and next asks.
- `raci-matrix`: clarify execution responsibility after stakeholder strategy is set.

## Step-by-Step Execution

| Step | Required input | How to execute | Output |
|---|---|---|---|
| Define the change or decision | Decision/change, deadline, affected groups. | State what outcome the grid is meant to influence. | Grid scope. |
| Identify stakeholders | Named people, teams, customers, regulators, partners. | List actors and remove duplicates or irrelevant observers. | Stakeholder list. |
| Score power and interest | Authority, influence, dependency, impact, concern level. | Place each actor on high/low power and high/low interest axes. | 2x2 power-interest grid. |
| Choose engagement strategy | Grid placement and relationship constraints. | Assign manage closely, keep satisfied, keep informed, or monitor. | Engagement category per actor. |
| Define communication actions | Category, message need, channel, owner, cadence. | Specify message, sender, timing, and feedback signal. | Communication and engagement plan. |

## Output Template

```markdown
### 1. Decision And Stakeholders
Decision:
Decision owner:
Deadline:
Stakeholders:

### 2. Grid
| Stakeholder | Power | Interest | Evidence / confidence | Quadrant |
|---|---|---|---|---|
|  |  |  |  |  |

### 3. Engagement Strategy
| Stakeholder | Objective | Message / ask | Channel | Owner |
|---|---|---|---|---|
|  |  |  |  |  |

### 4. Movement Signals
| Stakeholder | Expected signal | Watch-out | Escalation |
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

- Produce the method-specific outputs for Decision And Stakeholders, Grid, Engagement Strategy; do not substitute a generic framework summary.
- Tie every material score, causal claim, or stakeholder judgment to evidence or label it as an assumption.
- Include at least one disconfirming check, sensitivity, alternative explanation, or failure condition appropriate to the method.
- Convert the result into a named action or decision with an owner or stakeholder, timing, and observable signal.
- State missing inputs and the smallest validation action instead of inventing precision.
- Keep wording professional and plain enough that a smart non-specialist can use the output directly.
