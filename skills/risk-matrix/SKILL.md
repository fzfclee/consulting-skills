---
name: risk-matrix
description: Use when a plan, deal, project, or stakeholder move has material downside that needs explicit controls. Use when applying the Risk Matrix consulting method and when a user asks for Risk Matrix, method execution, structured diagnosis, or action planning.
license: Apache-2.0
---

# Risk Matrix

Use this skill to run `Risk Matrix` as a practical consulting method, not as a generic framework explanation.

## Method Notes

- Define risk as event + cause + consequence.
- Score likelihood, impact, and optional detectability, then assign owner and trigger.

## Required Inputs

Collect or infer these inputs before execution:

- planned action or project
- risk list
- impact definitions
- owners

If an input is missing, do not block automatically. Mark it as `missing`, state the assumption used, and add a validation action.

## When Not To Use

Do not use as a fear list. Each risk or force must have a trigger, owner, and response.

## Adjacent Methods

- `pre-mortem`: surface failure modes before a defined plan starts.
- `scenario-planning`: test strategy across uncertain external futures.

## Step-by-Step Execution

| Step | Required input | How to execute | Output |
|---|---|---|---|
| Define objective | Plan/project/decision and success criteria. | State what outcome risks threaten. | Risk scope. |
| List risks | Assumptions, dependencies, history, stakeholder input. | Write each risk as event + cause + consequence. | Risk register. |
| Score risks | Likelihood, impact, detectability/evidence. | Rate each risk using consistent anchors. | Risk matrix. |
| Plan responses | Top risks and constraints. | Assign mitigation, contingency, owner, and trigger. | Risk response plan. |
| Set monitoring | Triggers, cadence, governance. | Define review rhythm and escalation threshold. | Risk monitoring plan. |

## Output Template

```markdown
### 1. Scope And Scales
Decision / plan:
Horizon:
Likelihood scale:
Impact scale:

### 2. Risk Register
| Risk event | Cause | Consequence | Likelihood | Impact | Evidence |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

### 3. Response
| Priority risk | Prevent / reduce / transfer / accept | Owner | Due |
|---|---|---|---|
|  |  |  |  |

### 4. Monitoring
| Risk | Leading signal | Threshold | Contingency |
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

- Produce the method-specific outputs for Scope And Scales, Risk Register, Response; do not substitute a generic framework summary.
- Tie every material score, causal claim, or stakeholder judgment to evidence or label it as an assumption.
- Include at least one disconfirming check, sensitivity, alternative explanation, or failure condition appropriate to the method.
- Convert the result into a named action or decision with an owner or stakeholder, timing, and observable signal.
- State missing inputs and the smallest validation action instead of inventing precision.
- Keep wording professional and plain enough that a smart non-specialist can use the output directly.
