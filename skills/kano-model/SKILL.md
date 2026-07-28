---
name: kano-model
description: Use when deciding which customer needs or service features drive satisfaction, dissatisfaction, or differentiation. Use when applying the Kano Model consulting method and when a user asks for Kano Model, method execution, structured diagnosis, or action planning.
license: Apache-2.0
---

# Kano Model

Use this skill to run `Kano Model` as a practical consulting method, not as a generic framework explanation.

## Method Notes

- Classify features as must-be, performance, delighter, indifferent, or reverse.
- Kano categories shift over time; mark evidence age.

## Required Inputs

Collect or infer these inputs before execution:

- features or service attributes
- customer segment
- satisfaction evidence
- dissatisfaction evidence

If an input is missing, do not block automatically. Mark it as `missing`, state the assumption used, and add a validation action.

## When Not To Use

Do not use without a defined customer context and evidence of how feature presence and absence affect satisfaction. Kano classification alone does not set roadmap priority, cost, or sequence.

## Adjacent Methods

- `jobs-to-be-done`: understand the progress the customer is trying to make.
- `user-journey-mapping`: locate attributes and pain points across a chronological experience.

## Step-by-Step Execution

| Step | Required input | How to execute | Output |
|---|---|---|---|
| Define feature set | Features/service attributes and target segment. | List attributes in customer language. | Kano item list. |
| Collect satisfaction evidence | Survey/interview/VOC data for presence and absence of each item. | Capture how customers react if the attribute exists or is missing. | Functional/dysfunctional response data. |
| Classify categories | Response data. | Classify must-be, performance, delighter, indifferent, or reverse. | Kano classification. |
| Interpret investment | Categories, segment, maturity, cost. | Decide baseline requirements, performance investments, and differentiating delighters. | Feature priority implications. |
| Refresh assumptions | Evidence age and market expectations. | Mark which classifications need revalidation over time. | Kano review plan. |

## Output Template

```markdown
### 1. Scope And Evidence
Customer segment:
Decision:
Attributes tested:
Research basis:

### 2. Classification
| Attribute | Functional response | Dysfunctional response | Kano class | Confidence |
|---|---|---|---|---|
|  |  |  |  |  |

### 3. Investment Logic
| Attribute | Current performance | Priority | Reason |
|---|---|---|---|
|  |  |  |  |

### 4. Refresh Plan
| Assumption | Validation | Owner | Timing | Reclassification trigger |
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

- Produce the method-specific outputs for Scope And Evidence, Classification, Investment Logic; do not substitute a generic framework summary.
- Tie every material score, causal claim, or stakeholder judgment to evidence or label it as an assumption.
- Include at least one disconfirming check, sensitivity, alternative explanation, or failure condition appropriate to the method.
- Convert the result into a named action or decision with an owner or stakeholder, timing, and observable signal.
- State missing inputs and the smallest validation action instead of inventing precision.
- Keep wording professional and plain enough that a smart non-specialist can use the output directly.
