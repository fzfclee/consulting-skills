---
name: pestel-analysis
description: Use when market, policy, macro, or operating context may materially affect strategy or risk. Use when applying the PESTEL Analysis consulting method and when a user asks for PESTEL Analysis, method execution, structured diagnosis, or action planning.
license: Apache-2.0
---

# PESTEL Analysis

Use this skill to run `PESTEL Analysis` as a practical consulting method, not as a generic framework explanation.

## Method Notes

- Scan Political, Economic, Social, Technological, Environmental, and Legal forces.
- Keep only external forces that can change the decision.

## Required Inputs

Collect or infer these inputs before execution:

- market or situation
- geography
- time horizon
- known external trends

If an input is missing, do not block automatically. Mark it as `missing`, state the assumption used, and add a validation action.

## When Not To Use

Do not use PESTEL to assess internal capability or to collect trends with no decision consequence. Use it for external macro factors that could change a strategic choice, assumption, timing, or risk.

## Adjacent Methods

- `porter-five-forces`: industry structure and profit pressure.
- `competitive-positioning`: buyer-facing choice versus alternatives.

## Step-by-Step Execution

| Step | Required input | How to execute | Output |
|---|---|---|---|
| Set horizon and geography | Market, geography, industry, time horizon. | Define external environment boundary. | PESTEL scope. |
| Scan six categories | Political, Economic, Social, Technological, Environmental, Legal evidence. | List external forces under each category with source or confidence. | PESTEL factor list. |
| Filter material forces | Factor list, decision objective. | Keep only factors that can change opportunity, risk, cost, demand, or feasibility. | Material external forces. |
| Assess impact and timing | Material factors. | Rate direction, magnitude, likelihood, timing, and uncertainty. | Prioritized PESTEL table. |
| Define responses | Prioritized table. | Recommend adaptation, watch items, hedges, or validation needs. | External-context action plan. |

## Output Template

```markdown
### 1. Scope And Horizon
Market / geography:
Decision:
Time horizon:
Source cut-off:

### 2. External Forces
| Category | Force | Evidence / source | Direction | Timing |
|---|---|---|---|---|
|  |  |  |  |  |

### 3. Material Implications
| Force | Impact | Uncertainty | Exposure |
|---|---|---|---|
|  |  |  |  |

### 4. Response And Signposts
| Response | Owner | Leading sign | Revisit trigger |
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

- Produce the method-specific outputs for Scope And Horizon, External Forces, Material Implications; do not substitute a generic framework summary.
- Tie every material score, causal claim, or stakeholder judgment to evidence or label it as an assumption.
- Include at least one disconfirming check, sensitivity, alternative explanation, or failure condition appropriate to the method.
- Convert the result into a named action or decision with an owner or stakeholder, timing, and observable signal.
- State missing inputs and the smallest validation action instead of inventing precision.
- Keep wording professional and plain enough that a smart non-specialist can use the output directly.
