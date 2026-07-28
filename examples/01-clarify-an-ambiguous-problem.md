# Ambiguous Problem: Direct AI Answer vs Method-Skill Chain

> **Example note:** Blue Harbor Foods, its program, metrics, people, and events were created for this demonstration and do not refer to a specific organization.

This example uses the same input twice:

1. a direct AI answer with no named method;
2. a two-skill chain using `evidence-map` and `issue-tree`.

The purpose is not to prove that methods always produce a different conclusion. It is to show what becomes inspectable and actionable when an ambiguous statement is converted into a decision-ready problem.

## Shared Input

```text
Blue Harbor Foods is six months into an order-to-cash transformation across four business units.
The leadership team says, "The transformation is not working," and must decide within four weeks
whether to redesign governance, add adoption support, or pause the rollout.

Twelve interviews contain complaints about slow decisions, weak ownership, funding delays, low
adoption, and delivery speed. On-time delivery improved from 78% to 84%, and manual rework fell
from 22% to 19%. Monthly active use is 76% in two business units but 31% in the other two.

Decision logs show that ownership changed during delivery in 9 of 14 major decisions. Three of
four business units have no named owner for adoption after release. Funding approval was late
for 3 of 11 work packages, but there is no analysis linking those delays to adoption or delivery.

What is actually failing, and what should leadership do next?
```

## Run A: Direct AI Answer, No Method Skill

**Instruction**

```text
Answer the question directly. Do not use or name any consulting framework or method.
```

**Representative output**

> The transformation is not uniformly failing. Delivery and rework have improved, while adoption is uneven and decision ownership is unstable.
>
> Leadership should avoid pausing the whole program. Instead, define success measures, assign one accountable adoption owner in each business unit, clarify who owns decisions from planning through delivery, and focus support on the two low-usage units. Funding delays should be reviewed, but the available information does not show that they are the main cause.
>
> Run a four-week recovery sprint. Compare adoption barriers in the high- and low-usage units, fix decision ownership, and report progress using active use, cycle time, rework, and decision turnaround. At the end of the sprint, decide whether governance needs a broader redesign.

### What The Direct Answer Does Well

- Rejects the blanket statement that the entire transformation is failing.
- Notices uneven adoption and unstable ownership.
- Recommends targeted action instead of a full pause.
- Avoids treating funding delay as a proven cause.

### What The Direct Answer Does Not Preserve

- Which statements are facts, interpretations, or unsupported claims.
- A complete structure separating outcomes, operating mechanisms, enablement, and funding.
- Why adoption ownership and decision continuity should be analyzed before other branches.
- The evidence that would justify a wider governance redesign.

## Run B: Two-Skill Reasoning Chain

### Method Selection

| Sequence | Skill | Why it changes the work | Intermediate output |
|---|---|---|---|
| 1 | [`evidence-map`](../skills/evidence-map/SKILL.md) | Prevents repeated complaints from becoming facts and separates mixed outcome signals | Evidence ledger, confidence readout, and evidence gaps |
| 2 | [`issue-tree`](../skills/issue-tree/SKILL.md) | Converts "not working" into answerable branches tied to a leadership decision | Issue tree, evidence plan, and analysis priority |

Methods such as `five-whys-root-cause` are not used because there is not yet one bounded failure with a defensible causal chain.

### Step 1: Evidence Map

**Evidence question:** Is there enough evidence to pause or redesign the whole transformation?

| Evidence item | Type | Strength | Relevance | Supports or weakens |
|---|---|---:|---:|---|
| On-time delivery improved from 78% to 84% | Reported metric | Medium | High | Weakens the claim of total failure |
| Manual rework fell from 22% to 19% | Reported metric | Medium | Medium | Weakens the claim of total failure |
| Active use is 76% in two units and 31% in two units | Reported metric | Medium | High | Supports an uneven adoption problem |
| Ownership changed in 9 of 14 major decisions | Decision-log evidence | Strong | High | Supports decision-continuity risk |
| Three units have no named post-release adoption owner | Role evidence | Strong | High | Supports an accountability gap |
| Funding was late for 3 of 11 work packages | Process evidence | Medium | Medium | Shows delay, not primary causation |
| Funding delay is the main reason adoption is low | Interview claim | Weak | High | Not proven |
| Teams are resisting the operating model | Interview claim | Weak | Medium | Not yet behaviorally defined |

**Decision-critical gaps**

| Gap | Why it matters | Fastest check | Owner | Timing |
|---|---|---|---|---|
| Adoption funnel by unit and user role | Locates where use breaks down | Compare activation, completion, and repeat use | Product analytics lead | 1 week |
| Decision changes by type and approver | Tests whether governance instability causes rework or delay | Review 14 decision records and downstream effects | Program director | 1 week |
| Difference between high- and low-use units | Identifies local operating conditions | Paired interviews and workflow observation | Adoption lead | 2 weeks |
| Effect of funding delay | Prevents a visible issue from becoming the default cause | Compare delayed and on-time work packages | Finance partner | 2 weeks |

**Confidence readout**

- Strongly supported: adoption is uneven; ownership is unstable; post-release accountability is missing.
- Plausible but unproven: decision changes contribute to adoption and delivery variation.
- Risky assumption: funding delay is the primary cause.
- Do not conclude yet: the transformation as a whole has failed.

**Effect on the next step:** The issue structure must separate mixed outcomes from causal and operating questions. A whole-program pause is not supported.

### Step 2: Issue Tree

**Core question:** Which operating conditions explain the difference between acceptable delivery progress and weak adoption in two units, and what must change before the next rollout decision?

| Branch | Answerable sub-issue | Current evidence | Decision impact |
|---|---|---|---|
| Business outcomes | Are delivery, quality, adoption, and value moving in the required direction? | Delivery and rework improved; adoption split by unit; value missing | Defines what is and is not failing |
| Decision operating model | Are decision rights stable from planning through delivery? | Ownership changed in 9 of 14 decisions | May justify a governance intervention |
| Adoption mechanism | Does each unit have an owner, workflow fit, support, and reinforcement? | Three units lack an accountable owner | May justify targeted adoption action |
| Funding and capacity | Did approval delays block specific outcomes? | 3 of 11 packages delayed; causal link missing | Requires validation before reprioritization |
| Local context | What differs between high- and low-use units? | Missing | Determines whether one standard intervention will work |

**Priority analysis sequence**

1. Compare the adoption mechanism in high- and low-use units.
2. Trace the downstream effect of the nine ownership changes.
3. Test whether funding delay predicts adoption or delivery variance.
4. Define the missing value outcome before approving the next rollout.

**Disconfirming check:** If low-use units have stable ownership and the same workflow conditions as high-use units, the current adoption-owner hypothesis must be revised.

**Effect on the decision:** Leadership now has a bounded diagnostic sprint instead of a generic governance redesign.

## Decision Artifact

**Current decision:** Do not pause the full transformation and do not redesign all governance yet. Run a two-week evidence sprint focused on adoption variance and decision continuity, followed by two weeks of targeted intervention.

| Action | Owner | Timing | Evidence produced |
|---|---|---|---|
| Name a temporary adoption owner in every unit | Business-unit leaders | 3 days | Observable accountability boundary |
| Compare adoption funnels and workflows across four units | Product analytics + adoption lead | 1 week | Location and mechanism of drop-off |
| Trace downstream effects of 14 major decisions | Program director | 1 week | Evidence for or against governance redesign |
| Test funding-delay correlation | Finance partner | 2 weeks | Evidence for or against funding as primary cause |
| Define the value outcome for the next rollout gate | Executive sponsor | 2 weeks | Decision-ready success definition |

### Evaluation Scorecard

| Question | Leading signal | Decision threshold | Review |
|---|---|---|---|
| Is adoption ownership affecting use? | Every unit has a named owner and weekly intervention log | Low-use units improve activation or completion by at least 10 percentage points within four weeks | Weekly |
| Is decision instability material? | Decision changes are linked to delay, rework, or adoption impact | Redesign governance only if at least 5 of 9 changes produced material downstream impact | 2 weeks |
| Is funding the binding problem? | Delayed packages are compared with on-time packages | Treat funding as primary only if delay consistently predicts the outcome gap | 2 weeks |
| Should rollout continue? | Delivery, adoption, and value evidence are reviewed together | Continue only when the next unit has an owner, baseline, and measurable value target | 4 weeks |

## Comparison

| Deliverable | Direct AI answer | Method-skill chain |
|---|---|---|
| Final recommendation | Do not pause; target adoption and ownership | Same direction, with explicit evidence limits |
| Evidence discipline | Mentioned in narrative | Atomic evidence ledger and confidence readout |
| Problem structure | Several themes | Decision-linked issue tree |
| Priority logic | Implicit | Ordered branches based on decision impact |
| Action plan | Four-week recovery sprint | Named owners, timing, and evidence produced |
| Success and reversal gates | Broad metrics | Thresholds for governance redesign, funding diagnosis, and rollout |

## What The Comparison Shows

The direct answer is useful and reaches a reasonable direction. The method chain does not manufacture a different conclusion. It makes clear why the broad failure claim is unsupported, what should be analyzed first, and exactly what evidence would trigger a larger governance change.
