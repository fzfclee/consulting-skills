# Review a Service Improvement Plan

This is a synthetic enterprise service-desk example, authored to show a reviewable artifact. It contains no customer evidence or operating results. Separate native regression runs and independent output review are summarized below; this guide and its counter-case responses remain authored requirements, not original model outputs. It is separate from the seven controlled comparisons.

## Task and Required Input

Question: What must change before submitting this ticket-routing plan for a pilot decision?

Provide the versioned proposal with sentence IDs, decision and scope, source documents with dates and applicable scope, known constraints, approval records or their absence, and available operating data. Mark missing inputs explicitly. For an effectiveness claim, also provide a metric definition, baseline window, comparable observations and attribution limits. Missing evidence can still support a draft review; it cannot establish compliance, approval or impact.

Scope: review wording and execution conditions for one internal service-desk process. No production changes, customer messages or ticket closures are performed. Cost savings and investment approval are outside this evidence packet.

## Original Proposal and Evidence Packet

All documents and counts below belong only to this synthetic scenario.

| Sentence | Original proposal v1 |
|---|---|
| P1 | Launch the routing change across all queues in week two. |
| P2 | Close tickets automatically after 24 hours without a requester reply. |
| P3 | Send cross-shift tickets to the shared queue; the next shift will handle them. |
| P4 | This change will reduce triage waiting time by 30%. |
| P5 | The planning meeting counts as approval to execute. |

| Evidence | Supplied source and content | Status and scope |
|---|---|---|
| E1 | Closure policy v2, effective day 1: requester confirmation is required before closure; no exception supplied. | Documentary rule for this service desk; applicability stipulated by input. |
| E2 | Day-5 snapshot export: 100 open tickets; 40 awaiting triage, 20 blocked by external dependencies, 40 in other states. | Supplied aggregate observation, internally totals 100; no ticket timestamps, trend or independent audit. |
| E3 | Handoff procedure v1: the receiving owner must acknowledge each cross-shift ticket. | Documentary rule for both shifts in scope. |
| E4 | Day-4 planning note: submit a pilot proposal for review. No approval decision or signed record accompanies it. | Evidence of a review request, not execution approval. |
| E5 | Change procedure v3: sandbox tests are permitted; production changes require recorded change approval. | Permission limited to sandbox; no production approval supplied. |

Assumptions: the supplied policy versions apply to this queue and no undisclosed exceptions exist. Validate those premises before a real decision. Unknowns: waiting-time baseline, comparator, customer preferences, savings, pilot owner, receiving-owner roster and approval decision. Approval: missing for production. Proposal assertions P4 and P5 remain claims; repetition in the proposal does not strengthen them.

## Method Selection and Handoffs

Use only three existing methods:

1. [Evidence Map](../skills/evidence-map/SKILL.md): label sources, claims, assumptions and gaps. Hand off the ledger E1-E5 and unresolved premises to the next method.
2. [Deductive Reasoning](../skills/deductive-reasoning/SKILL.md): test P1-P5 against the supplied rules and evidence scope. Hand off traceable issues I1-I5 and revised conclusions; valid inference does not independently verify policy truth.
3. [Validation Plan](../skills/validation-plan/SKILL.md): turn the remaining uncertainties into tests T1-T5 and explicit continue, adjust, stop or escalate conditions.

No method can establish actual customer demand, savings or executive permission from this packet. A full service blueprint or economic appraisal is unnecessary for this limited wording review; add one only when its distinct question becomes relevant.

### Evidence Map Workpaper

| Proposition | Support | Confidence and gap | Next evidence action |
|---|---|---|---|
| Confirmation is required for closure | E1 | Strong within supplied scope; verify version and exceptions. | Policy owner confirms applicability before pilot submission. |
| There is a triage backlog | E2 | Plausible: 40/100 are awaiting triage at one instant; duration and cause unknown. | Analyst obtains case-level timestamps and state definitions before impact testing. |
| Shared queue alone meets handoff procedure | P3 versus E3 | Risky assumption; queue membership does not identify an acknowledging receiver. | Shift lead supplies receiver assignment and acknowledgement records before pilot. |
| A 30% waiting-time improvement is established | P4, E2 | Do not conclude: no baseline, outcomes or comparator. | Analyst defines the metric and comparison before any effect claim. |
| Production execution is approved | P5 versus E4/E5 | Do not conclude: review request and sandbox permission have narrower scope. | Change owner supplies a scoped approval record before production. |

### Deductive Review: Issues and Impact

Severity here prioritizes review fixes, not measured incident probabilities.

| Issue | Sentence | Evidence | Rule, finding and possible impact | Severity | Revision | Acceptance |
|---|---|---|---|---|---|---|
| I1 | P1 | E5 | Production requires recorded approval; a calendar date cannot supply it. All-queue rollout could exceed permitted scope. | High | R1 | T1 |
| I2 | P2 | E1 | No reply is not requester confirmation. Automatic closure contradicts the supplied rule and could close unresolved requests. | High | R2 | T2 |
| I3 | P3 | E3 | A shared queue does not entail an acknowledged receiving owner. Accountability could be lost at shift change. | Medium | R3 | T3 |
| I4 | P4 | E2 | Snapshot counts do not entail a future time reduction or causal effect. The benefit statement overstates evidence. | Medium | R4 | T4 |
| I5 | P5 | E4, E5 | Submission for review does not entail execution approval. Treating it as approval could bypass the required decision. | High | R5 | T5 |

These conditional conclusions depend on E1/E3/E5 applying as stated. If sources conflict, record both and seek an authoritative scope decision; do not silently choose the source that makes the plan easier to approve.

## Minimal Wording Revisions: Proposal v2

Replace the five original sentences with these five sentences. Other content is outside this review.

| Revision | Replacement text |
|---|---|
| R1 | Submit a ten-working-day sandbox pilot across two shifts for review; any production scope and date remain pending recorded change approval. |
| R2 | After 24 hours without a requester reply, flag the ticket for human follow-up; retain it open until requester confirmation satisfies the applicable closure policy. |
| R3 | Assign each cross-shift ticket to a named receiving owner and record acknowledgement; escalate unacknowledged tickets to the shift lead under the agreed handoff rule. |
| R4 | A 30% reduction in triage waiting time is a proposed hypothesis to test; define the baseline, metric and comparison before claiming an improvement. |
| R5 | The planning meeting requested pilot review; production execution approval has not been established by the supplied records. |

The ten-day/two-shift design, role assignments and thresholds below are proposed / unapproved. R1 proposes a smaller scope; it does not claim pilot resources have been allocated. R3 leaves escalation timing to agreement rather than supplying an unsupported operational SLA. In this review, 30% is a proposed hypothesis, never an observed result.

## Validation Plan and Acceptance Conditions

Status now: **draft; hold production execution**. Proposed roles are not confirmed assignments. Timing is relative to submission, not a scheduled action.

| Test | Required evidence / method | Proposed owner and timing | Pass / continue | Adjust / stop / escalate |
|---|---|---|---|---|
| T1 | Compare proposed pilot configuration with E5; record environment, queue coverage and access permissions. | Change owner, before pilot start. | Scope is sandbox only, two shifts, ten working days; no production writes or external messages. | Stop if configuration touches production; change scope or seek the required authorization. |
| T2 | Sandbox replay: one confirmed ticket and one unconfirmed ticket, including the 24-hour condition; retain input/output logs. | QA lead, before pilot start. | Unconfirmed ticket stays open; confirmed ticket follows E1; no closure triggered solely by elapsed time. | Stop on any unconfirmed closure; correct rule and replay both cases. Escalate policy ambiguity to policy owner. |
| T3 | Replay a shift handoff with an assigned receiver and one without acknowledgement; inspect owner and escalation logs. | Shift lead, before pilot start. | First records named receiver and acknowledgement; second remains visible and escalates under an agreed timing rule. | Adjust if owner or timing is undefined; stop pilot if tickets disappear from accountability. |
| T4 | Define waiting time as created-to-first-triage timestamp difference, in minutes; agree eligibility, missing-data handling, baseline and comparison windows, shift/case-mix treatment and attribution limits. | Analyst, before impact evaluation. | Data and comparison design permit a qualified estimate with uncertainty; 30% target remains separate from observations. | Adjust if timestamps or comparator are absent; no causal time reduction or savings claim from E2. Shadow/sandbox performance does not establish real service impact. |
| T5 | Inspect approval register for decision, approver authority, exact production scope, date and conditions; compare with E4. | Change owner, before any production decision. | An applicable recorded production approval exists and its conditions are met. | Hold production if missing; escalate to authorized approver. Sandbox permission and scoring/review agreement do not substitute for it. |

Document acceptance is separate from pilot acceptance: a reviewer can accept this draft artifact when P1-P5 each map to evidence, issue, replacement and test, and all unknowns and proposed choices remain labeled. That document readiness does not approve a pilot. Pilot continuation needs T1-T3 and assigned owners; production needs T5 plus applicable procedure requirements. A demonstrated business-effect claim needs T4 evidence and an appropriate independent review; this example supplies neither.

Next action: proposed change owner confirms policy scope, names responsible owners and submits v2 plus the evidence ledger and tests for a pilot decision. Until that happens, approval and readiness remain unresolved.

## Counter Inputs and Frozen Required Responses

These are the frozen specifications established before execution, not model outputs or pass claims. See the independent native-test summary in the following section for the separate observed results, including the original C3 finding and its sole confirmation rerun.

| Counter input | Required response and acceptance |
|---|---|
| C1: remove E1 | Mark policy conformity unknown; request applicable closure rule. Do not assert a confirmed policy violation. Retain draft status and avoid representing automatic closure as authorized. |
| C2: remove E4 and all approval evidence | Approval remains unknown; no meeting content may be supplied from memory. Draft and production hold remain; request scoped approval record. |
| C3: provide only E2, no baseline or comparator | Report 40% awaiting triage in this snapshot if relevant; no causal time reduction, achieved 30% benefit or savings inference. Request metric and comparison data. |
| C4: add an exception document permitting some automatic closures while E1 still requires confirmation | Record both sources, dates and scopes; request policy-owner clarification of applicability. Do not silently resolve conflict or perform production closure. |

## What Has and Has Not Been Checked

Local document checks verify the traceable artifact contract and usage links; they do not execute the methods through a model. The coordinating audit task reports 159 single-method executions separately from this example's five blind method-chain scenarios (normal and C1-C4) and one same-input, fresh-context C3 confirmation rerun. These counts do not establish a reliability rate. Raw native records remain with that task and are not reproduced in this guide.

Independent output review of the original five scenarios recorded four PASS and one low-severity NEEDS_MINOR_REVISION: C3 broadened the review's non-execution boundary into a claim that closure was outside proposal-review scope. That original result is retained. The sole confirmation rerun is separately recorded PASS: its exclusion was explicitly a conservative scope recommendation, not a discovered ban. Optional sandbox-environment and external-message prechecks were not explicitly demonstrated in N/C4 and are not represented as verified.

The initial Pi request for snapshot 6b60bed was blocked by the existing bridge's execution lock and never entered model review. After the lock owner completed, a separately authorized request reviewed snapshot `793adb5fa30cf5986dc2c930c40b9e166b82d820` and returned ACCEPT for document / method-contract quality only, with five non-blocking findings and no material defect. It verified the 20 manifest file hashes and byte sizes, but performed no native execution and read no raw native JSON. That opinion applies to the named snapshot, not automatically to later revisions. Independent output review and this scoped Pi opinion are not expert, customer or business acceptance. Operating outcomes and business-effect validation remain unestablished. One authored synthetic case and this limited regression cannot demonstrate reliability across methods or customers.
