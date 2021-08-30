# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 11:05:34 2020

@author: ikventure
"""

import csv
from datetime import datetime

import matplotlib.pyplot as plt

def get_weather_data(filename, dates, highs, lows):
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)
    
        #get dates, and high and low temperatures from this file.
        #dates, highs, lows = [], [], []
        for row in reader:
            try:
                current_date = datetime.strptime(row[0], '%Y-%m-%d')
                high = int(row[1])
                low = int(row[3])
            except ValueError:
                print(current_date, 'missing data')
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)
    
dates, highs, lows = [], [], []
filename1 = 'sitka_weather_2014.csv'
get_weather_data(filename1, dates, highs, lows)

#Plot Sikta weather data.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.6)
ax.plot(dates, lows, c='blue', alpha=0.6)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.15)

#Get Death Valley data.
dates, highs, lows = [], [], []
filename2 = 'death_valley_2014.csv'
get_weather_data(filename2, dates, highs, lows)

#Add Death Valley data to current plot.
ax.plot(dates, highs, c='red', alpha=0.3)
ax.plot(dates, lows, c='blue', alpha=0.3)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.05)

#Format plot
title = "Daily high and low temperatures - 2014"
title += "\nSitka, AK and Death Valley, CA"
ax.set_title(title, fontsize=20)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature(F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)
ax.set_ylim(10, 120)

plt.show()