---
name: user-journey-mapping
description: Use when improving a customer, employee, partner, or stakeholder experience across a process or lifecycle. Use when applying the User Journey Mapping consulting method and when a user asks for User Journey Mapping, method execution, structured diagnosis, or action planning.
license: Apache-2.0
---

# User Journey Mapping

Use this skill to run `User Journey Mapping` as a practical consulting method, not as a generic framework explanation.

## Method Notes

- Map one persona or segment through a timeline to accomplish one goal.
- Include actions, touchpoints, thoughts, emotions, pain points, and opportunities.

## Required Inputs

Collect or infer these inputs before execution:

- persona or user segment
- journey scope
- known touchpoints
- pain points and evidence

If an input is missing, do not block automatically. Mark it as `missing`, state the assumption used, and add a validation action.

## When Not To Use

Do not combine unrelated segments, goals, and journeys in one map. A journey map needs a defined user, context, goal, and evidence; it is not a substitute for an internal process map.

## Adjacent Methods

- `jobs-to-be-done`: why the customer seeks progress.
- `empathy-map`: a focused actor snapshot.
- `service-blueprint`: backstage processes and systems.

## Step-by-Step Execution

| Step | Required input | How to execute | Output |
|---|---|---|---|
| Define persona and goal | User segment, goal, scenario, start/end points. | Choose one journey for one user type. | Journey scope. |
| Map stages | Timeline, observed steps, channels. | Lay out chronological stages from trigger to outcome. | Journey stage map. |
| Add touchpoints and emotions | User actions, touchpoints, thoughts, feelings, evidence. | Fill each stage with actions, touchpoints, thoughts, emotions, and evidence. | Detailed journey map. |
| Find pain points and moments | Detailed map. | Identify friction, unmet needs, trust moments, and drop-off risks. | Pain point and opportunity list. |
| Prioritize interventions | Pain points, business owners, impact, effort. | Choose changes and validation signals by stage. | Journey improvement plan. |

## Output Template

```markdown
### 1. Persona, Goal, And Journey
Persona / segment:
Goal:
Trigger:
Start / end:
Evidence sources:

### 2. Journey Map
| Stage | Action | Touchpoint | Thought / emotion | Evidence |
|---|---|---|---|---|
|  |  |  |  |  |

### 3. Moments That Matter
| Stage | Friction / trust moment | Impact | Root evidence | Owner |
|---|---|---|---|---|
|  |  |  |  |  |

### 4. Intervention And Validation
| Change | Owner | Timing | User signal | Business guardrail |
|---|---|---|---|---|
|  |  |  |  |  |

### Evidence And Next Decision
- Confirmed facts:
- Assumptions:
- Missing evidence:
- Next action, owner, and timing:
- Expected signal and decision threshold:
```

## Quality Gate

- Produce the method-specific outputs for Persona, Goal, And Journey, Journey Map, Moments That Matter; do not substitute a generic framework summary.
- Tie every material score, causal claim, or stakeholder judgment to evidence or label it as an assumption.
- Include at least one disconfirming check, sensitivity, alternative explanation, or failure condition appropriate to the method.
- Convert the result into a named action or decision with an owner or stakeholder, timing, and observable signal.
- State missing inputs and the smallest validation action instead of inventing precision.
- Keep wording professional and plain enough that a smart non-specialist can use the output directly.
