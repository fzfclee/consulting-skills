---
name: evidence-map
description: Use when facts, claims, assumptions, missing evidence, and confidence levels need to be separated before diagnosis. Use when applying an evidence map, evidence ledger, fact-versus-assumption review, proof inventory, or evidence-strength assessment.
license: Apache-2.0
---

# Evidence Map

Use this skill to turn mixed user input into a clear evidence base before making a recommendation.

## Method Notes

- Evidence mapping separates what is known, inferred, assumed, missing, and contradicted.
- It is most useful early in a diagnostic, before strong hypotheses or action plans are formed.
- The goal is not to demand perfect proof; it is to prevent weak evidence from carrying strong conclusions.

## Required Inputs

Collect or infer these inputs before execution:

- decision or diagnostic question
- raw statements, observations, documents, or claims
- source of each statement when available
- current conclusion or proposed action
- decision deadline or consequence if relevant

If an input is missing, mark it as `missing`, state the assumption used, and add a validation action.

## When Not To Use

Do not use when the facts are already clean and the main need is choosing among options. Use `decision-matrix`, `weighted-scorecard`, or `effort-impact-matrix` instead.

## Step-by-Step Execution

| Step | Required input | How to execute | Output |
|---|---|---|---|
| Define the decision question | Decision, objective, current recommendation. | State the question the evidence must support or disprove. | Evidence question. |
| Extract evidence items | Raw notes, claims, observations, artifacts. | Split compound statements into atomic items. Keep one fact or claim per row. | Evidence inventory. |
| Classify item type | Each evidence item, source, timing. | Label each item as fact, direct observation, document, inference, assumption, hearsay, estimate, contradiction, or missing evidence. | Evidence type map. |
| Rate strength and relevance | Source quality, recency, directness, decision linkage. | Rate strength as strong / medium / weak / missing and relevance as high / medium / low. Explain why. | Evidence rating table. |
| Identify evidence gaps | Desired confidence, decision risk, weak or missing rows. | Name the 3-5 gaps most likely to change the conclusion. | Evidence gap list. |
| Convert gaps into tests | Evidence gaps, available access, timeline. | Define the fastest practical way to confirm, disconfirm, or reduce uncertainty. | Validation actions. |

## Output Template

```markdown
### 1. Evidence Question
- Decision / diagnosis to support:
- Current conclusion being tested:
- Decision consequence:

### 2. Evidence Map
| Evidence item | Type | Source | Strength | Relevance | Supports / weakens which claim | Notes |
|---|---|---|---|---|---|---|
|  | fact / observation / document / inference / assumption / hearsay / missing |  | strong / medium / weak / missing | high / medium / low |  |  |

### 3. Evidence Gaps
| Gap | Why it matters | Fastest way to check | Owner / actor | Deadline |
|---|---|---|---|---|
|  |  |  |  |  |

### 4. Confidence Readout
- Strongly supported:
- Plausible but not proven:
- Risky assumption:
- Do not conclude yet:

### 5. Next Diagnostic Move
- Next question or test:
- What result would change the recommendation:
```

## Quality Gate

- Split mixed statements instead of giving one vague evidence grade.
- Do not treat seniority, confidence, repetition, or relationship closeness as proof by itself.
- Separate fact evidence strength from inference confidence.
- Highlight contradictions rather than smoothing them over.
- Keep wording professional and plain enough that a smart non-specialist can use it.
