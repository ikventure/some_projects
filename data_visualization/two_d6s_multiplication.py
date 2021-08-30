# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 14:14:11 2020
multiplications.py ex15.8
@author: ikventure
"""

from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

#Create two D6 Dice.
die_1 = Die()
die_2 = Die()

results = []
for roll_num in range(1000):
    result = die_1.roll() * die_2.roll()
    results.append(result)

#Analyze the results.
frequencies = []
max_result = die_1.num_sides * die_2.num_sides
for value in range(1, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

#Visualize the results.
x_values = list(range(1, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling two D6 dice 1000 times', 
        xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d6_multi.html')