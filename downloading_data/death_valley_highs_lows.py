# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 16:50:44 2020
death_valley_2014.csv
with missing data
@author: ikventure
"""

import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    #get dates, and high and low temperatures from this file.
    dates, highs, lows = [], [], []
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
    
    #Plot the high and low temperatures.
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c='red', alpha=0.5)
    ax.plot(dates, lows, c='blue', alpha=0.5)
    ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
    
    #Format plot
    title = "Daily high and low temperatures - 2014\nDeath Valley, CA"
    ax.set_title(title, fontsize=20)
    ax.set_xlabel('', fontsize=16)
    fig.autofmt_xdate()
    ax.set_ylabel("Temperature(F)", fontsize=16)
    ax.set_ylim(bottom=0, top=120)
    ax.tick_params(axis='both', which='major', labelsize=16)
    
    plt.show()