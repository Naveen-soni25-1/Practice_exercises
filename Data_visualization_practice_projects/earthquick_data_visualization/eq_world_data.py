from pathlib import Path
import json

import plotly.express as px

# Load data
path = Path("eq_data/all_month.geojson")
contents = path.read_text(encoding="utf-8")
all_eq_data = json.loads(contents)
all_eq_dicts = all_eq_data["features"]
title = all_eq_data["metadata"]["title"]

# Prepare lists
mags = [eq_dict["properties"]["mag"] for eq_dict in all_eq_dicts if eq_dict["properties"]["mag"]  is not None and eq_dict["properties"]["mag"] >= 0]
lons = [eq_dict["geometry"]["coordinates"][0] for eq_dict in all_eq_dicts if eq_dict["properties"]["mag"]  is not None and eq_dict["properties"]["mag"] >= 0]
lats = [eq_dict["geometry"]["coordinates"][1] for eq_dict in all_eq_dicts if eq_dict["properties"]["mag"]  is not None and eq_dict["properties"]["mag"] >= 0]
eq_title = [eq_dict["properties"]["title"] for eq_dict in all_eq_dicts if eq_dict["properties"]["mag"]  is not None and eq_dict["properties"]["mag"] >= 0]

fig = px.scatter_geo(
    lat=lats,
    lon=lons,
    size=mags,
    color=mags,
    color_continuous_scale='viridis',
    labels={"color":"Magnitude"},
    hover_name=eq_title,
    title=title,
    projection="natural earth",
    opacity=0.5
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