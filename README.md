Crucifixion Date Script — Finding the Biblical Wednesday Passover
==================================================================

This project seeks to biblically and astronomically verify the year of Jesus Christ’s crucifixion, affirming what the Scriptures clearly teach: that Christ was crucified on a Wednesday, on Passover (14th of Nisan), and that the following day, the High Sabbath (15th of Nisan), was a Holy Convocation — not the weekly Saturday Sabbath, but still a required day of rest.

📖 Biblical Foundations
-----------------------

1. [Why the Crucifixion Was on Wednesday](https://github.com/TraxData313/crucifixion-date-determination/blob/main/why_crucifiction_was_on_wednesday.md)

2. Why the Crucifixion was on a Full Moon?

    - The **Passover** is commanded to occur on **the 14th day of the first month at even** (Leviticus 23:5).
    - The first biblical month (Nisan/Abib) is **lunar** and begins with the new moon (Exodus 12:2, Psalm 81:3).
    - Therefore, the **14th of Nisan always falls on a full moon**, because 14 days after a new moon is a full moon.
    - This is why our search for the date of the crucifixion is tied to identifying full moons.

🧮 Why Search AD 26–36?
-----------------------

- Jesus began His ministry at “about 30” (Luke 3:23).
- John the Baptist’s ministry began in the 15th year of Tiberius Caesar (Luke 3:1) → AD 29.
- His ministry lasted around 3.5 years, so the crucifixion likely occurred between AD 30–34.
- We search for a full moon (Passover) that fell on a Wednesday within this range.

📜 Script Output
----------------

The included Python script uses Skyfield to identify the full moon closest to Nisan 14 in each year from AD 26 to 36.

Result:
--------
| Year AD | Full Moon (Nisan 14?) | Weekday   |
|--------:|------------------------|-----------|
|      26 | 0026-04-19    | Sunday    |
|      27 | 0027-04-08    | Thursday  |
|      28 | 0028-03-27    | Monday    |
|      29 | 0029-04-15    | Sunday    |
|      30 | 0030-04-05    | Friday    |
|      31 | 0031-04-24    | Thursday  |
|      32 | 0032-04-12    | Monday    |
|      33 | 0033-04-02    | Saturday  |
|  **34** | **0034-03-22**| **Wednesday ✅** |
|      35 | 0035-04-09    | Monday    |
|      36 | 0036-04-27    | Sunday    |

✔️ AD 34 shows a full moon (Passover) falling on a Wednesday, making it the most scripturally accurate year for the crucifixion of Jesus Christ.

📚 External Confirmation
------------------------

These findings align with the detailed historical-astronomical data from peer-reviewed research. See:
**"The date of Nisan 14 in Jerusalem AD 26–36"**  
https://www.researchgate.net/figure/The-date-of-Nisan-14-in-Jerusalem-AD-26-36_tbl1_265114769

🛠 How to Run
-------------

1. Download the `de431_part-2.bsp` planetary ephemeris file from [NASA JPL](https://naif.jpl.nasa.gov/pub/naif/generic_kernels/spk/planets/).
2. Install Python dependencies:
   pip install skyfield pandas
3. Update the path in the script:
   eph = load('C:/Path/To/de431_part-2.bsp')
4. Run the script:
   python crucifixion_date.py

🙌 Conclusion
-------------

This project harmonizes Scripture and astronomy to affirm the literal three days and three nights death, burial, and resurrection of our Lord and Saviour Jesus Christ — without compromise.

“Sanctify them through thy truth: thy word is truth.”
— John 17:17 (KJV)
