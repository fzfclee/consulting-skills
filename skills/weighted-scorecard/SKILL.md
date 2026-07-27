---
name: weighted-scorecard
description: Use when a structured evaluation needs more detail than a simple decision matrix, especially for procurement, partner selection, or service qualification. Use when applying the Weighted Scorecard consulting method and when a user asks for Weighted Scorecard, method execution, structured diagnosis, or action planning.
license: Apache-2.0
---

# Weighted Scorecard

Use this skill to run `Weighted Scorecard` as a practical consulting method, not as a generic framework explanation.

## Method Notes

- Use eligibility gates before weighted scoring.
- Add scoring anchors so reviewers score consistently.

## Required Inputs

Collect or infer these inputs before execution:

- evaluation object
- criteria
- weights
- evidence and scoring scale

If an input is missing, do not block automatically. Mark it as `missing`, state the assumption used, and add a validation action.

## When Not To Use

Do not use before options are explicit enough to compare. First convert vague themes into executable options.

## Adjacent Methods

- `decision-matrix`: one-time choice with explicit tradeoffs.
- `rice-scoring`: Reach/Impact/Confidence/Effort backlog.
- `wsjf-prioritization`: delay-cost sequencing.

## Step-by-Step Execution

| Step | Required input | How to execute | Output |
|---|---|---|---|
| Set eligibility gates | Minimum requirements, risk constraints, must-have criteria. | Define pass/fail gates before weighted scoring. | Eligibility gate list. |
| Define dimensions | Evaluation goal, stakeholders, decision criteria. | Choose weighted dimensions and scoring anchors. | Scorecard rubric. |
| Collect evidence | Vendor/option data, interviews, proposals, references. | Attach evidence to each option and criterion. | Evidence pack. |
| Score and normalize | Rubric and evidence pack. | Score every option consistently and calculate weighted totals. | Weighted scorecard. |
| Decide with caveats | Scores, gates, risks, sensitivity. | Recommend winner, reserve option, or further diligence. | Decision and caveats. |

## Output Template

```markdown
### 1. Purpose And Eligibility
Evaluation purpose:
Entities:
Must-pass gates:
Evidence cut-off:

### 2. Dimensions And Anchors
| Dimension | Weight | Scoring anchor | Evidence standard |
|---|---|---|---|
|  |  |  |  |

### 3. Scores
| Entity | Dimension scores | Normalized total | Evidence gaps |
|---|---|---|---|
|  |  |  |  |

### 4. Sensitivity And Governance
Recommendation:
Sensitivity:
Override rule:
Review / approval owner:

### Evidence And Next Decision
- Confirmed facts:
- Assumptions:
- Missing evidence:
- Next action, owner, and timing:
- Expected signal and decision threshold:
```

## Quality Gate

- Produce the method-specific outputs for Purpose And Eligibility, Dimensions And Anchors, Scores; do not substitute a generic framework summary.
- Tie every material score, causal claim, or stakeholder judgment to evidence or label it as an assumption.
- Include at least one disconfirming check, sensitivity, alternative explanation, or failure condition appropriate to the method.
- Convert the result into a named action or decision with an owner or stakeholder, timing, and observable signal.
- State missing inputs and the smallest validation action instead of inventing precision.
- Keep wording professional and plain enough that a smart non-specialist can use the output directly.
