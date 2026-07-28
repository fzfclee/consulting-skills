# Recurring Problem: Direct AI Answer vs Method-Skill Chain

> **Example note:** CedarWorks, its portfolio process, metrics, and events were created for this demonstration and do not refer to a specific organization.

This example compares:

1. a direct AI diagnosis with no named method;
2. a three-skill chain using `change-event-timeline`, `systems-thinking`, and `constraint-analysis`.

## Shared Input

```text
CedarWorks runs a monthly portfolio review. The percentage of project updates submitted late
over six months was 34%, 39%, 12%, 31%, 15%, and 36%.

The 12% month followed daily reminders from the PMO. The 15% month followed two extra status
meetings. In both cases, lateness returned the next month.

Project leads prepare forecasts, regional finance partners approve source data, and the PMO
compiles the review pack. Across the six months, 68% of late submissions were waiting for
regional finance approval. The approval queue averages six working days against a two-day
target. Finance partners prioritize quarter-end close work, and no capacity is reserved for
portfolio approval.

When the pack is late, reviewers have less time to challenge assumptions. Recorded challenge
actions are 40% lower in late cycles. Several teams now say early submission creates little
value because the review will be rushed anyway.

What should CedarWorks change before the next two review cycles?
```

## Run A: Direct AI Answer, No Method Skill

**Instruction**

```text
Answer the question directly. Do not use or name any consulting framework or method.
```

**Representative output**

> The recurring delay is more likely a process and capacity problem than a reminder problem. Daily reminders and extra meetings created temporary compliance but did not change the finance approval queue.
>
> CedarWorks should set an earlier approval deadline, assign clear accountability to regional finance, reserve capacity before the review, and escalate items that exceed the two-day target. The PMO should publish a simple dashboard covering pending approvals, age of queue, and on-time submission.
>
> Test the new process for two cycles. Success means a lower approval time, fewer late updates, and enough review time to restore challenge quality.

### What The Direct Answer Does Well

- Identifies finance approval as the likely bottleneck.
- Recognizes that reminders and meetings produced temporary effects.
- Recommends capacity, accountability, escalation, and monitoring.
- Suggests a two-cycle test.

### What The Direct Answer Does Not Preserve

- The exact timing pattern that separates temporary interventions from persistent behavior.
- A closed feedback explanation for why late submission becomes self-reinforcing.
- Evidence that finance approval, rather than PMO compilation or project preparation, is the binding constraint.
- Where the bottleneck may move after approval capacity is improved.

## Run B: Three-Skill Reasoning Chain

### Method Selection

| Sequence | Skill | Why it changes the work | Intermediate output |
|---|---|---|---|
| 1 | [`change-event-timeline`](../skills/change-event-timeline/SKILL.md) | Distinguishes temporary intervention effects from the recurring baseline | Timeline, turning points, and causal checks |
| 2 | [`systems-thinking`](../skills/systems-thinking/SKILL.md) | Explains how delay, review quality, perceived value, and submission behavior reinforce one another | L1 dynamic map, feedback loop, and intervention stress test |
| 3 | [`constraint-analysis`](../skills/constraint-analysis/SKILL.md) | Tests which stall point currently controls throughput | Flow map, binding constraint, and next-constraint watchlist |

### Step 1: Change Event Timeline

| Cycle | Late submissions | Event or intervention | What changed next | Classification |
|---|---:|---|---|---|
| Month 1 | 34% | Normal process | Lateness remained high | Baseline |
| Month 2 | 39% | No structural change | PMO introduced daily reminders | Background |
| Month 3 | 12% | Daily reminders | Lateness returned to 31% | Temporary response |
| Month 4 | 31% | Reminder intensity reduced | Two extra meetings introduced | Return to baseline |
| Month 5 | 15% | Extra status meetings | Lateness returned to 36% | Temporary response |
| Month 6 | 36% | No capacity or policy change | Current problem persists | Return to baseline |

**Timeline hypothesis:** Attention-based interventions temporarily improve project-lead behavior, but the approval queue remains unchanged.

**What would weaken it:** If approval waiting time also fell substantially in months 3 and 5 and still failed to improve timeliness, another constraint may dominate.

**Effect on the next step:** The recurring pattern requires a dynamic explanation, not another reminder cycle.

### Step 2: Systems Thinking

**Level and boundary**

- Analysis level: L1 qualitative intervention stress test.
- In scope: forecast preparation, finance approval, PMO compilation, review quality, and submission behavior.
- Out of scope: project delivery performance itself.
- Horizon: the next three monthly cycles.
- Behavior over time: temporary improvement followed by return to roughly one-third late.

**Decision-relevant relationships**

| From variable | Direction | To variable | Polarity | Delay | Evidence |
|---|---|---|---|---|---|
| Finance approval queue | increases | approval time | + | Immediate | Strong |
| Approval time | increases | late submissions | + | Days | Strong |
| Late submissions | increase | available challenge time | - | Immediate | Strong |
| Available challenge time | increases | review challenge quality | + | Immediate | Medium |
| Review challenge quality | increases | perceived value of early submission | + | One cycle | Medium |
| Perceived value of early submission | increases | early-submission effort | + | One cycle | Assumption |
| Early-submission effort | increases | late submissions | - | One cycle | Assumption |

**Reinforcing loop R1: low-value review cycle**

More late data reduces challenge time; weaker challenge reduces the perceived value of submitting early; lower perceived value reduces early effort; lower effort produces more late data.

**Balancing response B1: management attention**

High lateness triggers reminders or meetings, which temporarily improve submission behavior. The effect fades because approval capacity and incentives do not change.

**Intervention stress test**

| Intervention | Expected effect | Delay | Side effect | Lower-regret adjustment |
|---|---|---|---|---|
| Add more reminders | Short-term reduction in lateness | Immediate | Fatigue; no queue change | Use only for exceptions |
| Reserve finance approval capacity | Lower approval queue and late rate | 1 cycle | Close work may be displaced | Time-box capacity and monitor close-work service level |
| Move deadline earlier | More buffer for PMO | Immediate | Work may simply queue earlier | Pair with reserved approval slots |

**Effect on the next step:** The likely leverage point is approval capacity and priority rules, but constraint analysis must confirm it controls the flow.

### Step 3: Constraint Analysis

**Goal:** At least 90% of portfolio updates approved and ready five working days before the monthly review.

**Flow:** Project forecast prepared -> regional finance approval -> PMO quality check -> pack compilation -> leadership review.

| Candidate constraint | Type | Evidence | Impact | Control boundary |
|---|---|---|---|---|
| Project-lead preparation | Capability / priority | Reminders temporarily improve results | Medium | Influence |
| Regional finance approval | Capacity / policy | 68% of late items wait here; six-day average vs two-day target | High | Inside |
| PMO quality check | Capacity | No queue evidence supplied | Unknown | Inside |
| Leadership review date | Policy | Fixed monthly date | Medium | Inside |

**Binding constraint:** Regional finance approval capacity and priority policy.

**What is only a symptom:** Late PMO compilation and repeated escalation meetings.

**Response**

| Action | Purpose | Owner | Expected signal | Next constraint to watch |
|---|---|---|---|---|
| Reserve two approval blocks in the ten days before review | Elevate approval capacity | Regional finance director | Queue age falls below three days | Project-lead preparation |
| Introduce completeness check before finance submission | Exploit available approval time | Project leads + PMO | Fewer approval returns | PMO quality-check capacity |
| Escalate only items older than three days | Protect attention | PMO lead | Exceptions become visible without daily reminders | Leadership decision latency |

**Effect on the decision:** The intervention changes from another reminder cycle to a controlled capacity-and-priority experiment, with explicit monitoring for the next bottleneck.

## Decision Artifact

**Current decision:** Replace broad reminders and extra meetings with a two-cycle approval-capacity experiment. Keep the existing review date.

| Measure | Baseline | Continue threshold | Adjust or stop threshold | Owner |
|---|---:|---:|---:|---|
| Source data approved by T-5 working days | Missing; establish in cycle 1 | At least 85% in cycle 1 and 90% in cycle 2 | Below 75% after reserved capacity | Finance director |
| Median finance approval time | 6 days | 3 days or less in cycle 1; 2 days in cycle 2 | No reduction after first cycle | Finance operations |
| Late portfolio updates | 36% latest | Below 20% then below 10% | Remains above 25% | PMO lead |
| Review challenge actions | 40% lower in late cycles | Recover to normal-cycle baseline | No recovery despite on-time pack | Portfolio chair |
| Quarter-end close service level | Current baseline | No material deterioration | More than 5% deterioration | CFO delegate |

**Model revision gate:** If approval time falls below two days but lateness remains above 20%, reassess project preparation and PMO quality check as the new binding constraint.

## Comparison

| Deliverable | Direct AI answer | Method-skill chain |
|---|---|---|
| Diagnosis | Approval is probably the bottleneck | Timeline, feedback loop, and binding-constraint evidence |
| Recurrence explanation | Temporary fixes did not last | Explains why the behavior returns |
| Intervention | Reserve capacity and monitor | Capacity experiment plus side-effect guardrail |
| Leading signals | General dashboard | Explicit thresholds by cycle |
| Failure condition | Broad two-cycle test | Model revision gate and next-constraint watchlist |

## What The Comparison Shows

The direct answer identifies the likely operational fix. The method chain adds a defensible explanation for recurrence, prevents another attention-only intervention, and states when the finance-approval diagnosis should be abandoned.
