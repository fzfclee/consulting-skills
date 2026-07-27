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

## Adjacent Methods

- `fishbone-diagram`: use when several cause branches must be compared.
- `systems-thinking`: use when feedback, delay, or incentives keep recreating the issue.
- `constraint-analysis`: use when one limiting factor is already visible.

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
### 1. Problem Statement
Observed problem:
Expected state:
Evidence:
Boundary:

### 2. Why Chain
| Level | Why did this occur? | Evidence | Assumption |
|---|---|---|---|
|  |  |  |  |

### 3. Root Cause Judgment
Candidate root cause:
Mechanism:
Inside control:
Alternative branch:

### 4. Corrective And Preventive Action
| Action | Owner | Timing | Recurrence signal | Validation |
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

- Produce the method-specific outputs for Problem Statement, Why Chain, Root Cause Judgment; do not substitute a generic framework summary.
- Tie every material score, causal claim, or stakeholder judgment to evidence or label it as an assumption.
- Include at least one disconfirming check, sensitivity, alternative explanation, or failure condition appropriate to the method.
- Convert the result into a named action or decision with an owner or stakeholder, timing, and observable signal.
- State missing inputs and the smallest validation action instead of inventing precision.
- Keep wording professional and plain enough that a smart non-specialist can use the output directly.
