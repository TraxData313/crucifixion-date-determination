Dating the Crucifixion to Wednesday Passover in 34 AD
==================================================================

This project biblically and astronomically pinpoints the year of Jesus Christ’s crucifixion to the Full Mooned Wednesday Passover in 34 AD (0034-03-22)

Search Conditions
-----------------------

1. Wednesday, because [the Crucifixion Was on a Wednesday](https://github.com/TraxData313/crucifixion-date-determination/blob/main/why_crucifiction_was_on_wednesday.md)

2. 14 days from the New moon between 8 March – 5 April:
    - Crucifixion was on a **Passover** (John 19:14)
    - The Passover is commanded to occur on **the 14th day of the first month at even** (Leviticus 23:5)
    - The first biblical month (Nisan/Abib) is lunar and begins with the **new moon** (Exodus 12:2, Psalm 81:3).
    - Nisan occured just before the Exodus from Egypt, **when "And the flax and the barley was smitten: for the barley was in the ear, and the flax was bolled."** (Exodus 9:31)
    - the barley is in the ear, and the flax is bolled" near Jerusalem **between 08.March – 05.April** ([relevant study proving that](https://jbqnew.jewishbible.org/jbq-past-issues/2017/453/modern-searches-aviv-barley-context-hebrew-calendar/?utm_source=chatgpt.com))

3. **If no new moon** appears in that range, count **14 days from the next new moon** (i.e. intercalated month)
    - If barley was not ripe, a 13th month (Adar II) was added. This was required to align the Passover with the firstfruits harvest (Leviticus 23:10-14).

4. AD 26–36
   - Jesus began His ministry at “about 30” (Luke 3:23).
   - John the Baptist’s ministry began in the 15th year of Tiberius Caesar (Luke 3:1) → AD 29.
   - His ministry lasted around 3.5 years, so the crucifixion likely occurred between AD 30–34.
   - We search for a full moon (Passover) that fell on a Wednesday within this range.


Search Execution and Results
----------------
### Execution:
Run python script **cru_years_astro_new_moon.py** to performs the search conditions: check the weekday on the Passovers from 26 to 36 AD, looking for the Wednesday Passover

### Results: 
Nisan & Passover Dates from AD 26–36:

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



📚 Further Confirmations
------------------------
- Passover in 34 AD on a Wednesday is also confirmed by these historical-astronomical data from peer-reviewed research [The date of Nisan 14 in Jerusalem AD 26–36](https://www.researchgate.net/figure/The-date-of-Nisan-14-in-Jerusalem-AD-26-36_tbl1_265114769), even though they were looking for a Friday
- The simpler, but less accurate script cru_years_astr_full_moon.py also confirms the Full Moon was on a Wednesday in 34 AD, and the Passover is on a Full Moon (Full Moon is ~14 days from the New Moon), further confirming that the Moon was fully lid that day


🙌 Conclusion
-------------
Based on the biblical calendar, barley ripening data, and astronomical new moon calculations, the only year from AD 26–36 in which Passover (14 Nisan) fell on a Wednesday, matching the Gospel chronology and scriptural requirements, is **AD 34**.


📖 License
-------------
All content in this repository is completely free to use, share, and cite — no license or permission required.
