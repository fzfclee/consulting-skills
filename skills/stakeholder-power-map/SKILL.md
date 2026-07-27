---
name: stakeholder-power-map
description: Use when a decision depends on named people, sponsors, blockers, buyers, approvers, influencers, or hidden veto rights. Use when applying the Stakeholder Power Map consulting method and when a user asks for Stakeholder Power Map, method execution, structured diagnosis, or action planning.
license: Apache-2.0
---

# Stakeholder Power Map

Use this skill to run `Stakeholder Power Map` as a practical consulting method, not as a generic framework explanation.

## Method Notes

- Classify formal power separately from informal influence.
- Do not confuse friendliness with support.
- Always separate confirmed stance from inferred stance.

## Required Inputs

Collect or infer these inputs before execution:

- stakeholder list
- decision to be influenced
- known facts about power, interest, stance, incentives

If an input is missing, do not block automatically. Mark it as `missing`, state the assumption used, and add a validation action.

## When Not To Use

Do not use as a personality-reading exercise. Use it only to clarify decision rights, influence, needs, and next engagement moves.

## Adjacent Methods

- `power-interest-grid`: use for a quick power-and-interest engagement classification.
- `account-plan`: use for the broader commercial relationship and growth plan.
- `raci-matrix`: use for responsibility after the decision and work are defined.

## Step-by-Step Execution

| Step | Required input | How to execute | Output |
|---|---|---|---|
| Define the decision arena | Decision, decision owner, deadline, desired outcome. | State what decision must move and what support means in observable terms. | Decision arena and support definition. |
| List stakeholders | Names, titles, formal roles, relationship facts, source evidence. | Create one row per stakeholder and mark facts vs assumptions. | Stakeholder inventory. |
| Score power and stance | Authority, budget control, veto power, influence, current stance. | Rate formal power, informal influence, interest, stance, and confidence. | Power/stance table. |
| Diagnose incentives and concerns | Known goals, risks, constraints, relationship history. | Infer what each person gains, fears, protects, or may resist. | Needs, concerns, and likely objections. |
| Plan engagement moves | Priority stakeholders, access paths, message options, timing. | Choose next ask, channel, sponsor path, fallback, and validation signal. | Stakeholder action plan. |

## Output Template

```markdown
### 1. Decision Arena
Decision:
Observable support needed:
Deadline:
Decision owner:

### 2. Power And Stance
| Stakeholder | Formal power | Informal influence | Stance | Evidence / confidence |
|---|---|---|---|---|
|  |  |  |  |  |

### 3. Incentives And Concerns
| Stakeholder | Gain sought | Loss feared | Likely objection |
|---|---|---|---|
|  |  |  |  |

### 4. Engagement Plan
| Priority | Stakeholder | Next ask | Channel / sponsor | Timing | Signal / fallback |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

### Evidence And Next Decision
- Confirmed facts:
- Assumptions:
- Missing evidence:
- Next action, owner, and timing:
- Expected signal and decision threshold:
```

## Quality Gate

- Produce the method-specific outputs for Decision Arena, Power And Stance, Incentives And Concerns; do not substitute a generic framework summary.
- Tie every material score, causal claim, or stakeholder judgment to evidence or label it as an assumption.
- Include at least one disconfirming check, sensitivity, alternative explanation, or failure condition appropriate to the method.
- Convert the result into a named action or decision with an owner or stakeholder, timing, and observable signal.
- State missing inputs and the smallest validation action instead of inventing precision.
- Keep wording professional and plain enough that a smart non-specialist can use the output directly.
