---
name: signal-vs-noise-filter
description: Use when a situation contains many facts, feelings, events, rumors, or weak cues and the real signal must be separated from noise. Use when applying signal detection, signal-versus-noise filtering, pattern relevance review, or decision-signal extraction.
license: Apache-2.0
---

# Signal vs Noise Filter

Use this skill to identify which observations should change the diagnosis or action plan.

## Method Notes

- A signal is information that changes the likely explanation, priority, risk, timing, or next action.
- Noise may be true but not decision-relevant.
- The method works best after an initial evidence map or fact clarification.

## Required Inputs

Collect or infer these inputs before execution:

- decision question or action choice
- list of observations, events, facts, cues, and concerns
- baseline expectation before the event
- timing of key changes
- available evidence strength

If an input is missing, mark it as `missing`, state the assumption used, and add a validation action.

## When Not To Use

Do not use when the problem has too few facts to compare. Use `evidence-map`, `5w1h-analysis`, or direct clarification first.

## Step-by-Step Execution

| Step | Required input | How to execute | Output |
|---|---|---|---|
| State the baseline | Prior expectation, normal pattern, status quo. | Clarify what would have happened if nothing material changed. | Baseline expectation. |
| List candidate signals | Observations, events, user concerns, timing. | Convert each item into a candidate signal. Remove duplicates. | Candidate signal list. |
| Rate decision relevance | Decision question, action options. | Ask whether this item changes explanation, priority, risk, timing, stakeholder stance, or validation need. | Relevance rating. |
| Rate evidence strength | Source, directness, recency, corroboration. | Mark each candidate as strong, medium, weak, or missing. | Evidence-strength rating. |
| Separate noise | Low-relevance or low-evidence items. | Keep true-but-not-actionable items in a noise list so they do not dominate the plan. | Noise list. |
| Name the core signal | High-relevance and sufficiently evidenced items. | Select the 1-3 signals most likely to change action. | Core signal diagnosis. |

## Output Template

```markdown
### 1. Baseline
- What we expected before the change:
- What changed:
- Why this matters:

### 2. Candidate Signal Table
| Candidate signal | Evidence strength | Decision relevance | Changes what? | Signal / noise / watchlist |
|---|---|---|---|---|
|  | strong / medium / weak / missing | high / medium / low | explanation / priority / risk / timing / stakeholder / validation |  |

### 3. Core Signals
1. [Core signal]
2. [Core signal]
3. [Core signal]

### 4. Noise and Watchlist
- Noise to avoid overreacting to:
- Watchlist item that needs more evidence:

### 5. Action Implication
- What the signal means:
- What it does not prove:
- Next validation:
```

## Quality Gate

- A signal must change a decision, not only feel interesting.
- Do not downgrade a real signal because it is politically uncomfortable.
- Do not upgrade a weak cue because it fits the preferred story.
- Name what the signal does not prove.
- Keep the final signal list short enough to guide action.
