---
name: inductive-reasoning
description: Use when patterns, trends, generalizations, or likely rules must be inferred from examples, cases, observations, data points, interviews, events, or repeated signals. Use when applying inductive reasoning, pattern inference, evidence-to-generalization synthesis, or trend interpretation.
license: Apache-2.0
---

# Inductive Reasoning

Use this skill to infer a likely pattern or general rule from observed evidence.

## Method Notes

- Inductive reasoning moves from specific observations to a broader pattern or generalization.
- Inductive conclusions are probabilistic, not certain.
- The method should make sample size, representativeness, exceptions, and confidence visible.
- It is useful for customer research, repeated stakeholder behavior, market signals, operational symptoms, and trend interpretation.

## Required Inputs

Collect or infer these inputs before execution:

- observations, examples, cases, data points, quotes, or events
- source and timing of observations
- population or context being generalized to
- known exceptions
- decision or hypothesis the pattern will inform

If an input is missing, mark it as `missing`, state the assumption used, and add a validation action.

## When Not To Use

Do not use when the conclusion must follow from formal rules or fixed criteria. Use `deductive-reasoning` instead.

## Step-by-Step Execution

| Step | Required input | How to execute | Output |
|---|---|---|---|
| Define the inference question | Decision context, target population. | State what pattern or generalization is being tested. | Inference question. |
| List observations | Cases, data points, quotes, events. | Put each observation in a separate row with source and timing. | Observation table. |
| Cluster patterns | Observation table. | Identify repeated behaviors, causes, needs, outcomes, or signals. | Pattern candidates. |
| Test strength | Sample size, representativeness, consistency. | Rate each pattern by frequency, diversity of support, and evidence quality. | Pattern strength table. |
| Look for exceptions | Known counterexamples, missing segments. | Identify observations that contradict or limit the pattern. | Exception list. |
| State likely generalization | Pattern strength and exceptions. | Write the conclusion with confidence and boundary conditions. | Inductive conclusion. |
| Define validation | Weakest evidence gaps. | Specify what additional evidence would strengthen or weaken the pattern. | Validation plan. |

## Output Template

```markdown
### 1. Inference Question
- What we are trying to infer:
- Population / context:
- Decision use:

### 2. Observation Table
| Observation | Source | Timing | Supports which pattern | Notes |
|---|---|---|---|---|
|  |  |  |  |  |

### 3. Pattern Candidates
| Pattern | Supporting observations | Exceptions | Confidence | Boundary |
|---|---|---|---|---|
|  |  |  | high / medium / low |  |

### 4. Inductive Conclusion
- Likely pattern:
- What it does not prove:
- What would strengthen it:
- What would weaken it:
```

## Quality Gate

- Do not overgeneralize from a thin or biased sample.
- Look for exceptions before writing the conclusion.
- State confidence as probability, not certainty.
- Keep the boundary of the generalization explicit.
- Preserve the link between conclusion and observations.
