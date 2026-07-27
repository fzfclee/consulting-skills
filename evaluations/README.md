# Public Evaluation Contract

## Purpose

The evaluation set checks whether loading a skill improves the quality of a decision artifact compared with a baseline answer that does not load the skill.

It is not intended to prove that one model or one framework is universally superior.

## Test Design

For every case:

1. Run the prompt without loading the named skill.
2. Run the same prompt with the named skill.
3. Remove model and condition labels.
4. Randomize answer order.
5. Score both answers independently.
6. Repeat with the display order reversed.
7. Record ties and evaluator disagreement instead of forcing a winner.

Do not tell the responding model the expected answer, suspected weakness, scoring outcome, or intended comparison.

## Rubric

Score each dimension from 0 to 4:

| Dimension | Question |
|---|---|
| Method fidelity | Did the answer execute the method correctly rather than mention it? |
| Input discipline | Did it identify missing inputs and avoid inventing facts? |
| Evidence discipline | Did it separate facts, assumptions, inferences, and unknowns? |
| Decision usefulness | Did the analysis materially improve the decision or diagnosis? |
| Actionability | Are actions, owners, timing, signals, and decision gates usable? |
| Boundary awareness | Did it state when the method or conclusion is not sufficient? |
| Plain language | Can a business reader understand and use the output? |

## Passing Standard

A skill passes a case when:

- it has no critical evidence or safety failure;
- it scores at least 20 of 28;
- it beats the baseline by at least 3 points or wins both blind pairwise judgments;
- the result remains stable after answer-order reversal.

Repository-level release readiness requires at least 80% of representative cases to pass. Structural validation alone is not behavioral validation.

## Cases

[`representative-cases.yaml`](representative-cases.yaml) contains 24 prompts across 12 representative skills. The file deliberately excludes expected answers.
