---
name: fifteen-percent-solutions
description: Use when the user needs immediate controllable next actions inside limited authority, resources, or certainty. Use when applying 15% Solutions, small controllable action, low-regret next step, agency boundary, or next-72-hour action planning.
license: Apache-2.0
---

# Fifteen Percent Solutions

Use this skill to find actions the user can take now without waiting for full authority, perfect certainty, or broad alignment.

## Method Notes

- A 15% solution is a small action inside the user's current control boundary.
- It should be meaningful enough to create evidence or movement, not just busy work.
- It is especially useful after diagnosis shows the full outcome depends on other people.

## Required Inputs

Collect or infer these inputs before execution:

- desired outcome
- user's role, authority, relationships, and constraints
- blockers outside the user's control
- available time, access, and resources
- risk tolerance

If an input is missing, mark it as `missing`, state the assumption used, and add a validation action.

## When Not To Use

Do not use when a high-risk action requires formal approval, legal review, compliance clearance, or irreversible commitment. Use `risk-matrix`, `raci-matrix`, or `communications-plan` first.

## Step-by-Step Execution

| Step | Required input | How to execute | Output |
|---|---|---|---|
| State the desired movement | Outcome, current blockage. | Define what progress would look like in the next few days. | Near-term progress target. |
| Map control boundary | Role, authority, access, constraints. | Separate what the user controls, influences, and cannot control. | Control boundary map. |
| Generate small actions | Control boundary, available resources. | List actions that require no new permission or only low-risk informal alignment. | Candidate 15% actions. |
| Screen for usefulness and risk | Candidate actions, risk tolerance, stakeholder context. | Keep actions that create evidence, open a door, reduce ambiguity, or build trust. Remove symbolic busy work. | Shortlisted actions. |
| Choose first action | Shortlist, timing, expected signal. | Select 1-3 actions for the next 24-72 hours. | Immediate action plan. |
| Define evidence signal | Action, expected response, decision gate. | State what result means continue, adjust, or stop. | Validation signal. |

## Output Template

```markdown
### 1. Near-Term Progress Target
- Desired movement in the next 24-72 hours:
- Current blocker:

### 2. Control Boundary
| Area | Inside my control | I can influence | Outside my control |
|---|---|---|---|
|  |  |  |  |

### 3. Candidate 15% Actions
| Action | Why it is within control | Expected signal | Risk level | Keep / drop |
|---|---|---|---|---|
|  |  |  | low / medium / high |  |

### 4. Recommended First Moves
1.
2.
3.

### 5. Decision Gate
- Continue if:
- Adjust if:
- Stop or escalate if:
```

## Quality Gate

- The action must be genuinely within the user's current control or low-risk influence.
- Do not recommend manipulation, pressure tactics, or hidden escalation.
- The action should generate evidence, trust, access, or clarity.
- Avoid over-investing before the validation signal appears.
- Keep instructions concrete: who, what, when, and what response to look for.
