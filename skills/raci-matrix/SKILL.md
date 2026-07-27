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

Do not use as a personality-reading exercise. Use it only to clarify decision rights, influence, needs, and next engagement moves.

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
### 1. Method Frame
- Decision / question:
- Scope:
- Evidence used:
- Key assumptions:

### 2. Working Output
- RACI matrix:
- ownership gaps:
- overlap conflicts:
- role clarification actions:

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
