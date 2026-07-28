---
name: decision-matrix
description: Use when choosing among options and the decision needs explicit criteria, tradeoffs, and defensible reasoning. Use when applying the Decision Matrix consulting method and when a user asks for Decision Matrix, method execution, structured diagnosis, or action planning.
license: Apache-2.0
---

# Decision Matrix

Use this skill to run `Decision Matrix` as a practical consulting method, not as a generic framework explanation.

## Method Notes

- Define criteria before scoring options.
- Weights should reflect the real decision, not post-hoc preference.

## Required Inputs

Collect or infer these inputs before execution:

- options
- decision criteria
- weights
- evidence for scoring

If an input is missing, do not block automatically. Mark it as `missing`, state the assumption used, and add a validation action.

## When Not To Use

Do not use when there is only one viable option, the decision criteria are not agreed, or mandatory requirements remain unresolved. Apply hard gates before weighted scoring.

## Adjacent Methods

- `weighted-scorecard`: repeatable governance evaluation across comparable entities.
- `rice-scoring`: product or initiative backlog prioritization.
- `wsjf-prioritization`: sequencing by Cost of Delay and Job Size.

## Step-by-Step Execution

| Step | Required input | How to execute | Output |
|---|---|---|---|
| Define decision | Decision statement, options, must-have constraints. | Remove non-viable options before scoring. | Viable option set. |
| Choose criteria | Objectives, stakeholder priorities, risk constraints. | Select criteria that actually decide success. | Criteria list. |
| Weight criteria | Criteria and decision priorities. | Assign weights totaling 100 percent or another explicit scale. | Weighted criteria. |
| Score options | Options, criteria, evidence. | Score each option against each criterion and record rationale. | Completed decision matrix. |
| Recommend and test | Scores and uncertain assumptions. | Pick recommendation, show tradeoffs, and test whether weight changes alter the choice. | Decision recommendation. |

## Output Template

```markdown
### 1. Decision And Eligibility
Decision:
Options:
Must-have gates:
Evidence cut-off date:

### 2. Weighted Criteria
| Criterion | Weight | Scoring anchor | Evidence source |
|---|---|---|---|
|  |  |  |  |

### 3. Option Scores
| Option | Criterion scores | Weighted total | Rationale / evidence |
|---|---|---|---|
|  |  |  |  |

### 4. Sensitivity And Recommendation
Recommendation:
Tradeoff accepted:
Weight / score that changes the result:
Validation action:

### Evidence And Next Decision
- Confirmed facts:
- Assumptions:
- Missing evidence:
- Next action, owner, and timing:
- Expected signal and decision threshold:
```

## Quality Gate

- Produce the method-specific outputs for Decision And Eligibility, Weighted Criteria, Option Scores; do not substitute a generic framework summary.
- Tie every material score, causal claim, or stakeholder judgment to evidence or label it as an assumption.
- Include at least one disconfirming check, sensitivity, alternative explanation, or failure condition appropriate to the method.
- Convert the result into a named action or decision with an owner or stakeholder, timing, and observable signal.
- State missing inputs and the smallest validation action instead of inventing precision.
- Keep wording professional and plain enough that a smart non-specialist can use the output directly.
