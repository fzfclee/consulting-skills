---
name: abductive-reasoning
description: Use when the best explanation must be inferred from incomplete, ambiguous, or competing evidence. Use when applying abductive reasoning, inference to the best explanation, mystery diagnosis, competing explanation review, or plausible hypothesis selection.
license: Apache-2.0
---

# Abductive Reasoning

Use this skill to choose the most plausible explanation when evidence is incomplete.

## Method Notes

- Abductive reasoning asks: what explanation would best account for the facts we see?
- The output is a ranked explanation, not proof.
- It is useful when stakeholder behavior, market signals, failures, or events can be explained in several ways.
- A good abductive diagnosis names what each explanation explains, what it fails to explain, and what evidence would change the ranking.

## Required Inputs

Collect or infer these inputs before execution:

- surprising fact, event, behavior, or outcome
- known evidence
- candidate explanations
- missing evidence
- decision consequence if the explanation is wrong

If an input is missing, mark it as `missing`, state the assumption used, and add a validation action.

## When Not To Use

Do not use when a formal rule already determines the conclusion. Use `deductive-reasoning` instead. Do not use when the task is broad pattern discovery; use `inductive-reasoning` first.

## Step-by-Step Execution

| Step | Required input | How to execute | Output |
|---|---|---|---|
| State the puzzle | Surprising fact or outcome. | Define what needs explaining. | Explanation question. |
| List evidence | Facts, signals, timing, observations. | Separate strong facts from interpretations and missing evidence. | Evidence list. |
| Generate explanations | Candidate causes, motives, mechanisms. | Create plausible explanations without settling too early. | Explanation candidates. |
| Score explanatory fit | Evidence and candidates. | Rate how well each explanation accounts for the facts, timing, and contradictions. | Fit table. |
| Check parsimony and risk | Candidates, assumptions, downside. | Prefer explanations that require fewer unsupported assumptions, while noting high-risk alternatives. | Plausibility ranking. |
| Identify discriminating evidence | Top explanations. | Define evidence that would clearly separate one explanation from another. | Validation tests. |
| State working explanation | Ranking and confidence. | Choose the best current explanation and action implication. | Working diagnosis. |

## Output Template

```markdown
### 1. Explanation Question
- What needs explaining:
- Why it matters:

### 2. Evidence Base
| Evidence item | Strength | Notes |
|---|---|---|
|  | strong / medium / weak / missing |  |

### 3. Competing Explanations
| Explanation | What it explains well | What it does not explain | Assumptions needed | Plausibility |
|---|---|---|---|---|
|  |  |  |  | high / medium / low |

### 4. Working Diagnosis
- Best current explanation:
- Main alternative:
- Evidence that would change the ranking:
- Next check:
```

## Quality Gate

- Do not present the best explanation as proven.
- Include at least one serious alternative explanation.
- Look for evidence that discriminates between explanations, not only more confirming evidence.
- Avoid overly complex explanations when a simpler one fits the evidence.
- Name the risk if the working explanation is wrong.
