# Product Prioritization: Direct AI Answer vs Method-Skill Chain

> **Example note:** LumenDesk, its products, customers, estimates, and financial figures were created for this demonstration and do not refer to a specific organization.

This example compares:

1. a direct AI recommendation with no named method;
2. a two-skill chain using `decision-matrix` and `risk-matrix`.

## Shared Input

```text
LumenDesk has 14 person-months of product capacity for the next quarter and must choose two
investments:

Option A: Reliability and observability. Requires 6 person-months. It addresses 120 monthly
sync incidents and is expected to reduce them by 40%, based on a small technical pilot.

Option B: Enterprise access controls. Requires 8 person-months. Three customers representing
$720,000 in annual recurring revenue say renewal depends on these controls. A security
architecture decision from an external identity vendor is due in ten days.

Option C: AI meeting summarizer. Requires 10 person-months. Sixty-two percent of surveyed users
express interest, but there is no willingness-to-pay or retention evidence.

Option D: Accessibility and compliance package. Requires 5 person-months. It is required for two
public-sector bids worth $450,000. Certification capacity is available only if booked within
three weeks.

Which two options should LumenDesk select?
```

## Run A: Direct AI Answer, No Method Skill

**Instruction**

```text
Answer the question directly. Do not use or name any consulting framework or method.
```

**Representative output**

> LumenDesk should prioritize Option B because it protects $720,000 of recurring revenue and Option D because it enables $450,000 of near-term pipeline. Together they require 13 person-months and fit the capacity limit.
>
> Option A is valuable and affects existing users, so it should become the fallback if the identity-vendor decision makes Option B infeasible. Option C should wait because user interest is not yet evidence of revenue or retention impact.
>
> Before committing, confirm the external identity dependency for B and reserve certification capacity for D. If B is blocked, select A and D.

### What The Direct Answer Does Well

- Selects the two options with the strongest commercial evidence.
- Respects the 14 person-month capacity constraint.
- Treats Option C survey interest cautiously.
- Provides Option A as a fallback.

### What The Direct Answer Does Not Preserve

- The criteria and weights behind the recommendation.
- Whether unresolved delivery gates permit a formal ranking at all.
- A consistent definition of likelihood and impact.
- Named risk owners, triggers, controls, and contingency timing.

## Run B: Two-Skill Reasoning Chain

### Method Selection

| Sequence | Skill | Why it changes the work | Intermediate output |
|---|---|---|---|
| 1 | [`decision-matrix`](../skills/decision-matrix/SKILL.md) | Checks mandatory eligibility before scoring | Blocking conditions and clarification actions; ranking deferred |
| 2 | [`risk-matrix`](../skills/risk-matrix/SKILL.md) | Helps resolve time-critical dependencies before the decision matrix resumes | Risk register, controls, triggers, and contingencies |

`rice-scoring` and `wsjf-prioritization` are not used because reach and cost-of-delay data are not comparable or sufficiently reliable across all options.

### Step 1: Decision Matrix

**Eligibility gates**

- Select exactly two options.
- Combined effort must not exceed 14 person-months.
- No option proceeds if a critical dependency makes delivery infeasible within the quarter.
- Evidence cut-off is the current planning date.

**Draft criteria for a later scoring run**

These illustrative weights and anchors are proposals, not stakeholder-approved inputs. Confirm them before scoring. No formal scores or ranking are produced while mandatory requirements remain unresolved.

| Criterion | Weight | 1-point anchor | 5-point anchor |
|---|---:|---|---|
| Revenue protection or creation | 30% | No evidenced commercial effect | Contractual or near-term material revenue |
| User or customer outcome | 20% | Minor or speculative benefit | Broad, material observed problem |
| Evidence strength | 15% | Opinion or interest only | Direct customer, operational, or contractual evidence |
| Time to value | 15% | Benefit unlikely this quarter | Benefit available within the quarter |
| Reversibility | 10% | High lock-in or difficult rollback | Easy to stage, stop, or redirect |
| Strategic fit | 10% | Peripheral | Directly supports target market and retention |

**Eligibility register**

| Option | Current evidence | Eligibility status / next check |
|---|---|---|
| A: Reliability | 6 person-month estimate; small pilot | No blocking dependency stated; confirm quarter delivery scope |
| B: Access controls | 8 person-month estimate; architecture decision due in ten days | Unresolved hard gate; hold outside formal ranking pending feasibility confirmation |
| C: AI summarizer | 10 person-month estimate; interest only | Cannot form a two-option pair within 14 person-months: even C + D requires 15 |
| D: Accessibility | 5 person-month estimate; certification slot must be booked | Eligibility depends on securing certification capacity and confirming bid timing |

**Capacity check only, without scores or preference order**

| Pair | Effort | Unused capacity | Unresolved eligibility |
|---|---:|---:|---|
| A + B | 14 | 0 | B architecture feasibility; A delivery scope |
| A + D | 11 | 3 | D certification capacity; A delivery scope |
| B + D | 13 | 1 | B architecture feasibility and D certification capacity |

All other pairs exceed capacity: A + C = 16, B + C = 18, C + D = 15. Capacity fit alone does not establish eligibility or commercial preference.

**Sensitivity plan after gates clear**

- Revisit commercial criteria if renewal evidence weakens or public bids move beyond the quarter.
- Test whether changes to agreed weights or evidence-backed scores change the eligible pair choice; no ranking sensitivity is claimed before scoring.

**Effect on the next step:** The decision matrix stops before scoring. Use the risk register to resolve the blocking gates, then resume with confirmed eligible options and agreed criteria.

### Step 2: Risk Matrix

**Scales:** Likelihood and impact use 1-5. Impact 5 means failure to deliver an option or loss of its commercial outcome. The ratings, proposed owners, controls, and escalation thresholds below are illustrative planning assumptions, not additional facts from the Shared Input; validate them with the responsible stakeholders.

| Risk event | Cause | Consequence | Likelihood | Impact | Evidence |
|---|---|---|---:|---:|---|
| B cannot finalize architecture | External identity-vendor decision is delayed or incompatible | Renewal feature misses the quarter | 3 | 5 | Decision pending in ten days |
| B customer renewal still fails | Access controls may be necessary but not sufficient | Expected protected revenue is overstated | 2 | 5 | Customer statements; signed renewal evidence not supplied |
| D misses certification slot | Booking is not completed within three weeks | Public bids become ineligible | 3 | 4 | Shared Input says capacity is available if booked; reservation not confirmed |
| D does not influence bid awards | Compliance is a gate but not a differentiator | Pipeline value is overstated | 3 | 3 | Bid requirement, no buyer preference evidence |
| A incidents worsen while deferred | Reliability investment is postponed | Support cost or churn risk increases | 3 | 4 | 120 incidents per month |

**Response and monitoring**

| Priority risk | Response | Owner | Trigger | Contingency |
|---|---|---|---|---|
| B architecture dependency | Obtain written go/no-go and run a two-day design spike | VP Engineering | No feasible decision by day 10 | Exclude B; check whether A + D clears its gates |
| D certification slot | Place refundable booking | Product operations | Slot not reserved by end of week 1 | Reassess D against A |
| Reliability while selection is pending | Create incident guardrail and reserve emergency capacity | Engineering director | Incidents exceed 150/month or a severity-1 pattern appears | Reassess scope and capacity before selecting a pair |
| Revenue evidence | Confirm renewal and bid decision criteria | Commercial lead | Customers will not document dependency | Rescore commercial criteria |

**Effect on the decision:** No pair is formally preferred yet. The risk outputs supply dated validation actions and conditions for reopening the decision matrix; they do not override its hard gates.

## Decision Artifact

**Current decision state:** Selection and formal ranking are blocked. Resolve the following gates and confirm the proposed decision criteria before selecting two options:

1. B receives architecture feasibility confirmation by day 10.
2. D secures certification capacity by the end of week 1.
3. Commercial owners document the renewal and bid requirements.
4. Reliability incidents remain below the escalation threshold.

**Contingency set:** If B fails its gate, A + D is the only capacity-fitting pair left, requiring 11 person-months, and can be selected only if A and D clear their gates. If D fails its gate, A + B is the only capacity-fitting pair left, requiring 14 person-months, subject to A and B eligibility. If both B and D fail, no two-option pair fits capacity. If both clear, compare all eligible pairs with agreed criteria and current evidence; this example does not invent a future ranking.

### Evaluation Scorecard

| Track | Leading signal | Success threshold | Change trigger | Review |
|---|---|---|---|---|
| B feasibility | Architecture decision and design spike | Feasible design within 8 person-month estimate | No decision by day 10 or estimate exceeds capacity | Day 10 |
| B commercial value | Written renewal condition | At least two of three customers confirm controls as a renewal gate | Requirement is only a preference | 2 weeks |
| D feasibility | Certification booking | Slot reserved within one week | No slot or delivery exceeds quarter | 1 week |
| D commercial value | Bid eligibility confirmation | Both bids accept planned certification path | Bid dates or eligibility change | 2 weeks |
| Deferred A risk | Incident count and severity | Fewer than 150 incidents/month and no repeated severity-1 issue | Threshold breached | Weekly |

## Comparison

| Deliverable | Direct AI answer | Method-skill chain |
|---|---|---|
| Recommendation | B + D, with A fallback | Selection blocked until mandatory gates clear |
| Priority rationale | Commercial value and capacity | Eligibility register, capacity arithmetic, and draft criteria for later approval |
| Sensitivity | General caveat | Identifies evidence changes to test when scoring becomes valid |
| Risk handling | Confirm dependencies | Event-cause-consequence register with owners |
| Decision gates | Mentioned | Dated go/no-go triggers and fallback pairs |
| Success measures | Not detailed | Feasibility, commercial evidence, and reliability guardrails |

## What The Comparison Shows

The direct answer proposes a conditional portfolio quickly. The method chain applies a stricter prerequisite: unresolved mandatory feasibility gates block scoring and ranking. It provides a capacity check and dated validation plan, then leaves the portfolio choice open until the evidence permits a decision. This constructed comparison illustrates that contract difference; it does not establish model superiority or a real business outcome.
