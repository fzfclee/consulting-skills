---
name: five-whys-root-cause
description: Use when a problem keeps recurring, the first explanation is too shallow, or the action plan risks treating symptoms. Use when applying the Five Whys Root Cause consulting method and when a user asks for Five Whys Root Cause, method execution, structured diagnosis, or action planning.
license: Apache-2.0
---

# Five Whys Root Cause

Use this skill to run `Five Whys Root Cause` as a practical consulting method, not as a generic framework explanation.

## Method Notes

- Ask why until reaching a controllable cause, not a person to blame.
- Branch when the answer has multiple causes.

## Required Inputs

Collect or infer these inputs before execution:

- problem statement
- evidence
- timeline
- constraints and failed fixes

If an input is missing, do not block automatically. Mark it as `missing`, state the assumption used, and add a validation action.

## When Not To Use

Do not use to assign blame. Use it to find controllable causes and recurrence prevention.

## Step-by-Step Execution

| Step | Required input | How to execute | Output |
|---|---|---|---|
| State problem | Observed issue, impact, scope, time. | Write one clear problem without blame. | Problem statement. |
| Ask first why | Problem and immediate evidence. | Explain the direct cause with evidence. | Cause 1. |
| Continue why chain | Previous cause and evidence. | Ask why again until reaching a controllable system/process cause. | Cause chain. |
| Branch if needed | Cause chain with multiple plausible causes. | Split into parallel why chains when one answer hides multiple causes. | Cause branches. |
| Convert to prevention | Root cause and constraints. | Define corrective action, owner, deadline, and recurrence check. | Root-cause action plan. |

## Output Template

```markdown
### 1. Method Frame
- Decision / question:
- Scope:
- Evidence used:
- Key assumptions:

### 2. Working Output
- cause chain:
- root cause candidates:
- evidence gaps:
- corrective actions:

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
