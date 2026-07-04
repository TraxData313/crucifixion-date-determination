"""
Nisan 14 (Passover) date analysis for AD 26-36, with proper lunar-calendar modeling.

Improvements over cru_years_astro_new_moon.py:
  1. Exact conjunction times via root-finding (skyfield.almanac), not daily sampling.
  2. 1 Nisan = evening of FIRST VISIBLE CRESCENT from Jerusalem (Yallop q-criterion),
     not the astronomical conjunction (the moon is invisible at conjunction; the
     crescent appears 1-2 days later, which is how the month actually began).
  3. Correct day counting: 14 Nisan daytime = 1 Nisan daytime + 13 days.
  4. Hebrew days run sunset-to-sunset; the weekday reported is that of the DAYTIME
     portion of 14 Nisan (when the crucifixion occurred).
  5. Intercalation (13th month, Adar II) modeled as explicit scenarios instead of
     a single hardcoded window.
  6. Dates reported in both proleptic Gregorian and Julian calendars.

Ephemeris: de441_excerpt_AD20-40.bsp — an excerpt of JPL DE441 covering AD 20-40,
generated with:
  python -m jplephem excerpt 20/1/1 40/1/1 \
      https://naif.jpl.nasa.gov/pub/naif/generic_kernels/spk/planets/de441_part-1.bsp \
      de441_excerpt_AD20-40.bsp
"""

from datetime import date, timedelta
from math import asin, cos, degrees, radians

import pandas as pd
from skyfield import almanac
from skyfield.api import load, wgs84

EPHEMERIS = 'de441_excerpt_AD20-40.bsp'
YEARS = range(26, 37)

# Jerusalem, Temple Mount area
JERUSALEM = wgs84.latlon(31.7784, 35.2354, elevation_m=750)

MOON_RADIUS_KM = 1737.4

# Yallop (1997) q-test thresholds for first crescent visibility
Q_THRESHOLDS = {
    'A (easy naked eye)':      0.216,
    'B (perfect conditions)': -0.014,
    'C (hard, needs finding)': -0.160,
}

eph = load(EPHEMERIS)
ts = load.timescale()
observer = eph['earth'] + JERUSALEM
sun, moon = eph['sun'], eph['moon']


# ---------------------------------------------------------------- calendar helpers

def gregorian_to_julian_calendar(d: date) -> date:
    """Convert a proleptic-Gregorian date to the Julian calendar date."""
    jdn = d.toordinal() + 1721425  # JDN at noon of that date
    c = jdn + 32082
    yr = (4 * c + 3) // 1461
    e = c - 1461 * yr // 4
    m = (5 * e + 2) // 153
    day = e - (153 * m + 2) // 5 + 1
    month = m + 3 - 12 * (m // 10)
    year = yr - 4800 + m // 10
    return date(year, month, day)


# sanity anchor: Gregorian 22 Mar AD 34 = Julian 24 Mar AD 34
assert gregorian_to_julian_calendar(date(34, 3, 22)) == date(34, 3, 24)


def fmt(d: date) -> str:
    return d.strftime('%Y-%m-%d')


def fmt_julian(d: date) -> str:
    return gregorian_to_julian_calendar(d).strftime('%d %b')


# ---------------------------------------------------------------- astronomy

def new_moons_of_year(year):
    """Exact conjunction times, January-June."""
    t0, t1 = ts.utc(year, 1, 1), ts.utc(year, 6, 30)
    times, phases = almanac.find_discrete(t0, t1, almanac.moon_phases(eph))
    return [t for t, p in zip(times, phases) if p == 0]


def vernal_equinox(year) -> date:
    t0, t1 = ts.utc(year, 1, 1), ts.utc(year, 6, 30)
    times, seasons = almanac.find_discrete(t0, t1, almanac.seasons(eph))
    for t, s in zip(times, seasons):
        if s == 0:
            return t.utc_datetime().date()
    raise ValueError(f'no equinox found in {year}')


def setting_time(body, day: date):
    """UTC time the body sets at Jerusalem on the evening of the given date."""
    t0 = ts.utc(day.year, day.month, day.day, 10)
    t1 = ts.utc(day.year, day.month, day.day, 23)
    f = almanac.risings_and_settings(eph, body, JERUSALEM)
    times, updown = almanac.find_discrete(t0, t1, f)
    for t, u in zip(times, updown):
        if u == 0:
            return t
    return None


def yallop_q(evening: date):
    """Yallop q value at 'best time' on the given evening; None if moon sets first."""
    sunset = setting_time(sun, evening)
    moonset = setting_time(moon, evening)
    if sunset is None or moonset is None:
        return None
    lag_days = moonset.tt - sunset.tt
    if lag_days <= 0:
        return None  # moon below horizon at sunset
    best = ts.tt_jd(sunset.tt + lag_days * 4.0 / 9.0)

    app_moon = observer.at(best).observe(moon).apparent()
    app_sun = observer.at(best).observe(sun).apparent()
    alt_m, _, dist_m = app_moon.altaz()
    alt_s, _, _ = app_sun.altaz()

    arcv = alt_m.degrees - alt_s.degrees
    arcl = app_moon.separation_from(app_sun).degrees
    sd_arcmin = degrees(asin(MOON_RADIUS_KM / dist_m.km)) * 60.0
    w = sd_arcmin * (1.0 - cos(radians(arcl)))
    return (arcv - (11.8371 - 6.3226 * w + 0.7319 * w ** 2 - 0.1018 * w ** 3)) / 10.0


def first_crescent_evening(conjunction, q_threshold) -> date:
    """First evening (UTC date) after conjunction when the crescent is visible."""
    conj_date = conjunction.utc_datetime().date()
    for offset in range(0, 5):
        evening = conj_date + timedelta(days=offset)
        q = yallop_q(evening)
        if q is not None and q > q_threshold:
            return evening
    raise ValueError(f'no visible crescent within 5 days of {conj_date}')


# ---------------------------------------------------------------- calendar model

def nisan14_from_conjunction(conjunction, q_threshold):
    """Crescent evening -> 1 Nisan -> daytime date of 14 Nisan."""
    crescent = first_crescent_evening(conjunction, q_threshold)
    # crescent evening starts 1 Nisan; its daytime is the next civil day;
    # 14 Nisan daytime = 1 Nisan daytime + 13 days
    return crescent + timedelta(days=14), crescent


def pick_nisan(year, rule, q_threshold):
    """Return (conjunction, intercalated?) for the lunation chosen as Nisan."""
    moons = new_moons_of_year(year)
    equinox = vernal_equinox(year)

    if rule == 'R1_aviv_window':
        # the repo's original rule: conjunction inside Gregorian 8 Mar - 5 Apr
        for t in moons:
            d = t.utc_datetime().date()
            if date(year, 3, 8) <= d <= date(year, 4, 5):
                return t, False
        for t in moons:  # none in window -> intercalate, take next conjunction
            if t.utc_datetime().date() > date(year, 4, 5):
                return t, True
    elif rule == 'R2_equinox':
        # 14 Nisan (daytime) must fall on or after the vernal equinox
        for t in moons:
            n14, _ = nisan14_from_conjunction(t, q_threshold)
            if n14 >= equinox:
                intercalated = t.utc_datetime().date() > date(year, 4, 1)
                return t, intercalated
    elif rule == 'R3_late_harvest':
        # Newton-style conservative rule: 1 Nisan itself not before the equinox
        for t in moons:
            n14, crescent = nisan14_from_conjunction(t, q_threshold)
            nisan1 = crescent + timedelta(days=1)
            if nisan1 >= equinox:
                intercalated = t.utc_datetime().date() > date(year, 4, 1)
                return t, intercalated
    raise ValueError(f'no Nisan found for {year} under {rule}')


# ---------------------------------------------------------------- run

RULES = ['R1_aviv_window', 'R2_equinox', 'R3_late_harvest']


def main():
    # -------- Table 1: raw astronomy + crescent (criterion B) per spring lunation
    print('=' * 100)
    print('TABLE 1 - Spring lunations, exact conjunctions, first crescent (Yallop B),')
    print('          resulting 14 Nisan. All dates proleptic Gregorian; Julian in ().')
    print('=' * 100)
    rows = []
    for year in YEARS:
        equinox = vernal_equinox(year)
        for t in new_moons_of_year(year):
            conj = t.utc_datetime()
            if not (2 <= conj.month <= 5):
                continue
            n14, crescent = nisan14_from_conjunction(t, Q_THRESHOLDS['B (perfect conditions)'])
            rows.append({
                'Year': year,
                'Conjunction (UTC)': conj.strftime('%Y-%m-%d %H:%M'),
                'Crescent eve': fmt(crescent),
                'Lag(d)': (crescent - conj.date()).days,
                '14 Nisan': f'{fmt(n14)} ({fmt_julian(n14)} jul)',
                'Weekday': n14.strftime('%A'),
                'Equinox': fmt(equinox),
            })
    print(pd.DataFrame(rows).to_string(index=False))

    # -------- Table 2: scenario grid (3 intercalation rules x 3 visibility criteria)
    print()
    print('=' * 100)
    print('TABLE 2 - 14 Nisan weekday under every scenario combination')
    print('=' * 100)
    scenario_rows = []
    for year in YEARS:
        row = {'Year': year}
        for rule in RULES:
            for crit_name, q_thr in Q_THRESHOLDS.items():
                t, intercalated = pick_nisan(year, rule, q_thr)
                n14, _ = nisan14_from_conjunction(t, q_thr)
                label = f"{rule.split('_')[0]}/{crit_name[0]}"
                mark = '+13m' if intercalated else ''
                row[label] = f'{n14.strftime("%a")} {fmt_julian(n14)}{mark}'
        scenario_rows.append(row)
    df2 = pd.DataFrame(scenario_rows)
    print(df2.to_string(index=False))
    print("\n(dates in Julian calendar; '+13m' = year intercalated under that rule)")

    # -------- Table 3: robustness summary per weekday hypothesis
    print()
    print('=' * 100)
    print('TABLE 3 - Which years give Wednesday / Thursday / Friday, in how many of')
    print('          the 9 scenario combinations')
    print('=' * 100)
    combos = [(r, c) for r in RULES for c in Q_THRESHOLDS]
    for weekday in ['Wednesday', 'Thursday', 'Friday']:
        counts = {}
        for year in YEARS:
            n = 0
            for rule, crit in combos:
                t, _ = pick_nisan(year, rule, Q_THRESHOLDS[crit])
                n14, _ = nisan14_from_conjunction(t, Q_THRESHOLDS[crit])
                if n14.strftime('%A') == weekday:
                    n += 1
            if n:
                counts[year] = n
        hits = ', '.join(f'AD {y}: {n}/9' for y, n in counts.items()) or 'none'
        print(f'  {weekday:<10} -> {hits}')


if __name__ == '__main__':
    main()
