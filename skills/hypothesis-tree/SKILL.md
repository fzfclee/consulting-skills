---
name: hypothesis-tree
description: Use when analysis should proceed by testing likely explanations rather than describing the whole situation. Use when applying the Hypothesis Tree consulting method and when a user asks for Hypothesis Tree, method execution, structured diagnosis, or action planning.
license: Apache-2.0
---

# Hypothesis Tree

Use this skill to run `Hypothesis Tree` as a practical consulting method, not as a generic framework explanation.

## Method Notes

- Each branch must be testable.
- Define disconfirmation evidence, not only supporting evidence.

## Required Inputs

Collect or infer these inputs before execution:

- core question
- candidate explanations
- available evidence
- decision deadline

If an input is missing, do not block automatically. Mark it as `missing`, state the assumption used, and add a validation action.

## When Not To Use

Do not use to decorate an answer. Use it when the problem is too messy to analyze directly.

## Adjacent Methods

- `issue-tree`: decompose the question into analysis branches before proposing explanations.
- `abductive-reasoning`: rank the best current explanation from incomplete evidence.

## Step-by-Step Execution

| Step | Required input | How to execute | Output |
|---|---|---|---|
| Frame hypothesis area | Problem, observed outcome, decision need. | State what explanation or bet needs testing. | Hypothesis frame. |
| Create competing hypotheses | Known facts and plausible causes. | List alternative explanations or strategic bets. | Top-level hypotheses. |
| Break into sub-hypotheses | Top-level hypotheses. | Make each branch testable and specific. | Hypothesis tree. |
| Define tests | Hypothesis tree and available evidence. | Specify supporting evidence and disconfirming evidence for each leaf. | Test plan. |
| Prioritize tests | Test plan, impact, speed, uncertainty. | Choose fastest tests that could change the decision. | Testing sequence. |

## Output Template

```markdown
### 1. Decision Question
Question:
Scope:
Current evidence:
Decision deadline:

### 2. Competing Hypotheses
| Hypothesis | Sub-hypotheses | Evidence for | Evidence against | Confidence |
|---|---|---|---|---|
|  |  |  |  |  |

### 3. Disconfirming Tests
| Hypothesis | Cheapest decisive test | Owner | Timing | Threshold |
|---|---|---|---|---|
|  |  |  |  |  |

### 4. Priority
First hypothesis to test:
Why:
Decision unlocked:

### Evidence And Next Decision
- Confirmed facts:
- Assumptions:
- Missing evidence:
- Next action, owner, and timing:
- Expected signal and decision threshold:
```

## Quality Gate

- Produce the method-specific outputs for Decision Question, Competing Hypotheses, Disconfirming Tests; do not substitute a generic framework summary.
- Tie every material score, causal claim, or stakeholder judgment to evidence or label it as an assumption.
- Include at least one disconfirming check, sensitivity, alternative explanation, or failure condition appropriate to the method.
- Convert the result into a named action or decision with an owner or stakeholder, timing, and observable signal.
- State missing inputs and the smallest validation action instead of inventing precision.
- Keep wording professional and plain enough that a smart non-specialist can use the output directly.
