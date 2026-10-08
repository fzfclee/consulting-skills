---
name: pricing-strategy-check
description: Use when designing, reviewing, or defending pricing for a product, service, project, or offer. Use when applying the Pricing Strategy Check consulting method and when a user asks for Pricing Strategy Check, method execution, structured diagnosis, or action planning.
license: Apache-2.0
---

# Pricing Strategy Check

Use this skill to run `Pricing Strategy Check` as a practical consulting method, not as a generic framework explanation.

## Method Notes

- Check value metric, package boundary, discount pressure, and proof strength.
- Pricing recommendations must tie to customer value and willingness to pay.

## Required Inputs

Collect or infer these inputs before execution:

- offer description
- target segment
- current or proposed price
- value evidence
- competitors

If an input is missing, do not block automatically. Mark it as `missing`, state the assumption used, and add a validation action.

## When Not To Use

Define the offer and customer segment before analysis. Choose scope: diagnostic / test-design / price recommendation. Missing willingness-to-pay or unit-economic evidence permits a labeled diagnostic and validation plan; it does not establish a validated price or launch endorsement. A price recommendation requires evidence on buyer willingness to pay, value alternatives and relevant economics, with remaining limits stated. A target margin or competitor price is not proof of willingness to pay. A pricing check cannot replace customer research or a legal review.

## Adjacent Methods

- `break-even-analysis`: calculate the economic threshold under a stated price.
- `cost-benefit-analysis`: compare total economic value and downside across options.

## Step-by-Step Execution

| Step | Required input | How to execute | Output |
|---|---|---|---|
| Clarify value and buyer | Segment, buying trigger, outcome value. | State what customer value the price is meant to capture. | Value/buyer frame. |
| Check price metric | Usage, seats, volume, outcome, project scope. | Assess whether the pricing unit matches how value is realized. | Price metric diagnosis. |
| Benchmark alternatives | Competitors, substitutes, status quo cost, switching costs. | Compare price level and packaging against alternatives. | Alternative price view. |
| Assess discount and margin risk | Sales motion, negotiation pattern, cost-to-serve. | Identify where price will leak or create delivery risk. | Pricing risk list. |
| Recommend test or change | Diagnosis, evidence, constraints. | In diagnostic/test-design scope, propose evidence collection and test thresholds. Make an evidence-bounded price/package recommendation only when willingness-to-pay and economics support it; label unresolved assumptions. | Pricing action plan. |

## Output Template

```markdown
### 1. Buyer Value And Price Metric
Analysis scope: diagnostic / test-design / price recommendation
Buyer / segment:
Outcome valued:
Price metric:
Current price structure:

### 2. Alternatives And Willingness
| Alternative | Total buyer cost | Value / gap | Evidence |
|---|---|---|---|
|  |  |  |  |

### 3. Economics And Risk
| Variable | Value / range | Margin effect | Discount risk |
|---|---|---|---|
|  |  |  |  |

### 4. Pricing Action
Recommendation:
Guardrail:
Test:
Success / stop threshold:

### Evidence And Next Decision
- Confirmed facts:
- Assumptions:
- Missing evidence:
- Next action, owner, and timing:
- Expected signal and decision threshold:
```

## Quality Gate

- Produce the method-specific outputs for Buyer Value And Price Metric, Alternatives And Willingness, Economics And Risk; do not substitute a generic framework summary.
- Tie every material score, causal claim, or stakeholder judgment to evidence or label it as an assumption.
- Include at least one disconfirming check, sensitivity, alternative explanation, or failure condition appropriate to the method.
- Convert the result into a named action or decision with an owner or stakeholder, timing, and observable signal.
- State missing inputs and the smallest validation action instead of inventing precision.
- Match conclusions to the selected scope: missing buyer or economic evidence yields a diagnostic/test plan, not a validated price or launch endorsement; keep target margin, competitor benchmarks and demonstrated willingness to pay distinct.
- Keep wording professional and plain enough that a smart non-specialist can use the output directly.
