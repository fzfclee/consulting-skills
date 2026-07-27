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

Do not use as a fear list. Each risk or force must have a trigger, owner, and response.

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
### 1. Method Frame
- Decision / question:
- Scope:
- Evidence used:
- Key assumptions:

### 2. Working Output
- force field map:
- driving and restraining force scores:
- change levers:
- resistance reduction plan:

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
