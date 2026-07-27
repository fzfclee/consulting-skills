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

## Adjacent Methods

- `hypothesis-tree`: organize competing explanations and disconfirming tests.
- `mece-framework`: audit an existing structure for overlap and coverage.

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
### 1. Core Question
Question:
Decision use:
Scope:
Constraints:

### 2. Issue Tree
| Branch | Sub-issue | Why it matters | MECE note |
|---|---|---|---|
|  |  |  |  |

### 3. Evidence Plan
| Leaf issue | Evidence needed | Source | Owner |
|---|---|---|---|
|  |  |  |  |

### 4. Priority Analysis
| Priority | Issue | Reason | Decision impact |
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

- Produce the method-specific outputs for Core Question, Issue Tree, Evidence Plan; do not substitute a generic framework summary.
- Tie every material score, causal claim, or stakeholder judgment to evidence or label it as an assumption.
- Include at least one disconfirming check, sensitivity, alternative explanation, or failure condition appropriate to the method.
- Convert the result into a named action or decision with an owner or stakeholder, timing, and observable signal.
- State missing inputs and the smallest validation action instead of inventing precision.
- Keep wording professional and plain enough that a smart non-specialist can use the output directly.
