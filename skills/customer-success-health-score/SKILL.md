---
name: customer-success-health-score
description: Use when assessing retention risk, expansion potential, account quality, or service intervention priority. Use when applying the Customer Success Health Score consulting method and when a user asks for Customer Success Health Score, method execution, structured diagnosis, or action planning.
license: Apache-2.0
---

# Customer Success Health Score

Use this skill to run `Customer Success Health Score` as a practical consulting method, not as a generic framework explanation.

## Method Notes

- Define healthy before scoring.
- Use adoption, realized value, relationship, support, commercial, and risk signals.

## Required Inputs

Collect or infer these inputs before execution:

- customer or account list
- usage/adoption signals
- value realization evidence
- relationship and support data

If an input is missing, do not block automatically. Mark it as `missing`, state the assumption used, and add a validation action.

## When Not To Use

Do not use for all users at once. Choose one segment, scenario, journey, job, or service context.

## Adjacent Methods

- `metrics-tree`: design causal drivers and guardrails before building a score.
- `user-journey-mapping`: diagnose where experience friction creates the risk signal.

## Step-by-Step Execution

| Step | Required input | How to execute | Output |
|---|---|---|---|
| Define health outcome | Retention, expansion, value realization, satisfaction objective. | State what healthy means for customer and business. | Health definition. |
| Select signal categories | Adoption, value, relationship, support, commercial, risk data. | Choose signals that predict health in this context. | Signal model. |
| Set weights and thresholds | Signal model, historical evidence, expert judgment. | Assign weights, green/yellow/red thresholds, and missing-data rules. | Health scoring rubric. |
| Score accounts | Customer/account data. | Calculate health tier and explain drivers. | Health score table. |
| Assign interventions | Health tier, owner capacity, account value. | Define save, nurture, expand, or monitor actions. | CS intervention plan. |

## Output Template

```markdown
### 1. Health Definition
Desired customer outcome:
Risk event:
Prediction window:
Population:

### 2. Signals And Weights
| Signal | Definition | Source | Weight | Threshold | Lag / leading |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

### 3. Customer Scores
| Customer | Score | Tier | Evidence gap | Primary risk |
|---|---|---|---|---|
|  |  |  |  |  |

### 4. Intervention Rules
| Tier / trigger | Action | Owner | Timing | Recovery signal |
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

- Produce the method-specific outputs for Health Definition, Signals And Weights, Customer Scores; do not substitute a generic framework summary.
- Tie every material score, causal claim, or stakeholder judgment to evidence or label it as an assumption.
- Include at least one disconfirming check, sensitivity, alternative explanation, or failure condition appropriate to the method.
- Convert the result into a named action or decision with an owner or stakeholder, timing, and observable signal.
- State missing inputs and the smallest validation action instead of inventing precision.
- Keep wording professional and plain enough that a smart non-specialist can use the output directly.
