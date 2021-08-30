# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 10:42:45 2020

@author: ikventure
"""

import csv

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = 'data/world_fires_1_day.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    lats, lons, brights = [], [], []
    for row in reader:
        lats.append(row[0])
        lons.append(row[1])
        bright = row[2]
        brights.append(float(bright)//100)

data = [{
    'type': 'scattergeo', 
    'lon': lons, 
    'lat': lats,
    'marker':{
        'size': [bright for bright in brights],
        'color': brights, 
        'colorscale': 'Reds',  
        'colorbar': {'title': 'Brightness'}
    },
}]

my_layout = Layout(title="World fires 1 day")

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='World fires 1 day.html')