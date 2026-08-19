# Proposal Shaping Extension

Use this extension when a deal or pursuit needs a client proposal, executive pitch, storyline, or proposal deck. The purpose is to make the proposal decision-led rather than feature-led.

## Core Principle

A strong proposal does not jump from a generic WHY to a preselected WHAT.

Build the missing bridge:

**Trigger / decision → what good looks like → what must be assessed → what is known vs unknown → target mechanism → enabling solution → adoption / assurance → next decision**

The bridge explains the problem deeply enough that the solution feels derived rather than asserted.

## 1. Define the Offer Before Writing the Story

State which offer is actually being sold:

- Advisory: diagnose and design the target state.
- Implementation: implement a largely defined target state.
- Hybrid advisory + implementation: diagnose, design, then enable and validate.
- Managed service: operate an agreed capability over time.

If the offer is unclear, do not hide the ambiguity with a generic platform story. Mark the offer hypothesis and validate it with the account / client-facing team.

## 2. Separate Four Evidence States

Never turn missing client information into invented client pain.

Use four explicit states:

| State | Meaning | Proposal treatment |
|---|---|---|
| Confirmed client fact | Directly supported by client input or reliable evidence | Use as client-specific context |
| Target-state POV | What good practice should look like in the domain | Present as a point of view, not a diagnosis |
| Working hypothesis | Plausible issue that still needs validation | Label as hypothesis / to validate |
| Diagnostic finding | Evidence-based conclusion from assessment | Use only after diagnostic work has occurred |

Before discovery, a proposal may show the target-state framework and the questions to assess. It must not show a fabricated maturity score, gap heatmap, or client-specific weakness.

## 3. Build the WHY-to-WHAT Bridge

A proposal should normally answer these questions in order:

1. **What has changed?** What external, business, technology, regulatory, or operating-model shift creates a decision now?
2. **Why does it matter to this buyer?** What management responsibility, value at stake, risk, or operating constraint is affected?
3. **What does good look like?** What dimensions define a credible target state?
4. **What specifically should be examined?** For each dimension, what management questions, evidence, indicators, and decision points matter?
5. **What do we know today?** Separate confirmed facts from unknowns and hypotheses.
6. **What mechanism is required?** Roles, decision rights, policies, lifecycle, governance cadence, exception handling, and assurance.
7. **What technology enables the mechanism?** Show how the platform operationalizes controls rather than replacing governance.
8. **How will people actually use it?** Include adoption, change management, training, incentives, operating rhythm, and feedback loops.
9. **What is the next buyer decision?** Discovery, pilot, approval, implementation, or scale decision.

Generic industry education should be compressed unless it changes the buyer's decision. Assume senior executives already understand basic industry facts.

## 4. Framework Depth Test

A framework is not useful because it has five boxes. Each dimension must contain four things:

| Requirement | Test |
|---|---|
| Definition | Is the dimension distinct from the others? |
| Management questions | Can an executive ask concrete questions about it? |
| Observable evidence / indicators | Can the organisation assess it without opinion-only scoring? |
| Decision implication | Would a weakness change a priority, control, investment, or action? |

If a dimension cannot pass all four tests, refine it before using it in the proposal.

## 5. Diagnostic Logic Without Premature Diagnosis

Before diagnostic work, present:

- the target-state dimensions;
- the concrete questions and evidence that would be assessed;
- an illustrative maturity logic if useful;
- the diagnostic outputs the client would receive.

Only after evidence collection should the proposal or follow-on deliverable show:

- current-state scores;
- strong / medium / weak ratings;
- gap heatmaps;
- prioritised exposures;
- remediation priorities.

A light maturity scale can be used after evidence exists, for example:

- 0 — Unmanaged
- 1 — Emerging
- 2 — Defined
- 3 — Controlled
- 4 — Scaled and Assured

Every score needs a stated evidence basis such as policies, interviews, inventory data, workflow walkthroughs, logs, control tests, or audit evidence.

## 6. Mechanism Before Platform

Do not present technology as governance itself.

A robust proposal distinguishes three layers:

### Governance mechanism

- scope and risk appetite;
- ownership and decision rights;
- classification and approval;
- policy and guardrails;
- lifecycle and material-change control;
- exception and escalation;
- governance cadence and management reporting.

### Enabling platform

- inventory / registry;
- runtime policy enforcement;
- human approval gates;
- monitoring and observability;
- evidence capture and audit integration;
- integration with authoritative enterprise systems.

### Adoption and assurance

- business onboarding;
- role readiness and training;
- lightweight change management;
- first-, second-, and third-line assurance where relevant;
- control testing, incidents, feedback, and continuous improvement.

The platform should operationalize the mechanism and federate with authoritative systems where possible rather than create a duplicate source of truth.

## 7. Minimum Viable Governance POV

Especially in fast-moving AI environments, business adoption often moves faster than central governance. The answer should not be a heavy bureaucracy that the business routes around.

A strong POV is:

> Governance must be strong at material decision points and lightweight everywhere else.

Design control intensity according to delegated authority, materiality, risk, reversibility, and evidence requirements. Make human intervention explicit where accountability cannot be delegated.

## 8. Agent Governance Pressure Test

For Agent Governance, use a target-state framework such as the following as a starting hypothesis. Refine it for the client and regulatory context rather than treating the five dimensions as universal truth.

| Dimension | Core management question | What to examine |
|---|---|---|
| Purpose, Portfolio & Value | What Agents exist, why do they exist, and are they worth operating? | Active / staged / paused / retired inventory; use cases; business purpose; value hypothesis; adoption; cost; duplication; portfolio priority |
| Accountability & Decision Rights | Who owns the Agent, what authority is delegated, and when must a human decide? | Business and technical owners; approval rights; autonomy level; human-AI decision boundary; non-delegable decisions; escalation rights |
| Risk, Lifecycle & Policy | How is each Agent classified, approved, changed, reviewed, suspended, and retired? | Risk tier; data / model / tool / action policies; development-to-production lifecycle; prompt / model / tool / permission changes; material-change criteria; periodic review |
| Runtime Control & Evidence | Can the organisation control, observe, reconstruct, and recover material Agent actions? | Workload identity; in-path policy coverage; human gates; blocked / exception events; monitoring; incident handling; source / version / policy lineage; evidence completeness; resilience |
| Operating Model, Adoption & Assurance | How does governance run day to day without slowing the business? | Governance roles and forums; first / second / third line responsibilities; onboarding; training; change management; business adoption; control testing; audit findings; deviation learning; continuous improvement |

Examples of management questions are more useful than generic feature descriptions:

- How many Agents are live, staged, paused, or retired?
- Which Agents are high risk or highly autonomous?
- Which high-risk Agents lack a named accountable owner or mandatory human gate?
- Which Agents have undergone a material change without revalidation?
- Which runtime actions were blocked, overridden, or escalated?
- Can every material action be reconstructed with source, version, policy, and human evidence?
- Which Agents create value, which need remediation, and which should be stopped?

Do not populate these answers for a client until the diagnostic has produced evidence.

## 9. Derive the Roadmap From the Logic

Do not force every proposal into a standard 12-week implementation plan. The roadmap should follow the offer and the evidence available.

For a hybrid governance offer, a credible sequence is:

1. **Diagnose and prioritise** — inventory, interviews, evidence review, target-state assessment, priority gaps.
2. **Design the target mechanism** — roles, decision rights, policies, lifecycle, operating cadence, platform requirements.
3. **Enable and pilot** — configure the platform around one or more priority use cases and test normal / exception scenarios.
4. **Validate and mobilise** — test control effectiveness, evidence, adoption, operating readiness, and scale prerequisites.

Duration is a hypothesis until scope, architecture, approvals, dependencies, and client responsibilities are known.

## 10. C-Level Storyline Test

Before finalising the main deck, test whether the buyer can answer these questions after the first few pages:

- What decision do I need to make?
- Why now for my organisation?
- What does good look like?
- What do we know and what still needs diagnosis?
- Why is the proposed mechanism the right response?
- What role does the platform play?
- What is the smallest credible next commitment?

If the deck mainly teaches industry basics, lists product features, or explains implementation before these questions are answered, the storyline is not ready.

## 11. Proposal Quality Gate

Before delivery, check:

- The offer type is explicit.
- Client facts, target-state POV, hypotheses, and diagnostic findings are not mixed.
- The proposal does not invent a client maturity score before diagnosis.
- WHY is developed deeply enough to derive WHAT.
- The target-state framework passes the framework depth test.
- Governance mechanism is separated from enabling technology.
- Adoption and change management are visible where the solution changes ways of working.
- The governance design is as lightweight as the risk allows.
- Every proposed capability traces to a management need, control gap, or validated hypothesis.
- The roadmap is derived from scope and dependencies rather than copied from a template.
- Generic content is removed when a C-level audience is likely to know it already.
- The final page asks for a specific buyer decision or commitment.
