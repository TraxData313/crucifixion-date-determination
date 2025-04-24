from skyfield.api import load
from datetime import timedelta
import pandas as pd
from datetime import datetime

# Load ephemeris
eph = load('C:/Users/anton/Desktop/de431_part-2.bsp')  # Download this file https://naif.jpl.nasa.gov/pub/naif/generic_kernels/spk/planets/ from here and ajust the path to your download location
ts = load.timescale()

earth, moon, sun = eph['earth'], eph['moon'], eph['sun']

results = []

def find_new_moon_in_window(start_date, end_date):
    t0 = ts.utc(start_date.year, start_date.month, start_date.day)
    t1 = ts.utc(end_date.year, end_date.month, end_date.day)

    times = []
    phases = []

    for day_offset in range((t1.utc_datetime() - t0.utc_datetime()).days):
        t = ts.utc(t0.utc_datetime() + timedelta(days=day_offset))
        e = earth.at(t)
        sun_lon = e.observe(sun).apparent().ecliptic_latlon()[1].degrees
        moon_lon = e.observe(moon).apparent().ecliptic_latlon()[1].degrees
        phase = (moon_lon - sun_lon) % 360
        times.append(t)
        phases.append(phase)

    if not phases:
        return None

    # Новолуние ≈ фаза около 0°
    closest_idx = min(range(len(phases)), key=lambda i: min(phases[i], 360 - phases[i]))
    return times[closest_idx].utc_datetime()

# Process years AD 26–36
for year in range(26, 37):
    # Основен прозорец: 8 март – 5 април
    aviv_start = datetime(year, 3, 8)
    aviv_end = datetime(year, 4, 5)

    new_moon = find_new_moon_in_window(aviv_start, aviv_end)

    added_13th_month = False

    if not new_moon:
        # Няма новолуние в прозореца → високосна година, търси следващото
        added_13th_month = True
        extended_start = datetime(year, 4, 6)
        extended_end = datetime(year, 5, 5)
        new_moon = find_new_moon_in_window(extended_start, extended_end)

    nisan_14 = new_moon + timedelta(days=14)

    weekday = nisan_14.strftime('%A')

    results.append({
        'Year AD': year,
        'Added 13th Month?': 'Yes' if added_13th_month else 'No',
        '1 Nisan (New Moon)': new_moon.strftime('%Y-%m-%d %H:%M:%S'),
        '14 Nisan (Passover)': nisan_14.strftime('%Y-%m-%d %H:%M:%S'),
        'Weekday (Passover)': weekday
    })

# Filter for Wednesday only
df = pd.DataFrame(results)
wednesday_df = df[df['Weekday (Passover)'] == 'Wednesday']

# Output only matching years
print()
print(df)
print()
print("📜 Years where 14 Nisan fell on a Wednesday (possible crucifixion years):\n")
print(wednesday_df.to_string(index=False))
