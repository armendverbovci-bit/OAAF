# Operational AI Assurance Framework (OAAF)

## Deciding, on evidence, whether a deployed AI system should keep operating

Version 1.0, November 2026

Armend Verbovci

Licensed under Creative Commons Attribution 4.0 International (CC BY 4.0)

*This is the plain-text version of the framework. A formatted PDF and an assessment workbook are in the [downloads](downloads/) folder.*

## Document control

| Item | Detail |
|---|---|
| Title | Operational AI Assurance Framework (OAAF) |
| Version | 1.0 (first public release) |
| Date | November 2026 |
| Author | Armend Verbovci |
| Contact | armendverbovci@gmail.com |
| Companion files | Assessment workbook, plain-text version, machine-readable data file (oaaf.json) and an AI assistant skill for running an assessment, published with this document. |
| DOI | https://doi.org/10.5281/zenodo.24352952 |
| Licence | CC BY 4.0. You may copy, adapt and use this framework, including commercially, provided you credit the author. |
| Status | Published method for use and comment. Not a standard, certification scheme or legal guidance. |

**Suggested citation.** Verbovci, A. (2026). *Operational AI Assurance Framework (OAAF), Version 1.0.* Zenodo. https://doi.org/10.5281/zenodo.24352952

**Statement of independence.** This framework was developed by the author in a personal capacity, in his own time, from public standards, published literature and general professional knowledge. It does not use, describe or represent the material, systems, data or views of any employer, client or regulator. All worked examples are synthetic.

**Disclaimer.** OAAF is offered as a practical method. Applying it does not establish compliance with any law or standard, and it does not replace sector regulation, legal advice or a competent safety assessment. Users remain responsible for their own decisions.

**Feedback.** Comments, corrections and results from real use are welcome by email. Later versions will be published under the same record.

## Contents

1. Executive summary
2. Introduction
3. Principles
4. Scoping the system
5. Operational control states
6. Requirements
7. Assessment and decision rules
8. Using OAAF in practice
9. Limitations and open issues

- Annex A. Templates
- Annex B. Worked examples
- Annex C. Reproducibility check
- Annex D. Mapping to ISO/IEC 42001, NIST AI RMF and the EU AI Act
- Annex E. Origins: what was borrowed from aviation safety management
- Annex F. Glossary
- Annex G. Development history
- References
- About the author

## 1. Executive summary

**In one sentence:** OAAF is a free, sector-neutral method for deciding, on evidence, whether a deployed AI system or AI agent should keep operating, be restricted, or be stopped, adapted from aviation safety management.

Most AI assurance effort today goes into the period before a system is switched on: evaluations, benchmarks, red-teaming, impact assessments and policy sign-off. Far less goes into the question an operator actually faces every day once the system is live: **should this system keep running, in this form, right now?** NIST's report on monitoring deployed AI systems (NIST AI 800-4, March 2026) put it plainly: monitoring best practice, validated methods and even common terminology are still nascent.

Safety-critical industries solved a version of this problem decades ago. Aviation does not certify an aircraft or an air traffic system and then walk away. It runs a continuous operating regime: named people with real authority, defined degraded modes, occurrence reporting, investigation, controlled change and a formal return to service after something goes wrong.

OAAF adapts that operating regime to AI-enabled systems in any sector. It is deliberately small:

- **One scoping step.** Define the system as it is actually operated, list what it can *do*, and rate each capability with a two-question test. This sets how much of the framework applies.
- **Five operational control states**, from Normal to Unacceptable, covering both the model and the service around it.
- **36 requirements** in seven domains. A low-consequence system needs only 8 of them. A high-consequence system needs all 36.
- **Fixed decision rules.** Findings are rated Routine, Significant or Critical by rule, not by assessor judgement, and lead to one of three outcomes per capability: Ready, Ready with Conditions, or Not Ready. There is no percentage score, because one missing stop mechanism should never be averaged away by thirty satisfied requirements elsewhere.

Two ideas distinguish OAAF from most governance material:

- **Negative-space assurance.** The riskiest path in many AI systems is the one where nobody looks: the transaction auto-approved, the case not escalated, the job quietly deprioritised. OAAF requires that path to be monitored.
- **Boundary assurance.** In worked examples, real gaps sat between functions rather than inside them: model risk and IT operations, change management and vendor management, training and incentive design, internal change control and an external model provider. OAAF asks questions that cross those seams.

OAAF does not replace ISO/IEC 42001, the NIST AI Risk Management Framework or the EU AI Act. It sits underneath them, turning their requirements into an operating regime for one deployed system. Annex D maps the connections.

## 2. Introduction

### 2.1 Purpose

OAAF gives an organisation a repeatable way to decide whether a specific AI-enabled system, in its actual operating context, is acceptable to operate, needs restricting, or should be stopped, and to keep making that decision as the system, its data and its suppliers change.

### 2.2 The problem it addresses

Pre-deployment evaluation is necessary but it is not enough, for four reasons that come up again and again in practice:

1. **The model is not the system.** Harm usually arises from the combination of model, prompts, data, tools, integrations, people and process, not from the model alone.
2. **Systems change after approval.** Prompts are edited, knowledge sources are updated, and third-party model providers change behaviour, sometimes without notice.
3. **Oversight concentrates where it is visible.** Human review tends to focus on what the AI flags. What it silently approves or ignores often gets no review at all.
4. **Nobody has defined what "degraded" means.** Many organisations can switch a system off, but few have agreed in advance when they would, who decides, and what happens next.

Regulation is moving in the same direction. The EU AI Act requires providers of high-risk systems to run post-market monitoring (Article 72) and report serious incidents (Article 73), requires those systems to be designed for effective human oversight (Article 14), and requires deployers to monitor their operation (Article 26). Following the Digital Omnibus on AI, Regulation (EU) 2026/1744, which entered into force on 27 July 2026, high-risk obligations for Annex III systems apply from 2 December 2027 and for Annex I systems from 2 August 2028. The Commission is due to publish guidance, including a template for the post-market monitoring plan, by 2 September 2027. Organisations therefore have a window to build a sound operating regime rather than retrofit one.

### 2.3 What OAAF is, and what it is not

| OAAF is | OAAF is not |
|---|---|
| A method for running and assessing one deployed AI-enabled system | An organisation-wide AI management system (that is ISO/IEC 42001) |
| Usable by a governance, risk, safety or operations lead without an AI engineering background | A model evaluation or testing method |
| Sector-neutral, from customer service to critical infrastructure | A certification scheme or a claim of legal compliance |
| Proportionate: depth scales with consequence | A maturity model or a scoring system |

### 2.4 Who it is for

- Owners and operators of deployed AI systems, including AI agents, who need to know whether they are in control.
- Heads of AI governance, risk, compliance or internal audit who need an operational test beneath their policy framework.
- Independent assessors who need a method that two people can apply and reach the same answer.
- Regulators and sector bodies looking for a practical example of in-service AI assurance.

Typical situations where OAAF helps:

- an AI system or agent is about to go live and someone has to sign off that it is ready;
- a system is already live and nobody has defined when it should be restricted or switched off;
- a model provider has changed or updated the model behind a live system;
- something has gone wrong and the system needs to be stopped, investigated and returned to service;
- an organisation needs a practical basis for post-market monitoring or deployer monitoring under the EU AI Act.

### 2.5 Origin

OAAF adapts the logic of the Safety Management System used in aviation (ICAO Annex 19 and ICAO Doc 9859): accountable managers, hazard identification, defined operating limits, occurrence reporting, investigation, management of change and return to service. It borrows the logic, not the vocabulary. No aviation knowledge is needed to use it. Annex E sets out exactly what was borrowed and how it was translated.

### 2.6 Relationship to other work

OAAF builds on and complements existing frameworks rather than competing with them.

- **ISO/IEC 42001** sets the management system for AI at organisation level. **ISO/IEC 23894** covers AI risk management and **ISO/IEC 42005** covers AI system impact assessment across the lifecycle. **ISO/IEC TS 8200** addresses controllability of automated AI systems. OAAF assumes these may exist and provides the system-level operating regime beneath them.
- The **NIST AI Risk Management Framework** (Govern, Map, Measure, Manage) defines outcomes and can be applied to individual systems. OAAF offers one concrete way to carry out Measure and Manage once a system is in service. **NIST AI 800-4** (2026) describes why monitoring deployed AI is hard; OAAF proposes a practical structure for doing it.

Several 2026 publications cover ground adjacent to OAAF and are worth reading alongside it:

- **Operational AI Deployment Assurance (OADA)** (Alsayed, 2026) proposes a governance layer between evaluation and deployment, with deployment readiness classifications, escalation states and assurance scores, demonstrated on fairness in facial recognition.
- **AI-GRACE** (Cuneo, Chun and Khanna, 2026) operationalises agentic AI use cases from objectives and obligations to architecture, including an Agent Operating Envelope and Risk-Aligned Independence Levels.
- **CAGE-1** (Sure, 2026) evaluates enterprise AI agents across twelve control dimensions, with a focus on proving that an action was controlled before it became binding.
- **The Decision Evidence Maturity Model** (Solozobov, 2026) tests whether the evidence an agent system keeps can actually answer a specific question about a specific decision.
- **Toward Continuous Assurance for the Democratization of AI Agent Creation in Industry** (Levy and Berger, 2026) proposes scheduled readiness checks and assurance records for agents built by non-engineers, whose behaviour can degrade silently when models, tools or permissions change.
- **AI as an Aviation Safety Decision Maker** (Clark, 2026) argues that aviation safety management systems must evolve to treat AI as both a hazard source and a safety control.

OAAF's contribution is not any single concept in that list. Operating envelopes, escalation states and evidence requirements appear in several of them. Its contribution is the combination of: an in-service operating regime that runs for the life of the system, including occurrence learning, change from external providers and return to service; explicit treatment of negative space and organisational seams; sector neutrality; and decision rules designed so that two assessors reach the same conclusion from the same evidence.

## 3. Principles

1. **System of operation.** Assurance applies to the AI-enabled system as deployed and operated: the model, data, software, tools, interfaces, people, processes and environment. Assurance of the model alone does not establish that operation is acceptable.
2. **Context dependency.** Operational risk depends on context, not capability. The same model can be harmless answering staff questions and consequential approving payments.
3. **Proportionality.** Rigour scales with consequence. Applying the same depth to every system is a design fault, not thoroughness.
4. **Continuous, not one-off.** Assurance is maintained for the life of the system through a mix of continuous, periodic and event-triggered activity. It does not mean watching every parameter every second.
5. **Assurance is not performance.** Good performance figures are not the same as evidence that you would notice if performance degraded.
6. **Acceptable, not absolute.** The objective is acceptable operation within a defined context and risk tolerance, not a claim that a system is "safe".
7. **Independence in proportion to risk.** Higher-consequence systems warrant review by someone other than the team that built or runs them.
8. **Accountability requires authority.** A named owner who cannot actually restrict or stop the system is a control deficiency, not a control.
9. **Negative-space assurance.** Assurance must cover what the system does not flag, escalate or surface. The path where AI output becomes action with no human looking is usually the least examined and the most consequential.

## 4. Scoping the system

Scoping decides how much of OAAF applies. It takes four steps and is recorded on a single System Card (Annex A, Template A1).

### 4.1 Define the system of operation

Record, in plain language:

- purpose and intended outcome;
- users, operators and people affected by the output;
- AI components (models, providers, versions) and non-AI components;
- data and knowledge sources, tools and integrations, and the permissions the system holds in other systems;
- the human oversight arrangement;
- assumptions and known limitations;
- a **materiality threshold**: the level of financial, operational or other consequence above which the organisation treats an error as material. Where no threshold is set, any consequence that moves money, commits the organisation to a third party or communicates externally on its behalf is treated as material.

### 4.2 List the capabilities

A **capability** is something the system can cause to happen: approve a transaction, send a reply, reorder a queue, raise an order, recommend a diagnosis, flag a case for review. Assess capabilities, not models. One model often supports several capabilities with very different consequences.

For AI agents, treat each class of tool action as a capability.

### 4.3 Rate each capability: the two-question test

**Question 1. Human acceptance.** Must a human actively accept this specific output before it takes effect?

- Only a positive act counts: an approval, a release, a click to send. A human being *able* to see the output, sampling a proportion of outputs, or being able to intervene afterwards does **not** count.

**Question 2. Consequence.** If the output is wrong, would the resulting harm either:

- (a) be **irreversible before it would normally be detected**, or
- (b) exceed the **materiality threshold**?

Reversible means the organisation can fully restore the previous state itself, without a third party's cooperation, before harm materialises. Judge the reversibility of the *consequence*, not of the action. Reordering a work queue can be undone in seconds; the two-hour delay it caused cannot.

| | Q2: Yes | Q2: No |
|---|---|---|
| **Q1: No** (no positive human acceptance) | **High** | Medium |
| **Q1: Yes** (positive human acceptance) | Medium | Low |

Capability Criticality is a three-value attribute used in exactly two places: setting the minimum Consequence Tier (4.4) and rating findings (7.3). **It is not a second tier system and should not be extended into one.**

### 4.4 Set the Consequence Tier

The Consequence Tier sets which requirements apply. It is a scoping device, not a maturity rating: a Tier 1 system is not an immature system.

| Factor | Tier 1 | Tier 2 | Tier 3 |
|---|---|---|---|
| Worst credible harm | Minor financial or reputational | Operational disruption, material financial loss, harm to individuals that is recoverable | Severe or irreversible harm to people, critical services or the organisation |
| Reversibility | Easily reversed | Reversible with effort | Difficult or impossible to reverse |
| Autonomy | Easily overridden | Meaningful autonomy with a human in the loop | Limited or no practical override window |

The highest applicable factor governs. **A system with any High capability is at least Tier 2.**

### 4.5 Note the regulatory overlay

Legal or sector classification (for example EU AI Act high-risk status, financial, medical or aviation regulation) is recorded separately. It adds obligations regardless of tier but does not itself set the tier. A system can be Tier 2 by consequence and carry heavy regulatory obligations, or the reverse.

### 4.6 Draw the decision paths

For every Medium or High capability, draw its **Operational Decision Path**:

> Input → AI processing → AI decision → human acceptance *or no human acceptance* → system action → external consequence

The "no human acceptance" branch must always be drawn, even if the answer is "this never happens". Drawing it is what exposes negative space.

### 4.7 What applies

| Consequence Tier | Requirements that apply |
|---|---|
| Tier 1 | 8 |
| Tier 2 | 25 |
| Tier 3 | 36 |

## 5. Operational control states

Control states describe **what controls must be in place**, not how well the model is scoring. A system can post excellent metrics while in a poor operational state, and the reverse.

| State | Meaning | Typical controls | Typical decision authority |
|---|---|---|---|
| S0 Normal | Operating within validated conditions | Standard monitoring | Operating team |
| S1 Degraded | Operating conditions or assurance margin have deteriorated, but remain within tolerance | Enhanced monitoring, increased sampling | Operating team, owner informed |
| S2 Restricted | Operation permitted only with added controls | Human acceptance inserted on affected capabilities, reduced limits | Accountable owner |
| S3 Contained | Capability constrained, isolated or switched to fallback | Fallback process, controlled recovery | Accountable owner, management informed |
| S4 Unacceptable | Continued operation exceeds accepted risk | Stop the affected capability | Accountable owner or anyone with stop authority |

States must be defined for both:

- **model condition**: quality, drift, unexpected behaviour; and
- **service condition**: availability, latency, stale or missing data, monitoring outages, dependency failure. For each capability, record what happens when the AI is unavailable: does the process fail safe or fail open?

States apply per capability. One capability can be Restricted while others run normally.

Leaving S3 or S4 requires the return-to-service process (P5-04).

## 6. Requirements

There are 36 requirements in seven domains. Each is tagged with the tier from which it applies; it then applies at every higher tier. Requirements marked **◆** are **control-critical**: they are the requirements an organisation needs in order to detect a problem and stop it. They carry more weight in the decision rules (Section 7.3).

Each requirement is written to pass one test: *what specific evidence would make an assessor say yes rather than no?* The typical evidence column gives examples, not an exhaustive list.

### P1 Accountability and authority

| ID | Requirement | Tier | Typical evidence |
|---|---|---|---|
| P1-01 ◆ | A named individual is designated as accountable owner of the deployed system. | 1 | Appointment record, System Card |
| P1-02 | Technical, risk and business responsibilities for the system are documented and assigned to named roles. | 2 | Responsibility matrix |
| P1-03 | An escalation path from the accountable owner to senior management is documented. | 2 | Procedure, organisation chart |
| P1-04 | An accountability statement sets out the responsibilities of suppliers, model providers and deployers. | 3 | Signed statement, contract clauses |
| P1-05 ◆ | (a) The accountable owner holds documented authority to *initiate* restriction or stopping of any capability; and (b) a mechanism exists to *execute* it within a response time set for each capability, and it has been exercised within the review period. | 2 | Delegation of authority, runbook, test or exercise record |

### P2 Context, hazards and risk

| ID | Requirement | Tier | Typical evidence |
|---|---|---|---|
| P2-01 | Foreseeable misuse and credible failure modes relevant to the operating context are documented. | 1 | Hazard list on the System Card |
| P2-02 | Structured hazard identification covers model, data, integration, infrastructure, human-factors and external-dependency failure modes, including hazards whose controls are owned by other functions (see the Boundary Rule, 7.2). | 2 | Hazard log with owner and interface recorded for each hazard |
| P2-03 | Risk is assessed using a documented method covering at least severity and likelihood, and where relevant detectability and control effectiveness. | 2 | Risk register, method statement |
| P2-04 | The risk record is reviewed at a defined interval of no more than 12 months, and after every material change and every occurrence classed as Deviation or above. | 3 | Review records |

### P3 Operational boundaries

| ID | Requirement | Tier | Typical evidence |
|---|---|---|---|
| P3-01 ◆ | Conditions requiring restriction, containment or cessation of operation are documented and provided to the accountable owner. | 1 | Operating limits on the System Card |
| P3-02 ◆ | Operational control states are defined for this system, covering both model condition and service condition, including fail-safe or fail-open behaviour when the AI is unavailable. | 2 | State definitions |
| P3-03 ◆ | Measurable trigger conditions are defined for each transition between states. | 2 | Trigger table, alert configuration |
| P3-04 ◆ | Decision authority is defined for each transition between states. | 3 | Authority table |
| P3-05 | State transitions and their rationale are logged. | 3 | State log |
| P3-06 ◆ | The system's technical permissions in other systems are limited to the capabilities declared in the System Definition. Any further permission is removed, or declared and assessed. | 2 | Permission inventory compared with capability list |

### P4 Continuous assurance

| ID | Requirement | Tier | Typical evidence |
|---|---|---|---|
| P4-01 ◆ | Operational performance is monitored and reviewed by a named person at a defined interval. | 1 | Dashboard, review record |
| P4-02 | Safety-relevant indicators are distinguished from general performance indicators. | 2 | Indicator list with classification |
| P4-03 ◆ | Targets and trigger levels are defined for safety-relevant indicators and linked to the state triggers in P3-03. | 2 | Indicator specification |
| P4-04 | Assurance coverage is reported using hazard-signal mapping: for each hazard in the risk record, whether an operational signal exists that would detect it before harm (full, partial or none), reported as three counts. *Interim method; see 9.2.* | 3 | Hazard-signal map |
| P4-05 | Both leading indicators (conditions that precede harm) and lagging indicators (harm and near misses that occurred) are tracked at a defined interval. | 3 | Indicator reports |
| P4-06 ◆ | For each High capability, monitoring covers the path where output became action with no human acceptance, using sampling, outcome tracking or independent checks. | 2 | Negative-space monitoring records |

### P5 Occurrence and learning

| ID | Requirement | Tier | Typical evidence |
|---|---|---|---|
| P5-01 | A channel exists for reporting problems with system output, and users and affected staff know how to use it. | 1 | Channel, reports received |
| P5-02 | Occurrences are classified using a taxonomy that distinguishes at least deviation, near miss and incident (see Annex F). | 2 | Occurrence log |
| P5-03 | Occurrences classed as Deviation or above are investigated for cause, and corrective action is recorded. | 2 | Investigation reports, action log |
| P5-04 | A return-to-service process is defined and evidenced for any capability leaving S3 or S4. | 3 | Return-to-service records |
| P5-05 | Lessons from occurrences are fed into the risk record (P2) and the change process (P6). | 3 | Traceable updates |

### P6 Change assurance

| ID | Requirement | Tier | Typical evidence |
|---|---|---|---|
| P6-01 | A configuration baseline is maintained that is sufficient to reconstruct the system that produced any given output: model and version, prompts and instructions, tools and the permissions they used, data and knowledge sources, persistent memory or context stores, and thresholds. | 1 | Configuration records, version history |
| P6-02 | The operational significance of each change is assessed and recorded before release, judged by its potential effect on behaviour, boundaries, controls or risk, not by its technical size. | 1 | Change records |
| P6-03 | Changes are classified by impact level (administrative, configuration, behavioural, functional, boundary, safety control), with evidence requirements that increase with impact. | 2 | Change procedure, classified changes |
| P6-04 | Changes classed as behavioural or higher are re-assessed against the risk record and operational boundaries before release. | 3 | Re-assessment records |
| P6-05 | External dependencies that can materially change system behaviour, including model providers and third-party data, are subject to change detection, version pinning, supplier notification, or evidenced compensating monitoring, in proportion to their significance. | 2 | Supplier terms, version pinning, drift monitoring |

### P7 Human and AI operation

| ID | Requirement | Tier | Typical evidence |
|---|---|---|---|
| P7-01 | Every human role that receives, accepts or acts on system output is identified. | 1 | Role list |
| P7-02 | Risks of over-reliance and under-reliance are assessed for each such role. | 2 | Human factors assessment |
| P7-03 | Escalation authority and criteria are documented for each such role. | 2 | Procedure |
| P7-04 | Competency requirements are defined and current for everyone holding intervention authority. | 3 | Training and competency records |
| P7-05 | Degradation of oversight effectiveness is assessed, including workload, alert saturation, complacency and incentives that discourage challenge. | 3 | Assessment, workload data |

**Cross-cutting concerns.** Cybersecurity (including prompt injection and manipulation), data integrity, privacy and resilience are not separate domains. They appear as hazards in P2, as service conditions in P3 and as dependencies in P6. Organisations with existing security and privacy controls should record them as evidenced controls under the Boundary Rule (7.2), not duplicate them.

## 7. Assessment and decision rules

This section turns individual findings into a decision. Without it, a conclusion is an informed impression of a compliance table, and two competent assessors can reach opposite conclusions from the same evidence. Annex C shows that this happened in testing, and that these rules corrected it.

### 7.1 Assessment values

| Value | Meaning |
|---|---|
| Compliant | The control is defined, in use, and there is a record showing it operating within the review period. At Tier 1, defined and in use is sufficient. |
| Partially Compliant | The control is defined but is incomplete, inconsistently applied, or has no record of operation. |
| Not Demonstrated | The available evidence is insufficient to establish that the control is defined and in use. This does not mean the control does not exist. |
| Not Applicable | The requirement is above the system's Consequence Tier. |

The **review period** is 12 months, or the time since the last material change, whichever is shorter.

### 7.2 Evidence rules

**Rule 1. Evidenced, not assumed.** A control owned by another function counts only if it is evidenced against *this* system: a named owner, a record the assessor has seen, and a demonstrated link to this system's decision path. "IT will have a disaster recovery plan" and "vendor management covers that supplier" are assumptions. An assumed control is Not Demonstrated. It may be recorded as a candidate compensating control pending evidence.

**Rule 2. Absence of harm is not evidence.** A clean incident record does not downgrade an unassessed risk, and it is not evidence of control effectiveness where the monitoring that would have detected the harm is absent or its coverage is unknown (P4-04, P4-06).

**Rule 3. The Boundary Rule.** A hazard that can affect a capability's decision path must be recorded in the system's hazard identification even when its control is owned by another function. The record names the owning function and the interface. Recording a hazard is not a claim to own its control, but a hazard owned elsewhere and recorded nowhere is invisible.

### 7.3 Finding criticality

Every Partially Compliant or Not Demonstrated result becomes a finding. Its criticality is derived, not judged:

| | Affects a High capability | Affects a Medium capability | Affects only Low capabilities |
|---|---|---|---|
| **Control-critical requirement ◆** | **Critical** | Significant | Routine |
| **Other requirement** | Significant | Significant | Routine |

- A finding that applies to more than one capability, such as the absence of an accountable owner, is rated separately for each capability it affects.
- An assessor may raise a finding by one level, with written reasons. A finding may never be lowered.
- There are three levels only. There is no fourth level and no numeric score.

### 7.4 Decision outcomes

Decisions are made **per capability**:

| Outcome | When it applies |
|---|---|
| **Not Ready** | Any open Critical finding affecting the capability. |
| **Ready with Conditions** | Significant findings and no open Critical finding. Each condition has an owner and a date. |
| **Ready** | Routine findings only, or none. |

A Critical finding is cleared only by:

- an evidenced compensating control (Rule 1); or
- a documented, time-limited risk acceptance signed by someone holding authority under P1-05(a) to stop that capability. The capability then becomes Ready with Conditions and the acceptance is listed as a condition.

Neither remediation intent nor a large number of Compliant results elsewhere clears a Critical finding.

A capability that is already operating and is found Not Ready should move to S2 Restricted (if a human acceptance step or reduced limits can be inserted) or S3 Contained until the finding is cleared.

### 7.5 Why decisions are made per capability

"Restrict the auto-approval path, continue the review path" is usually a better outcome than stopping everything or nothing. It gives the organisation a proportionate action it can actually take, which makes it more likely to act at all.

### 7.6 When to assess

| Trigger | Scope |
|---|---|
| Before first operation | Full assessment |
| Periodic review, at least every 12 months | Full assessment |
| Change classed as behavioural or higher (P6-03) | Affected capabilities |
| Before leaving S3 or S4 (return to service) | Affected capabilities |
| Proposal to retire, or a capability no longer meets its purpose | Retirement decision |

<div class="keep"><h3>7.7 The operating loop</h3>
<p>OAAF runs as a continuous loop rather than a one-off approval:</p>
<blockquote><p>Define → Assess → Bound → Monitor → Detect → Intervene → Report → Investigate → Correct → Verify → Return, Restrict or Retire → Learn → back to Define</p></blockquote></div>

## 8. Using OAAF in practice

### 8.1 Quick start for a Tier 1 system

A Tier 1 system needs eight requirements. In practice this is one afternoon and one page:

1. Complete the System Card (Template A1): purpose, owner, capabilities, materiality threshold.
2. Run the two-question test on each capability. If any is High, the system is Tier 2; stop and use 8.2.
3. List foreseeable misuse and failure modes (P2-01).
4. Write down when you would restrict or stop the system (P3-01).
5. Name who reviews performance and how often (P4-01).
6. Set up a way for users to report problems (P5-01).
7. Record the current configuration and start a change log that notes the likely effect of each change (P6-01, P6-02).
8. List the people who act on the output (P7-01).

### 8.2 Full assessment

1. **Scope** (Section 4). Complete the System Card and capability register. Agree the tier and criticality with the accountable owner before collecting evidence.
2. **Draw decision paths** for Medium and High capabilities, including the no-acceptance branch.
3. **Collect evidence** against each applicable requirement. Prefer records of operation over documents.
4. **Record findings** in the findings register (Template A3), applying Rules 1 to 3.
5. **Derive criticality** using the table in 7.3.
6. **Decide per capability** using 7.4, and record the decision (Template A4).
7. **Set the control state** of any capability found Not Ready.
8. **Agree conditions**, owners and dates, and schedule the next trigger.

### 8.3 Independence

At Tier 1, the operating team may assess its own system. At Tier 2, the assessment should be reviewed by someone outside the team that runs the system. At Tier 3, it should be carried out by someone independent of both the build and the operating teams, internal or external.

### 8.4 AI agents

Agents are covered by the same structure. In practice:

- each class of tool action is a capability and gets its own two-question test;
- P3-06 matters most: agents often run with broad service credentials, so the system can do more than its declared capabilities, and anything undeclared has never been rated;
- persistent memory and context stores are part of the configuration baseline (P6-01), because they change behaviour without any code or prompt change;
- the agent's choices *not* to act (items skipped, deprioritised or deferred) are negative space and fall under P4-06 when the capability is High.

### 8.5 Starting from an existing management system

Organisations with ISO/IEC 42001, a model risk framework or a functioning change board will find much of OAAF already in place. Assess the existing controls against the requirements using Rule 1, and concentrate effort on the requirements marked ◆, P4-06 and P6-05, where mature organisations most often have gaps (see Annex B2).

## 9. Limitations and open issues

OAAF is version 1.0. Its weaknesses are stated plainly so that users can judge them.

### 9.1 Reproducibility is designed for, not yet proven

The decision rules were tested by having two assessor viewpoints reassess the same synthetic case (Annex C). They converged under these rules where they had diverged before. That is a design check, not a field trial. Independent assessors applying OAAF to the same real system is the next test needed. Readers who run one are invited to share the results.

Some judgement remains, in particular:

- whether a materiality threshold set by the organisation is reasonable (the assessor records it but does not replace it);
- the boundary between tiers for systems near a threshold; and
- the line between Partially Compliant and Compliant for controls with weak records.

### 9.2 Assurance coverage is measured crudely

Hazard-signal mapping (P4-04) counts only hazards that have been identified. It says nothing about hazards nobody has thought of. It is an interim method and is deliberately reported as three counts rather than a percentage, to avoid false precision.

### 9.3 The worked examples are synthetic

They were designed to stress the framework, not drawn from real organisations. Real use will find problems they did not.

### 9.4 What has deliberately not been built

- A maturity model. No decision in the worked examples needed one.
- A certification or accreditation scheme. This would first need demonstrated agreement between independent assessors.
- A numeric score. See 7.3.
- Software tooling beyond the templates in Annex A.

### 9.5 Rules for future versions

New components will be added only when a worked case or real use shows that the existing framework cannot reach a reliable decision without them. Each addition will cite the finding that justifies it. This rule has been applied to every change since the first draft (Annex G).

## Annex A. Templates

### A1 System Card

| Field | Entry |
|---|---|
| System name and version | |
| Purpose and intended outcome | |
| Accountable owner (P1-01) | |
| Users, operators and affected people | |
| AI components (model, provider, version) | |
| Data and knowledge sources | |
| Tools, integrations and permissions held | |
| Human oversight arrangement | |
| Materiality threshold | |
| Assumptions and known limitations | |
| Foreseeable misuse and failure modes (P2-01) | |
| Conditions for restriction or stopping (P3-01) | |
| Regulatory overlay | |
| Consequence Tier and reason | |
| Date and next review | |

### A2 Capability register

| Capability | Q1: positive human acceptance? | Q2: irreversible before detection or above materiality? | Criticality | Response time to stop (P1-05b) | Decision path drawn? |
|---|---|---|---|---|---|
| | Yes / No | Yes / No | High / Medium / Low | | Yes / No |

### A3 Findings register

| Finding no. | Requirement | Value | Evidence seen | Capability affected | Control-critical? | Criticality | Action, owner, date |
|---|---|---|---|---|---|---|---|
| | | Partially Compliant / Not Demonstrated | | | Yes / No | Routine / Significant / Critical | |

### A4 Decision record

| Capability | Open Critical | Open Significant | Outcome | Control state set | Conditions | Accepted risks (signatory, expiry) |
|---|---|---|---|---|---|---|
| | | | Ready / Ready with Conditions / Not Ready | S0 to S4 | | |

A spreadsheet version of these templates, with the two-question test and the criticality rules built in, is published alongside this document.

## Annex B. Worked examples

All three examples are synthetic. They were chosen to stress different parts of the framework: an ungoverned system, a well-governed one, and an AI agent with a deliberately ambiguous capability.

### B1 InboxAgent: an ungoverned enterprise agent

**System.** An agent reads incoming customer emails, retrieves account and order data, drafts replies, and can issue refunds and reschedule deliveries without human review. Ambiguous cases go to a human queue. It uses an external foundation model that the provider updates without notice. Monitoring covers uptime and latency only. No AI risk record exists. Changes go through standard software release with no behavioural review. No materiality threshold has been set.

**Scoping.**

| Capability | Q1 | Q2 | Criticality |
|---|---|---|---|
| Issue refund or reschedule without review | No | Yes (no threshold set, so financial actions are material by default) | High |
| Draft reply for human sending | Yes | No | Low |
| Route ambiguous case to human queue | No | No | Medium |

Consequence Tier: Tier 2 (system has a High capability; harm is financial and recoverable).

**Key findings.**

| Requirement | Value | Criticality | Note |
|---|---|---|---|
| P1-01 ◆ | Partially Compliant | Critical for refunds | Engineering lead is de facto owner, no designation |
| P3-03 ◆ | Not Demonstrated | Critical | No triggers for restricting refunds |
| P4-06 ◆ | Not Demonstrated | Critical | Refunds issued without review are never sampled |
| P6-01 | Partially Compliant | Significant | Internal code versioned; provider model version not recorded |
| P6-05 | Not Demonstrated | Significant | Silent provider updates neither detected nor pinned |
| P3-06 ◆ | Not Demonstrated | Critical | Agent's account can also edit customer records, an undeclared capability |

**Decision.** Refunds and rescheduling: Not Ready, move to S2 (insert human acceptance) until an owner is designated, triggers exist, permissions are reduced and unreviewed refunds are sampled. Routing to the human queue: Ready with Conditions. Drafting replies for human sending: Ready.

**What it shows.** Uptime monitoring is not operational assurance. The sharpest single finding was the invisible provider update: a live, unassessed change to a system that moves money.

### B2 SentryModel: a well-governed fraud-scoring system

**System.** A bank scores every transaction for fraud. Above threshold, transactions are held for a trained analyst. Below threshold, they are approved automatically and no human ever sees them. The bank has a certified AI management system, a model risk function, independent validation, a change board and quarterly committee reporting.

**Scoping.**

| Capability | Q1 | Q2 | Criticality |
|---|---|---|---|
| Auto-approve below threshold | No | Yes (funds leave; fraud loss not recoverable before detection) | High |
| Hold and flag above threshold | Yes (analyst decides) | Yes (a wrongly released hold moves funds) | Medium |

Consequence Tier: Tier 3 (regulated financial service, irreversible loss, limited override window).

**Result.** In the original assessment, 21 of 34 requirements were Compliant. The organisation does most of this well. The findings that remained all sat at **seams between functions**:

| Requirement | Value | Criticality | Seam |
|---|---|---|---|
| P1-05 ◆ | Partially Compliant | Critical | Owner can initiate; execution needs a change board quorum taking 48 hours or more |
| P2-02 | Not Demonstrated | Significant | Infrastructure outage hazards left to IT, recorded nowhere (Boundary Rule) |
| P3-02 ◆ / P3-03 ◆ | Partially / Not Demonstrated | Critical | Model-quality states defined; no state or trigger for scoring service outage, so fail-open versus fail-closed is undefined |
| P4-06 ◆ | Not Demonstrated | Critical | All review effort is on held transactions; auto-approved transactions are not sampled |
| P6-05 | Not Demonstrated | Significant | Third-party device and identity data feeds managed as general vendors, outside AI change control |
| P7-02 | Not Demonstrated | Significant | Analyst throughput targets create an unassessed incentive to accept the score |

**Decision.** Auto-approve capability: Not Ready, move to S2 (lower the auto-approval limit and add outcome sampling) until fail-safe behaviour and negative-space monitoring are evidenced. Hold and flag capability: Ready with Conditions.

**What it shows.** A mature management system can still leave the most consequential path, the one where no human looks, almost unexamined. Governance effort follows visibility. OAAF's questions are designed to follow consequence instead.

### B3 Field Operations Agent: an agent with an ambiguous capability

This example was written to test the hardest open question from earlier drafts: whether two assessors would rate an ambiguous capability the same way.

**System.** A utility uses an AI agent to support maintenance of its water distribution network. It reads sensor alerts and work orders, drafts the weekly maintenance schedule for a supervisor to approve, raises purchase orders for spare parts below 2,000 euros, and continuously reorders the field crews' job queue. Supervisors can see the queue and can override it, but do not approve individual reorderings. Emergency bursts are handled by a separate control room, not the agent. The agent uses a third-party model through an API, keeps persistent notes between sessions, and runs under a shared service account in the asset management system. The materiality threshold is set at 2,000 euros.

**Scoping, and the ambiguous capability.**

| Capability | Q1 | Q2 | Criticality |
|---|---|---|---|
| Draft weekly schedule | Yes (supervisor approves) | No | Low |
| Raise purchase orders below 2,000 euros | No | No (below threshold; supplier cancellation within 24 hours, checked daily) | Medium |
| Reorder crew job queue | **No** (supervisors can see and override, but that is visibility, not positive acceptance) | **Yes** (reordering is reversible, but a delayed repair is not; a deprioritised leak keeps leaking) | **High** |

Under the earlier wording ("output becomes action without human review"), the queue capability could reasonably have been rated Medium by one assessor ("supervisors review the queue") and High by another. The two-question test removes that ambiguity: visibility does not count as acceptance, and reversibility is judged on the consequence, not the action.

Consequence Tier: Tier 2 (High capability present; harm is service disruption and water loss, recoverable; emergencies handled outside the agent).

**Key findings.**

| Requirement | Value | Criticality | Note |
|---|---|---|---|
| P3-06 ◆ | Not Demonstrated | Critical | Shared service account can also close work orders and edit asset records, neither declared |
| P4-06 ◆ | Not Demonstrated | Critical | No check on jobs the agent pushed down the queue |
| P3-03 ◆ | Partially Compliant | Critical | Triggers exist for model errors, none for stale sensor data |
| P6-01 | Partially Compliant | Significant | Persistent agent notes not in the configuration baseline; past decisions cannot be reconstructed |
| P7-02 | Not Demonstrated | Significant | Supervisors have stopped checking the queue order since the agent was introduced |
| P6-05 | Partially Compliant | Significant | Model version pinned, but provider deprecation dates not tracked |

**Decision.** Queue reordering: Not Ready, move to S2 (supervisor accepts any change that moves a job down by more than one day) until permissions are reduced and deprioritised jobs are sampled. Purchase orders: Ready with Conditions. Schedule drafting: Ready.

**What it shows.** Two new elements were needed for agents, and both were added to the framework as a result of this example: P3-06 (permissions limited to declared capabilities), and the inclusion of persistent memory and tool permissions in the configuration baseline (P6-01).

## Annex C. Reproducibility check

During development, the SentryModel case (B2) was assessed from two deliberately different viewpoints: a strict assessor and a pragmatic one, working from identical evidence. Under the earlier draft, which had no decision rules, they reached opposite conclusions. The causes were specific:

| Cause | Example | Fix in version 1.0 |
|---|---|---|
| "Authority to stop" was ambiguous | Owner could initiate a stop; execution took 48 hours | P1-05 split into authority to initiate and mechanism to execute |
| Unclear whether to record hazards owned elsewhere | Infrastructure outage left to IT | Rule 3, the Boundary Rule |
| Assumed controls treated as evidence | "IT probably has a recovery plan" | Rule 1, evidenced not assumed |
| Absence of harm used to downgrade risk | Automation bias rated low because nothing had gone wrong | Rule 2, absence of harm is not evidence |
| Severity left to judgement | Same gap rated Critical by one and Significant by the other | Criticality derived by rule (7.3) |

Re-running the contested items under version 1.0:

| Item | Before (strict / pragmatic) | After (both) |
|---|---|---|
| P1-05 | Not Demonstrated / Partially Compliant | Partially Compliant, Critical |
| P2-02 | Not Demonstrated / Not Applicable | Not Demonstrated, Significant |
| P3-03 | Critical / Significant | Not Demonstrated, Critical |
| P6-05 | Critical / Significant | Not Demonstrated, Significant |
| P7-02 | Significant / Routine | Not Demonstrated, Significant |
| Overall | Not Ready / Ready with Conditions | Auto-approve: Not Ready. Hold and flag: Ready with Conditions |

The remaining dependency was that both assessors had to assign the same Capability Criticality in the first place. The two-question test in 4.3 was written to close that gap, and was then checked against the ambiguous capability in B3. This is a design check by one author taking two viewpoints, not a trial with independent assessors (see 9.1).

## Annex D. Mapping to ISO/IEC 42001, NIST AI RMF and the EU AI Act

This mapping is indicative. It shows where OAAF requirements support the operation of other frameworks. Meeting an OAAF requirement does not by itself establish conformity with any standard or compliance with any law.

| OAAF domain | ISO/IEC 42001 clauses | NIST AI RMF functions | EU AI Act articles |
|---|---|---|---|
| P1 Accountability and authority | 5 Leadership | Govern | 14 Human oversight; 17 Quality management system; 26 Deployer obligations |
| P2 Context, hazards and risk | 6 Planning; 8 Operation | Map | 9 Risk management system |
| P3 Operational boundaries | 8 Operation | Manage | 9 Risk management; 14 Human oversight |
| P4 Continuous assurance | 9 Performance evaluation | Measure | 26 Deployer monitoring; 72 Post-market monitoring |
| P5 Occurrence and learning | 10 Improvement | Manage | 72 Post-market monitoring; 73 Serious incident reporting |
| P6 Change assurance | 6 Planning; 8 Operation | Manage; Govern | 12 Record-keeping; 15 Accuracy, robustness and cybersecurity |
| P7 Human and AI operation | 7 Support | Govern; Map | 14 Human oversight; 26 Deployer obligations |

Related standards that OAAF users may find relevant: ISO/IEC 23894 (AI risk management), ISO/IEC 42005 (AI system impact assessment), ISO/IEC TS 8200 (controllability of automated AI systems), ISO/IEC TR 5469 (functional safety and AI systems), and ISO/IEC 5338 (AI system life cycle processes).

## Annex E. Origins: what was borrowed from aviation safety management

OAAF was developed by someone who spent more than two decades in air traffic control and air navigation safety management. The question behind it was simple: the AI industry is meeting a problem that aviation met long ago, namely that a system which worked in testing is not, on that evidence alone, acceptable to operate. What can be borrowed, and what has to change?

The aviation Safety Management System (ICAO Annex 19) has four components. OAAF maps to them as follows:

| Aviation SMS component | What it means in aviation | OAAF equivalent |
|---|---|---|
| Safety policy and objectives | Accountable manager, postholders, management commitment | P1, Principle 8 |
| Safety risk management | Hazard identification, risk assessment and mitigation | P2, P3, Capability Criticality |
| Safety assurance | Performance monitoring, management of change, continuous improvement | P4, P5, P6 |
| Safety promotion | Training, competence, communication, safety culture | P7, P5-01 |

Specific concepts and how they were translated:

| Aviation concept | OAAF translation | What changed |
|---|---|---|
| Accountable manager with real authority | Accountable owner with authority to initiate, plus a mechanism to execute (P1-05) | Split into initiate and execute, because AI ownership is often separated from infrastructure control |
| Flight envelope and operating limits | Operational boundaries and control states (P3) | Applied to both model condition and service condition |
| Degraded modes and contingency procedures | Control states S1 to S4 | Applied per capability rather than to the whole system |
| Mandatory and voluntary occurrence reporting | Occurrence classification and investigation (P5) | Taxonomy adapted to AI behaviour, including the unsafe condition category |
| Management of change | Change assurance (P6) | Extended to changes made by external model providers without notice |
| Return to service after maintenance or an event | Return-to-service process (P5-04) | Unchanged in principle |
| Safety performance indicators and targets | Safety-relevant indicators, targets and trigger levels (P4) | Separated from general performance indicators |
| Just culture | Reporting channel (P5-01) and assessment of incentives (P7-05) | Framed around oversight effectiveness |

What was deliberately *not* borrowed: certification by a single authority before operation, prescriptive rules for specific technologies, and aviation's vocabulary. AI systems change too often, and are used in too many sectors, for those to transfer.

## Annex F. Glossary

**Accountable owner.** The named individual answerable for the operation of a deployed AI system.

**Assurance coverage.** The extent to which identified hazards would be detected by operational monitoring before harm occurs.

**Boundary assurance.** Assurance that examines the interfaces between organisational functions, where controls are most often assumed rather than evidenced.

**Capability.** Something the system can cause to happen.

**Capability Criticality.** High, Medium or Low, assigned by the two-question test (4.3).

**Consequence Tier.** Tier 1, 2 or 3, setting which requirements apply (4.4).

**Control-critical requirement.** A requirement marked ◆, needed to detect a problem and stop it.

**Control state.** S0 Normal, S1 Degraded, S2 Restricted, S3 Contained or S4 Unacceptable (Section 5).

**Materiality threshold.** The level of consequence above which the organisation treats an error as material (4.1).

**Negative space.** Outputs that became action with no human acceptance, and choices the system made not to act, flag or escalate.

**Occurrence classes.**

- *Observation*: a potentially relevant anomaly.
- *Unsafe condition*: a state in which a safety barrier is missing or degraded, though nothing has gone wrong yet (for example, monitoring has silently stopped).
- *Deviation*: the system operated outside expected behaviour.
- *Near miss*: an occurrence that did not cause harm but could have under reasonably foreseeable circumstances.
- *Incident*: an occurrence that caused harm.
- *Serious incident*: an incident with high-severity consequences, or one meeting a regulatory definition of serious incident.

**Operational Decision Path.** The route from input to external consequence for one capability, including the branch with no human acceptance (4.6).

**Review period.** 12 months, or the time since the last material change, whichever is shorter.

**System of operation.** The AI-enabled system as deployed and operated, including people and process.

## Annex G. Development history

OAAF was developed between September and November 2026 through a sequence of drafts, each reviewed critically before the next was written. The review discipline was that nothing could be added without a specific finding to justify it.

| Stage | What changed | Why |
|---|---|---|
| Concept | Aviation safety management logic proposed as a basis for AI operational assurance | Gap between pre-deployment evaluation and in-service operation |
| Architecture | Seven domains, system definition, control states | Need for a structure usable outside aviation |
| Requirements | 34 testable requirements, tiered | Need for something an assessor can test |
| Precision pass | Unfalsifiable wording removed; consequence separated from regulatory status | Several requirements could not be assessed objectively |
| Stress test | Proportionality confirmed across low, medium and high consequence | Risk that the framework was overkill for simple systems |
| Case B1 | External provider change, configuration baseline | Silent model updates were invisible |
| Case B2 | Negative-space and boundary assurance | Mature governance still missed the unreviewed path |
| Reproducibility check | Evidence rules, derived criticality, per-capability decisions | Two assessors reached opposite conclusions |
| Version 1.0 | Two-question criticality test, materiality threshold, P3-06, agent guidance, interim coverage method, Tier 1 quick start | Ambiguous capability in Case B3; the low-value automatic action problem; adoption cost for small systems |

## References

1. Regulation (EU) 2024/1689 laying down harmonised rules on artificial intelligence (Artificial Intelligence Act). Official Journal of the European Union, 2024.
2. Regulation (EU) 2026/1744 (Digital Omnibus on AI), amending Regulation (EU) 2024/1689. Official Journal of the European Union, L series, 24 July 2026. In force 27 July 2026.
3. National Institute of Standards and Technology. *Artificial Intelligence Risk Management Framework (AI RMF 1.0)*, NIST AI 100-1, 2023.
4. Rao, A., Keller, A., Kalra, N., Steed, R., Kwegyir-Aggrey, K., Klyman, K., Staheli, D. and Bergman, A. *Challenges to the Monitoring of Deployed AI Systems*, NIST AI 800-4. Center for AI Standards and Innovation, March 2026. doi:10.6028/NIST.AI.800-4
5. ISO/IEC 42001:2023 Information technology. Artificial intelligence. Management system.
6. ISO/IEC 23894:2023 Information technology. Artificial intelligence. Guidance on risk management.
7. ISO/IEC 42005:2025 Information technology. Artificial intelligence. AI system impact assessment.
8. ISO/IEC 42006:2025 Information technology. Artificial intelligence. Requirements for bodies providing audit and certification of artificial intelligence management systems.
9. ISO/IEC TS 8200:2024 Information technology. Artificial intelligence. Controllability of automated artificial intelligence systems.
10. ISO/IEC TR 5469:2024 Artificial intelligence. Functional safety and AI systems.
11. ICAO. *Annex 19 to the Convention on International Civil Aviation: Safety Management.*
12. ICAO. *Doc 9859, Safety Management Manual.*
13. Regulation (EU) No 376/2014 on the reporting, analysis and follow-up of occurrences in civil aviation.
14. European Union Aviation Safety Agency. *EASA Concept Paper on Artificial Intelligence*, Proposed Issue 03, June 2026.
15. Alsayed, K. A. *Operational AI Deployment Assurance: Governance-State Orchestration Under Threshold-Sensitive Deployment Conditions.* arXiv:2605.27827, May 2026.
16. Cuneo, J., Chun, D. and Khanna, G. *AI-GRACE: A Use-Case Operationalization Framework for Agentic AI.* arXiv:2609.21192, 2026.
17. Sure, R. W. *CAGE-1: Control, Assurance, and Governance Evaluation for Enterprise Agentic AI.* arXiv:2607.03510, July 2026.
18. Solozobov, O. *Decision Evidence Maturity Model for Agentic AI: A Property-Level Method Specification.* arXiv:2605.04093, 2026.
19. Clark, A. *AI as an Aviation Safety Decision Maker.* Zenodo, August 2026. Record 22156499.
20. Levy, N. and Berger, H. *Toward Continuous Assurance for the Democratization of AI Agent Creation in Industry.* arXiv:2607.21495, 2026.

## About the author

Armend Verbovci is an air navigation services professional with more than twenty years in aviation. He spent ten years as a tower and approach rated air traffic controller, and more than a decade leading safety, quality and compliance functions for air navigation service providers in Europe and the Middle East, including serving as a regulatory safety postholder, developing safety cases for airspace and system changes, and directing more than 400 safety investigations. He holds an MSc in Aviation Safety from Florida Institute of Technology and an IATA Diploma in ANSP Management, and has a background in IT engineering.

His interest is in the practical transfer of safety management from industries that have operated high-consequence systems for decades into AI, where the same questions are now being asked: who is accountable, how would we know, and what happens next.

Contact: armendverbovci@gmail.com
