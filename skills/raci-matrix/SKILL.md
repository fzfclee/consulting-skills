---
name: raci-matrix
description: Use when ownership, approval rights, handoffs, or decision authority are unclear. Use when applying the RACI Matrix consulting method and when a user asks for RACI Matrix, method execution, structured diagnosis, or action planning.
license: Apache-2.0
---

# RACI Matrix

Use this skill to run `RACI Matrix` as a practical consulting method, not as a generic framework explanation.

## Method Notes

- Use exactly one Accountable owner per decision or deliverable whenever possible.
- Responsible does the work; Accountable owns the result; Consulted gives two-way input; Informed receives one-way updates.

## Required Inputs

Collect or infer these inputs before execution:

- work items or decisions
- roles or named owners
- current responsibility ambiguity
- decision cadence

If an input is missing, do not block automatically. Mark it as `missing`, state the assumption used, and add a validation action.

## When Not To Use

Do not use before the work products, decisions, and role boundaries are defined. RACI clarifies accountability for work; it does not resolve stakeholder resistance, authority gaps, or capacity shortages.

## Adjacent Methods

- `change-impact-analysis`: diagnose affected groups and adoption needs.
- `communications-plan`: define messages, channels, cadence, and feedback.

## Step-by-Step Execution

| Step | Required input | How to execute | Output |
|---|---|---|---|
| Define rows | Decisions, deliverables, process steps, or recurring tasks. | Write each row as one accountable work item with a clear completion point. | RACI row list. |
| Define columns | Roles, named owners, teams, approvers, contributors. | Use roles when many people rotate; use names when accountability is personal. | Role/owner column list. |
| Assign R/A/C/I | Rows, columns, known authority, handoff rules. | Assign Responsible, Accountable, Consulted, and Informed; keep one Accountable when possible. | Draft RACI matrix. |
| Find role defects | Draft matrix. | Flag no Accountable, multiple Accountables, no Responsible, over-consulting, or missing informed parties. | Ownership gap list. |
| Confirm operating rules | Gap list, governance cadence, escalation path. | Define sign-off, handoff, update cadence, and unresolved-role decision owner. | Final RACI and role clarification actions. |

## Output Template

```markdown
### 1. Scope And Decision Rights
Process / project:
Decision rows:
Roles:
Escalation owner:

### 2. RACI Matrix
| Work / decision | R | A | C | I | Timing |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

### 3. Defects
| Row | Missing / duplicate accountability | Conflict | Fix |
|---|---|---|---|
|  |  |  |  |

### 4. Operating Rules
| Rule | Owner | Trigger | Escalation path |
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

- Produce the method-specific outputs for Scope And Decision Rights, RACI Matrix, Defects; do not substitute a generic framework summary.
- Tie every material score, causal claim, or stakeholder judgment to evidence or label it as an assumption.
- Include at least one disconfirming check, sensitivity, alternative explanation, or failure condition appropriate to the method.
- Convert the result into a named action or decision with an owner or stakeholder, timing, and observable signal.
- State missing inputs and the smallest validation action instead of inventing precision.
- Keep wording professional and plain enough that a smart non-specialist can use the output directly.
