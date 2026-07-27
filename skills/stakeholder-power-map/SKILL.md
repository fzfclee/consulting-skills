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
### 1. Method Frame
- Decision / question:
- Scope:
- Evidence used:
- Key assumptions:

### 2. Working Output
- stakeholder map:
- stance diagnosis:
- engagement priorities:
- relationship actions:

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
