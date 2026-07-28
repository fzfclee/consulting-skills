# Account Strategy: Direct AI Answer vs Method-Skill Chain

> **Example note:** BrightGrid Analytics, Alderstone University, CampusMeter, the stakeholders, and the commercial details were created for this demonstration and do not refer to specific organizations.

This example compares:

1. a direct AI answer with no named method;
2. a two-skill chain using `stakeholder-power-map` and `account-plan`.

## Shared Input

```text
BrightGrid Analytics wants to win a two-building energy-analytics pilot at Alderstone University.
The university expects to decide whether to open a competitive process in six weeks.

CampusMeter, the incumbent, has served the university for five years and is already integrated
with the building-management system. The Facilities Director shared twelve months of utility
data with BrightGrid and is friendly, but says they will not advocate for a supplier change
without comparative evidence.

The Procurement Manager controls the sourcing process and previously renewed CampusMeter.
BrightGrid has not met this person. The Sustainability Lead wants better building-level carbon
data and is willing to join a benchmark review. IT Security can veto any pilot that requires
new cloud data flows. The CFO delegate controls the pilot budget.

BrightGrid has evidence from three reference campuses showing 8% to 12% avoidable-energy
identification, but has no Alderstone result. What should BrightGrid do next?
```

## Run A: Direct AI Answer, No Method Skill

**Instruction**

```text
Answer the question directly. Do not use or name any consulting framework or method.
```

**Representative output**

> BrightGrid should not ask the Facilities Director to replace the incumbent immediately. It should propose a low-risk benchmark using the data already shared, with clear success criteria and no operational disruption.
>
> Ask the Facilities Director and Sustainability Lead to sponsor an introduction to Procurement and IT Security. Tailor the case to each stakeholder: financial savings for the CFO delegate, fair process for Procurement, data controls for IT, and auditable carbon information for Sustainability.
>
> Use the three-campus results as supporting proof, but be explicit that Alderstone performance is unproven. The immediate goal should be permission to run the benchmark and agree how a pilot would be evaluated.

### What The Direct Answer Does Well

- Avoids attacking or demanding replacement of the incumbent.
- Uses a benchmark to reduce buyer risk.
- Recognizes that Procurement and IT Security must be involved.
- Adapts the value proposition to stakeholder concerns.

### What The Direct Answer Does Not Preserve

- Formal authority, informal influence, stance, and confidence for each stakeholder.
- Which relationships are facts and which support assumptions still need validation.
- The buying path from access to benchmark to funded pilot.
- Observable signals that distinguish polite interest from real account progress.

## Run B: Two-Skill Reasoning Chain

### Method Selection

| Sequence | Skill | Why it changes the work | Intermediate output |
|---|---|---|---|
| 1 | [`stakeholder-power-map`](../skills/stakeholder-power-map/SKILL.md) | Separates friendliness from support and reveals formal vetoes and access gaps | Decision arena, power/stance map, and engagement priorities |
| 2 | [`account-plan`](../skills/account-plan/SKILL.md) | Converts stakeholder insight into a commercial sequence, proof plan, and next commitment | Account objective, buying path, value/proof map, and 30-day actions |

`raci-matrix` is not used because the immediate problem is gaining access and validating the buying path, not assigning delivery responsibilities.

### Step 1: Stakeholder Power Map

**Decision arena**

- Decision: whether Alderstone opens a fair process for a two-building pilot.
- Observable support: permission to run a benchmark, access to required stakeholders, and written pilot criteria.
- Deadline: six weeks.
- Formal decision owner: not fully confirmed; Procurement controls sourcing and the CFO delegate controls budget.

| Stakeholder | Formal power | Informal influence | Current stance | Evidence / confidence |
|---|---:|---:|---|---|
| Facilities Director | Medium | High | Open to evidence, not committed | Shared data and stated condition; strong |
| Procurement Manager | High | Medium | Unknown; incumbent familiarity may favor status quo | Role confirmed, stance inferred; low |
| Sustainability Lead | Low | Medium | Supportive of benchmark | Willing to join review; strong |
| IT Security | Veto | Medium | Unknown | Formal veto confirmed; stance missing |
| CFO delegate | High budget power | Medium | Unknown | Budget role confirmed; criteria missing |
| CampusMeter | No buyer authority | High incumbent influence | Will defend position | Five-year integration; medium |

**Incentives and concerns**

| Stakeholder | Gain sought | Loss feared | Likely objection |
|---|---|---|---|
| Facilities Director | Credible savings without disruption | Operational risk and reputational cost of change | "Why disturb a working integration?" |
| Procurement Manager | Defensible and fair sourcing | Process challenge or supplier favoritism | "Why should this bypass the normal process?" |
| Sustainability Lead | Auditable building-level data | Another tool that does not improve reporting | "Can the result support our reporting cycle?" |
| IT Security | Controlled data flow | Unapproved cloud exposure | "What data leaves the campus environment?" |
| CFO delegate | Verified financial benefit | Paying for an unproven pilot | "What is the payback and stop condition?" |

**Priority engagement moves**

| Priority | Stakeholder | Next ask | Channel | Timing | Signal / fallback |
|---|---|---|---|---|---|
| 1 | Facilities Director | Sponsor a benchmark review and introductions | Joint meeting with Sustainability Lead | Week 1 | Meeting accepted; otherwise request permission for a written benchmark |
| 2 | Procurement Manager | Confirm process and comparison rules | Sponsor introduction | Week 2 | Written process and criteria; otherwise send a process-neutral capability note |
| 3 | IT Security | Run early data-flow screen | Technical session | Week 2 | No fatal architecture objection |
| 4 | CFO delegate | Validate payback and budget gate | Benchmark readout | Week 4 | Agreed economic threshold |

**Disconfirming check:** If Procurement states that no competitive process can occur this cycle, the account plan must shift from a six-week pursuit to evidence-building for the next cycle.

**Effect on the next step:** The friendly Facilities relationship is an access path, not proof of sponsorship. The account plan must earn a fair comparison mechanism.

### Step 2: Account Plan

**Account objective:** Secure a buyer-approved benchmark and, if it passes agreed gates, a paid two-building pilot. Do not seek an immediate incumbent replacement.

**Buying path**

| Stage | Required commitment | Current status | Evidence needed to advance |
|---|---|---|---|
| Access | Introductions to Procurement and IT | Missing | Facilities sponsorship |
| Process | Written sourcing and comparison rules | Missing | Procurement confirmation |
| Technical eligibility | Acceptable data flow and integration burden | Unknown | IT pre-screen |
| Value proof | Alderstone-specific savings opportunity | Not yet proven | Benchmark result |
| Funding | Pilot budget and payback gate | Unknown | CFO criteria |
| Pilot | Scope, owner, success metrics, and stop condition | Future | Joint pilot charter |

**Value, competition, and proof**

| Buyer need | BrightGrid value hypothesis | Current proof | Alternative strength | Proof gap |
|---|---|---|---|---|
| Reduce avoidable energy | Multi-building anomaly analysis | 8%-12% identification at three reference campuses | Incumbent has local integration | Alderstone-specific result |
| Improve carbon reporting | Building-level audit trail | Demonstration only | Existing reports require no change | Reporting acceptance test |
| Avoid operational disruption | Read-only benchmark before integration | Proposed architecture | Incumbent is already embedded | IT validation |
| Defend procurement decision | Transparent comparison criteria | Draft benchmark protocol | Status quo is low effort | Buyer-approved process |

**30-day action plan**

| Action | Owner | Timing | Expected commitment or signal | Fallback |
|---|---|---|---|---|
| Produce a two-page benchmark protocol | BrightGrid account lead | 3 days | Facilities and Sustainability agree scope | Reduce to one building |
| Request Procurement and IT introductions | Facilities Director | Week 1 | Meetings booked | Written questions routed through sponsor |
| Complete security pre-screen | BrightGrid technical lead + IT | Week 2 | No fatal data-flow issue | Offer on-premise analysis |
| Run benchmark on approved data | Analytics lead | Weeks 2-3 | Quantified opportunity with confidence range | Report no material opportunity honestly |
| Agree pilot economics and decision rule | Account lead + CFO delegate | Week 4 | Payback and stop threshold documented | Do not propose a paid pilot |

**Effect on the decision:** The pursuit advances only through buyer commitments. Friendly access without process, technical, value, and budget evidence is no longer treated as account progress.

## Decision Artifact

**Current decision:** Pursue permission for a transparent benchmark, not incumbent replacement. Advance to a paid pilot only if access, process, technical, and value gates are all passed.

### Account Progress Scorecard

| Gate | Success signal | Stop or defer trigger | Review |
|---|---|---|---|
| Sponsor access | Facilities Director makes Procurement and IT introductions | No introduction or permission after two direct requests | End of week 1 |
| Fair process | Procurement documents evaluation path | Process excludes a pilot this cycle | End of week 2 |
| Technical eligibility | IT confirms acceptable data handling | Fatal security or integration burden | End of week 2 |
| Value evidence | Benchmark identifies at least 6% addressable energy with traceable evidence | Result below threshold or cannot be validated | End of week 3 |
| Economic case | Buyer accepts a pilot payback threshold of 12 months or less | No budget owner or no agreed economic gate | End of week 4 |

## Comparison

| Deliverable | Direct AI answer | Method-skill chain |
|---|---|---|
| Immediate recommendation | Propose a low-risk benchmark | Same recommendation |
| Stakeholder judgment | Role-based narrative | Power, influence, stance, and confidence separated |
| Buying path | General introductions | Six explicit commitments from access to pilot |
| Proof strategy | Use campus evidence and be transparent | Buyer need, alternative strength, and proof gap by row |
| Action plan | Suggested meetings | Owners, timing, expected commitment, and fallback |
| Progress definition | Interest and benchmark | Gates that distinguish polite interest from executable progress |

## What The Comparison Shows

The direct answer gives sound sales advice. The method chain reduces the risk of mistaking a friendly contact for a sponsor, makes hidden vetoes visible, and converts account activity into a sequence of buyer commitments that can be stopped when the opportunity is not real.
