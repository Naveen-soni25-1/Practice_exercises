from pathlib import Path
import json

path = Path('eq_data/all_day.geojson')
content = path.read_text(encoding="utf-8")
all_eq_data = json.loads(content)

all_eq_dict = all_eq_data['features']
print(len(all_eq_dict))

mags, lons, lats = [], [], []
for eq_dict in all_eq_dict:
    mag = eq_dict['properties']['mag']
    lon = eq_dict["geometry"]["coordinates"][0]
    lat = eq_dict["geometry"]["coordinates"][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)


print(mags[:10], lons[:10], lats[:10])