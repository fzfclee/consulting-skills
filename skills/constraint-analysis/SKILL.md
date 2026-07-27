---
name: constraint-analysis
description: Use when progress is limited by bottlenecks, scarce resources, binding constraints, dependencies, policy limits, capacity limits, decision rights, or one factor that controls throughput. Use when applying constraint analysis, bottleneck diagnosis, theory of constraints, limiting-factor review, or constraint removal planning.
license: Apache-2.0
---

# Constraint Analysis

Use this skill to identify the constraint that most limits progress and decide how to address it.

## Method Notes

- A constraint is the factor that most limits the system's ability to reach the goal.
- Many issues are annoyances; only a few are binding constraints.
- The method should distinguish symptoms, bottlenecks, dependencies, policy constraints, resource constraints, and self-imposed constraints.
- Removing a constraint may move the bottleneck elsewhere, so follow-up monitoring matters.

## Required Inputs

Collect or infer these inputs before execution:

- goal or desired throughput
- current process, path, or action sequence
- observed blockage or delay
- resources, capacity, decision rights, dependencies, and policies
- evidence of where work queues, stalls, or fails

If an input is missing, mark it as `missing`, state the assumption used, and add a validation action.

## When Not To Use

Do not use when the issue is mainly unclear preference or option selection. Use `decision-matrix` or `weighted-scorecard` instead.

## Step-by-Step Execution

| Step | Required input | How to execute | Output |
|---|---|---|---|
| Define the goal | Desired outcome, throughput, or progress. | State what the system is trying to achieve. | Goal statement. |
| Map the flow | Process steps, dependencies, owners. | List the sequence from start to desired outcome. | Flow map. |
| Identify stall points | Evidence of delays, queues, rework, rejection, missing approvals. | Mark where progress slows or stops. | Bottleneck candidates. |
| Classify constraints | Resources, capability, policy, market, decision rights, information. | Label each candidate constraint type. | Constraint table. |
| Find the binding constraint | Evidence, impact, dependency logic. | Identify which constraint limits progress most right now. | Binding constraint. |
| Choose response | Constraint type, control boundary. | Decide whether to exploit, elevate, remove, redesign around, or monitor the constraint. | Constraint action. |
| Predict next constraint | Flow map, action. | Anticipate where the bottleneck may move after intervention. | Next-constraint watchlist. |

## Output Template

```markdown
### 1. Goal And Flow
- Goal:
- Current flow:
- Desired throughput / progress:

### 2. Constraint Candidates
| Candidate constraint | Type | Evidence | Impact | Control boundary |
|---|---|---|---|---|
|  | resource / capacity / capability / policy / decision rights / information / market / self-imposed |  | high / medium / low | inside / influence / outside |

### 3. Binding Constraint
- Current binding constraint:
- Why this is the constraint:
- What is only a symptom:

### 4. Response Plan
| Action | Purpose | Owner / actor | Expected signal | Next constraint to watch |
|---|---|---|---|---|
|  | exploit / elevate / remove / redesign / monitor |  |  |  |
```

## Quality Gate

- Do not treat every problem as a constraint.
- Use evidence of throughput, delay, queue, rejection, or dependency to identify the binding constraint.
- Separate what is inside control from what only can be influenced.
- Watch for the next bottleneck after the current one is addressed.
- Avoid solving a non-binding issue just because it is visible.
