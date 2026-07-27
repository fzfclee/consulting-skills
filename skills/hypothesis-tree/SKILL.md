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
### 1. Method Frame
- Decision / question:
- Scope:
- Evidence used:
- Key assumptions:

### 2. Working Output
- hypothesis tree:
- testable branches:
- evidence plan:
- disconfirmation criteria:

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
