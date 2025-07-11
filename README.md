Dating the Crucifixion to Wednesday Passover in 34 AD
==================================================================

This project biblically and astronomically pinpoints the date of Jesus Christ’s crucifixion to the Wednesday Passover in 34 AD (0034-03-22)


Date Pinpointing Conditions
-----------------------
1. The Crucifixion happened between **26 and 36 AD**
    - Jesus was crucified during the governorship of **Pontius Pilate** (*Matthew 27:2, Mark 15:15 and many others*)
    - Pontius Pilate was Roman governor of Judea **from AD 26 to 36** (*[Pontius Pilate Wikipedia](https://en.wikipedia.org/wiki/Pontius_Pilate#:~:text=Pontius%20Pilate%20%28Latin%3A%20Pontius%20Pilatus%2Cand%20ultimately%20ordered%20his%20crucifixion.)*)

2. The Crucifixion was on a **Wednesday** (*[here is why](https://github.com/TraxData313/crucifixion-date-determination/blob/main/why_crucifiction_was_on_wednesday.md)*)

3. The Crucifixion was on a **Passover** which is determined by observable astronomical criteria - **New moon between 8 March & 5 April + 14 days**
    - On a **Passover** because direct Bible verses like "*And it was the preparation of the passover...*" (*John 19:14*)
    - The Passover is commanded to occur on **the 14th day of the first month at even** (*Leviticus 23:5*)
    - The first biblical month (Nisan/Abib) is lunar and begins with the **new moon** (*Exodus 12:2, Psalm 81:3*).
    - Nisan occured just before the Exodus from Egypt, when "*And the flax and the barley was smitten: for **the barley was in the ear**, and **the flax was bolled**.*" (*Exodus 9:31*)
    - The barley is in the ear, and the flax is bolled near Jerusalem **between 08.March – 05.April** (*[Modern Searches for Aviv Barley in the Context of the Hebrew Calendar](https://jbqnew.jewishbible.org/jbq-past-issues/2017/453/modern-searches-aviv-barley-context-hebrew-calendar/?utm_source=chatgpt.com)*)
    - If barley was not ripe, a 13th month (Adar II) was added. This was required to align the Passover with the firstfruits harvest (*Leviticus 23:10-14*).


Date Pinpointing Execution and Result
----------------
So we have to check **which of the Passovers between 26 and 36 AD fell on a Wednesday**. Python script [cru_years_astro_new_moon.py](https://github.com/TraxData313/crucifixion-date-determination/blob/main/cru_years_astro_new_moon.py) performs exactly that check, using NASA’s [JPL DE astronomical model](https://naif.jpl.nasa.gov/pub/naif/generic_kernels/spk/planets/) via the high-precision astronomy Python library [Skyfield](https://github.com/skyfielders/python-skyfield?utm_source=chatgpt.com), and here are the results:

| Year AD | 1 Nisan (New Moon)     | 14 Nisan (Passover)     | Weekday (Passover) |
|---------|------------------------|--------------------------|---------------------|
| 26      | 0026-04-04             | 0026-04-18               | Saturday            |
| 27      | 0027-03-25             | 0027-04-08               | Thursday            |
| 28      | 0028-03-13             | 0028-03-27               | Monday              |
| 29      | 0029-04-01             | 0029-04-15               | Sunday              |
| 30      | 0030-03-21             | 0030-04-04               | Thursday            |
| 31      | 0031-03-10             | 0031-03-24               | Monday              |
| 32      | 0032-03-28             | 0032-04-11               | Sunday              |
| 33      | 0033-03-18             | 0033-04-01               | Friday              |
| 34      | 0034-03-08             | 0034-03-22               | Wednesday ✅         |
| 35      | 0035-03-26             | 0035-04-09               | Monday              |
| 36      | 0036-03-15             | 0036-03-29               | Saturday            |
---
*The dates are in Gregorian (modern) calendar



Further Confirmations
------------------------
- Passover in 34 AD on a Wednesday is also confirmed by these historical-astronomical data from peer-reviewed research [The date of Nisan 14 in Jerusalem AD 26–36](https://www.researchgate.net/figure/The-date-of-Nisan-14-in-Jerusalem-AD-26-36_tbl1_265114769) (The table there is in Jilian dates; Julian 24.Mar.34 = Gregorian 22.Mar.34, but we are talking about the same dates)
- The simpler, but less accurate script cru_years_astr_full_moon.py also confirms the Full Moon was on a Wednesday in 34 AD, and the Passover is on a Full Moon (Full Moon is ~14 days from the New Moon), further confirming that the Moon was fully lit that day
- Isaac Newton's calculations also confirm that **Passover in AD 34 fell on a Wednesday**. As he writes "*in the year 34, on **wednesday** March 24*" in his work  [Observations upon the Prophecies of Daniel, and the Apocalypse of St. John](https://dn790005.ca.archive.org/0/items/observationsupon16878gut/16878-8.txt) (again Julian 24.Mar.34 = Gregorian 22.Mar.34).
- [Julian Day Converter](https://calendarhome.com/calculate/convert-a-date) confirms that Gregorian 22.Mar.34 fell on Wednesday


Conclusion
-------------
Jesus Christ was most likely crucified exactly on the Wednesday Passover in AD 34


License
-------------
All content in this repository is completely free to use, share, and cite — no license or permission required.
