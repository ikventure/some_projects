# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 09:59:50 2020
mpl_squares.py ch15.2
@author: ikventure
"""

import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)


#设置图表标题，并给坐标轴加上标签
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

#设置刻度标记的大小
ax.tick_params(axis="both", labelsize=14)

plt.show()