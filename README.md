Dating the Crucifixion to Wednesday Passover in 34 AD
==================================================================

This project biblically and astronomically dates the crucifixion of Jesus Christ, most probably to the Wednesday Passover in 34 AD (**0034-03-22** Gregorian = 24.Mar.34 Julian), with one clearly stated alternative (Wednesday, 23 April 31 AD) and explicit probabilities for each — see [the probability analysis below](#how-certain-is-this-probabilities).


Date Pinpointing Conditions
-----------------------
1. The Crucifixion happened between **26 and 36 AD**
    - Jesus was crucified during the governorship of **Pontius Pilate** (*Matthew 27:2, Mark 15:15 and many others*)
    - Pontius Pilate was Roman governor of Judea **from AD 26 to 36** (*[Pontius Pilate Wikipedia](https://en.wikipedia.org/wiki/Pontius_Pilate#:~:text=Pontius%20Pilate%20%28Latin%3A%20Pontius%20Pilatus%2Cand%20ultimately%20ordered%20his%20crucifixion.)*)
    - Additionally: John the Baptist began preaching in the 15th year of Tiberius, AD 28/29 (*Luke 3:1*), and Jesus' ministry spans at least three Passovers (*John 2:13, 6:4, 11:55*) — which pushes the crucifixion realistically to **AD 32 or later**

2. The Crucifixion was on a **Wednesday** (*[here is why](why_crucifiction_was_on_wednesday.md)*)

3. The Crucifixion was on a **Passover**, which is determined by observable astronomical criteria
    - On a **Passover** because of direct Bible verses like "*And it was the preparation of the passover...*" (*John 19:14*)
    - The Passover is commanded to occur on **the 14th day of the first month at even** (*Leviticus 23:5*)
    - The first biblical month (Nisan/Abib) is lunar and begins with the **new moon** (*Exodus 12:2, Psalm 81:3*) — in practice, with the **first visible crescent** sighted at evening from Jerusalem, 1–2 days after the astronomical conjunction
    - Nisan occurred just before the Exodus from Egypt, when "*And the flax and the barley was smitten: for **the barley was in the ear**, and **the flax was bolled**.*" (*Exodus 9:31*)
    - The barley is in the ear, and the flax is bolled near Jerusalem **between 08.March – 05.April** (*[Modern Searches for Aviv Barley in the Context of the Hebrew Calendar](https://jbqnew.jewishbible.org/jbq-past-issues/2017/453/modern-searches-aviv-barley-context-hebrew-calendar/?utm_source=chatgpt.com)*)
    - If barley was not ripe, a 13th month (Adar II) was added. This was required to align the Passover with the firstfruits harvest (*Leviticus 23:10-14*). Whether a given year received this 13th month is the **one genuinely uncertain input** in the whole calculation — see the probabilities section below.


Date Pinpointing Execution and Result
----------------
We check **which of the Passovers between 26 and 36 AD fell on a Wednesday**. Python script [nisan14_analysis.py](nisan14_analysis.py) performs that check using NASA's [JPL DE441 astronomical model](https://naif.jpl.nasa.gov/pub/naif/generic_kernels/spk/planets/) via the high-precision astronomy library [Skyfield](https://github.com/skyfielders/python-skyfield), modeling the calendar the way it actually worked:

- exact new-moon conjunction times (not daily sampling),
- **1 Nisan = first visible crescent** from Jerusalem (Yallop visibility criterion),
- 14 Nisan = 1 Nisan + 13 days, with sunset-to-sunset day boundaries,
- intercalation (13th month) treated as explicit scenarios.

Results under the main scenario (equinox rule — 14 Nisan on/after the vernal equinox — with standard crescent visibility):

| Year AD | 1 Nisan (first crescent) | 14 Nisan (Passover)      | Weekday (Passover) |
|---------|--------------------------|--------------------------|---------------------|
| 26      | 0026-04-06 *             | 0026-04-19               | Sunday              |
| 27      | 0027-03-26               | 0027-04-08               | Thursday            |
| 28      | 0028-03-15               | 0028-03-28               | Tuesday             |
| 29      | 0029-04-03               | 0029-04-16               | Monday              |
| 30      | 0030-03-23               | 0030-04-05               | Friday              |
| 31      | 0031-03-12               | 0031-03-25               | Tuesday **          |
| 32      | 0032-03-30               | 0032-04-12               | Monday              |
| 33      | 0033-03-19               | 0033-04-01               | Friday              |
| 34      | 0034-03-09               | 0034-03-22               | Wednesday ✅ **      |
| 35      | 0035-03-28               | 0035-04-10               | Tuesday             |
| 36      | 0036-03-16               | 0036-03-29               | Saturday            |
---
*The dates are in Gregorian (modern) calendar; Julian = Gregorian + 2 days in this era (e.g. Gregorian 22.Mar.34 = Julian 24.Mar.34)*
*\* AD 26 shown with its intercalated (13th-month) Nisan — its March Passover would fall before the equinox*
*\*\* AD 31 and AD 34 are intercalation-sensitive: if AD 34 received a 13th month its Passover moves to Thursday 20.Apr (Gregorian); if AD 31 received one, its Passover moves to **Wednesday 23.Apr** (Gregorian). See probabilities below.*

**Only AD 34 gives a Wednesday Passover under the main scenario.**


How certain is this? (Probabilities)
------------------------
The astronomy above is settled to the day (see verification below). The one open input is a human decision: **did the Sanhedrin add a 13th month (Adar II) in a given year?** Assuming the crucifixion was on a Wednesday, weighing each candidate by (a) the probability of the calendar decision it requires and (b) its fit with the Luke 3:1 / three-Passovers chronology:

| Candidate date (Gregorian) | Probability | Requires |
|---|---|---|
| **Wednesday, 22 March AD 34** | **~70–75%** | AD 34 was *not* intercalated (its Passover falls 1 day after the equinox — earliest in the range, but valid under the equinox rule) |
| Wednesday, 23 April AD 31 | ~25% | AD 31 *was* intercalated (plausible: its regular Passover falls only 4 days after the equinox) |
| Wednesday, 26 April AD 28 | ~2–3% | intercalation of an already-late Passover, and conflicts with Luke 3:1 |

Full reasoning, sensitivity analysis and scenario tables: [claude_verification_and_probabilities.md](claude_verification_and_probabilities.md) and [nisan14_results.md](nisan14_results.md).


Further Confirmations
------------------------
- The corrected computation reproduces, **to the exact day, every row** of the peer-reviewed historical-astronomical table [The date of Nisan 14 in Jerusalem AD 26–36](https://www.researchgate.net/figure/The-date-of-Nisan-14-in-Jerusalem-AD-26-36_tbl1_265114769) (Humphreys & Waddington, Nature 306, 1983; their table is in Julian dates: Julian 24.Mar.34 = Gregorian 22.Mar.34) — including **Wednesday 24.Mar.34** for the non-intercalated AD 34.
- **Isaac Newton's** calculations in [Observations upon the Prophecies of Daniel, and the Apocalypse of St. John](https://dn790005.ca.archive.org/0/items/observationsupon16878gut/16878-8.txt) independently confirm both the astronomy and the year: he computes "*in the year 34, on wednesday March 24*" for the March lunation, and concludes "*Thus all the characters of the Passion agree to the year 34*". (To be fair to Newton: he himself favored the intercalated branch of AD 34, arriving at Friday 23 April — the intercalation question again. His astronomy and ours agree to the day on every date he lists.)
- The simpler cross-check script [cru_years_astr_full_moon.py](cru_years_astr_full_moon.py) confirms the Full Moon fell midweek in March AD 34 — the Passover moon was fully lit that Wednesday.
- [Julian Day Converter](https://calendarhome.com/calculate/convert-a-date) confirms that Gregorian 22.Mar.34 fell on Wednesday.


Verification
------------
This repository's calculation was independently reviewed and rebuilt in July 2026 by **Claude** — Anthropic's AI (model **Claude Fable 5**), running as the Claude Code agent: exact conjunctions, crescent visibility from Jerusalem, correct day counting, and explicit intercalation scenarios. The corrected model matches Newton (1733) and Humphreys & Waddington (1983) to the day on every comparable date. The review, the problems it found in the original scripts, and the full scenario analysis are documented in [claude_verification_and_probabilities.md](claude_verification_and_probabilities.md). The original README is preserved in the repository's git history; the original scripts (`cru_years_astro_new_moon.py`, `cru_years_astr_full_moon.py`) are kept for history.

To reproduce: `pip install skyfield pandas`, then `python nisan14_analysis.py` — the required ephemeris excerpt (`de441_excerpt_AD20-40.bsp`, 2.2 MB, JPL DE441 for AD 20–40) ships with the repository.


Conclusion
-------------
Jesus Christ was most likely crucified on the **Wednesday Passover, 22 March 34 AD** (Gregorian; 24 March Julian) — at roughly **3:1 odds** against the alternative Wednesday Passover of **23 April 31 AD**, the choice between them hinging on whether those years received a 13th calendar month.


License
-------------
All content in this repository is completely free to use, share, and cite — no license or permission required.
