# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 14:14:17 2020
mpl_die_rolling.py ex15.10
@author: ikventure
"""

import matplotlib.pyplot as plt

from die import Die

#Create two D6 Dice.
die_1 = Die()
die_2 = Die()

results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

#Analyze the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

#Visualize the results.
x_values = list(range(2, max_result+1))

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(x_values, frequencies, linewidth=3)

ax.set_title("Results for rolling two dice 1000 times", fontsize=24)
ax.set_xlabel("Result", fontsize=14)
ax.set_ylabel("Times", fontsize=14)

ax.tick_params(axis='both', labelsize=14)

plt.show()