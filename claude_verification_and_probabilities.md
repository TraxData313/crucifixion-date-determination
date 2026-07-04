# Independent Verification and Probability Analysis — by Claude (Fable 5)

This document records a full independent review of this repository's
astronomical argument: what was checked, what problems were found, how they
were fixed, and — assuming the crucifixion was on a Wednesday — what
probability each candidate date deserves.

The review was performed in July 2026 by **Claude**, Anthropic's AI (model
**Claude Fable 5**), running as the Claude Code agent, at the repository
author's request. Claude independently downloaded and read the cited primary
sources, rebuilt the astronomical computation from scratch, and validated it
against two historical computations before drawing any conclusions.

The corrected computation lives in [nisan14_analysis.py](nisan14_analysis.py);
the full scenario tables are in [nisan14_results.md](nisan14_results.md).
The original README, as it stood before this review, is preserved in the
repository's git history.

---

## 1. What was checked

1. The two original Python scripts (`cru_years_astro_new_moon.py`,
   `cru_years_astr_full_moon.py`) — logic, astronomy, and calendar handling.
2. The cited sources — Isaac Newton's text was downloaded from archive.org and
   read in context; the results were compared row-by-row against the
   Humphreys & Waddington table ([The date of Nisan 14 in Jerusalem AD 26–36](https://www.researchgate.net/figure/The-date-of-Nisan-14-in-Jerusalem-AD-26-36_tbl1_265114769),
   Nature 306, 1983).
3. The whole calculation was redone from scratch with a corrected model
   (see §3) on the JPL DE441 ephemeris, and validated against both sources.

## 2. Problems found in the original work

### 2.1 The Newton citation was out of context

The README quoted Newton's "*in the year 34, on wednesday March 24*" as a
confirmation. The full sentence in
[Of the Times of the Birth and Passion of Christ](https://dn790005.ca.archive.org/0/items/observationsupon16878gut/16878-8.txt) reads:

> "...in the year 34, on wednesday *March* 24, **or rather, for avoiding the
> Equinox which fell on the same day, and for having a fitter time for
> harvest, on thursday *Apr.* 22**"

Newton computed Wednesday 24 March as the *hypothetical* date if Nisan were
the March lunation — and immediately rejected it, arguing AD 34 had an
intercalated 13th month; after applying the (anachronistic, later-rabbinic)
*Adu* postponement rule he concluded **Friday 23 April AD 34**. So Newton is a
legitimate *computational* cross-check that the March-moon Passover of AD 34
fell on a Wednesday, and an independent witness for the **year** 34
("*Thus all the characters of the Passion agree to the year 34*") — but an
opponent of the Wednesday 24 March date itself.

### 2.2 The month began with the visible crescent, not the conjunction

The original script treated the astronomical new moon (conjunction — when the
moon is invisible) as 1 Nisan. The biblical month began with the **first
visible crescent** at evening in Jerusalem, typically 1–2 days after
conjunction (Newton himself describes the Sanhedrin's sighting procedure).
Combined with an off-by-one in day counting (14 Nisan = 1 Nisan **+ 13** days,
not + 14), the original method landed one day early whenever the crescent lag
was 2 days — which is why its table disagreed with the Humphreys & Waddington
table it cited as confirmation on roughly half the rows (e.g. AD 30:
Thursday 6 April Julian instead of the correct Friday 7 April).

### 2.3 Dead code and a sampling artifact — including on the key year

- The intercalation fallback in `cru_years_astro_new_moon.py` could never
  execute: the window-search function always returns the sample closest to
  phase 0°, however far from a real conjunction, so `added_13th_month` was
  always `False`.
- The sky was sampled once per day at 00:00 UTC, so conjunction dates could
  shift by a day. Critically, the exact conjunction of the March AD 34
  lunation is **7 March 06:20 UTC (Gregorian)** — *outside* the script's own
  8 March – 5 April aviv window. The script reported "8 March" only because
  the window's first sample happened to be the one closest to conjunction.
  Applied exactly, the repository's own rule would have intercalated AD 34
  and produced **Thursday 22 April**, not Wednesday. (The *crescent*, however,
  appeared on the evening of 8 March — exactly on the window boundary — so a
  crescent-based reading of the window passes by zero days. Either way, AD 34
  is a knife-edge case.)
- Minor: weekdays were taken from UTC timestamps rather than the daylight
  portion of the sunset-to-sunset Hebrew day; the full-moon script's 40-day
  window can contain two full moons.

## 3. The corrected model

[nisan14_analysis.py](nisan14_analysis.py) computes, for each year AD 26–36:

1. **Exact conjunction times** by root-finding (Skyfield / JPL DE441; the
   repo ships a 2.2 MB excerpt `de441_excerpt_AD20-40.bsp` covering AD 20–40).
2. **First visible crescent** from Jerusalem, evaluated each evening at
   Yallop's "best time" with the Yallop (1997) q-criterion, at three
   strictness levels (A / B / C).
3. **1 Nisan** = the day beginning at that evening's sunset;
   **14 Nisan daytime = 1 Nisan daytime + 13 days**, weekday taken from the
   daylight portion (when the crucifixion occurred).
4. **Three intercalation rules** as explicit scenarios: R1 = the original
   aviv window; R2 = 14 Nisan on/after the vernal equinox (the best-attested
   ancient rule); R3 = Newton-style late/harvest rule (1 Nisan not before the
   equinox).

**Validation:** under criterion B the model reproduces, to the exact day,
*every* row of the Humphreys & Waddington table **and** all of Newton's
pre-postponement dates for AD 31–36 — including both of his AD 34 dates
(Wednesday 24 March and Thursday 22 April). Two independent historical
computations, three centuries apart, now agree with this code.

## 4. What the corrected results say

Full tables in [nisan14_results.md](nisan14_results.md). The essentials
(Julian dates; Gregorian = Julian − 2 days in this era):

- **Friday hypothesis** (traditional): AD 30 (7 April) survives *all* tested
  scenario combinations; AD 33 (3 April) survives most. This is why these two
  dominate the scholarly literature.
- **Wednesday hypothesis** (this repo's thesis): the candidates are mutually
  exclusive branches of the intercalation question —
  - **AD 34, Wednesday 24 March Julian / 22 March Gregorian** — requires that
    AD 34 was **not** intercalated (equinox rule applied at its tightest
    margin: Passover just 1 day after the equinox, the earliest in the range).
  - **AD 31, Wednesday 25 April Julian / 23 April Gregorian** — requires that
    AD 31 **was** intercalated (its non-intercalated Passover, 27 March, is
    itself only 4 days after the equinox, so this branch is plausible).
  - AD 28, Wednesday 28 April Julian — only under the strictest harvest rule,
    and effectively excluded by external chronology (see §5).
- **Thursday hypothesis**: AD 27 (10 April) and AD 34 (22 April — Newton's own
  pre-postponement date, the intercalated branch of the same year).

## 5. Probabilities, assuming the crucifixion was on a Wednesday

Each candidate's weight is the product of two factors: (a) the probability of
the calendar decision it requires (intercalation or not), and (b) its fit with
independent chronology — John the Baptist began in Tiberius' 15th year,
AD 28/29 (*Luke 3:1*), and Jesus' ministry spans at least three Passovers
(*John 2:13, 6:4, 11:55*), placing the crucifixion realistically at AD 32+.

| Candidate (Gregorian) | Probability | Requires |
|---|---|---|
| **Wednesday, 22 March AD 34** | **~70–75%** | AD 34 not intercalated (~40–50%) × chronology fits well (~1.0) |
| **Wednesday, 23 April AD 31** | **~25%** | AD 31 intercalated (~25–35%) × tight chronology (~0.4–0.5) |
| Wednesday, 26 April AD 28 | ~2–3% | intercalation of an already-late Passover (~10%) × chronology nearly excludes it (~0.05) |

Sensitivity of this distribution:

- Ignoring the *Luke 3:1* constraint (the README's original conditions use
  only Pilate's tenure): roughly 60% / 35% / 5%.
- Accepting Newton's harvest argument as the norm (barley rarely aviv in
  early March): the top two nearly swap — AD 34 ≈ 35–40%, AD 31 ≈ 55–60%.
  This is the single strongest lever in the whole calculation.
- Treating the equinox rule as strictly applied (as later rabbinic sources
  describe): AD 34 rises to ~85%+.

## 6. Bottom line

The astronomy is now settled to the day and cross-validated against Newton
(1733) and Humphreys & Waddington (1983). What it cannot settle is one human
decision: whether the Sanhedrin added a 13th month in a given year. That
decision flips AD 34 between Wednesday 24 March and Thursday 22 April, and
AD 31 between Tuesday 27 March and Wednesday 25 April. Under the Wednesday
hypothesis the most probable date remains **Wednesday, 22 March AD 34
(Gregorian)** — at roughly **3:1 odds** against the alternative
**Wednesday, 23 April AD 31** — with the assumptions behind that ratio stated
explicitly above.
