# Career Decision: Direct ChatGPT Answer vs Method-Skill Chain

> **Example note:** This scenario was created for demonstration. Avery, Northstar Mobility, the roles, events, timelines, and thresholds do not refer to a specific person or company.

This example tests a practical question: **what does a method-skill chain produce beyond the final recommendation?**

It uses the same input twice:

1. a direct answer with no named method skill;
2. a four-skill reasoning chain selected because each method creates a useful intermediate deliverable.

This is a controlled illustration, not a scientific LLM benchmark. Results can vary by model and run. The comparison does not claim that named methods automatically make a conclusion correct.

## Shared Input

```text
Avery is a product operations manager at Northstar Mobility, a 400-person software company.
The company has announced an acquisition, and Avery's role may be redesigned or
consolidated during the next four to six months.

A written retention plan would pay Avery a bonus after an integration milestone in five months.
A director has mentioned that a product strategy role may open, but there is no approved
requisition, budget, or interview process. Two external recruiters have made contact, but Avery
has no interview or offer. Avery's savings would cover about three months of normal expenses.

Should Avery resign now, stay passively for the retention bonus, focus on the possible internal
role, or remain employed while testing internal and external options in parallel?
```

## Run A: Direct Answer, No Method Skill

**Instruction**

```text
Answer the question directly. Do not use or name any consulting framework or method.
```

**Representative output**

> Avery should probably not resign now. There is no confirmed internal role or external offer, the retention bonus is documented, and three months of savings provides limited room for a long search.
>
> A more practical approach is to remain employed while building alternatives. Avery should confirm the retention-plan conditions, ask the director when the possible role will be approved or rejected, and turn recruiter interest into actual interviews. The current job should still be done professionally, but Avery should avoid waiting passively for the acquisition to determine the outcome.
>
> Set a review point in four weeks. If the internal role becomes funded or an external offer appears, compare the real options. If neither develops, continue the search and reassess whether the retention bonus still compensates for the growing role risk.
>
> In short: protect income for now and create options in parallel.

### What The Direct Answer Does Well

- Gives a sensible recommendation quickly.
- Uses the written retention plan and limited financial runway.
- Treats the possible internal role as unconfirmed.
- Suggests parallel option-building and a review point.

### What The Direct Answer Does Not Preserve

- An inspectable fact-versus-assumption workpaper.
- A stakeholder map showing who controls the retention plan, reorganization, and possible roles.
- A scenario set showing what futures the recommendation must survive.
- An explicit comparison showing why one option outranks the others.
- An execution scorecard showing owners, success measures, and evidence that would reverse the recommendation.

## Run B: Four-Skill Reasoning Chain

### Method Selection

| Sequence | Skill | Why it changes the work | Intermediate output |
|---|---|---|---|
| 1 | [`evidence-map`](../skills/evidence-map/SKILL.md) | Prevents acquisition uncertainty from being treated as proof that Avery's role will disappear | Fact/assumption boundary and evidence gaps |
| 2 | [`stakeholder-power-map`](../skills/stakeholder-power-map/SKILL.md) | Separates a manager's opinion, HR policy, budget authority, and hiring authority | Decision rights and stakeholder actions |
| 3 | [`scenario-planning`](../skills/scenario-planning/SKILL.md) | Tests the decision across different acquisition, internal-role, and market outcomes | Robust moves, contingent moves, and signposts |
| 4 | [`weighted-scorecard`](../skills/weighted-scorecard/SKILL.md) | Makes the trade-offs and assumptions behind the preferred option visible | Ranked options, sensitivity, and decision gates |

Methods were selected before execution. A method was included only when its output created a useful workpaper or materially changed the action, validation, risk judgment, or decision threshold.

### Step 1: Evidence Map

**Evidence question:** Is there enough evidence to justify resigning before another option is executable?

| Evidence item | Type | Strength | Decision relevance |
|---|---|---:|---:|
| The acquisition has been formally announced | Stated fact | Strong | High |
| Avery's role may change during integration | Stated fact, outcome unknown | Medium | High |
| A written retention plan pays after a five-month milestone | Documented fact | Strong | High |
| The possible internal role has no requisition, budget, or interview process | Stated fact | Strong | High |
| Two recruiters have contacted Avery; no interview or offer exists | Stated fact | Strong | High |
| Savings cover about three months of normal expenses | Stated estimate | Medium | High |
| The acquisition will eliminate Avery's role | Assumption | Missing | High |
| The director's interest will become an approved role | Assumption | Weak | High |
| External roles will match Avery's current level and compensation | Assumption | Missing | High |

**Evidence gaps most likely to change the decision**

1. Retention-plan eligibility, payment conditions, and treatment if the role is consolidated.
2. The integration decision timetable and who approves the future organization design.
3. Requisition, budget owner, level, and decision date for the possible internal role.
4. External-market evidence: qualified interviews, role level, and compensation range.
5. A personal minimum cash-runway threshold.

**Effect on the next step:** The evidence supports active preparation, but not immediate resignation. The next analysis must identify who controls each unknown.

### Step 2: Stakeholder Power Map

| Stakeholder | Relevant power | Current stance | Evidence confidence | Next ask |
|---|---|---|---|---|
| Current manager | Shapes present scope and performance narrative | Wants integration continuity; future role view may be incomplete | Medium | Confirm role-design process and near-term expectations |
| HR / integration office | Owns retention terms and reorganization process | Policy-based, not a career sponsor | Strong | Confirm written eligibility, dates, and consolidation treatment |
| Product strategy director | May sponsor an internal role | Interested, but has no approved requisition | Low | Ask for business problem, budget owner, approval path, and decision date |
| External hiring managers | Control external offers | Unknown; recruiter contact is not hiring evidence | Strong | Convert recruiter contact into qualified interviews |
| Avery | Controls search intensity, financial threshold, and acceptance gates | Can protect option value | Strong | Define exit gates before urgency decides |

**Effect on the next step:** The possible internal role is an option to qualify, not a plan. HR controls the retention facts, while hiring managers control offer evidence.

### Step 3: Scenario Planning

**Horizon:** the next six months.

| Plausible scenario | What happens | Robust move | Triggered response |
|---|---|---|---|
| Role continues after integration | Avery's scope remains useful, although priorities change | Maintain performance, document outcomes, and test the market | Decide whether the redesigned role meets long-term goals |
| Role is consolidated before the milestone | Employment or bonus eligibility changes earlier than expected | Verify policy, preserve runway, and build external traction now | Accelerate the search when a formal consolidation notice appears |
| Internal strategy role is approved | Requisition, budget, level, and process become real | Keep the relationship active without stopping market tests | Compare the written internal option against acceptance gates |
| External offer arrives | A hiring process produces an executable alternative | Build evidence and interview readiness | Move only when the offer passes the agreed gates |

**No-regret moves**

- Confirm the retention plan and integration timetable in writing.
- Convert current achievements into portable, quantified evidence.
- Ask the director for concrete internal-role milestones.
- Turn recruiter contact into interviews instead of treating interest as an option.
- Set a minimum financial-runway and offer-acceptance threshold.

**Effect on the next step:** Remaining employed while building options performs reasonably across all four scenarios. Immediate resignation only becomes preferable if a separate red-line condition appears.

### Step 4: Weighted Scorecard

Scoring uses a 1–5 scale. Weights and scores are explicit illustrative assumptions, not measured facts.

| Criterion | Weight | Resign now | Stay passively | Internal role as primary bet | Stay + parallel options |
|---|---:|---:|---:|---:|---:|
| Near-term financial resilience | 25% | 1 | 5 | 4 | 4 |
| Future role and growth fit | 20% | 3 | 1 | 4 | 4 |
| Option value | 20% | 3 | 1 | 2 | 5 |
| Reversibility | 15% | 1 | 4 | 3 | 5 |
| Current evidence strength | 10% | 1 | 3 | 2 | 4 |
| Energy and search sustainability | 10% | 2 | 2 | 3 | 3 |
| **Weighted total / 5** | **100%** | **1.85** | **2.75** | **3.15** | **4.25** |

**Sensitivity check**

- If acquisition conditions make continued employment unacceptable, resignation becomes a gated exception rather than a scored preference.
- If the internal role becomes a funded written offer, it should be rescored as a real option.
- If an external offer exceeds the agreed threshold, the parallel strategy has produced an executable choice.

## Decision Artifact

**Current decision:** Remain employed while actively qualifying internal and external options. Do not resign based only on acquisition uncertainty or informal interest.

**Acceptance gates for a move**

- written role, level, and reporting line;
- scope and decision authority consistent with the work;
- confirmed compensation, budget, and start date;
- adequate employment security and financial runway;
- stronger long-term positioning than the redesigned current role.

**Next 30 days**

| Action | Owner | Timing | Evidence produced |
|---|---|---|---|
| Confirm retention terms and integration decision dates | Avery + HR | 1 week | Written financial and timing boundary |
| Qualify the possible internal role | Avery + strategy director | 2 weeks | Requisition path, budget owner, and decision date or a clear “not yet” |
| Run a focused external-market test | Avery | 30 days | Qualified conversations, interviews, level and compensation feedback |
| Build a quantified achievement portfolio | Avery | 30 days | Reusable evidence for internal and external selection |

**Review gate:** Reassess after 30 days or immediately when a formal role decision, written offer, retention-policy change, or red-line condition appears.

### Execution And Evaluation Scorecard

The thresholds below are illustrative and should be calibrated to the user's market, seniority, and time horizon.

| Decision track | Leading signal | Success metric / decision gate | Adjust or stop trigger | Review timing |
|---|---|---|---|---|
| Current role and retention | Written retention terms and integration dates | Financial value and role risk can be compared using confirmed conditions | Eligibility becomes unclear or role risk changes materially | Weekly |
| Internal opportunity | Director identifies the role problem, budget owner, and approval path | A written, funded role passes all acceptance gates | No requisition path or decision date after two direct checks | 2 weeks |
| External market | Qualified hiring-manager conversations and interviews | At least one written offer passes role, authority, compensation, and security gates | After 30 days, no qualified conversations or repeated level mismatch | 30 days |
| Financial resilience | Savings plan and monthly expense baseline are current | Runway remains above Avery's minimum threshold through the search horizon | Runway falls below the threshold without an executable option | Monthly |
| Overall decision readiness | One or more options becomes executable | A formal option passes every acceptance gate and is better than the current path | No option passes the gates; continue the parallel strategy and revise search inputs | Monthly or on material event |

This scorecard separates **activity** from **success**. Recruiter messages and interviews are leading signals; a written option that passes the agreed gates is the decision outcome.

## Comparison

| Deliverable | Direct answer | Four-skill chain |
|---|---|---|
| Final recommendation | Stay and build options in parallel | Same current recommendation |
| Intermediate workpapers | Not preserved | Evidence map, stakeholder map, scenario set, and weighted scorecard |
| Reasoning trace | Concise narrative | Each method records its input, output, and effect on the next step |
| Action plan | Useful general actions | Named actions with owner, timing, and evidence produced |
| Success measures | Broad review advice | Leading signals, success gates, adjust/stop triggers, and review cadence |
| Reversal conditions | Broad | Written gates and evidence that triggers rescoring |
| Reuse | Answer is mainly consumed once | Workpapers can support review, workshop discussion, or a later decision update |
| Effort | Fast and concise | More work, justified when the decision consequence is high |

## What The Comparison Shows

The method chain did **not** create a dramatically different headline recommendation. The main difference is what remains available after the answer.

The direct answer provides a reasonable conclusion and several useful actions. The method-based run additionally provides:

1. inspectable intermediate outputs for every selected method;
2. a trace from input to method output to the next analytical step;
3. an action plan with owners, timing, and expected evidence;
4. success metrics, decision gates, and conditions for adjusting or reversing the recommendation.

The method chain does not guarantee that the conclusion is more accurate. It makes the reasoning reviewable, the plan executable, and the result measurable. For a low-consequence question, the direct answer may be enough. For a high-consequence decision, those additional deliverables can justify the extra effort.

Chinese version: [`career-change-comparison.zh-CN.md`](career-change-comparison.zh-CN.md).
