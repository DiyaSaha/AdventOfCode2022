# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 12:28:00 2023

@author: DiyaSa
"""
elves = dict()
key = 0
array = []
with open('q1input.txt', 'r') as f:
    for line in f:
        array.append(line.strip())
        if line == '\n':
            elves[key] = array
            key+=1 #reset
            array = [] #reset
            
        
f.close()

total = 0 
totalCaloriesList = []
for key in elves.keys():
    for calories in elves[key]:
        if calories != '':
            total += int(calories)
    totalCaloriesList.append(total)        
    total = 0
    
    
totalCaloriesList.sort(reverse = True)
print('Top 3 total calories are:', totalCaloriesList[0:3])
print('SUM OF Top 3 total calories are:', sum(totalCaloriesList[0:3]))
