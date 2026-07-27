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
### 1. Method Frame
- Decision / question:
- Scope:
- Evidence used:
- Key assumptions:

### 2. Working Output
- scorecard:
- ranked results:
- score rationale:
- decision recommendation:

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
