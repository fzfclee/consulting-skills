# Fictional Product Adoption: Direct AI Answer vs Method-Skill Chain

> **Privacy note:** Harborline Manufacturing, FlowApprove, all users, metrics, costs, and interviews are entirely fictional.

This example compares:

1. a direct AI answer with no named method;
2. a three-skill chain using `evidence-map`, `jobs-to-be-done`, and `metrics-tree`.

## Shared Fictional Input

```text
Harborline Manufacturing introduced an internal purchase-request product called FlowApprove.
It targets 620 managers, but monthly active use is 23%. Among users who start a request, 58%
leave before submission.

Plant supervisors have the lowest monthly use at 12%. Their common alternative is email plus a
spreadsheet. Completed requests in FlowApprove reach final approval in a median of 3.1 days,
compared with 4.8 days for the manual process.

Eighteen interviews produced these observations:
- 11 users say supplier and cost-center data must be re-entered;
- 9 are unsure whether a submitted request is progressing;
- 7 ask for a management dashboard;
- the product team proposes an AI assistant and more training.

The product costs $480,000 per year. Its value case depends on reducing coordination time,
approval delay, and avoidable purchase errors. Harborline has eight weeks to decide what to
change and how to test whether ROI can improve.
```

## Run A: Direct AI Answer, No Method Skill

**Instruction**

```text
Answer the question directly. Do not use or name any consulting framework or method.
```

**Representative output**

> FlowApprove appears to create value after a request is completed, but too many users fail before submission. Harborline should focus first on the request workflow rather than adding a management dashboard or AI assistant.
>
> For plant supervisors, prefill supplier and cost-center data, show an immediate submission confirmation and visible approval status, and provide role-specific support. Pilot these changes in two plants before a wider rollout.
>
> Measure start-to-submit conversion, repeat use, approval time, coordination hours saved, and purchase-error rate. If usage and completion improve without increasing errors, expand the intervention. If not, conduct further workflow observation before funding more features.

### What The Direct Answer Does Well

- Focuses on the 58% pre-submission drop-off.
- Chooses one low-adoption segment.
- Prioritizes workflow friction and status visibility over feature volume.
- Suggests a pilot and relevant metrics.

### What The Direct Answer Does Not Preserve

- Which interview statements are observations, requests, or untested explanations.
- The specific progress plant supervisors are trying to make.
- Push, pull, anxiety, habit, and alternative forces affecting adoption.
- The mathematical or causal link from product behavior to ROI.
- Exact thresholds for scaling, adjusting, or stopping.

## Run B: Three-Skill Reasoning Chain

### Method Selection

| Sequence | Skill | Why it changes the work | Intermediate output |
|---|---|---|---|
| 1 | [`evidence-map`](../skills/evidence-map/SKILL.md) | Separates observed behavior from requested features and product-team hypotheses | Adoption evidence ledger and validation gaps |
| 2 | [`jobs-to-be-done`](../skills/jobs-to-be-done/SKILL.md) | Defines the progress sought by one segment and the forces keeping the manual workaround in place | Job statement, forces map, and adoption tests |
| 3 | [`metrics-tree`](../skills/metrics-tree/SKILL.md) | Connects activation and workflow behavior to measurable operating value and ROI | Outcome, drivers, leading indicators, guardrails, and cadence |

`kano-model` is not used because feature satisfaction categories do not yet explain the observed non-adoption mechanism.

### Step 1: Evidence Map

**Evidence question:** What is supported strongly enough to choose the first adoption intervention?

| Evidence item | Type | Strength | Relevance | Interpretation |
|---|---|---:|---:|---|
| Monthly active use is 23% | Product metric | Strong | High | Broad adoption is low |
| Plant-supervisor monthly use is 12% | Segment metric | Strong | High | Priority segment is identifiable |
| 58% of starters leave before submission | Funnel metric | Strong | High | Primary behavioral break is pre-submission |
| Completed digital requests take 3.1 vs 4.8 days manually | Comparative metric | Medium | High | Value exists after completion |
| 11 users report duplicate data entry | Interview observation | Medium | High | Likely workflow friction |
| 9 users report uncertainty after submission | Interview observation | Medium | High | Likely anxiety and status gap |
| 7 users request a dashboard | Feature request | Weak | Medium | Does not prove adoption impact |
| AI assistant will improve adoption | Product-team assumption | Missing | Medium | No supporting test |
| More training will fix low use | Product-team assumption | Weak | Medium | No segment-level evidence |

**Evidence gaps**

| Gap | Fastest test | Why it matters |
|---|---|---|
| Exact field or step causing abandonment | Instrument field-level exit and observe 10 supervisors | Determines the minimum workflow change |
| Whether prefill is technically feasible | Two-day data-integration spike | Tests delivery feasibility |
| Coordination time by channel | One-week time diary for digital and manual requests | Converts behavior into financial value |
| Error-rate difference | Sample 100 completed requests per channel | Protects against faster but lower-quality processing |

**Effect on the next step:** A dashboard and AI assistant are not supported as first interventions. The next method should explain the supervisor's progress and switching barriers.

### Step 2: Jobs To Be Done

**Target circumstance**

- Target customer: plant supervisor handling an urgent maintenance purchase.
- Trigger: equipment requires a part or service and delay may affect production.
- Current workaround: email a known buyer, attach a spreadsheet, and chase status through messages.
- Progress sought: submit a complete request once, know who owns it, and avoid production delay.

**Job statement**

> When an urgent plant purchase is needed, I want to submit the required information once and see who is acting on it, so I can keep production moving without repeatedly chasing Procurement.

**Forces of progress**

| Force | Evidence | Strength | Product implication |
|---|---|---:|---|
| Push: manual approval takes 4.8 days | Comparative metric | Medium | Faster completion is meaningful |
| Pull: digital completion takes 3.1 days | Product metric | Medium | Show expected progress and owner |
| Anxiety: request may disappear after submission | 9 interviews | Medium | Confirmation and visible status are essential |
| Anxiety: wrong supplier or cost center may delay work | Duplicate-entry complaints | Medium | Prefill and validation should reduce risk |
| Habit: known buyer responds to email | Current workaround | Medium | Product must preserve human escalation path |
| Pull toward dashboard | 7 requests | Weak for supervisors | May serve managers, not the first adoption job |

**Adoption tests**

| Barrier or outcome | Offer response | Test | Signal |
|---|---|---|---|
| Re-entry burden | Prefill supplier and cost center | A/B pilot in two plants | Lower abandonment at affected fields |
| Status anxiety | Confirmation, named approver, and expected next step | Prototype usability test then live pilot | Fewer status-chasing messages |
| Habit of emailing buyer | Forward email into a prefilled draft | Assisted pilot | Digital completion without forcing abrupt behavior change |
| Need for urgent escalation | Visible escalation path | Scenario test | Users can resolve stalled requests without bypassing controls |

**Effect on the next step:** The first intervention is a supervisor workflow package, not a general feature release. Metrics must connect it to business value.

### Step 3: Metrics Tree

**Top outcome:** Monthly net operating value from FlowApprove for plant purchase requests.

**Illustrative logic**

```text
Gross monthly value
= completed digital requests
  x verified coordination hours saved per request
  x loaded hourly cost
  + verified delay or error cost avoided

Net value
= gross monthly value - allocated monthly product and support cost
```

| Level | Metric | Formula or definition | Why it matters | Owner |
|---|---|---|---|---|
| Outcome | Net operating value | Gross verified value minus allocated cost | Tests ROI directly | Finance business partner |
| Driver | Completed digital requests | Eligible requests x activation x start-to-submit conversion | Connects adoption to value | Product lead |
| Driver | Repeat digital use | Users completing a second request within 30 days / activated users | Distinguishes trial from adoption | Product analytics |
| Driver | Hours saved | Manual coordination time minus digital coordination time | Converts workflow change to value | Process owner |
| Driver | Approval-cycle reduction | Manual median minus digital median | Tests operational outcome | Procurement operations |
| Guardrail | Purchase error rate | Requests returned or corrected / completed requests | Prevents speed from reducing quality | Procurement control |

**Effect on the decision:** The product change becomes a measurable value hypothesis. Scale depends on verified workflow value and repeat behavior, not on an isolated increase in logins.

## Decision Artifact

**Current decision:** Run a six-week pilot for 60 plant supervisors in two plants. Test prefill, submission confirmation, visible status, and a controlled escalation path. Do not build the dashboard or AI assistant as part of this test.

### Pilot Scorecard

| Metric | Baseline | Scale threshold | Adjust or stop threshold | Review |
|---|---:|---:|---:|---|
| Start-to-submit conversion | 42% | At least 65% | Below 52% after two iterations | Weekly |
| Plant-supervisor monthly use | 12% | At least 30% in pilot population | Below 20% by week 4 | Biweekly |
| 30-day repeat use | Establish in week 1 | At least 45% | Below 30% | End of pilot |
| Median approval cycle | 3.1 days for completed digital requests | 3.1 days or less | More than 3.5 days | Weekly |
| Coordination time saved | Missing | At least 45 minutes per completed request | Less than 20 minutes | Weeks 3 and 6 |
| Purchase error rate | Establish from sample | No more than 1 percentage point above manual baseline | Guardrail breached for two weeks | Weekly |
| ROI evidence | Current annual cost is $480,000 | Annualized verified value shows a credible path above cost | No credible path after pilot and sensitivity test | End of pilot |

**Model revision gate:** If conversion improves but repeat use does not, the main problem is likely ongoing workflow value rather than initial usability.

## Comparison

| Deliverable | Direct AI answer | Method-skill chain |
|---|---|---|
| First intervention | Prefill, status, and targeted pilot | Same intervention, tied to evidence and one job |
| Research discipline | General observations | Fact, request, and assumption ledger |
| User understanding | Friction and uncertainty | Circumstance, progress, forces, and workaround |
| ROI logic | Track usage and hours saved | Explicit behavior-to-value equation |
| Experiment | Two-plant pilot | Population, duration, thresholds, guardrails, and model revision |
| Feature control | Defer dashboard and AI | Documents why they are not first-order tests |

## What The Comparison Shows

The direct answer proposes a credible product improvement. The method chain shows why that intervention is preferable to popular feature requests, how user behavior produces financial value, and what result would prove that improved usability still does not solve the underlying adoption problem.
