# Nisan 14 in AD 26–36 — corrected analysis and scenario study

This document reports the results of [nisan14_analysis.py](nisan14_analysis.py), which replaces
the original conjunction-based calculation with a full model of how the biblical
lunar calendar actually worked, and treats the genuinely uncertain choices
(crescent visibility, intercalation of a 13th month) as explicit scenarios
instead of silent assumptions.

## Method

1. **Exact new-moon conjunction times** via root-finding on JPL DE441
   (excerpt `de441_excerpt_AD20-40.bsp`, 2.2 MB, covers AD 20–40).
2. **1 Nisan begins at the first visible crescent** after conjunction, evaluated
   from Jerusalem at each evening's "best time" using the Yallop (1997)
   q-criterion. Three visibility strictness levels are tested:
   **A** (easily visible), **B** (visible under perfect conditions — the middle,
   most realistic assumption), **C** (hard to see).
3. **14 Nisan daytime = 1 Nisan daytime + 13 days** (1 Nisan is day 1, not day 0),
   with Hebrew sunset-to-sunset day boundaries. The weekday reported is that of
   the *daylight* portion of 14 Nisan — when the crucifixion took place.
4. **Three intercalation rules** decide which lunation is Nisan:
   - **R1 — aviv window** (the repo's original rule): conjunction falls inside
     Gregorian 8 March – 5 April; otherwise a 13th month is added.
   - **R2 — equinox rule**: the earliest lunation whose 14 Nisan falls on or
     after the vernal equinox. This is the best-attested ancient criterion
     (later rabbinic sources; Anatolius on Jewish practice).
   - **R3 — late/harvest rule** (Newton's reasoning): 1 Nisan itself must not
     precede the equinox, so Passover falls ~2+ weeks after it, comfortably
     inside the barley harvest.

## Validation

The model reproduces, to the exact day, two independent historical computations:

- **Humphreys & Waddington** (Nature 306, 1983, "Dating the Crucifixion"),
  criterion B: AD 27 Thu 10 Apr, AD 28 Tue 30 Mar, AD 29 Mon 18 Apr,
  AD 30 Fri 7 Apr, AD 31 Tue 27 Mar, AD 33 Fri 3 Apr, AD 34 Wed 24 Mar,
  AD 35 Tue 12 Apr, AD 36 Sat 31 Mar (all Julian) — every row matches.
- **Isaac Newton** (*Of the Times of the Birth and Passion of Christ*, 1733):
  his pre-postponement dates for AD 31–36 all match, **including both of his
  AD 34 dates**: Wednesday 24 March (no intercalation) and Thursday 22 April
  (with intercalation, which he favoured).

## Results — 14 Nisan under every scenario (Julian dates; `+13m` = intercalated year)

| Year | R1 aviv window | R2 equinox rule | R3 late/harvest |
|------|----------------|-----------------|-----------------|
| 26 | Sun 21 Apr | Sun 21 Apr +13m | Sun 21 Apr +13m |
| 27 | Thu 10 Apr | Thu 10 Apr | Thu 10 Apr |
| 28 | Tue 30 Mar | Tue 30 Mar | Wed 28 Apr +13m |
| 29 | Mon 18 Apr | Mon 18 Apr | Mon 18 Apr |
| 30 | **Fri 7 Apr** | **Fri 7 Apr** | **Fri 7 Apr** |
| 31 | Tue 27 Mar | Tue 27 Mar | **Wed 25 Apr +13m** |
| 32 | Mon 14 Apr | Mon 14 Apr | Mon 14 Apr |
| 33 | **Fri 3 Apr** | **Fri 3 Apr** | Sat 2 May +13m |
| 34 | Thu 22 Apr +13m | **Wed 24 Mar** | Thu 22 Apr +13m |
| 35 | Tue 12 Apr | Tue 12 Apr | Tue 12 Apr |
| 36 | Sat 31 Mar | Sat 31 Mar | Mon 30 Apr +13m |

(Shown for visibility criterion B; criteria A/C change only a few marginal rows —
AD 27 and AD 32 can shift by one day, AD 28/31 R3 dates shift within late April.
Full 3×3 grid is printed by the script.)

## Key finding about AD 34

The exact conjunction of the March AD 34 lunation is **7 March, 06:20 UTC
(Gregorian)** = 9 March Julian. That is **outside the repo's own aviv window
(8 March – 5 April)** — the original script reported "8 March" only because it
sampled the sky once per day starting exactly at the window edge. Applied
precisely, the repo's own rule R1 intercalates AD 34 and yields
**Thursday 22 April**, not Wednesday.

However, the *first visible crescent* fell on the evening of 8 March
(Gregorian) — exactly on the window boundary. So under a crescent-based reading
of the window, AD 34 passes by zero days. Either way, AD 34 is a knife-edge
case: its March Passover (24 March Julian) falls just **one day after the
vernal equinox**, the earliest possible Passover in the whole AD 26–36 range.
Whether the Sanhedrin would have intercalated that year (Newton argued yes,
for barley-ripeness reasons) is the single assumption on which the
Wednesday-AD 34 result stands or falls.

## What remains possible, per weekday hypothesis

Counting across all 9 scenario combinations (3 rules × 3 visibility criteria):

| Hypothesis | Candidates (Julian date, combos supporting) |
|------------|---------------------------------------------|
| **Friday** (traditional) | **AD 30, 7 Apr — 9/9 (fully robust)**; AD 33, 3 Apr — 6/9; AD 27, 11 Apr — 3/9 |
| **Thursday** | AD 27, 10 Apr — 6/9; AD 34, 22 Apr (+13m) — 6/9 |
| **Wednesday** | AD 34, 24 Mar — 3/9 (only under the equinox rule, no intercalation); AD 31, 25 Apr (+13m) — 3/9 (only under the late/harvest rule); AD 28, 28 Apr (+13m) — 2/9 |

Interpretation:

- **If the crucifixion was on a Friday**, AD 30 (7 April) is robust under every
  tested assumption; AD 33 (3 April) survives everything except the strict
  harvest rule. This is why these two dominate the scholarly literature.
- **If it was on a Wednesday** (this repo's thesis), the candidates are
  mutually exclusive branches of the intercalation question:
  - **AD 34, 24 March Julian / 22 March Gregorian** — requires that AD 34 was
    *not* intercalated, i.e. the equinox rule was applied at its tightest
    margin (Passover 1 day after equinox) and the barley was already aviv in
    early March. Supported by the best-attested rule (R2), opposed by Newton's
    harvest argument.
  - **AD 31, 25 April Julian** — requires that AD 31 *was* intercalated.
    Its non-intercalated Passover (27 March) is also very early, only 4 days
    after the equinox, so this branch is not exotic.
- **If it was on a Thursday**, AD 34 reappears as 22 April (the intercalated
  branch — Newton's own pre-postponement date), alongside AD 27.

## Honest bottom line

The astronomy is now settled to the day and cross-validated against Newton and
Humphreys & Waddington. What it cannot settle is a human decision: whether the
Sanhedrin added a 13th month in a given year. That decision flips AD 34 between
**Wednesday 24 March** and **Thursday 22 April**, and AD 31 between **Tuesday
27 March** and **Wednesday 25 April**. Any presentation of a single "pinpointed"
date should state which branch of that decision it assumes — and why.
