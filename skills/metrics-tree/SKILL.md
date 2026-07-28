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

Do not use before the outcome metric and decision purpose are defined, or when proposed driver relationships cannot be tested. A metrics tree explains performance logic; it is not a dashboard inventory.

## Adjacent Methods

- `north-star-metric`: select one leading expression of delivered value.
- `balanced-scorecard`: balance financial, customer, process, and capability objectives.

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
### 1. Outcome Definition
Top outcome:
Population / scope:
Time window:
Unit:

### 2. Driver Tree
| Level | Metric | Formula | Causal rationale | Owner |
|---|---|---|---|---|
|  |  |  |  |  |

### 3. Leading Signals And Guardrails
| Metric | Type | Threshold | Data source | Risk controlled |
|---|---|---|---|---|
|  |  |  |  |  |

### 4. Operating Cadence
| Review | Frequency | Decision triggered | Owner |
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

- Produce the method-specific outputs for Outcome Definition, Driver Tree, Leading Signals And Guardrails; do not substitute a generic framework summary.
- Tie every material score, causal claim, or stakeholder judgment to evidence or label it as an assumption.
- Include at least one disconfirming check, sensitivity, alternative explanation, or failure condition appropriate to the method.
- Convert the result into a named action or decision with an owner or stakeholder, timing, and observable signal.
- State missing inputs and the smallest validation action instead of inventing precision.
- Keep wording professional and plain enough that a smart non-specialist can use the output directly.
