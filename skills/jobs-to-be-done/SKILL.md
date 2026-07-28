---
name: jobs-to-be-done
description: Use when product, service, sales, or messaging work needs to understand why someone would switch, buy, adopt, or reject. Use when applying the Jobs To Be Done consulting method and when a user asks for Jobs To Be Done, method execution, structured diagnosis, or action planning.
license: Apache-2.0
---

# Jobs To Be Done

Use this skill to run `Jobs To Be Done` as a practical consulting method, not as a generic framework explanation.

## Method Notes

- Describe progress in a circumstance, not a product category.
- Capture functional, social, and emotional forces plus push, pull, anxiety, and habit.

## Required Inputs

Collect or infer these inputs before execution:

- target customer
- situation
- current workaround
- desired progress
- switching evidence

If an input is missing, do not block automatically. Mark it as `missing`, state the assumption used, and add a validation action.

## When Not To Use

Do not use to translate feature requests directly into a backlog or to infer a job from demographics. Anchor the analysis in a specific struggling moment, desired progress, context, and current alternatives.

## Adjacent Methods

- `empathy-map`: one actor's perceptions and behavior.
- `user-journey-mapping`: chronological user experience.
- `service-blueprint`: frontstage/backstage operating process.

## Step-by-Step Execution

| Step | Required input | How to execute | Output |
|---|---|---|---|
| Define circumstance | Customer situation, trigger, current workaround. | Describe when the customer starts looking for progress. | Job circumstance. |
| Write job statement | Customer goal, struggle, desired progress. | Express the job as progress, not product usage. | Job statement. |
| Map forces | Pushes, pulls, anxieties, habits, alternatives. | Identify forces moving the customer toward or away from change. | Forces-of-progress map. |
| Define success criteria | Functional, social, emotional outcomes. | State what good enough looks like in customer language. | Outcome criteria. |
| Translate to offer | Job, forces, outcomes. | Recommend product, service, message, sales, or validation implications. | JTBD action implications. |

## Output Template

```markdown
### 1. Circumstance And Progress
Target customer:
Triggering situation:
Current workaround:
Progress sought:

### 2. Job Statement
When:
I want to:
So I can:
Evidence:

### 3. Forces And Outcomes
| Push / pull / anxiety / habit | Evidence | Strength | Implication |
|---|---|---|---|
|  |  |  |  |

### 4. Offer And Adoption Tests
| Outcome / barrier | Offer response | Test | Signal |
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

- Produce the method-specific outputs for Circumstance And Progress, Job Statement, Forces And Outcomes; do not substitute a generic framework summary.
- Tie every material score, causal claim, or stakeholder judgment to evidence or label it as an assumption.
- Include at least one disconfirming check, sensitivity, alternative explanation, or failure condition appropriate to the method.
- Convert the result into a named action or decision with an owner or stakeholder, timing, and observable signal.
- State missing inputs and the smallest validation action instead of inventing precision.
- Keep wording professional and plain enough that a smart non-specialist can use the output directly.
