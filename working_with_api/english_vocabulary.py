# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 16:15:44 2020

@author: ikventure
"""

filename = 'SUM_of_cet4+6+toefl+gre.txt'
txt = open(filename, "r").read()
txt = txt.lower()
all_words = txt.split()
words1, words2 = [], []
for word in all_words:
    if len(word) == 6 and word[0] == word[-1] and word[1] != word[4]:
        words1.append(word)
    if len(word) == 5 and word[0] == word[-1] and word[1] != word[3]:
        words2.append(word)
print(len(words1))
print(len(words2))
for word1 in words1:
    for word2 in words2:
        if word1[0:2] == word2[0:2] and word1[4:6] == word2[3:5]:
            print(word1 + " " + word2)