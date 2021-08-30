# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 20:43:18 2020
show_color_scales.py
@author: ikventure
"""

from plotly import colors

for key in colors.PLOTLY_SCALES.keys():
    print(key)