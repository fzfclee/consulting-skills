---
name: balanced-scorecard
description: Use when performance management needs a broader view than financial or single KPI tracking. Use when applying the Balanced Scorecard consulting method and when a user asks for Balanced Scorecard, method execution, structured diagnosis, or action planning.
license: Apache-2.0
---

# Balanced Scorecard

Use this skill to run `Balanced Scorecard` as a practical consulting method, not as a generic framework explanation.

## Method Notes

- Use financial, customer, internal process, and learning/capability perspectives.
- Limit metrics per perspective so the scorecard stays usable.

## Required Inputs

Collect or infer these inputs before execution:

- strategy or objective
- current metrics
- stakeholders
- time horizon

If an input is missing, do not block automatically. Mark it as `missing`, state the assumption used, and add a validation action.

## When Not To Use

Do not use to create a large KPI catalog. Use it to connect outcomes, drivers, owners, and decisions.

## Adjacent Methods

- `metrics-tree`: decompose one outcome into causal drivers and guardrails.
- `north-star-metric`: define one leading value metric for a product or service.

## Step-by-Step Execution

| Step | Required input | How to execute | Output |
|---|---|---|---|
| Clarify strategy | Strategic objective and business context. | State the strategy the scorecard must translate into measures. | Strategy frame. |
| Set four perspectives | Financial, customer, internal process, learning/capability context. | Define objectives under each perspective. | Perspective objectives. |
| Choose measures | Objectives, data availability, owners. | Select a few measures per perspective with formula and cadence. | Scorecard metrics. |
| Set targets and initiatives | Measures, baseline, ambition, resources. | Define target, owner, initiative, and review rhythm. | Targets and initiatives. |
| Check balance | Scorecard draft. | Remove overload and check whether short-term financial goals crowd out capability and customer measures. | Balanced scorecard. |

## Output Template

```markdown
### 1. Strategy And Scope
Strategy objective:
Time horizon:
Target operating unit:
Key assumptions:

### 2. Four-Perspective Scorecard
| Perspective | Objective | Measure | Baseline | Target | Initiative | Owner |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

### 3. Cause-And-Effect Logic
| Leading objective | Expected effect | Lagging outcome | Evidence strength |
|---|---|---|---|
|  |  |  |  |

### 4. Review Cadence
| Measure | Review frequency | Trigger | Corrective action |
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

- Produce the method-specific outputs for Strategy And Scope, Four-Perspective Scorecard, Cause-And-Effect Logic; do not substitute a generic framework summary.
- Tie every material score, causal claim, or stakeholder judgment to evidence or label it as an assumption.
- Include at least one disconfirming check, sensitivity, alternative explanation, or failure condition appropriate to the method.
- Convert the result into a named action or decision with an owner or stakeholder, timing, and observable signal.
- State missing inputs and the smallest validation action instead of inventing precision.
- Keep wording professional and plain enough that a smart non-specialist can use the output directly.
