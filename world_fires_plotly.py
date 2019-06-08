import csv

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline


filename = 'data/world_fires_7_day.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    lat_index = header_row.index('latitude')
    lon_index = header_row.index('longitude')
    bright_index = header_row.index('bright_ti4')

    lats, lons, brights = [], [], []
    for row in reader:
        lat = float(row[lat_index])
        lon = float(row[lon_index])
        bright = float(row[bright_index])
        lats.append(lat)
        lons.append(lon)
        brights.append(bright)

data = ([{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': brights,
    'marker': ({
        # 'size': [5*bright for bright in brights],
        'color': brights,
        'colorscale': 'RdBu',
        'colorbar': {'title': 'Brightness'},
        }),
    }])
my_layout = Layout(title='Fire around the World in the Last 7 Day')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='wold_fires_7_day.html')
