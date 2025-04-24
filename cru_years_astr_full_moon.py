from skyfield.api import load
from datetime import timedelta
import pandas as pd

# Load the long-range ephemeris
eph = load('C:/Users/anton/Desktop/de431_part-2.bsp')  # Update path if needed
ts = load.timescale()

earth, moon, sun = eph['earth'], eph['moon'], eph['sun']

results = []

def get_full_moon_near_passover(year):
    # Start after the spring equinox
    t0 = ts.utc(year, 3, 21)
    t1 = ts.utc(year, 4, 30)

    times = []
    phases = []

    for day_offset in range((t1.utc_datetime() - t0.utc_datetime()).days):
        t = ts.utc(year, 3, 21 + day_offset)
        e = earth.at(t)
        sun_lon = e.observe(sun).apparent().ecliptic_latlon()[1].degrees
        moon_lon = e.observe(moon).apparent().ecliptic_latlon()[1].degrees
        phase = (moon_lon - sun_lon) % 360
        times.append(t)
        phases.append(phase)

    # Find time where phase is closest to 180° (full moon)
    closest_idx = min(range(len(phases)), key=lambda i: abs(phases[i] - 180))
    full_moon_time = times[closest_idx].utc_datetime()
    return full_moon_time

# Process AD 26–36
for year in range(26, 37):
    full_moon = get_full_moon_near_passover(year)
    results.append({
        'Year AD': year,
        'Full Moon (Nisan 14?)': full_moon.strftime('%Y-%m-%d %H:%M:%S'),
        'Weekday': full_moon.strftime('%A')
    })

# Output results
df = pd.DataFrame(results)
print(df.to_string(index=False))
