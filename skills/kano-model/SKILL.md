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

Do not use for all users at once. Choose one segment, scenario, journey, job, or service context.

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
### 1. Method Frame
- Decision / question:
- Scope:
- Evidence used:
- Key assumptions:

### 2. Working Output
- Kano classification:
- priority implications:
- research gaps:
- feature/service plan:

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
