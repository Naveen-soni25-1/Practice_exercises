from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt
import mplcursors

path_1 = Path('weather_data\sitka_weather_2021_full.csv')
lines_1 = path_1.read_text().splitlines()
reader_1 = csv.reader(lines_1)
header_row1 = next(reader_1)

path_2 = Path('weather_data\death_valley_2021_full.csv')
lines_2 = path_2.read_text().splitlines()
reader_2 = csv.reader(lines_2)
header_row_2 = next(reader_2)

date_1, pcrpt_1 = [], []
date_2, pcrpt_2 = [], []

for row in reader_1:
    try:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        pcrp = float(row[5])
    except:
        continue
    else:
        date_1.append(current_date)
        pcrpt_1.append(pcrp)

for row in reader_2:
    try:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        pcrp = float(row[3])
    except:
        continue
    else:
        date_2.append(current_date)
        pcrpt_2.append(pcrp)

plt.style.use("dark_background")
fig, (ax1,ax2) = plt.subplots(1, 2, figsize=(10, 7), dpi=100)

line_1 = ax1.plot(date_1, pcrpt_1, c="pink", alpha=0.7, linewidth=2, marker="o", label="Sitka Precipitate")[0]
ax1.set_title("Daily Precipitate Data", fontsize=24)
ax1.set_xlabel("Time", fontsize=16)
ax1.set_ylabel("Precipitate", fontsize=16)
ax1.legend(loc="best", title="Sitka", fontsize=16)

line_2 = ax2.plot(date_2, pcrpt_2, c="indigo", alpha=0.7, linewidth=2, marker="v", label="Death_valley Precipitate")[0]
ax2.set_title("Daily Precipitate Data", fontsize=24)
ax2.set_xlabel("Time", fontsize=16)
ax2.set_ylabel("Precipitate", fontsize=16)
ax2.legend(loc="best", title="Death_valley", fontsize=16)

fig.align_titles()
fig.align_labels()

mplcursors.cursor([line_1, line_2], hover=True)

plt.tight_layout()
plt.show()