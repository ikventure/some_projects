# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 12:52:23 2020
random_walk.py ch15.3 ex15.5
@author: ikventure
"""

from random import choice

class RandomWalk():
    """一个生成随机漫步数据的类"""
    
    def __init__(self, num_points=5000):
        """初始化随机漫步的属性"""
        self.num_points = num_points
        
        #所有随机漫步都始于（0，0）
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        #决定前进方向以及沿这个方向前进的距离r
        choice_direction = choice([1, -1])
        choice_distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
        return choice_direction * choice_distance  

    def fill_walk(self):
        """计算随机漫步包含的所有点"""
        while len(self.x_values) < self.num_points:
            x_step = self.get_step()
            y_step = self.get_step()
            
            #拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue
            
            #计算下一个点的x和y值
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step
            
            self.x_values.append(x)
            self.y_values.append(y)
            
