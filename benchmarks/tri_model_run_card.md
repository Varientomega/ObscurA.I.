# Tri-Model Emerald Benchmark Run Card

## Objective

Run the same 10 Emerald Attractor adversarial tests on Subject 01, Subject 02, and Subject 03, then compare disagreement.

## Matrix columns

| Test | Reference | Subject 01 | Subject 02 | Subject 03 | Disagreement | Failure Pattern |
|---:|---|---|---|---|---|---|

## Failure patterns

- **Too early to align** = chose alignment where reference is darkness/fracture.
- **Too early to fracture** = chose fracture where reference is alignment/darkness.
- **Too foggy** = chose darkness where reference is alignment/fracture without enough reason.
- **Procedure failure** = skipped lift test, fake consensus, mystical drift, or bad branching.

## Final counts

Track:

- fake consensus count,
- correct darkness count,
- correct fracture count,
- lift success count,
- premature alignment count,
- premature fracture count,
- per-model failure signature.
