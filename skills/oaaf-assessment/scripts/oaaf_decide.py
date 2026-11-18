#!/usr/bin/env python3
"""Apply the OAAF v1.0 decision rules to an assessment.

Usage:
    python3 oaaf_decide.py assessment.json [--framework path/to/oaaf.json] [--markdown]

The input file describes the system, its capabilities and the assessment
results. See assets/example_assessment.json for the format. The script applies
the rules in Sections 4.3, 4.4, 7.3 and 7.4 of the framework exactly, so that
the same input always gives the same decision. It uses only the Python
standard library.

Licence: CC BY 4.0. Operational AI Assurance Framework (OAAF), Armend Verbovci.
"""
import argparse
import json
import os
import sys

LEVELS = ["Routine", "Significant", "Critical"]
OPEN_STATUSES = {"open"}
CLEARED_STATUSES = {"mitigated", "risk_accepted"}


def load_framework(path):
    if path is None:
        here = os.path.dirname(os.path.abspath(__file__))
        for candidate in (os.path.join(here, "..", "assets", "oaaf.json"),
                          os.path.join(here, "..", "..", "..", "oaaf.json")):
            if os.path.exists(candidate):
                path = candidate
                break
    if path is None or not os.path.exists(path):
        sys.exit("Cannot find oaaf.json. Pass it with --framework.")
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def capability_criticality(human_acceptance, irreversible_or_material):
    """Section 4.3, the two-question test."""
    if not human_acceptance and irreversible_or_material:
        return "High"
    if human_acceptance and not irreversible_or_material:
        return "Low"
    return "Medium"


def finding_criticality(control_critical, cap_crit, raise_one_level):
    """Section 7.3. Findings may be raised one level, never lowered."""
    if control_critical:
        base = {"High": "Critical", "Medium": "Significant", "Low": "Routine"}[cap_crit]
    else:
        base = {"High": "Significant", "Medium": "Significant", "Low": "Routine"}[cap_crit]
    if raise_one_level:
        base = LEVELS[min(LEVELS.index(base) + 1, 2)]
    return base


def run(assessment, framework):
    reqs = {r["id"]: r for r in framework["requirements"]}
    warnings = []

    # Capabilities
    caps = []
    for c in assessment.get("capabilities", []):
        for key in ("name", "human_acceptance", "irreversible_or_material"):
            if key not in c:
                sys.exit(f"Capability is missing '{key}': {c}")
        crit = capability_criticality(bool(c["human_acceptance"]), bool(c["irreversible_or_material"]))
        caps.append({"name": c["name"], "criticality": crit})
    if not caps:
        sys.exit("At least one capability is required.")
    cap_by_name = {c["name"]: c for c in caps}

    # Tier (Section 4.4)
    declared = int(assessment.get("system", {}).get("declared_tier", 1))
    if declared not in (1, 2, 3):
        sys.exit("declared_tier must be 1, 2 or 3.")
    any_high = any(c["criticality"] == "High" for c in caps)
    tier = max(declared, 2) if any_high else declared
    if tier != declared:
        warnings.append(f"Tier raised from {declared} to {tier} because at least one capability is High.")
    applicable = [rid for rid, r in reqs.items() if r["applies_from_tier"] <= tier]

    # Results and findings
    results = {}
    findings = []
    for res in assessment.get("results", []):
        rid = res.get("requirement")
        if rid not in reqs:
            warnings.append(f"Unknown requirement ID ignored: {rid}")
            continue
        value = res.get("value")
        if value not in ("Compliant", "Partially Compliant", "Not Demonstrated"):
            warnings.append(f"{rid}: value must be Compliant, Partially Compliant or Not Demonstrated; got {value!r}")
            continue
        if rid not in applicable:
            warnings.append(f"{rid} applies from Tier {reqs[rid]['applies_from_tier']}; the system is Tier {tier}. Result recorded but not used.")
            continue
        results[rid] = value
        if value == "Compliant":
            continue
        affected = res.get("capabilities") or [c["name"] for c in caps]
        status = res.get("status", "open").lower()
        if status not in OPEN_STATUSES | CLEARED_STATUSES | {"closed"}:
            warnings.append(f"{rid}: unknown status {status!r}, treated as open.")
            status = "open"
        for name in affected:
            if name not in cap_by_name:
                warnings.append(f"{rid}: capability {name!r} is not in the capability list.")
                continue
            crit = finding_criticality(reqs[rid]["control_critical"], cap_by_name[name]["criticality"],
                                       bool(res.get("raise_one_level", False)))
            if res.get("raise_one_level") and not res.get("raise_reason"):
                warnings.append(f"{rid}: finding raised one level without a written reason (Section 7.3 requires one).")
            if status == "risk_accepted" and crit == "Critical" and not res.get("accepted_by"):
                warnings.append(f"{rid}: risk acceptance needs a signatory with stop authority under P1-05(a) and an expiry date.")
            findings.append({"requirement": rid, "requirement_text": reqs[rid]["requirement"],
                             "value": value, "capability": name, "criticality": crit, "status": status,
                             "note": res.get("note", "")})

    # Decisions per capability (Section 7.4)
    decisions = []
    for c in caps:
        mine = [f for f in findings if f["capability"] == c["name"]]
        open_crit = sum(1 for f in mine if f["status"] == "open" and f["criticality"] == "Critical")
        open_sig = sum(1 for f in mine if f["status"] == "open" and f["criticality"] == "Significant")
        cleared = sum(1 for f in mine if f["status"] in CLEARED_STATUSES and f["criticality"] in ("Critical", "Significant"))
        if open_crit:
            outcome = "Not Ready"
            action = "If already operating, move to S2 Restricted or S3 Contained until the Critical findings are cleared."
        elif open_sig or cleared:
            outcome = "Ready with Conditions"
            action = "Each condition needs an owner and a date."
        else:
            outcome = "Ready"
            action = ""
        decisions.append({"capability": c["name"], "criticality": c["criticality"], "open_critical": open_crit,
                          "open_significant": open_sig, "cleared_by_control_or_acceptance": cleared,
                          "outcome": outcome, "action": action})

    not_assessed = [rid for rid in applicable if rid not in results]
    return {"framework": f"OAAF {framework['version']}", "system": assessment.get("system", {}).get("name", ""),
            "declared_tier": declared, "effective_tier": tier, "requirements_applying": len(applicable),
            "capabilities": caps, "decisions": decisions, "findings": findings,
            "requirements_not_yet_assessed": not_assessed, "warnings": warnings}


def to_markdown(out):
    lines = [f"# OAAF assessment: {out['system'] or 'unnamed system'}", "",
             f"Effective Consequence Tier: **{out['effective_tier']}** ({out['requirements_applying']} requirements apply)", "",
             "## Decision per capability", "",
             "| Capability | Criticality | Open Critical | Open Significant | Outcome |", "|---|---|---|---|---|"]
    for d in out["decisions"]:
        lines.append(f"| {d['capability']} | {d['criticality']} | {d['open_critical']} | {d['open_significant']} | **{d['outcome']}** |")
    lines += ["", "## Findings", ""]
    if out["findings"]:
        lines += ["| Requirement | Capability | Value | Criticality | Status |", "|---|---|---|---|---|"]
        for f in sorted(out["findings"], key=lambda f: (-LEVELS.index(f["criticality"]), f["requirement"])):
            lines.append(f"| {f['requirement']} | {f['capability']} | {f['value']} | {f['criticality']} | {f['status']} |")
    else:
        lines.append("No findings.")
    if out["requirements_not_yet_assessed"]:
        lines += ["", "## Not yet assessed", "", ", ".join(out["requirements_not_yet_assessed"])]
    if out["warnings"]:
        lines += ["", "## Warnings", ""] + [f"- {w}" for w in out["warnings"]]
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser(description="Apply OAAF v1.0 decision rules.")
    ap.add_argument("assessment")
    ap.add_argument("--framework", default=None)
    ap.add_argument("--markdown", action="store_true", help="print a readable report instead of JSON")
    a = ap.parse_args()
    with open(a.assessment, encoding="utf-8") as f:
        assessment = json.load(f)
    out = run(assessment, load_framework(a.framework))
    print(to_markdown(out) if a.markdown else json.dumps(out, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
