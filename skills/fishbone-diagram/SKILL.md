---
name: fishbone-diagram
description: Use when a problem may have multiple operational, human, process, system, or environmental causes. Use when applying the Fishbone Diagram consulting method and when a user asks for Fishbone Diagram, method execution, structured diagnosis, or action planning.
license: Apache-2.0
---

# Fishbone Diagram

Use this skill to run `Fishbone Diagram` as a practical consulting method, not as a generic framework explanation.

## Method Notes

- Use categories such as people, process, systems, policy, environment, and measurement.
- Prioritize cause branches for evidence testing.

## Required Inputs

Collect or infer these inputs before execution:

- problem statement
- observed symptoms
- process context
- candidate cause categories

If an input is missing, do not block automatically. Mark it as `missing`, state the assumption used, and add a validation action.

## When Not To Use

Do not use for a single verified linear cause or treat category branches as proven causes. Fishbone analysis is for exploring multiple cause families that still require evidence.

## Adjacent Methods

- `five-whys-root-cause`: follow one selected branch deeper.
- `systems-thinking`: use for feedback and behavior over time.
- `constraint-analysis`: use for a proven binding bottleneck.

## Step-by-Step Execution

| Step | Required input | How to execute | Output |
|---|---|---|---|
| Define effect | Problem statement, defect, service failure, or outcome gap. | Place the problem at the head of the fishbone. | Effect statement. |
| Choose categories | Domain context. | Select people, process, systems, policy, environment, measurement, or custom categories. | Cause categories. |
| Populate causes | Evidence, team input, process facts. | List possible causes under each category. | Fishbone cause map. |
| Mark evidence | Cause map and available data. | Label causes as evidenced, assumed, contradicted, or unknown. | Evidence-coded fishbone. |
| Prioritize tests | Evidence-coded fishbone. | Choose top cause branches and validation tests. | Root-cause test plan. |

## Output Template

```markdown
### 1. Effect And Boundary
Observed effect:
Location / period:
Baseline:
In scope / out of scope:

### 2. Cause Map
| Category | Possible cause | Evidence status | Mechanism |
|---|---|---|---|
|  |  |  |  |

### 3. Priority Causes
| Cause | Impact if true | Testability | Confidence |
|---|---|---|---|
|  |  |  |  |

### 4. Test Plan
| Test | Owner | Timing | Confirming / disconfirming signal |
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

- Produce the method-specific outputs for Effect And Boundary, Cause Map, Priority Causes; do not substitute a generic framework summary.
- Tie every material score, causal claim, or stakeholder judgment to evidence or label it as an assumption.
- Include at least one disconfirming check, sensitivity, alternative explanation, or failure condition appropriate to the method.
- Convert the result into a named action or decision with an owner or stakeholder, timing, and observable signal.
- State missing inputs and the smallest validation action instead of inventing precision.
- Keep wording professional and plain enough that a smart non-specialist can use the output directly.
