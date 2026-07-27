---
name: issue-tree
description: Use when the problem is broad, ambiguous, or mixing symptoms, causes, decisions, and actions. Use when applying the Issue Tree consulting method and when a user asks for Issue Tree, method execution, structured diagnosis, or action planning.
license: Apache-2.0
---

# Issue Tree

Use this skill to run `Issue Tree` as a practical consulting method, not as a generic framework explanation.

## Method Notes

- Start with one decision-relevant question.
- Branches should be collectively sufficient and minimally overlapping.

## Required Inputs

Collect or infer these inputs before execution:

- core question
- known constraints
- decision deadline
- available evidence

If an input is missing, do not block automatically. Mark it as `missing`, state the assumption used, and add a validation action.

## When Not To Use

Do not use to decorate an answer. Use it when the problem is too messy to analyze directly.

## Step-by-Step Execution

| Step | Required input | How to execute | Output |
|---|---|---|---|
| Define core question | Decision/problem, scope, deadline. | Write one question the analysis must answer. | Core issue. |
| Split first level | Core issue and known context. | Create major branches that cover the answer space. | First-level issue tree. |
| Decompose branches | First-level branches. | Break each branch into answerable sub-questions. | Detailed issue tree. |
| Attach evidence needs | Detailed tree. | For each leaf, define data/evidence needed and current status. | Evidence plan. |
| Prioritize analysis | Evidence plan and decision impact. | Pick the branches most likely to change the recommendation. | Analysis sequence. |

## Output Template

```markdown
### 1. Method Frame
- Decision / question:
- Scope:
- Evidence used:
- Key assumptions:

### 2. Working Output
- issue tree:
- priority branches:
- analysis questions:
- evidence plan:

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
