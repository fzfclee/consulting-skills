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

Do not use for all users at once. Choose one segment, scenario, journey, job, or service context.

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
### 1. Method Frame
- Decision / question:
- Scope:
- Evidence used:
- Key assumptions:

### 2. Working Output
- segmentation logic:
- segment profiles:
- priority segments:
- segment-specific actions:

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
