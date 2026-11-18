---
name: oaaf-assessment
description: Assess whether a deployed AI system or AI agent should keep operating, be restricted or be stopped, using the Operational AI Assurance Framework (OAAF v1.0). Use when someone needs to sign off an AI system or agent for go-live, set up monitoring or kill-switch criteria for a live AI system, decide what to do after an AI incident or a model provider update, run an operational readiness review, or build a practical basis for EU AI Act post-market or deployer monitoring. Works for any sector and needs no AI engineering background.
license: CC-BY-4.0
metadata:
  author: Armend Verbovci
  version: "1.0"
---

# OAAF assessment

The Operational AI Assurance Framework (OAAF) is a free, sector-neutral method for deciding, on evidence, whether a deployed AI system or AI agent should keep operating, be restricted, or be stopped. It adapts aviation safety management to AI. The full text is in `references/FRAMEWORK.md` and the rules in machine-readable form are in `assets/oaaf.json`. Credit the framework as: Verbovci, A. (2026). Operational AI Assurance Framework (OAAF), Version 1.0. CC BY 4.0.

Use this skill to guide a person through an assessment conversationally, then apply the decision rules exactly. Ask one or two questions at a time. Use plain language. Do not invent evidence: if the person does not know, record it as Not Demonstrated.

## Choose the right depth

- **Quick question** ("when should we switch our chatbot off?"): answer from the relevant section of `references/FRAMEWORK.md` and point to the requirement IDs.
- **Quick start** (simple, low-consequence system): run steps 1 to 3, then check the 8 Tier 1 requirements.
- **Full assessment**: run all steps.

## Step 1. Define the system of operation

Collect: purpose; accountable owner; users and affected people; AI components (model, provider, version); data and knowledge sources; tools, integrations and the permissions the system holds; human oversight arrangement; known limitations; and the **materiality threshold** (the consequence above which an error counts as material). If no threshold is set, anything that moves money, commits the organisation to a third party or communicates externally on its behalf is material.

## Step 2. List capabilities and rate each one

A capability is something the system can cause to happen (approve, send, reorder, raise an order, flag). For agents, each class of tool action is a capability. For each, ask exactly two questions:

1. **Human acceptance:** must a human actively accept this specific output before it takes effect? Only a positive act counts. Being able to see it, sampling, or being able to intervene afterwards does not count.
2. **Consequence:** if the output is wrong, would the harm be irreversible before it would normally be detected, or exceed the materiality threshold? Judge reversibility of the consequence, not of the action.

| | Q2 Yes | Q2 No |
|---|---|---|
| Q1 No | High | Medium |
| Q1 Yes | Medium | Low |

For every Medium or High capability, sketch the decision path: input → AI decision → human acceptance *or none* → action → consequence. Always discuss the "none" branch. That is where unmonitored risk usually sits.

## Step 3. Set the Consequence Tier

- Tier 1: minor, easily reversed harm. 8 requirements apply.
- Tier 2: operational disruption, material financial loss or recoverable harm to individuals. 25 apply.
- Tier 3: severe or irreversible harm. All 36 apply.

The highest factor governs. Any High capability makes the system at least Tier 2. Record legal or sector classification (for example EU AI Act high-risk) separately; it adds obligations but does not set the tier.

## Step 4. Assess the applicable requirements

Load the list from `assets/oaaf.json` (field `requirements`, filter by `applies_from_tier`). Work domain by domain (P1 to P7). For each requirement, ask what evidence exists and record one value:

- **Compliant**: defined, in use, and a record shows it operating in the last 12 months (or since the last material change). At Tier 1, defined and in use is enough.
- **Partially Compliant**: defined but incomplete, inconsistent, or no record of operation.
- **Not Demonstrated**: evidence insufficient. This does not mean the control does not exist.

Apply three evidence rules strictly:

1. **Evidenced, not assumed.** A control owned by another team counts only if there is a named owner, a record, and a link to this system. "IT will have a recovery plan" is Not Demonstrated.
2. **Absence of harm is not evidence.** "Nothing has gone wrong" never downgrades an unassessed risk.
3. **Boundary Rule.** Hazards that can affect the decision path must be recorded even if another team owns the control.

Requirements marked control-critical in `oaaf.json` (`control_critical: true`) are the ones needed to detect a problem and stop it. Give them most attention.

## Step 5. Apply the decision rules

Do not judge severity yourself. Write the assessment as JSON in the format of `assets/example_assessment.json` and run:

```
python3 scripts/oaaf_decide.py assessment.json --markdown
```

If code cannot be run, apply the rules by hand:

- Finding criticality, per capability affected: control-critical requirement on a High capability → **Critical**; any other finding on a High or Medium capability → **Significant**; findings on Low capabilities → **Routine**. A finding may be raised one level with written reasons, never lowered.
- Decision per capability: any open Critical → **Not Ready**; otherwise any Significant, or Critical cleared by an evidenced compensating control or a signed, time-limited risk acceptance → **Ready with Conditions**; otherwise **Ready**.
- A capability already operating that is Not Ready should move to **S2 Restricted** (add human acceptance or reduce limits) or **S3 Contained** until cleared. There is no overall percentage score.

## Step 6. Report

Give the person:

1. A one-paragraph conclusion: the decision for each capability and why.
2. The decision table and findings (from the script output).
3. Conditions or actions, each with a suggested owner and date.
4. What remains unassessed.
5. When to reassess: at least every 12 months, after any behavioural change or provider model update, and before returning any stopped capability to service.

Offer the companion spreadsheet (OAAF v1.0 Assessment Workbook) if they want to keep records outside the conversation.

## Notes

- OAAF complements ISO/IEC 42001, the NIST AI RMF and the EU AI Act; it does not establish compliance with them. Say so if asked.
- Keep sector regulation and existing safety management processes in place. OAAF is the in-service operating layer for the AI element, not a replacement.
- If the person's situation does not fit (for example pure model research with no deployment), say OAAF is not the right tool.
