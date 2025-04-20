Crucifixion Date Script — Finding the Biblical Wednesday Passover
==================================================================

This project seeks to biblically and astronomically verify the year of Jesus Christ’s crucifixion, affirming what the Scriptures clearly teach: that Christ was crucified on a Wednesday, on Passover (14th of Nisan), and that the following day, the High Sabbath (15th of Nisan), was a Holy Convocation — not the weekly Saturday Sabbath, but still a required day of rest.

📖 Biblical Foundations
-----------------------

1. High Sabbath Explained

    “The Jews therefore, because it was the preparation, that the bodies should not remain upon the cross on the sabbath day, (for that sabbath day was an high day)...”
    — John 19:31 (KJV)

    - The High Sabbath (John 19:31) refers to Nisan 15, the first day of the Feast of Unleavened Bread.
    - Both the **weekly Sabbath** and the **High Sabbath** are called **holy convocations** and **days of rest**:
        - “Six days shall work be done: but the seventh day is the sabbath of rest, **an holy convocation**; **ye shall do no work therein**: it is the sabbath of the LORD in all your dwellings.” — Leviticus 23:3 (KJV)
    - It is explicitly called a **holy convocation** and a day of **rest**:
        - “And on the fifteenth day of the same month is the feast of unleavened bread unto the LORD: seven days ye must eat unleavened bread. In the first day ye shall have **an holy convocation**: **ye shall do no servile work therein**.” — Leviticus 23:6–7 (KJV)
        - “In the fourteenth day of the first month at even is the LORD's passover. And on the fifteenth day... **ye shall do no manner of servile work therein**.” — Numbers 28:16–18 (KJV)
    - This High Sabbath is distinct from the weekly Sabbath (Saturday). Every 15th of Nisan is a Sabbath regardless of the day of the week.

2. The Crucifixion Timing

    - Jesus was crucified on Passover, the 14th of Nisan, which was a Wednesday that year.
    - The next day (Thursday, 15th of Nisan) was the High Sabbath.
    - The women couldn’t go to the tomb that day (Luke 23:56), then rested again on the weekly Sabbath (Saturday).
    - They **prepared spices and ointments** between the two Sabbaths (Luke 23:56), which is **only possible if Friday was a work day** — impossible under the traditional Friday crucifixion model.

3. Three Days and Three Nights — Literally

    “For as Jonas was three days and three nights in the whale’s belly; so shall the Son of man be three days and three nights in the heart of the earth.”
    — Matthew 12:40 (KJV)

    - Wednesday sunset to Saturday sunset = literal 3 days and 3 nights:
      - Wed night, Thu day, Thu night, Fri day, Fri night, Sat day.
    - Christ rose after the Sabbath, before dawn Sunday (Matthew 28:1–6, John 20:1).

4. Why Search for the Full Moon?

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
