from pathlib import Path
from datetime import datetime
import csv

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import mplcursors

# === Load & Parse Data ===
path = Path('weather_data/death_valley_2021_full.csv')
lines = path.read_text().splitlines()
reader = csv.reader(lines)

header_row = next(reader)
STATION_INDEX = header_row.index("NAME")
MAX_TEMP_INDEX = header_row.index("TMAX")
MIN_TEMP_INDEX = header_row.index("TMIN")
DATE_INDEX = header_row.index("DATE")

dates, highs, lows = [], [], []
station_name = None

for row in reader:
    try:
        if not station_name:
            station_name = row[STATION_INDEX].strip()
        current_date = datetime.strptime(row[DATE_INDEX], '%Y-%m-%d')
        high = int(row[MAX_TEMP_INDEX])
        low = int(row[MIN_TEMP_INDEX])
    except (ValueError, IndexError):
        continue
    else:
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

# === Plotting Setup ===
plt.style.use("seaborn-v0_8-whitegrid")
fig, ax = plt.subplots(figsize=(14, 6), dpi=120)

# === Main Lines and Fill ===
ax.plot(dates, highs, color='orangered', label='Max Temp (°F)', linewidth=2)
ax.plot(dates, lows, color='royalblue', label='Min Temp (°F)', linewidth=2)
ax.fill_between(dates, highs, lows, facecolor='lightsteelblue', alpha=0.3)

# === Annotations ===
max_temp = max(highs)
min_temp = min(lows)
max_index = highs.index(max_temp)
min_index = lows.index(min_temp)
ax.annotate(f'Hottest: {max_temp}°F', xy=(dates[max_index], max_temp),
            xytext=(dates[max_index], max_temp + 5),
            arrowprops=dict(arrowstyle='->', color='red'),
            color='red', fontsize=10)

ax.annotate(f'Coldest: {min_temp}°F', xy=(dates[min_index], min_temp),
            xytext=(dates[min_index], min_temp - 10),
            arrowprops=dict(arrowstyle='->', color='blue'),
            color='blue', fontsize=10)

# === Axes Formatting ===
ax.set_title(f"{station_name} - 2021 Daily Temperature Overview", fontsize=20, weight='bold')
ax.set_xlabel("Date", fontsize=14)
ax.set_ylabel("Temperature (°F)", fontsize=14)
ax.legend(loc="upper right", fontsize=12)

ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b'))

fig.autofmt_xdate()
ax.grid(True, linestyle='--', alpha=0.3)

# === Interactive Cursor ===
mplcursors.cursor(hover=True).connect("add", lambda sel: sel.annotation.set_text(
    f"{sel.artist.get_label()}\n{sel.target[0].strftime('%b %d')}\n{int(sel.target[1])}°F"
))

# === Optional Save ===
# fig.savefig("death_valley_2021_weather_chart.png", bbox_inches='tight')

plt.tight_layout()
plt.show()