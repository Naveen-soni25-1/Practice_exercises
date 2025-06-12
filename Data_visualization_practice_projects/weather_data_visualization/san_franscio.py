from collections import defaultdict
from pathlib import Path
from datetime import datetime
import csv

import matplotlib.pyplot as plt
import mplcursors

path = Path('weather_data\san_franscio.csv')
lines = path.read_text().splitlines()
reader =csv.reader(lines)
header_row = next(reader)

station_data = defaultdict(lambda: {"date":[], "tmaxs":[], "tmins":[]})
station = "USC00047339"

for row in reader:
        if row[0] == "USC00047339":
            try:
                current_date = datetime.strptime(row[2], '%Y-%m-%d')
                tmax = int(row[9])
                tmin = int(row[10])
            except:
                continue
            else:
                station_data[station]["date"].append(current_date)
                station_data[station]["tmaxs"].append(tmax)
                station_data[station]["tmins"].append(tmin)


plt.style.use("seaborn-v0_8")
fig, ax = plt.subplots(figsize=(10, 5), dpi=100)
for data in station_data.values():
   line_1 = ax.plot(data["date"], data["tmaxs"], marker='o', linewidth=1, c="indigo", label="Max Temperature", alpha=0.4)[0]
   line_2 = ax.plot(data["date"], data["tmins"], marker='v', linewidth=1, c="purple", label="Min Temperature", alpha=0.4)[0]
   ax.fill_between(data["date"], data["tmaxs"], data["tmins"], facecolor="blue", alpha=0.2)
   ax.set_title("Daily High & Low Temperature", fontsize=24)
   ax.set_xlabel("Time", fontsize=14)
   ax.set_ylabel("Temperature (F)", fontsize=14)
   ax.legend(loc="best", title="Temperature")

   fig.autofmt_xdate()
   fig.align_labels()

mplcursors.cursor([line_1, line_2], hover=True)

plt.show()