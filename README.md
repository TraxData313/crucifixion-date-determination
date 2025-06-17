Dating the Crucifixion to Wednesday Passover in 34 AD
==================================================================

This project biblically and astronomically pinpoints the date of Jesus Christ’s crucifixion to the Wednesday Passover in 34 AD (0034-03-22)


Date Pinpointing Conditions
-----------------------
1. The Crucifixion happened between **26 and 36 AD**
    - Jesus was crucified during **Pontius Pilate** (*Matthew 27:2, Mark 15:15 and many others*)
    - Pontius Pilate was Roman governor of Judea **from AD 26 to 36** (*[Pontius Pilate Wikipedia](https://en.wikipedia.org/wiki/Pontius_Pilate#:~:text=Pontius%20Pilate%20%28Latin%3A%20Pontius%20Pilatus%2Cand%20ultimately%20ordered%20his%20crucifixion.)*)

2. The Crucifixion was on a **Passover** which is **14 days from the New moon between 8 March – 5 April**
    - On a **Passover** because direct Bible verses like "*And it was the preparation of the passover...*" (*John 19:14*)
    - The Passover is commanded to occur on **the 14th day of the first month at even** (*Leviticus 23:5*)
    - The first biblical month (Nisan/Abib) is lunar and begins with the **new moon** (*Exodus 12:2, Psalm 81:3*).
    - Nisan occured just before the Exodus from Egypt, when "*And the flax and the barley was smitten: for **the barley was in the ear**, and **the flax was bolled**.*" (*Exodus 9:31*)
    - The barley is in the ear, and the flax is bolled near Jerusalem **between 08.March – 05.April** (*[Modern Searches for Aviv Barley in the Context of the Hebrew Calendar](https://jbqnew.jewishbible.org/jbq-past-issues/2017/453/modern-searches-aviv-barley-context-hebrew-calendar/?utm_source=chatgpt.com)*)
    - If barley was not ripe, a 13th month (Adar II) was added. This was required to align the Passover with the firstfruits harvest (*Leviticus 23:10-14*).

3. The Crucifixion was on a **Wednesday** (*[here is why](https://github.com/TraxData313/crucifixion-date-determination/blob/main/why_crucifiction_was_on_wednesday.md)*)


Date Pinpointing Execution and Result
----------------
So we have to check **which of the Passovers between 26 to 36 AD fell on a Wednesday**. Python script [cru_years_astro_new_moon.py](https://github.com/TraxData313/crucifixion-date-determination/blob/main/cru_years_astro_new_moon.py) performs exactly that check, using NASA’s [JPL DE astronomical model](https://naif.jpl.nasa.gov/pub/naif/generic_kernels/spk/planets/) via the high-precision astronomy Python library [Skyfield](https://github.com/skyfielders/python-skyfield?utm_source=chatgpt.com), and here are the results:

| Year AD | Added 13th Month? | 1 Nisan (New Moon)     | 14 Nisan (Passover)     | Weekday (Passover) |
|---------|--------------------|------------------------|--------------------------|---------------------|
| 26      | No                 | 0026-04-04    | 0026-04-18      | Saturday            |
| 27      | No                 | 0027-03-25    | 0027-04-08      | Thursday            |
| 28      | No                 | 0028-03-13    | 0028-03-27      | Monday              |
| 29      | No                 | 0029-04-01    | 0029-04-15      | Sunday              |
| 30      | No                 | 0030-03-21    | 0030-04-04      | Thursday            |
| 31      | No                 | 0031-03-10    | 0031-03-24      | Monday              |
| 32      | No                 | 0032-03-28    | 0032-04-11      | Sunday              |
| 33      | No                 | 0033-03-18    | 0033-04-01      | Friday              |
| 34      | No                 | 0034-03-08    | 0034-03-22      | Wednesday ✅        |
| 35      | No                 | 0035-03-26    | 0035-04-09      | Monday              |
| 36      | No                 | 0036-03-15    | 0036-03-29      | Saturday            |

---



Further Confirmations
------------------------
- Passover in 34 AD on a Wednesday is also confirmed by these historical-astronomical data from peer-reviewed research [The date of Nisan 14 in Jerusalem AD 26–36](https://www.researchgate.net/figure/The-date-of-Nisan-14-in-Jerusalem-AD-26-36_tbl1_265114769), even though they were looking for a Friday
- The simpler, but less accurate script cru_years_astr_full_moon.py also confirms the Full Moon was on a Wednesday in 34 AD, and the Passover is on a Full Moon (Full Moon is ~14 days from the New Moon), further confirming that the Moon was fully lid that day


Conclusion
-------------
Given the search criteria, it looks reasonable to say that **Jesus Christ was most likely crucified on the Wednesday Passover in AD 34**.


License
-------------
All content in this repository is completely free to use, share, and cite — no license or permission required.
