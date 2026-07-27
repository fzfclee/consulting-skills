---
name: go-to-market-diagnosis
description: Use when a product, service, or consulting offer needs market entry, growth, or conversion improvement. Use when applying the Go To Market Diagnosis consulting method and when a user asks for Go To Market Diagnosis, method execution, structured diagnosis, or action planning.
license: Apache-2.0
---

# Go To Market Diagnosis

Use this skill to run `Go To Market Diagnosis` as a practical consulting method, not as a generic framework explanation.

## Method Notes

- Diagnose segment, problem, offer, message, channel, proof, pricing, and sales motion.
- Identify the weakest link before recommending tactics.

## Required Inputs

Collect or infer these inputs before execution:

- target customers
- offer
- channels
- sales process
- conversion or traction evidence

If an input is missing, do not block automatically. Mark it as `missing`, state the assumption used, and add a validation action.

## When Not To Use

Do not use as a sales slogan. Use it to clarify value, buying logic, proof, operating fit, and next commercial action.

## Adjacent Methods

- `competitive-positioning`: focus on the buyer's choice versus alternatives.
- `customer-segmentation`: define distinct customer groups and service logic.
- `business-model-canvas`: test the full value creation and capture model.

## Step-by-Step Execution

| Step | Required input | How to execute | Output |
|---|---|---|---|
| Define GTM goal | Market, segment, offer, growth/conversion goal. | State what GTM outcome is underperforming or planned. | GTM frame. |
| Assess fit chain | Problem, segment, offer, message, channel, proof, price, sales motion. | Evaluate each link for fit and evidence. | GTM fit chain. |
| Find bottleneck | Fit chain and performance evidence. | Identify the weakest link limiting progress. | GTM bottleneck. |
| Design experiments | Bottleneck, constraints, available channels. | Define tests for message, channel, offer, proof, or sales motion. | Experiment backlog. |
| Set operating cadence | Experiments, metrics, owners. | Define next sprint, success signals, and review cadence. | GTM action plan. |

## Output Template

```markdown
### 1. Growth Goal And Evidence
Goal:
Segment:
Offer:
Current funnel evidence:

### 2. Fit Chain
| Element | Current hypothesis | Evidence | Gap |
|---|---|---|---|
|  |  |  |  |

### 3. Binding GTM Bottleneck
Bottleneck:
Why it constrains growth:
Alternative explanation:
Confidence:

### 4. Experiments
| Experiment | Owner | Timing | Cost | Success threshold | Next decision |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

### Evidence And Next Decision
- Confirmed facts:
- Assumptions:
- Missing evidence:
- Next action, owner, and timing:
- Expected signal and decision threshold:
```

## Quality Gate

- Produce the method-specific outputs for Growth Goal And Evidence, Fit Chain, Binding GTM Bottleneck; do not substitute a generic framework summary.
- Tie every material score, causal claim, or stakeholder judgment to evidence or label it as an assumption.
- Include at least one disconfirming check, sensitivity, alternative explanation, or failure condition appropriate to the method.
- Convert the result into a named action or decision with an owner or stakeholder, timing, and observable signal.
- State missing inputs and the smallest validation action instead of inventing precision.
- Keep wording professional and plain enough that a smart non-specialist can use the output directly.
