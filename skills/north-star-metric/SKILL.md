---
name: north-star-metric
description: Use when a product, service, or business needs one organizing success metric plus supporting driver logic. Use when applying the North Star Metric consulting method and when a user asks for North Star Metric, method execution, structured diagnosis, or action planning.
license: Apache-2.0
---

# North Star Metric

Use this skill to run `North Star Metric` as a practical consulting method, not as a generic framework explanation.

## Method Notes

- The metric should reflect recurring customer value and be a leading indicator of growth.
- Add input metrics and guardrail metrics.

## Required Inputs

Collect or infer these inputs before execution:

- business model
- user value proposition
- growth goal
- available metrics

If an input is missing, do not block automatically. Mark it as `missing`, state the assumption used, and add a validation action.

## When Not To Use

Do not use when customer value, product scope, or strategic objective is unclear, or when one metric would hide harm across segments. Pair the north star with explicit guardrails.

## Adjacent Methods

- `metrics-tree`: connect an outcome to input drivers and guardrails.
- `balanced-scorecard`: manage several strategic perspectives rather than one value metric.

## Step-by-Step Execution

| Step | Required input | How to execute | Output |
|---|---|---|---|
| Define core value | Product/service value proposition and user segment. | State the recurring customer value the product should create. | Core value statement. |
| Propose NSM | Core value, growth model, retention logic. | Choose one metric that captures delivered value and predicts growth. | North Star metric candidate. |
| Map input metrics | User behaviors and business drivers. | Identify measurable behaviors that drive the NSM. | Input metric tree. |
| Add guardrails | Quality, margin, risk, user trust, support burden. | Define counter-metrics that prevent gaming or regression. | Guardrail set. |
| Validate usability | Data availability, team ownership, actionability. | Check whether teams can influence and review the metric. | NSM operating plan. |

## Output Template

```markdown
### 1. Core Value
User:
Value event:
Frequency:
Business linkage:

### 2. North-Star Candidate
Metric:
Formula:
Why it reflects value:
Manipulation risk:

### 3. Input Metrics And Guardrails
| Metric | Type | Mechanism | Owner | Threshold |
|---|---|---|---|---|
|  |  |  |  |  |

### 4. Operating Plan
| Review | Cadence | Decision | Validation / revision trigger |
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

- Produce the method-specific outputs for Core Value, North-Star Candidate, Input Metrics And Guardrails; do not substitute a generic framework summary.
- Tie every material score, causal claim, or stakeholder judgment to evidence or label it as an assumption.
- Include at least one disconfirming check, sensitivity, alternative explanation, or failure condition appropriate to the method.
- Convert the result into a named action or decision with an owner or stakeholder, timing, and observable signal.
- State missing inputs and the smallest validation action instead of inventing precision.
- Keep wording professional and plain enough that a smart non-specialist can use the output directly.
