---
name: service-blueprint
description: Use when improving service delivery, handoffs, operational reliability, or customer-facing execution. Use when applying the Service Blueprint consulting method and when a user asks for Service Blueprint, method execution, structured diagnosis, or action planning.
license: Apache-2.0
---

# Service Blueprint

Use this skill to run `Service Blueprint` as a practical consulting method, not as a generic framework explanation.

## Method Notes

- Start from a specific customer journey.
- Map customer actions, frontstage, backstage, support processes, systems, and evidence.

## Required Inputs

Collect or infer these inputs before execution:

- service scope
- customer journey
- roles
- systems and process evidence

If an input is missing, do not block automatically. Mark it as `missing`, state the assumption used, and add a validation action.

## When Not To Use

Do not use for all users at once. Choose one segment, scenario, journey, job, or service context.

## Step-by-Step Execution

| Step | Required input | How to execute | Output |
|---|---|---|---|
| Select service scenario | Customer journey, service scope, user goal. | Choose one journey scenario and outcome. | Blueprint scope. |
| Map customer actions | Journey stages and touchpoints. | Write customer-visible actions in sequence. | Customer action row. |
| Map frontstage and evidence | People, channels, scripts, forms, physical/digital evidence. | Add visible service interactions and artifacts. | Frontstage/evidence rows. |
| Map backstage and support | Internal teams, systems, policies, handoffs. | Add backstage work, support processes, systems, and dependencies. | Backstage/support rows. |
| Diagnose failures | Completed blueprint. | Identify handoff gaps, wait states, rework, missing ownership, and system constraints. | Service improvement plan. |

## Output Template

```markdown
### 1. Method Frame
- Decision / question:
- Scope:
- Evidence used:
- Key assumptions:

### 2. Working Output
- service blueprint:
- failure points:
- handoff gaps:
- operational improvements:

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
