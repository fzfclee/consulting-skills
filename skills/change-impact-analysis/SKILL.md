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

Do not use before the proposed change, affected groups, processes, systems, locations, and timing are defined. It identifies what must adapt; it does not replace a delivery plan or risk assessment.

## Adjacent Methods

- `force-field-analysis`: compare forces supporting and resisting a defined change.
- `raci-matrix`: assign responsibility after the work and decisions are clear.
- `communications-plan`: design audience messages, channels, cadence, and feedback.

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
### 1. Change Definition
What changes:
What stays the same:
Decision owner:
Rollout horizon:

### 2. Impact And Readiness
| Group / role | Process / tool / behavior impact | Severity | Readiness evidence | Risk |
|---|---|---|---|---|
|  |  |  |  |  |

### 3. Support Plan
| Need | Intervention | Owner | Timing | Adoption signal |
|---|---|---|---|---|
|  |  |  |  |  |

### 4. Rollout Controls
| Gate | Trigger | Decision | Escalation path |
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

- Produce the method-specific outputs for Change Definition, Impact And Readiness, Support Plan; do not substitute a generic framework summary.
- Tie every material score, causal claim, or stakeholder judgment to evidence or label it as an assumption.
- Include at least one disconfirming check, sensitivity, alternative explanation, or failure condition appropriate to the method.
- Convert the result into a named action or decision with an owner or stakeholder, timing, and observable signal.
- State missing inputs and the smallest validation action instead of inventing precision.
- Keep wording professional and plain enough that a smart non-specialist can use the output directly.
