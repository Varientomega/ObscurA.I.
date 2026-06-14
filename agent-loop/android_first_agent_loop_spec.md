# Android-First Always-On Emerald Agent Loop

## Objective

Upgrade the Emerald dashboard/CLI into an Android-first agent loop that captures contradictions, classifies them as alignment/darkness/fracture, stores receipts, tracks reward, and recommends the next minimum observation or commercial action.

## Core loop

```text
capture -> parse -> classify -> receipt -> next_observation -> reward -> reinvest
```

## Modules

### 1. Capture Layer

Sources:

- chat text,
- pasted notes,
- voice transcripts,
- OCR from screenshots,
- project files,
- benchmark outputs.

### 2. Emerald Parser

Extracts:

- seed,
- law,
- branches,
- paradox,
- missing-axis candidates,
- literal absolutes,
- evidence gaps.

### 3. Classifier

Modes:

- alignment,
- darkness,
- fracture.

### 4. Receipt Store

Append-only local store for every attractor trace and reward receipt.

### 5. Reward Tracker

Scores scientific value, commercial value, personal agency value, and evidence strength.

### 6. Next-Observation Recommender

Produces the smallest useful next step.

### 7. Drift Alarm

Triggers when the system repeatedly skips lift tests, claims fake alignment, or leaves reward receipts uncashed.

## Android path

1. Use local HTML dashboard in Android browser.
2. Wrap dashboard as PWA.
3. Run CLI through Termux.
4. Build native Kotlin app with SQLite receipt store.
5. Add notification-based next-observation reminders.
