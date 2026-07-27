---
name: effort-impact-matrix
description: Use when there are multiple possible next actions and the user needs quick wins, major projects, fill-ins, or deprioritized items. Use when applying the Effort Impact Matrix consulting method and when a user asks for Effort Impact Matrix, method execution, structured diagnosis, or action planning.
license: Apache-2.0
---

# Effort Impact Matrix

Use this skill to run `Effort Impact Matrix` as a practical consulting method, not as a generic framework explanation.

## Method Notes

- Normalize items so each one is an executable action.
- Use quick wins, major bets, fill-ins, and deprioritize/defer.

## Required Inputs

Collect or infer these inputs before execution:

- candidate actions
- impact estimate
- effort estimate
- time or resource constraints

If an input is missing, do not block automatically. Mark it as `missing`, state the assumption used, and add a validation action.

## When Not To Use

Do not use before options are explicit enough to compare. First convert vague themes into executable options.

## Adjacent Methods

- `rice-scoring`: prioritize a backlog using Reach, Impact, Confidence, and Effort.
- `wsjf-prioritization`: sequence work using Cost of Delay divided by Job Size.
- `decision-matrix`: make a one-time option choice using explicit weighted criteria.

## Step-by-Step Execution

| Step | Required input | How to execute | Output |
|---|---|---|---|
| List actions | Candidate actions or initiatives. | Rewrite broad ideas into one-action items. | Normalized action list. |
| Define scoring anchors | Objective, constraints, available capacity. | Define what high/medium/low impact and effort mean. | Scoring scale. |
| Score each action | Action list, evidence, effort estimates. | Rate impact and effort separately; mark confidence. | Scored action table. |
| Place quadrants | Scored table. | Classify quick wins, major bets, fill-ins, and defer/drop items. | Effort-impact matrix. |
| Choose sequence | Matrix, dependencies, timing, risk. | Recommend first actions, later actions, and items to reject or validate. | Sequenced action plan. |

## Output Template

```markdown
### 1. Scope And Anchors
Decision horizon:
Impact definition:
Effort definition:
Constraints:

### 2. Action Scores
| Action | Impact | Effort | Evidence / assumption | Confidence |
|---|---|---|---|---|
|  |  |  |  |  |

### 3. Quadrant Map
| Quadrant | Actions | Why |
|---|---|---|
|  |  |  |

### 4. Sequence
| Order | Action | Owner | Timing | Expected signal | Stop condition |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

### Evidence And Next Decision
- Confirmed facts:
- Assumptions:
- Missing evidence:
- Next action, owner, and timing:
- Expected signal and decision threshold:
```

## Quality Gate

- Produce the method-specific outputs for Scope And Anchors, Action Scores, Quadrant Map; do not substitute a generic framework summary.
- Tie every material score, causal claim, or stakeholder judgment to evidence or label it as an assumption.
- Include at least one disconfirming check, sensitivity, alternative explanation, or failure condition appropriate to the method.
- Convert the result into a named action or decision with an owner or stakeholder, timing, and observable signal.
- State missing inputs and the smallest validation action instead of inventing precision.
- Keep wording professional and plain enough that a smart non-specialist can use the output directly.
