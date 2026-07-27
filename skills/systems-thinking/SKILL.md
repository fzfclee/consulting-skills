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
- time horizon and behavior-over-time pattern
- time delays or unintended consequences
- evidence for relationship direction, loop logic, and expected trend

If an input is missing, mark it as `missing`, state the assumption used, and add a validation action.

## When Not To Use

Do not use when the issue is a one-off decision with stable criteria. Use `decision-matrix`, `deductive-reasoning`, or `risk-matrix` instead.

## Adjacent Methods

- `five-whys-root-cause`: one linear cause chain.
- `fishbone-diagram`: several operational cause categories.
- `constraint-analysis`: one binding bottleneck.

## Step-by-Step Execution

| Step | Required input | How to execute | Output |
|---|---|---|---|
| Select level and boundary | Decision need, scope, time horizon, available evidence. | Choose L0 for a qualitative dynamic map or L1 when a proposed intervention must be stress-tested. State what is inside, outside, and not modeled. | Level statement and system boundary. |
| Describe behavior over time | Outcome history, trend, recurring episodes, baseline. | Describe the pattern before explaining it: growth, decline, oscillation, plateau, overshoot, or repeated return. Mark missing time-series evidence. | Behavior-over-time pattern. |
| Identify key variables | Actors, resources, decisions, behaviors, metrics, constraints. | Keep only variables that can materially change the outcome within the chosen horizon. Mark owner and evidence strength. | Decision-relevant variable list. |
| Map directional relationships | Variables, observations, causal evidence. | For each link, state whether the source increases or decreases the target, assign positive, negative, or unknown polarity, and mark delay and evidence. | Signed relationship map. |
| Close feedback loops | Signed relationships. | Trace closed paths. Label reinforcing loops that amplify change and balancing loops that counter it. Do not call an open chain a loop. | Named R/B loops and dominant conditions. |
| Add delays, incentives, and constraints | Process timing, rules, rewards, decision rights. | Show where response is delayed, which incentives create behavior, and which constraints limit adjustment. | Dynamic mechanism diagnosis. |
| Identify leverage points | Loops, constraints, control rights, intervention options. | Find changes that alter information, incentives, rules, capacity, delay, or decision rights. Rate controllability and evidence. | Ranked leverage points. |
| Stress-test intervention | Proposed action, loops, delay, affected actors. | Predict direction over time, lag, compensating response, side effects, and problem displacement. Define a lower-regret version. | L1 intervention stress test. |
| Define learning loop | Expected trend, leading indicators, review cadence. | Set signals, thresholds, owner, review date, and the assumption that must be revised if the pattern differs. | Monitoring and model-revision plan. |

## Output Template

```markdown
### 1. Level, Boundary, And Time
- Analysis level: L0 qualitative dynamic map / L1 decision stress test
- Problem / system:
- In scope:
- Out of scope:
- Time horizon:
- Behavior-over-time pattern:

### 2. Variables And Relationships
| From variable | Direction | To variable | Polarity (+/-/unknown) | Delay | Evidence / assumption |
|---|---|---|---|---|---|
|  | increases / decreases |  |  |  |  |

### 3. Feedback Loops
| Loop | Type | Mechanism | Dominant when | Evidence strength |
|---|---|---|---|---|
|  | reinforcing / balancing |  |  |  |

### 4. Incentives, Constraints, And Leverage
| Actor / rule | Incentive or constraint | Behavior created | Leverage point | Control owner |
|---|---|---|---|---|
|  |  |  |  |  |

### 5. Intervention Stress Test
| Intervention | Expected direction over time | Delay | Side effect / displacement | Low-regret adjustment |
|---|---|---|---|---|
|  |  |  |  |  |

### 6. Leading Signals And Model Revision
| Signal | Expected trend | Review date | Continue / adjust / stop threshold | Model assumption revised if |
|---|---|---|---|---|
|  |  |  |  |  |
```

## Quality Gate

- State whether the output is L0 or L1; never imply L2 simulation, calibrated forecasting, or quantitative stock-and-flow modeling.
- Define the system boundary, excluded scope, time horizon, and behavior-over-time pattern.
- Give each material relationship a direction and polarity; mark unknown polarity rather than inventing it.
- Include at least one reinforcing or balancing loop only when the loop closes; a long cause list is not a system map.
- Mark delays, incentives, constraints, evidence strength, and assumptions.
- Stress-test at least one intervention for side effects, problem displacement, and delayed response.
- Define leading signals, expected trend, decision threshold, and when the model should be revised.
- Use a simpler root-cause, constraint, or decision method when dynamic complexity is absent.
