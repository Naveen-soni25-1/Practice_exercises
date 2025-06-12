from pathlib import Path
import csv
from datetime import datetime

import plotly.express as px

# Load and read data
path = Path('eq_data/world_fires_1_day.csv')  # Use forward slashes or raw string
lines = path.read_text().splitlines()
reader = csv.reader(lines)
header_row = next(reader)

# Indexes for important columns
lat_idx = header_row.index("latitude")
lon_idx = header_row.index("longitude")
bright_idx = header_row.index("brightness")
scan_idx = header_row.index("scan")
track_idx = header_row.index("track")
date_idx = header_row.index("acq_date")
time_idx = header_row.index("acq_time")
satellite_idx = header_row.index("satellite")
daynight_idx = header_row.index("daynight")

# Extract data
lats, lons, brightness, scan, track, current_date, time, satellite, daynight = [], [], [], [], [], [], [], [], []

for row in reader:
    try:
        lats.append(float(row[lat_idx]))
        lons.append(float(row[lon_idx]))
        brightness.append(float(row[bright_idx]))
        scan.append(float(row[scan_idx]))
        track.append(float(row[track_idx]))
        current_date.append(datetime.strptime(row[date_idx], "%Y-%m-%d"))
        time.append(row[time_idx])  # Keeping time as string for hover info
        satellite.append(row[satellite_idx])
        daynight.append(row[daynight_idx])
    except ValueError:
        # Skip rows with invalid/missing data
        continue

# Create Plotly figure
fig = px.scatter_geo(
    lat=lats,
    lon=lons,
    size=brightness,
    color=brightness,
    color_continuous_scale='viridis',
    hover_data={
        "scan": scan,
        "track": track,
        "date": current_date,
        "time": time,
        "satellite": satellite,
        "day/night": daynight,
    },
    labels={"color": "brightness"},
    opacity=0.5
)

fig.update_geos(
    showcoastlines=True, coastlinecolor="royalblue",
    showland=True, landcolor="forestgreen",
    showrivers=True, rivercolor="skyblue",
    showocean=True, oceancolor="lightblue",
    showcountries=True, countrycolor='lightcyan',
)

fig.show()
