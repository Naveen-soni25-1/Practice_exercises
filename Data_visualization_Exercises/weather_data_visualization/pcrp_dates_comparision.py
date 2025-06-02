from pathlib import Path
import csv
from datetime import datetime
import matplotlib.pyplot as plt
import mplcursors

# Read Sitka data
path_1 = Path('weather_data/sitka_weather_2021_full.csv')
lines_1 = path_1.read_text().splitlines()
reader_1 = csv.reader(lines_1)
header_row1 = next(reader_1)

# Read Death Valley data
path_2 = Path('weather_data/death_valley_2021_full.csv')
lines_2 = path_2.read_text().splitlines()
reader_2 = csv.reader(lines_2)
header_row2 = next(reader_2)

date_1, pcrp_1 = [], []
date_2, pcrp_2 = [], []

for row in reader_1:
    try:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        pcrp = float(row[5])
        date_1.append(current_date)
        pcrp_1.append(pcrp)
    except:
        continue

for row in reader_2:
    try:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        pcrp = float(row[3])
        date_2.append(current_date)
        pcrp_2.append(pcrp)
    except:
        continue

# Match dates
pcrp_dict_2 = dict(zip(date_2, pcrp_2))
common_dates = [d for d in date_1 if d in pcrp_dict_2]
sitka_pcrp = [pcrp_1[date_1.index(d)] for d in common_dates] # .index() is a prebuilt search method in Python for lists return index
dv_pcrp = [pcrp_dict_2[d] for d in common_dates]

# Plot the graph
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots(figsize=(10, 5), dpi=100)
line_1 = ax.plot(date_1, pcrp_1, c='purple', linewidth=1.3, alpha=0.3, marker="o", label="Sitka")[0]
line_2 = ax.plot(date_2, pcrp_2, c="indigo", linewidth=1.5, alpha=0.5, marker="v", label="Death Valley")[0]
ax.fill_between(common_dates, sitka_pcrp, dv_pcrp, facecolor='blue', alpha=0.2)

# Labeling
ax.set_title("Daily Precipitation: Sitka vs Death Valley", fontsize=20)
ax.set_xlabel('', fontsize=14)
ax.set_ylabel("Precipitation (inches)", fontsize=14)
ax.tick_params(labelsize=12)
fig.autofmt_xdate()
ax.legend(loc="best", title="Location")

# Interactive tooltip
cursor = mplcursors.cursor([line_1, line_2], hover=True)

plt.show()
