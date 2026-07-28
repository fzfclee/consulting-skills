---
name: customer-segmentation
description: Use when treating all customers the same is obscuring priorities, offer design, or service strategy. Use when applying the Customer Segmentation consulting method and when a user asks for Customer Segmentation, method execution, structured diagnosis, or action planning.
license: Apache-2.0
---

# Customer Segmentation

Use this skill to run `Customer Segmentation` as a practical consulting method, not as a generic framework explanation.

## Method Notes

- Segment for a decision, not for taxonomy beauty.
- Use needs, behavior, value, buying context, and service cost.

## Required Inputs

Collect or infer these inputs before execution:

- customer universe
- needs or behaviors
- value data
- usage or buying evidence

If an input is missing, do not block automatically. Mark it as `missing`, state the assumption used, and add a validation action.

## When Not To Use

Do not use without a defined customer population and evidence of differences that change needs, economics, behavior, or treatment. Avoid segments based on convenient demographics that do not change a decision.

## Adjacent Methods

- `jobs-to-be-done`: understand progress and switching forces within a segment.
- `empathy-map`: build an evidence-based snapshot of one segment or actor.

## Step-by-Step Execution

| Step | Required input | How to execute | Output |
|---|---|---|---|
| Define segmentation decision | Business question, offer, service, or GTM decision. | State what the segmentation must help decide. | Segmentation purpose. |
| Choose variables | Needs, behaviors, value, buying context, service cost. | Select dimensions tied to the decision. | Segmentation dimensions. |
| Create segments | Customer data, interviews, usage, purchase patterns. | Group customers with clear inclusion/exclusion rules. | Segment definitions. |
| Profile segments | Segment definitions plus value and needs data. | Describe size, value, pain, channel, willingness to pay, and support needs. | Segment profiles. |
| Prioritize actions | Profiles and strategy constraints. | Choose target, adapt, test, serve differently, or deprioritize. | Segment strategy. |

## Output Template

```markdown
### 1. Segmentation Purpose
Decision to support:
Population:
Available evidence:
Excluded scope:

### 2. Segment Definitions
| Segment | Defining need / behavior | Size / value evidence | Service need | Confidence |
|---|---|---|---|---|
|  |  |  |  |  |

### 3. Segment Profiles
| Segment | Trigger | Desired outcome | Barrier | Best offer / channel |
|---|---|---|---|---|
|  |  |  |  |  |

### 4. Action And Validation
| Segment | Action | Owner | Signal | Re-segmentation trigger |
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

- Produce the method-specific outputs for Segmentation Purpose, Segment Definitions, Segment Profiles; do not substitute a generic framework summary.
- Tie every material score, causal claim, or stakeholder judgment to evidence or label it as an assumption.
- Include at least one disconfirming check, sensitivity, alternative explanation, or failure condition appropriate to the method.
- Convert the result into a named action or decision with an owner or stakeholder, timing, and observable signal.
- State missing inputs and the smallest validation action instead of inventing precision.
- Keep wording professional and plain enough that a smart non-specialist can use the output directly.
