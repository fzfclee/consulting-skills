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

Do not use to create a large KPI catalog. Use it to connect outcomes, drivers, owners, and decisions.

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
### 1. Method Frame
- Decision / question:
- Scope:
- Evidence used:
- Key assumptions:

### 2. Working Output
- north-star metric:
- input metric tree:
- guardrails:
- measurement caveats:

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
