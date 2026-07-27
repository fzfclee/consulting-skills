---
name: change-event-timeline
description: Use when the timing of events, turning points, stakeholder behavior changes, or cause-and-effect sequence must be clarified. Use when applying a change event timeline, turning-point analysis, event sequence map, or before-after signal review.
license: Apache-2.0
---

# Change Event Timeline

Use this skill to find what changed, when it changed, and which change most likely matters.

## Method Notes

- Many diagnoses fail because they treat all facts as equally current.
- A timeline helps distinguish long-standing background facts from recent trigger events.
- The goal is to identify turning points, causal candidates, and validation questions.

## Required Inputs

Collect or infer these inputs before execution:

- situation or decision question
- key events and dates or approximate sequence
- before-state and after-state
- stakeholders involved in each event
- observed behavior, decision, metric, or risk change

If an input is missing, mark it as `unknown`, state the assumption used, and add a validation action.

## When Not To Use

Do not use when timing is irrelevant or the decision is purely comparative. Use `decision-matrix` or `weighted-scorecard` instead.

## Step-by-Step Execution

| Step | Required input | How to execute | Output |
|---|---|---|---|
| Define the before-state | Baseline relationship, process, metric, or expectation. | Describe the stable pattern before the relevant change. | Baseline state. |
| Build event list | Dates, approximate sequence, stakeholder actions, decisions. | Put events in chronological order; include uncertainty when dates are approximate. | Event timeline. |
| Mark turning points | Event list, behavior or outcome change. | Identify events after which behavior, risk, support, urgency, or outcome changed. | Turning-point candidates. |
| Distinguish trigger vs background | Timeline, evidence strength, alternative explanations. | Separate events that merely existed from events that likely changed the system. | Trigger/background classification. |
| Infer causal hypotheses | Turning points, stakeholder moves, external events. | Generate possible explanations that fit the timeline. | Timeline-based hypotheses. |
| Define next evidence | Weak links, unknown dates, missing stakeholder rationale. | Specify what evidence would confirm or weaken the inferred turning point. | Timeline validation plan. |

## Output Template

```markdown
### 1. Baseline Before The Change
- Before-state:
- Normal pattern:
- What would have continued without disruption:

### 2. Change Event Timeline
| Timing | Event | Stakeholders | Evidence strength | What changed after this? | Trigger / background / unknown |
|---|---|---|---|---|---|
|  |  |  | strong / medium / weak / missing |  |  |

### 3. Likely Turning Points
1.
2.
3.

### 4. Timeline-Based Hypotheses
| Hypothesis | Supporting timeline evidence | What would weaken it | Next check |
|---|---|---|---|
|  |  |  |  |

### 5. Action Implication
- Most important change to respond to:
- What not to over-interpret:
- Next validation:
```

## Quality Gate

- Do not invent exact dates when only sequence is known.
- Separate sequence from causation.
- Identify background conditions that matter but did not trigger the change.
- Highlight missing dates or missing reasons if they change the diagnosis.
- Keep the timeline focused on events that affect the decision.
