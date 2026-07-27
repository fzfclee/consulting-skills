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

Do not use before options are explicit enough to compare. First convert vague themes into executable options.

## Step-by-Step Execution

| Step | Required input | How to execute | Output |
|---|---|---|---|
| Clarify value and buyer | Segment, buying trigger, outcome value. | State what customer value the price is meant to capture. | Value/buyer frame. |
| Check price metric | Usage, seats, volume, outcome, project scope. | Assess whether the pricing unit matches how value is realized. | Price metric diagnosis. |
| Benchmark alternatives | Competitors, substitutes, status quo cost, switching costs. | Compare price level and packaging against alternatives. | Alternative price view. |
| Assess discount and margin risk | Sales motion, negotiation pattern, cost-to-serve. | Identify where price will leak or create delivery risk. | Pricing risk list. |
| Recommend test or change | Diagnosis, evidence, constraints. | Recommend price, package, proof, pilot, or negotiation action. | Pricing action plan. |

## Output Template

```markdown
### 1. Method Frame
- Decision / question:
- Scope:
- Evidence used:
- Key assumptions:

### 2. Working Output
- pricing diagnosis:
- value metric fit:
- risk areas:
- pricing actions:

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
