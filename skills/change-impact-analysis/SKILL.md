---
name: change-impact-analysis
description: Use when implementing process, system, organization, policy, or operating-model changes. Use when applying the Change Impact Analysis consulting method and when a user asks for Change Impact Analysis, method execution, structured diagnosis, or action planning.
license: Apache-2.0
---

# Change Impact Analysis

Use this skill to run `Change Impact Analysis` as a practical consulting method, not as a generic framework explanation.

## Method Notes

- Describe current-to-future behavior changes by affected group.
- Assess impact severity, readiness, capability gap, and resistance.

## Required Inputs

Collect or infer these inputs before execution:

- change description
- affected groups
- current vs future process
- adoption constraints

If an input is missing, do not block automatically. Mark it as `missing`, state the assumption used, and add a validation action.

## When Not To Use

Do not use as a fear list. Each risk or force must have a trigger, owner, and response.

## Step-by-Step Execution

| Step | Required input | How to execute | Output |
|---|---|---|---|
| Define change | Current state, future state, go-live date. | State what will change in work, decisions, tools, or incentives. | Change definition. |
| Identify affected groups | Teams, roles, customers, partners, stakeholders. | List who is affected and how. | Affected group map. |
| Assess impact | Current/future workflows, workload, capability, readiness. | Rate impact severity, readiness, resistance, and capability gap. | Impact assessment. |
| Design support | Impact assessment. | Define communication, training, sponsor, process, system, or policy support. | Adoption support plan. |
| Plan rollout controls | Support plan, timing, risks. | Set owner, cadence, feedback loop, and escalation path. | Change rollout plan. |

## Output Template

```markdown
### 1. Method Frame
- Decision / question:
- Scope:
- Evidence used:
- Key assumptions:

### 2. Working Output
- impact assessment:
- affected stakeholder groups:
- support needs:
- change actions:

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
