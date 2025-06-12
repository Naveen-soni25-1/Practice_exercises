from pathlib import Path
import json

import plotly.express as px

path = Path('eq_data/1.0_hour.geojson')
contents = path.read_text(encoding="utf-8")
eq_data = json.loads(contents)
title = eq_data["metadata"]["title"]
all_eq_dicts = eq_data["features"]

mags = [eq["properties"]["mag"] for eq in all_eq_dicts ]
lons = [eq["geometry"]["coordinates"][0] for eq in all_eq_dicts ]
lats = [eq["geometry"]["coordinates"][1] for eq in all_eq_dicts ]
eq_title = [eq["properties"]["title"] for eq in all_eq_dicts ]


fig = px.scatter_geo(
    lon=lons,
    lat=lats,
    size=mags,
    hover_name=eq_title,
    projection="natural earth",
)
fig.update_geos(
    resolution=110,
    showcoastlines=True, coastlinecolor="royalblue",
    showocean=True, oceancolor="LightBlue",
    showrivers=True, rivercolor="Blue",
    showcountries=True, countrycolor='lightcyan',
    showland=True, landcolor="forestgreen"
)

fig.show()