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
- For a single-product constant unit-price/unit-cost model in one period, q >= 0, fixed cost F >= 0, price p and variable cost v give profit(q) = (p - v)q - F. Use consistent units, currency and period. If F > 0 and p - v > 0, break-even q = F / (p - v); for indivisible units, round up for a non-loss volume. If F > 0 and p - v <= 0, no feasible nonnegative quantity breaks even; a negative quantity is not a target.
- If F = 0, q = 0 breaks even in this model; positive quantities break even only when p = v, gain when p > v, and lose when p < v. Revenue, time-to-payback, savings or nonconstant/multi-product models need their own stated formula, assumptions and domain; do not mechanically reuse the unit-volume formula.

## Required Inputs

Collect or infer these inputs before execution:

- fixed costs
- variable costs
- price or benefit per unit
- time horizon
- constraints

If an input is missing, do not block automatically. Mark it as `missing`, state the assumption used, and add a validation action.

## When Not To Use

Do not use when fixed costs, variable costs, unit revenue, and the relevant time horizon cannot be estimated. Break-even analysis tests an economic threshold; it does not establish overall strategic fit.

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
- State the model domain and denominator condition beside the formula/result; report no feasible break-even when appropriate rather than an invalid negative-volume target.
- Keep wording professional and plain enough that a smart non-specialist can use the output directly.
