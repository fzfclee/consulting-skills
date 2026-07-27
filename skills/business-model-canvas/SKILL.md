---
name: business-model-canvas
description: Use when clarifying how a business, product, offer, or venture creates, delivers, and captures value. Use when applying the Business Model Canvas consulting method and when a user asks for Business Model Canvas, method execution, structured diagnosis, or action planning.
license: Apache-2.0
---

# Business Model Canvas

Use this skill to run `Business Model Canvas` as a practical consulting method, not as a generic framework explanation.

## Method Notes

- Cover the nine BMC blocks: customer segments, value propositions, channels, relationships, revenue, resources, activities, partners, and costs.
- Check alignment across value proposition, channel, revenue, and cost logic.

## Required Inputs

Collect or infer these inputs before execution:

- business or offer
- customer segments
- value proposition
- operating model

If an input is missing, do not block automatically. Mark it as `missing`, state the assumption used, and add a validation action.

## When Not To Use

Do not use as a sales slogan. Use it to clarify value, buying logic, proof, operating fit, and next commercial action.

## Adjacent Methods

- `pricing-strategy-check`: focus on price architecture and value capture.
- `go-to-market-diagnosis`: diagnose segment, offer, channel, message, and sales-motion fit.

## Step-by-Step Execution

| Step | Required input | How to execute | Output |
|---|---|---|---|
| Define model scope | Company/product/service/offer and time horizon. | Choose the business model unit being described. | Canvas scope. |
| Fill customer/value blocks | Customer segments, jobs/pains/gains, value proposition. | Define who is served and what value is promised. | Customer/value blocks. |
| Fill delivery/revenue blocks | Channels, customer relationships, revenue streams. | Describe how value reaches customers and how money is made. | Delivery/revenue blocks. |
| Fill operating/cost blocks | Key activities, resources, partners, cost structure. | Describe what must exist to deliver the model. | Operating/cost blocks. |
| Test alignment | All nine blocks. | Check contradictions, weak assumptions, and missing proof. | Model risks and test plan. |

## Output Template

```markdown
### 1. Scope And Customer
Business / offer:
Target segment:
Customer problem / job:
Evidence:

### 2. Value And Delivery
| Block | Current design | Evidence | Risk / contradiction |
|---|---|---|---|
|  |  |  |  |

### 3. Economics
| Revenue source | Price logic | Cost driver | Key assumption | Test |
|---|---|---|---|---|
|  |  |  |  |  |

### 4. Priority Tests
| Hypothesis | Minimum test | Owner | Timing | Pass / fail threshold |
|---|---|---|---|---|
|  |  |  |  |  |

### Evidence And Next Decision
- Confirmed facts:
- Assumptions:
- Missing evidence:
- Next action, owner, and timing:
- Expected signal and decision threshold:
```

## Quality Gate

- Produce the method-specific outputs for Scope And Customer, Value And Delivery, Economics; do not substitute a generic framework summary.
- Tie every material score, causal claim, or stakeholder judgment to evidence or label it as an assumption.
- Include at least one disconfirming check, sensitivity, alternative explanation, or failure condition appropriate to the method.
- Convert the result into a named action or decision with an owner or stakeholder, timing, and observable signal.
- State missing inputs and the smallest validation action instead of inventing precision.
- Keep wording professional and plain enough that a smart non-specialist can use the output directly.
