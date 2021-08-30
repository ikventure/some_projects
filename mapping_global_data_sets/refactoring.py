# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 20:49:44 2020
refactoring.py ex16.6
@author: ikventure
"""

import json

#Explore the structure of the data.
filename = 'data/eq_data_30_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']

value_lines = []
for eq_dict in all_eq_dicts:
    value_line = eq_dict
    value_lines.append(eq_dict)

print(value_lines[:10])