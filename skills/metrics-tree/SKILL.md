---
name: metrics-tree
description: Use when a decision or plan needs measurable success criteria, driver logic, and diagnostic metrics. Use when applying the Metrics Tree consulting method and when a user asks for Metrics Tree, method execution, structured diagnosis, or action planning.
license: Apache-2.0
---

# Metrics Tree

Use this skill to run `Metrics Tree` as a practical consulting method, not as a generic framework explanation.

## Method Notes

- Start with one outcome, then decompose drivers and leading indicators.
- Add guardrails to prevent gaming or local optimization.

## Required Inputs

Collect or infer these inputs before execution:

- north-star outcome
- business model or process
- available data
- owners

If an input is missing, do not block automatically. Mark it as `missing`, state the assumption used, and add a validation action.

## When Not To Use

Do not use to create a large KPI catalog. Use it to connect outcomes, drivers, owners, and decisions.

## Step-by-Step Execution

| Step | Required input | How to execute | Output |
|---|---|---|---|
| Define top outcome | Business/product objective and time window. | Write the outcome metric and why it matters. | Top metric. |
| Decompose drivers | Business model, funnel, process, user behavior. | Break the outcome into mathematical or causal drivers. | Driver tree. |
| Add leading indicators | Driver tree and process timing. | Identify measures that move before the top outcome changes. | Leading indicator set. |
| Add guardrails | Risk, quality, cost, customer experience, fairness constraints. | Choose metrics that prevent gaming. | Guardrail metrics. |
| Define operating use | Owners, data sources, review cadence. | Set formula, owner, threshold, and action trigger. | Metric operating plan. |

## Output Template

```markdown
### 1. Method Frame
- Decision / question:
- Scope:
- Evidence used:
- Key assumptions:

### 2. Working Output
- metrics tree:
- driver definitions:
- guardrail metrics:
- measurement gaps:

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
