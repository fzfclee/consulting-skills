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
- How close Option A is to Option D and what assumption changes the ranking.
- A consistent definition of likelihood and impact.
- Named risk owners, triggers, controls, and contingency timing.

## Run B: Two-Skill Reasoning Chain

### Method Selection

| Sequence | Skill | Why it changes the work | Intermediate output |
|---|---|---|---|
| 1 | [`decision-matrix`](../skills/decision-matrix/SKILL.md) | Makes strategic, user, evidence, speed, and reversibility tradeoffs explicit | Weighted option ranking and sensitivity |
| 2 | [`risk-matrix`](../skills/risk-matrix/SKILL.md) | Prevents a high-scoring option from hiding a time-critical dependency | Risk register, controls, triggers, and contingencies |

`rice-scoring` and `wsjf-prioritization` are not used because reach and cost-of-delay data are not comparable or sufficiently reliable across all options.

### Step 1: Decision Matrix

**Eligibility gates**

- Select exactly two options.
- Combined effort must not exceed 14 person-months.
- No option proceeds if a critical dependency makes delivery infeasible within the quarter.
- Evidence cut-off is the current planning date.

**Weighted criteria**

| Criterion | Weight | 1-point anchor | 5-point anchor |
|---|---:|---|---|
| Revenue protection or creation | 30% | No evidenced commercial effect | Contractual or near-term material revenue |
| User or customer outcome | 20% | Minor or speculative benefit | Broad, material observed problem |
| Evidence strength | 15% | Opinion or interest only | Direct customer, operational, or contractual evidence |
| Time to value | 15% | Benefit unlikely this quarter | Benefit available within the quarter |
| Reversibility | 10% | High lock-in or difficult rollback | Easy to stage, stop, or redirect |
| Strategic fit | 10% | Peripheral | Directly supports target market and retention |

**Option scores**

| Option | Revenue | User outcome | Evidence | Speed | Reversibility | Fit | Weighted total / 5 |
|---|---:|---:|---:|---:|---:|---:|---:|
| A: Reliability | 3 | 5 | 4 | 4 | 4 | 4 | 3.90 |
| B: Access controls | 5 | 3 | 5 | 4 | 3 | 5 | 4.25 |
| C: AI summarizer | 2 | 3 | 2 | 2 | 3 | 3 | 2.40 |
| D: Accessibility | 4 | 3 | 4 | 5 | 4 | 4 | 3.95 |

**Feasible pair comparison**

| Pair | Effort | Combined score | Main tradeoff |
|---|---:|---:|---|
| A + B | 14 | 8.15 | Protects users and renewals but does not unlock public bids |
| A + D | 11 | 7.85 | Strong risk reduction; leaves 3 person-months unused |
| B + D | 13 | 8.20 | Strongest evidenced commercial portfolio; two external dependencies |

**Sensitivity**

- A overtakes D if reliability receives a score of 5 on revenue impact or if the public bids slip beyond the planning horizon.
- B remains first unless the renewal evidence weakens or the vendor dependency makes delivery infeasible.

**Effect on the next step:** B + D is the provisional portfolio, but both options require explicit risk gates.

### Step 2: Risk Matrix

**Scales:** Likelihood and impact use 1-5. Impact 5 means failure to deliver the selected option or loss of the commercial outcome.

| Risk event | Cause | Consequence | Likelihood | Impact | Evidence |
|---|---|---|---:|---:|---|
| B cannot finalize architecture | External identity-vendor decision is delayed or incompatible | Renewal feature misses the quarter | 3 | 5 | Decision pending in ten days |
| B customer renewal still fails | Access controls are necessary but not sufficient | Expected protected revenue is overstated | 2 | 5 | Customer statements, no signed renewal |
| D misses certification slot | Booking is not completed within three weeks | Public bids become ineligible | 3 | 4 | Certification availability confirmed |
| D does not influence bid awards | Compliance is a gate but not a differentiator | Pipeline value is overstated | 3 | 3 | Bid requirement, no buyer preference evidence |
| A incidents worsen while deferred | Reliability investment is postponed | Support cost or churn risk increases | 3 | 4 | 120 incidents per month |

**Response and monitoring**

| Priority risk | Response | Owner | Trigger | Contingency |
|---|---|---|---|---|
| B architecture dependency | Obtain written go/no-go and run a two-day design spike | VP Engineering | No feasible decision by day 10 | Replace B with A |
| D certification slot | Place refundable booking | Product operations | Slot not reserved by end of week 1 | Reassess D against A |
| Deferred reliability | Create incident guardrail and reserve emergency capacity | Engineering director | Incidents exceed 150/month or a severity-1 pattern appears | Pull forward A or reduce B/D scope |
| Revenue evidence | Confirm renewal and bid decision criteria | Commercial lead | Customers will not document dependency | Rescore commercial criteria |

**Effect on the decision:** B + D remains preferred only as a conditional portfolio. The risk outputs supply the dated gates and fallback combinations that the score alone cannot provide.

## Decision Artifact

**Conditional decision:** Select B and D, using 13 person-months, only after the following gates:

1. B receives architecture feasibility confirmation by day 10.
2. D secures certification capacity by the end of week 1.
3. Commercial owners document the renewal and bid requirements.
4. Reliability incidents remain below the escalation threshold.

**Fallback:** If B fails its gate, select A + D. If D fails its gate, compare A + B against current commercial evidence.

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
| Recommendation | B + D, with A fallback | Same provisional portfolio |
| Priority rationale | Commercial value and capacity | Explicit criteria, weights, scores, and pair eligibility |
| Sensitivity | General caveat | States what evidence makes A overtake D |
| Risk handling | Confirm dependencies | Event-cause-consequence register with owners |
| Decision gates | Mentioned | Dated go/no-go triggers and fallback pairs |
| Success measures | Not detailed | Feasibility, commercial evidence, and reliability guardrails |

## What The Comparison Shows

The direct answer reaches the same sensible portfolio quickly. The method chain makes the ranking auditable and turns dependency concerns into timed decision gates. Its value is not a more complicated score; it is knowing exactly when B + D should no longer remain the preferred choice.
