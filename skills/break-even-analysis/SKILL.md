---
name: break-even-analysis
description: Use when a commercial, operational, or investment decision needs a threshold for viability. Use when applying the Break Even Analysis consulting method and when a user asks for Break Even Analysis, method execution, structured diagnosis, or action planning.
license: Apache-2.0
---

# Break Even Analysis

Use this skill to run `Break Even Analysis` as a practical consulting method, not as a generic framework explanation.

## Method Notes

- Separate fixed cost, variable cost, unit economics, and time horizon.
- State the exact threshold that makes the option viable.

## Required Inputs

Collect or infer these inputs before execution:

- fixed costs
- variable costs
- price or benefit per unit
- time horizon
- constraints

If an input is missing, do not block automatically. Mark it as `missing`, state the assumption used, and add a validation action.

## When Not To Use

Do not use before options are explicit enough to compare. First convert vague themes into executable options.

## Adjacent Methods

- `cost-benefit-analysis`: compare broader benefits, costs, timing, and risk.
- `pricing-strategy-check`: test price metric, willingness to pay, margin, and discount risk.

## Step-by-Step Execution

| Step | Required input | How to execute | Output |
|---|---|---|---|
| Define break-even unit | Decision, economics, unit of value. | Choose unit, revenue, margin, savings, or time as the threshold. | Break-even definition. |
| Separate cost types | Fixed cost, variable cost, recurring cost, one-off cost. | Classify costs so the formula is clear. | Cost structure. |
| Estimate unit economics | Price, margin, savings, utilization, adoption. | Calculate contribution or benefit per unit. | Unit economics. |
| Calculate threshold | Cost structure and unit economics. | Compute break-even quantity, revenue, savings, or months. | Break-even threshold. |
| Test realism | Market size, capacity, adoption, timeline. | Assess whether reaching the threshold is plausible. | Viability interpretation. |

## Output Template

```markdown
### 1. Decision And Unit
Decision:
Unit of analysis:
Time horizon:
Currency / tax treatment:

### 2. Economics
| Input | Value | Source | Confidence |
|---|---|---|---|
|  |  |  |  |

### 3. Break-Even Result
Contribution margin per unit:
Break-even volume / time:
Formula:
Capacity check:

### 4. Sensitivity And Decision
| Variable change | New threshold | Decision implication | Validation action |
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

- Produce the method-specific outputs for Decision And Unit, Economics, Break-Even Result; do not substitute a generic framework summary.
- Tie every material score, causal claim, or stakeholder judgment to evidence or label it as an assumption.
- Include at least one disconfirming check, sensitivity, alternative explanation, or failure condition appropriate to the method.
- Convert the result into a named action or decision with an owner or stakeholder, timing, and observable signal.
- State missing inputs and the smallest validation action instead of inventing precision.
- Keep wording professional and plain enough that a smart non-specialist can use the output directly.
