# Market Entry: Direct AI Answer vs Method-Skill Chain

> **Example note:** FieldNova, Ardenia, the regulations, market data, competitors, customers, and economics were created for this demonstration and do not refer to a specific organization or market.

This example compares:

1. a direct AI answer with no named method;
2. a three-skill chain using `pestel-analysis`, `porter-five-forces`, and `competitive-positioning`.

## Shared Input

```text
FieldNova is a mid-sized provider of predictive maintenance services for industrial sites. It
is considering entry into Ardenia, the sample national market used in this example, over the next 18 months.

Market evidence supplied in the example:
- industrial maintenance spending is estimated to grow 7% annually;
- foreign providers need a locally licensed partner for safety-critical sites;
- new industrial data-residency guidance is expected within nine months;
- the local currency moved within a 12% range last year;
- three established providers bundle service with equipment contracts;
- the ten largest buyers account for 64% of addressable spending;
- only four local partners hold the relevant safety certification;
- buyers outside the capital often require hybrid or on-premise operation;
- buyers consistently request local-language, 24/7 incident response.

FieldNova reduced unplanned downtime by 18% in its home-market reference sites, but has no
Ardenia proof. Its target gross margin is at least 35%. A preliminary local-partner proposal
would produce an estimated 32% gross margin before currency protection.

Should FieldNova approve a broad launch, run a focused market test, or stay out?
```

## Run A: Direct AI Answer, No Method Skill

**Instruction**

```text
Answer the question directly. Do not use or name any consulting framework or method.
```

**Representative output**

> FieldNova should not approve a broad launch yet. Market growth is attractive, but licensing, data residency, concentrated buyers, scarce partners, incumbent bundling, and a current margin estimate below target create material uncertainty.
>
> Run a focused market test with one licensed partner and one clearly defined segment. Confirm data-hosting requirements, negotiate economics above the 35% margin threshold, and secure buyer interest before building a national operating model.
>
> The test should include local-language support, a hybrid deployment option, and a paid pilot. Proceed only if FieldNova can demonstrate local downtime value, acceptable partner economics, and at least several credible customers.

### What The Direct Answer Does Well

- Rejects a broad launch.
- Identifies regulation, partner scarcity, buyer concentration, and margin as key risks.
- Recommends a focused partner-led test.
- Defines several reasonable entry conditions.

### What The Direct Answer Does Not Preserve

- Which macro forces are material and when they may affect the decision.
- How each industry force captures profit or weakens bargaining power.
- The exact buyer segment, alternative set, and defensible position.
- The evidence and signposts that would turn a focused test into a launch or exit.

## Run B: Three-Skill Reasoning Chain

### Method Selection

| Sequence | Skill | Why it changes the work | Intermediate output |
|---|---|---|---|
| 1 | [`pestel-analysis`](../skills/pestel-analysis/SKILL.md) | Filters external conditions that can invalidate entry feasibility or timing | Material external-force map and signposts |
| 2 | [`porter-five-forces`](../skills/porter-five-forces/SKILL.md) | Tests structural profit pressure rather than relying on 7% market growth | Force-strength profile and economic response |
| 3 | [`competitive-positioning`](../skills/competitive-positioning/SKILL.md) | Identifies one buyer choice FieldNova may credibly win | Segment, alternatives, defensible difference, and proof test |

`business-model-canvas` is not used because a full operating model is premature until the entry thesis passes its regulatory, economic, and buyer gates.

### Step 1: PESTEL Analysis

**Scope:** Predictive maintenance services for safety-critical industrial sites in Ardenia over 18 months.

| Category | Material force | Direction | Timing | Evidence status |
|---|---|---|---|---|
| Political | No decision-relevant policy evidence supplied | Unknown | Missing | Missing |
| Economic | 7% spending growth | Positive | 18 months | Estimate |
| Economic | 12% currency range | Negative / uncertain | Immediate | Historical estimate |
| Social | Buyers require local-language 24/7 response | Entry requirement | Immediate | Repeated buyer request |
| Technological | Hybrid or on-premise operation outside the capital | Cost and delivery burden | Immediate | Buyer evidence |
| Environmental | No material environmental requirement supplied | Unknown | Missing | Missing |
| Legal | Licensed local partner required | Entry constraint | Immediate | Stated rule |
| Legal | Data-residency guidance expected | Uncertain architecture risk | Within 9 months | Pending guidance |

**Material implications and signposts**

| Force | Decision implication | Response | Revisit trigger |
|---|---|---|---|
| Licensed-partner rule | No direct-only entry | Qualify at least two partners | Fewer than two viable partners |
| Data-residency uncertainty | Avoid irreversible cloud architecture | Design hybrid pilot | Guidance prohibits proposed data flow |
| Currency volatility | Current 32% margin may deteriorate | Price in local currency protection | Hedged margin remains below 35% |
| Local support expectation | Remote home-market model is insufficient | Cost a partner-led 24/7 model | Service cost breaks margin gate |

**Effect on the next step:** Entry is feasible only through a partner and flexible architecture. Industry structure must show whether attractive economics remain.

### Step 2: Porter Five Forces

**Industry boundary:** Predictive maintenance services for mid-sized regulated industrial sites in Ardenia, excluding equipment sales.

| Force | Strength | Evidence | Profit mechanism | Trend |
|---|---|---|---|---|
| Rivalry | High | Three established providers bundle service with equipment | Bundling reduces standalone price visibility | Stable |
| Buyer power | High | Top ten buyers control 64% of spending | Concentrated buyers demand proof and price concessions | Stable |
| Supplier / partner power | High | Only four certified local partners | Partners capture margin and control delivery access | May increase |
| Threat of entrants | Medium | Licensing and support requirements slow entry | Barriers protect incumbents but do not prevent capable entrants | Stable |
| Substitutes | High | In-house maintenance teams and OEM service contracts | Buyers can avoid a standalone provider | Stable |

**Structural diagnosis**

- Market growth does not imply attractive standalone economics.
- Partner and buyer power can push gross margin below the 35% target.
- A broad undifferentiated launch would compete against bundled incumbents and the status quo.
- The potentially attractive niche is a buyer with mixed equipment, costly downtime, and dissatisfaction with single-OEM visibility.

**Strategic responses**

| Response | Force addressed | Feasibility | Risk | Validation |
|---|---|---|---|---|
| Target mixed-equipment sites | Rivalry and substitutes | Medium | Segment may be small | Size qualified account list |
| Qualify two partners | Partner power | Medium | Limited certified supply | Compare economics and service capability |
| Use paid diagnostic before full pilot | Buyer power | High | Buyer may expect free work | Test willingness to pay |
| Contract in protected margin bands | Currency and buyer power | Medium | Buyer resistance | Price test with three accounts |

**Effect on the next step:** FieldNova needs a narrow segment where multi-vendor independence matters enough to overcome incumbent integration and price pressure.

### Step 3: Competitive Positioning

**Target buyer:** Operations leader at a mid-sized, regulated plant with mixed-vendor equipment, high downtime cost, and no unified failure view.

**Choice frame**

| Buyer criterion | FieldNova hypothesis | Bundled incumbent | In-house team | Current proof gap |
|---|---|---|---|---|
| Multi-vendor visibility | Independent analytics across equipment brands | Strong only for own equipment | Depends on internal tools | No Ardenia implementation |
| Downtime reduction | 18% home-market reference result | Local installed-base knowledge | High contextual knowledge | Local baseline and attribution |
| Regulatory operation | Partner-led licensed delivery | Already established | Internal compliance | Partner and data design not approved |
| 24/7 local response | Delivered through certified partner | Existing local support | Existing internal staff | Service-level capability and cost |
| Commercial risk | Paid diagnostic before rollout | Bundled contract may appear simpler | No new vendor cost | Buyer willingness to pay |

**Defensible difference hypothesis**

> For regulated plants with mixed-vendor equipment and costly downtime, FieldNova provides an independent failure view and a paid diagnostic that quantifies avoidable downtime before a larger commitment, unlike single-OEM bundles or fragmented internal monitoring.

This position is not yet proven. It survives only if local buyers value multi-vendor independence and a paid diagnostic enough to support target economics.

**Buyer validation**

| Test | Success threshold | Failure signal |
|---|---|---|
| Segment interviews | At least 6 of 10 qualified buyers rank multi-vendor visibility among top three criteria | Buyers prefer bundled simplicity or price |
| Partner economics | At least two partners can deliver protected gross margin of 35% or more | All viable models remain below threshold |
| Commercial intent | Three written expressions of interest and one paid diagnostic | Interest remains informal or free-only |
| Technical eligibility | Hybrid design passes partner and buyer security review | Data-residency path remains blocked |
| Local value proof | Paid diagnostic identifies a credible downtime opportunity | No material opportunity or attribution |

**Effect on the decision:** The entry question changes from "Is Ardenia attractive?" to "Can FieldNova win one defined buyer choice at protected economics and with local proof?"

## Decision Artifact

**Current decision:** Do not approve a broad national launch. Authorize a 90-day qualification sprint for the mixed-equipment regulated-plant segment.

### 90-Day Entry Scorecard

| Gate | Owner | Proceed threshold | Stop or redesign trigger | Timing |
|---|---|---|---|---|
| Regulatory path | Country lead + legal | Licensed partner and acceptable hybrid data design | Proposed delivery is not legally or technically viable | 30 days |
| Partner economics | Commercial lead | Two partner models at 35%+ protected gross margin | All credible models remain below 35% | 45 days |
| Segment demand | Market lead | 6 of 10 buyers validate the problem and criteria | Buyer need is weak or points to another segment | 45 days |
| Commercial commitment | Sales lead | Three written interests and one paid diagnostic | No paid commitment after ten qualified conversations | 75 days |
| Local proof | Delivery lead | Diagnostic supports a credible pilot value case | No measurable value or unacceptable delivery burden | 90 days |

**Decision after 90 days**

- Approve a limited two-site pilot only if all five gates pass.
- Redesign the segment or offer if regulatory and economic gates pass but buyer gates fail.
- Exit the entry effort if regulatory feasibility or protected margin fails.

## Comparison

| Deliverable | Direct AI answer | Method-skill chain |
|---|---|---|
| Recommendation | Focused partner-led test | Same direction, narrowed to one segment |
| External context | List of major risks | Material PESTEL forces with timing and signposts |
| Industry economics | General concentration concern | Five-force profit mechanisms and responses |
| Positioning | Local support and hybrid deployment | Buyer, alternatives, differentiator, and proof gap |
| Entry plan | Pilot before launch | 90-day qualification sprint with five gates |
| Exit logic | Stay out if conditions fail | Explicit stop, redesign, and pilot thresholds |

## What The Comparison Shows

The direct answer correctly avoids a broad launch. The method chain shows why market growth is not enough, identifies the narrow buyer choice FieldNova may win, and turns a vague pilot recommendation into a staged investment decision with explicit exit conditions.
