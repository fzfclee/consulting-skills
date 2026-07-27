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

## Adjacent Methods

- `user-journey-mapping`: user experience without backstage operations.
- `jobs-to-be-done`: demand and switching logic.
- `empathy-map`: perceptions of one actor.

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
### 1. Service Scope
Customer / segment:
Journey start / end:
Service outcome:
Evidence:

### 2. Blueprint
| Stage | Customer action | Frontstage | Evidence | Backstage | Support system |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

### 3. Failures And Handoffs
| Point | Failure / delay | Cause | Owner | Customer impact |
|---|---|---|---|---|
|  |  |  |  |  |

### 4. Improvement Plan
| Intervention | Owner | Timing | Service signal | Guardrail |
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

- Produce the method-specific outputs for Service Scope, Blueprint, Failures And Handoffs; do not substitute a generic framework summary.
- Tie every material score, causal claim, or stakeholder judgment to evidence or label it as an assumption.
- Include at least one disconfirming check, sensitivity, alternative explanation, or failure condition appropriate to the method.
- Convert the result into a named action or decision with an owner or stakeholder, timing, and observable signal.
- State missing inputs and the smallest validation action instead of inventing precision.
- Keep wording professional and plain enough that a smart non-specialist can use the output directly.
