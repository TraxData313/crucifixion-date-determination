Crucifixion Date Script — Finding the Biblical Wednesday Passover
==================================================================

This project seeks to biblically and astronomically verify the year of Jesus Christ’s crucifixion, affirming what the Scriptures clearly teach: that Christ was crucified on a Wednesday, on Passover (14th of Nisan), and that the following day, the High Sabbath (15th of Nisan), was a Holy Convocation — not the weekly Saturday Sabbath, but still a required day of rest.

📖 Biblical Foundations
-----------------------

1. High Sabbath Explained

    “The Jews therefore, because it was the preparation, that the bodies should not remain upon the cross on the sabbath day, (for that sabbath day was an high day)...”
    — John 19:31 (KJV)

    - The High Sabbath (John 19:31) refers to Nisan 15, the first day of the Feast of Unleavened Bread, a holy convocation (Leviticus 23:6–7).
    - This High Sabbath is distinct from the weekly Sabbath (Saturday). Every 15th of Nisan is a Sabbath regardless of the day of the week.

2. The Crucifixion Timing

    - Jesus was crucified on Passover, the 14th of Nisan, which was a Wednesday that year.
    - The next day (Thursday, 15th of Nisan) was the High Sabbath.
    - The women couldn't go to the tomb that day (Luke 23:56), then rested again on the weekly Sabbath (Saturday).

3. Three Days and Three Nights — Literally

    “For as Jonas was three days and three nights in the whale’s belly; so shall the Son of man be three days and three nights in the heart of the earth.”
    — Matthew 12:40 (KJV)

    - Wednesday sunset to Saturday sunset = literal 3 days and 3 nights:
      - Wed night, Thu day, Thu night, Fri day, Fri night, Sat day.
    - Christ rose after the Sabbath, before dawn Sunday (Matthew 28:1–6, John 20:1).

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
 Year AD Full Moon (Nisan 14?)   Weekday
      26   0026-04-19 00:00:00    Sunday
      27   0027-04-08 00:00:00  Thursday
      28   0028-03-27 00:00:00    Monday
      29   0029-04-15 00:00:00    Sunday
      30   0030-04-05 00:00:00    Friday
      31   0031-04-24 00:00:00  Thursday
      32   0032-04-12 00:00:00    Monday
      33   0033-04-02 00:00:00  Saturday
      34   0034-03-22 00:00:00 Wednesday ✅
      35   0035-04-09 00:00:00    Monday
      36   0036-04-27 00:00:00    Sunday

✔️ AD 34 shows a full moon (Passover) falling on a Wednesday, making it the most scripturally accurate year for the crucifixion of Jesus Christ.

🛠 How to Run
-------------

1. Download the `de431_part-2.bsp` planetary ephemeris file from NASA JPL.
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


