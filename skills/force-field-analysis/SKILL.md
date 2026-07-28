---
name: force-field-analysis
description: Use when adoption, stakeholder support, or organizational movement depends on shifting incentives and resistance. Use when applying the Force Field Analysis consulting method and when a user asks for Force Field Analysis, method execution, structured diagnosis, or action planning.
license: Apache-2.0
---

# Force Field Analysis

Use this skill to run `Force Field Analysis` as a practical consulting method, not as a generic framework explanation.

## Method Notes

- List driving and restraining forces separately.
- Reducing a restraining force is often better than adding pressure.

## Required Inputs

Collect or infer these inputs before execution:

- desired change
- supporting forces
- resisting forces
- stakeholders
- constraints

If an input is missing, do not block automatically. Mark it as `missing`, state the assumption used, and add a validation action.

## When Not To Use

Do not use when the target change and relevant actors are unclear. Avoid generic pros-and-cons lists: each driving or restraining force needs evidence, relative strength, and a practical response.

## Adjacent Methods

- `change-impact-analysis`: assess affected groups, readiness, and adoption support.
- `stakeholder-power-map`: diagnose named sponsors, blockers, incentives, and vetoes.

## Step-by-Step Execution

| Step | Required input | How to execute | Output |
|---|---|---|---|
| Define change | Desired change, current state, target state. | State the behavior or decision that must shift. | Change statement. |
| List driving forces | Sponsors, incentives, pressures, benefits. | Identify forces pushing toward the change. | Driving-force list. |
| List restraining forces | Concerns, incentives, risks, capacity, politics. | Identify forces resisting the change. | Restraining-force list. |
| Score forces | Force lists and evidence. | Rate strength, addressability, owner, and evidence quality. | Force field map. |
| Choose levers | Force field map. | Decide which restraining forces to reduce and which driving forces to strengthen. | Change lever plan. |

## Output Template

```markdown
### 1. Change Objective
Desired change:
Current state:
Decision owner:
Time horizon:

### 2. Forces
| Force | Driver / restraint | Strength | Evidence | Controllability |
|---|---|---|---|---|
|  |  |  |  |  |

### 3. Net Diagnosis
Dominant drivers:
Dominant restraints:
Fragile assumptions:

### 4. Intervention Plan
| Force to change | Move | Owner | Timing | Signal / side effect |
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

- Produce the method-specific outputs for Change Objective, Forces, Net Diagnosis; do not substitute a generic framework summary.
- Tie every material score, causal claim, or stakeholder judgment to evidence or label it as an assumption.
- Include at least one disconfirming check, sensitivity, alternative explanation, or failure condition appropriate to the method.
- Convert the result into a named action or decision with an owner or stakeholder, timing, and observable signal.
- State missing inputs and the smallest validation action instead of inventing precision.
- Keep wording professional and plain enough that a smart non-specialist can use the output directly.
