---
name: cost-benefit-analysis
description: Use when deciding whether an action is worth the resources, attention, or tradeoffs required. Use when applying the Cost Benefit Analysis consulting method and when a user asks for Cost Benefit Analysis, method execution, structured diagnosis, or action planning.
license: Apache-2.0
---

# Cost Benefit Analysis

Use this skill to run `Cost Benefit Analysis` as a practical consulting method, not as a generic framework explanation.

## Method Notes

- Compare against a clear baseline.
- Include timing, confidence, opportunity cost, and downside case.

## Required Inputs

Collect or infer these inputs before execution:

- option or investment
- benefit estimates
- cost estimates
- time horizon
- risk assumptions

If an input is missing, do not block automatically. Mark it as `missing`, state the assumption used, and add a validation action.

## When Not To Use

Do not use before options are explicit enough to compare. First convert vague themes into executable options.

## Adjacent Methods

- `break-even-analysis`: calculate the threshold volume, price, or time.
- `decision-matrix`: compare options across non-financial criteria as well as economics.

## Step-by-Step Execution

| Step | Required input | How to execute | Output |
|---|---|---|---|
| Define baseline | Current state, proposed option, time horizon. | State what the option is compared against. | Baseline and option definition. |
| Estimate benefits | Revenue, savings, risk reduction, learning, strategic value. | List benefits by type, owner, timing, and confidence. | Benefit estimate table. |
| Estimate costs | Fixed cost, variable cost, time, coordination, opportunity cost. | List costs and timing, including hidden effort. | Cost estimate table. |
| Compare scenarios | Benefits, costs, assumptions. | Calculate or reason through base, upside, and downside cases. | Scenario comparison. |
| Recommend threshold | Scenario comparison and constraints. | Recommend go/no-go/test-first and assumptions to validate. | Cost-benefit recommendation. |

## Output Template

```markdown
### 1. Decision Baseline
Decision:
Baseline / do-nothing case:
Time horizon:
Discount / timing assumption:

### 2. Benefits And Costs
| Item | Type | Amount / range | Timing | Evidence | Confidence |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

### 3. Scenarios
| Scenario | Net value | Key assumption | Downside |
|---|---|---|---|
|  |  |  |  |

### 4. Recommendation And Threshold
Recommendation:
Break condition:
Owner:
Validation action:

### Evidence And Next Decision
- Confirmed facts:
- Assumptions:
- Missing evidence:
- Next action, owner, and timing:
- Expected signal and decision threshold:
```

## Quality Gate

- Produce the method-specific outputs for Decision Baseline, Benefits And Costs, Scenarios; do not substitute a generic framework summary.
- Tie every material score, causal claim, or stakeholder judgment to evidence or label it as an assumption.
- Include at least one disconfirming check, sensitivity, alternative explanation, or failure condition appropriate to the method.
- Convert the result into a named action or decision with an owner or stakeholder, timing, and observable signal.
- State missing inputs and the smallest validation action instead of inventing precision.
- Keep wording professional and plain enough that a smart non-specialist can use the output directly.
