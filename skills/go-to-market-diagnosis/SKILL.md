---
name: go-to-market-diagnosis
description: Use when a product, service, or consulting offer needs market entry, growth, or conversion improvement. Use when applying the Go To Market Diagnosis consulting method and when a user asks for Go To Market Diagnosis, method execution, structured diagnosis, or action planning.
license: Apache-2.0
---

# Go To Market Diagnosis

Use this skill to run `Go To Market Diagnosis` as a practical consulting method, not as a generic framework explanation.

## Method Notes

- Diagnose segment, problem, offer, message, channel, proof, pricing, and sales motion.
- Identify the weakest link before recommending tactics.

## Required Inputs

Collect or infer these inputs before execution:

- target customers
- offer
- channels
- sales process
- conversion or traction evidence

If an input is missing, do not block automatically. Mark it as `missing`, state the assumption used, and add a validation action.

## When Not To Use

Do not use as a sales slogan. Use it to clarify value, buying logic, proof, operating fit, and next commercial action.

## Step-by-Step Execution

| Step | Required input | How to execute | Output |
|---|---|---|---|
| Define GTM goal | Market, segment, offer, growth/conversion goal. | State what GTM outcome is underperforming or planned. | GTM frame. |
| Assess fit chain | Problem, segment, offer, message, channel, proof, price, sales motion. | Evaluate each link for fit and evidence. | GTM fit chain. |
| Find bottleneck | Fit chain and performance evidence. | Identify the weakest link limiting progress. | GTM bottleneck. |
| Design experiments | Bottleneck, constraints, available channels. | Define tests for message, channel, offer, proof, or sales motion. | Experiment backlog. |
| Set operating cadence | Experiments, metrics, owners. | Define next sprint, success signals, and review cadence. | GTM action plan. |

## Output Template

```markdown
### 1. Method Frame
- Decision / question:
- Scope:
- Evidence used:
- Key assumptions:

### 2. Working Output
- GTM diagnosis:
- fit gaps:
- priority experiments:
- execution actions:

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
