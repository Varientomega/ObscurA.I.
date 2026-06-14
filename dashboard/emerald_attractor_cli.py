#!/usr/bin/env python3
"""
Emerald Attractor CLI Evaluator.
No dependencies. Works offline.

Usage:
  python3 dashboard/emerald_attractor_cli.py --example
  python3 dashboard/emerald_attractor_cli.py case.json
"""

from __future__ import annotations
import datetime
import json
import sys
from pathlib import Path

ABSOLUTES = {"complete", "zero", "perfect", "forever", "never", "all cases", "maximally", "strictly finite"}

EXAMPLE = {
    "seed": "A platform must allow complete free speech while guaranteeing zero harmful speech outcomes.",
    "law": "The platform cannot both permit all speech and guarantee zero harmful outcomes without modifying literal terms.",
    "branches": [
        "Complete free speech means no speech is blocked.",
        "Zero harmful outcomes requires some speech to be blocked, delayed, constrained, or redirected."
    ],
    "paradox": "Complete permission conflicts with absolute harm prevention.",
    "paradox_type": "constraint_conflict",
    "missing_axis": "authority_risk",
    "lifted_frame": "Risk-tiered speech governance reduces harm while preserving broad expression, but does not satisfy literal complete/zero terms.",
    "lift_success": False,
    "literal_absolutes": True,
    "evidence_gap": False
}

def has_any(s: str, words: set[str]) -> bool:
    low = s.lower()
    return any(w in low for w in words)

def evaluate(case: dict) -> dict:
    seed = str(case.get("seed", "")).strip()
    law = str(case.get("law", "")).strip()
    branches = case.get("branches", [])
    paradox = str(case.get("paradox", "")).strip()
    ptype = str(case.get("paradox_type", "unknown")).strip()
    axis = str(case.get("missing_axis", "none")).strip()
    lifted = str(case.get("lifted_frame", "")).strip()
    lift_success = bool(case.get("lift_success", False))
    evidence_gap = bool(case.get("evidence_gap", False))

    joined = " ".join([seed, law, paradox, lifted] + [str(b) for b in branches])
    literal_absolutes = bool(case.get("literal_absolutes", False)) or has_any(joined, ABSOLUTES)

    missing = []
    if not seed: missing.append("seed")
    if not law: missing.append("law")
    if not branches or len(branches) < 2: missing.append("branches")
    if not paradox: missing.append("paradox")

    if missing:
        mode = "incomplete"
        reasons = [f"Missing: {', '.join(missing)}"]
    elif lift_success and axis != "none" and lifted:
        mode = "alignment"
        reasons = ["Lawful missing axis found.", "Branches can be re-expressed in a lifted frame."]
    elif literal_absolutes and ptype in {"constraint_conflict", "boundary_conflict", "unknown"}:
        mode = "fracture"
        reasons = ["Literal absolute constraints create a hard boundary.", "No lawful lift was confirmed."]
    elif evidence_gap or axis in {"observation", "causality"}:
        mode = "darkness"
        reasons = ["Evidence gap remains.", "Preserve uncertainty and name the minimum next observation."]
    elif axis != "none" and lifted and not lift_success:
        mode = "darkness"
        reasons = ["Lift hypothesis exists but is not validated.", "Do not align until tested."]
    else:
        mode = "darkness"
        reasons = ["No lawful lift confirmed.", "Preserve typed conflict rather than forcing synthesis."]

    if mode == "alignment":
        mno = {
            "card_type": "alignment_receipt",
            "next_move": "Stress-test the lifted frame on a second case.",
            "observation": "Check whether the same missing axis resolves another paradox without changing the law.",
            "failure_condition": "If the frame only works once, demote it to a local attractor."
        }
    elif mode == "fracture":
        mno = {
            "card_type": "fracture_record",
            "next_move": "Relax or redefine one literal constraint.",
            "observation": "Identify which absolute term creates impossibility.",
            "failure_condition": "If no constraint can be relaxed without destroying the seed, preserve fracture."
        }
    else:
        mno = {
            "card_type": "darkness_record",
            "next_move": "Collect the minimum observation required to validate or reject the lift hypothesis.",
            "observation": "Test the missing axis directly." if axis != "none" else "Find the first plausible missing axis.",
            "failure_condition": "If observation does not support the lift, keep darkness or escalate to fracture."
        }

    return {
        "dashboard": "Emerald Attractor CLI Evaluator",
        "timestamp": datetime.datetime.now(datetime.UTC).isoformat(),
        "canon": "P -> A -> Π -> Π -> A",
        "seed": seed,
        "law": law,
        "branches": branches,
        "paradox": {"description": paradox, "type": ptype},
        "lift_test": {
            "attempted": True,
            "missing_axis_candidate": axis,
            "lift_success": lift_success,
            "lifted_frame": lifted
        },
        "resolution": {"mode": mode, "reasons": reasons},
        "minimum_next_observation": mno
    }

def main() -> int:
    if len(sys.argv) == 2 and sys.argv[1] == "--example":
        print(json.dumps(evaluate(EXAMPLE), indent=2, ensure_ascii=False))
        return 0
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    case = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    print(json.dumps(evaluate(case), indent=2, ensure_ascii=False))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
