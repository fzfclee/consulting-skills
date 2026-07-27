---
name: systems-thinking
description: Use when a problem involves interacting actors, feedback loops, delays, incentives, constraints, unintended consequences, or repeated patterns over time. Use when applying systems thinking, causal loop analysis, system mapping, leverage point identification, or dynamic complexity diagnosis.
license: Apache-2.0
---

# Systems Thinking

Use this skill to understand how parts of a system interact and why behavior persists over time.

## Method Notes

- Systems thinking focuses on relationships, feedback loops, delays, incentives, and patterns.
- It is useful when direct cause-and-effect explanations are too shallow.
- The goal is to identify leverage points, not to draw a complicated map for its own sake.
- Keep the system boundary explicit so the analysis stays usable.

## Required Inputs

Collect or infer these inputs before execution:

- system or problem boundary
- actors, components, processes, or variables
- repeated pattern or outcome
- incentives, constraints, and feedback signals
- time delays or unintended consequences

If an input is missing, mark it as `missing`, state the assumption used, and add a validation action.

## When Not To Use

Do not use when the issue is a one-off decision with stable criteria. Use `decision-matrix`, `deductive-reasoning`, or `risk-matrix` instead.

## Step-by-Step Execution

| Step | Required input | How to execute | Output |
|---|---|---|---|
| Define system boundary | Problem scope, actors, time horizon. | State what is inside and outside the analysis. | System boundary. |
| Identify key variables | Actors, resources, behaviors, metrics, constraints. | List variables that materially influence the outcome. | Variable list. |
| Map relationships | Variables, evidence. | Show how one variable affects another; mark direction and strength when known. | Relationship map. |
| Identify feedback loops | Relationship map. | Find reinforcing loops, balancing loops, and vicious or virtuous cycles. | Loop diagnosis. |
| Add delays and incentives | Process timing, stakeholder motives. | Mark where effects appear late or incentives drive behavior. | Delay and incentive map. |
| Find leverage points | Loops, constraints, decision rights. | Identify where a small change could shift system behavior. | Leverage point list. |
| Anticipate side effects | Proposed leverage points. | Check likely unintended consequences and monitoring signals. | Intervention caveats. |

## Output Template

```markdown
### 1. System Boundary
- Problem / system:
- In scope:
- Out of scope:
- Time horizon:

### 2. Key Variables
| Variable | Actor / owner | Current behavior | Evidence |
|---|---|---|---|
|  |  |  |  |

### 3. Feedback Loops
| Loop | Type | How it works | Current effect |
|---|---|---|---|
|  | reinforcing / balancing |  |  |

### 4. Leverage Points
| Leverage point | Why it matters | Possible intervention | Risk / side effect | Signal to monitor |
|---|---|---|---|---|
|  |  |  |  |  |
```

## Quality Gate

- Keep the map decision-useful, not exhaustive.
- Do not confuse a long cause list with a system.
- Include feedback, delay, or incentive logic; otherwise use a simpler method.
- State where evidence is weak or inferred.
- Always check unintended consequences.
