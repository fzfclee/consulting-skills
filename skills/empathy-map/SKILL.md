---
name: empathy-map
description: Use when stakeholder motivation is unclear and the work requires a grounded, human view before messaging or intervention design. Use when applying the Empathy Map consulting method and when a user asks for Empathy Map, method execution, structured diagnosis, or action planning.
license: Apache-2.0
---

# Empathy Map

Use this skill to run `Empathy Map` as a practical consulting method, not as a generic framework explanation.

## Method Notes

- Use Says, Thinks, Does, Feels; optionally add pains, gains, pressures, and trust signals.
- Never put guesses into Says or Does.

## Required Inputs

Collect or infer these inputs before execution:

- target person or segment
- observed behavior
- quotes or facts
- uncertain assumptions

If an input is missing, do not block automatically. Mark it as `missing`, state the assumption used, and add a validation action.

## When Not To Use

Do not use as a personality-reading exercise. Use it only to clarify decision rights, influence, needs, and next engagement moves.

## Adjacent Methods

- `jobs-to-be-done`: customer progress and switching forces.
- `user-journey-mapping`: chronological experience across stages.
- `service-blueprint`: service operations and handoffs.

## Step-by-Step Execution

| Step | Required input | How to execute | Output |
|---|---|---|---|
| Choose target | One user, persona, buyer, stakeholder, or segment. | State the person/context and the decision the map should support. | Empathy-map scope. |
| Collect evidence | Quotes, observed behavior, meeting notes, interview notes, usage data. | Separate direct evidence from interpretation before filling quadrants. | Evidence list. |
| Fill quadrants | Evidence list. | Map Says, Thinks, Does, and Feels; optionally add pains, gains, pressures, and trust signals. | Empathy map. |
| Identify patterns | Completed map. | Find contradictions, repeated concerns, hidden anxieties, and unmet needs. | Need and concern diagnosis. |
| Translate to action | Diagnosis, message goal, product/service/action options. | Define message, question, offer, service change, or validation step. | Action implications. |

## Output Template

```markdown
### 1. Actor And Evidence
Actor / segment:
Situation:
Decision to inform:
Evidence sources:

### 2. Observed And Inferred Map
| Dimension | Observation | Fact / inference | Evidence | Confidence |
|---|---|---|---|---|
|  |  |  |  |  |

### 3. Needs And Tensions
| Need / fear | Supporting evidence | Implication |
|---|---|---|
|  |  |  |

### 4. Actionable Test
| Hypothesis | Conversation / observation | Owner | Signal |
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

- Produce the method-specific outputs for Actor And Evidence, Observed And Inferred Map, Needs And Tensions; do not substitute a generic framework summary.
- Tie every material score, causal claim, or stakeholder judgment to evidence or label it as an assumption.
- Include at least one disconfirming check, sensitivity, alternative explanation, or failure condition appropriate to the method.
- Convert the result into a named action or decision with an owner or stakeholder, timing, and observable signal.
- State missing inputs and the smallest validation action instead of inventing precision.
- Keep wording professional and plain enough that a smart non-specialist can use the output directly.
