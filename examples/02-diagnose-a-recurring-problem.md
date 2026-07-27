# Diagnose A Recurring Problem

## Situation

A monthly portfolio review is repeatedly late. Adding reminders and more status meetings improves timeliness for one cycle, then the delay returns.

## Inputs

- six months of review dates and late submissions;
- process steps and owners;
- escalation history;
- incentives, dependencies, capacity limits, and handoffs;
- previous fixes and their duration of effect.

## Selected Methods

| Method | Why it changes the decision | Intermediate output | Effect on next step |
|---|---|---|---|
| `change-event-timeline` | Shows when behavior changed and whether fixes had only temporary effects. | Event, intervention, and outcome timeline. | Identifies repeated patterns and candidate delays. |
| `systems-thinking` | Tests feedback, incentives, and delayed effects rather than assuming a linear cause. | Boundary, variable map, loops, delays, and leverage points. | Reframes the problem from weak reminders to a self-reinforcing late-data cycle. |
| `constraint-analysis` | Determines which bottleneck actually controls throughput. | Flow map and binding constraint. | Focuses action on late source-data approval rather than adding another meeting. |

## Methods Not Used

- Do not use `fishbone-diagram`: the evidence already points to interacting dynamics, not only a broad cause inventory.
- Do not use `pre-mortem`: the problem is active, not a future project being rehearsed.

## Decision Artifact

The binding constraint is source-data approval, reinforced by a cycle in which late data leads to rushed review, rushed review reduces challenge quality, and low challenge quality reduces the perceived value of submitting early. The intervention is an earlier approval gate with a named owner and a leading signal: percentage of source data approved five working days before review.
