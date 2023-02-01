# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 15:28:20 2023

@author: DiyaSa
"""

'''
The list of items for each rucksack is given as characters all on a single line.
 A given rucksack always has the same number of items in each of its two compartments,
 so the first half of the characters represent items in the first compartment, 
 while the second half of the characters represent items in the second compartment.


'''
def findCommon(comp1, comp2):
    for item in comp1:
        if item in comp2:
            return item

def char_position(letter):
    return ord(letter) - 96


def findCommonThreeElfGrp(ls):
    for item in ls[0]:
        if item in ls[1] and item in ls[2]:
            return item

def findTotalPriority(commonItems):
    total = 0 
    for eachItem in commonItems:
        if eachItem.isupper():
            total += (58 + char_position(eachItem))
        else:
            total += char_position(eachItem)
    return total
            

rucksackContents =  open('q3input.txt', 'r').readlines()
commonItems = []
#split in half and find comment item in each compartment
for each in rucksackContents:
    each.strip()
    mid = len(each)//2
    comp1 = each[0:mid] #not inclusive of mid index
    comp2 = each[mid:-1]
    commonItems.append(findCommon(comp1, comp2))

   
print(findTotalPriority(commonItems))



#Three elf groups (partb)
commonItemsPartb = []
ThreeElfGroup = []
counter = 0
for content in rucksackContents:
    counter+=1
    ThreeElfGroup.append(content.strip())
    if counter == 3: #index 3 not inclusive so 0:2
        commonItemsPartb.append(findCommonThreeElfGrp(ThreeElfGroup))
        #reset variables
        ThreeElfGroup = []
        counter = 0

print(findTotalPriority(commonItemsPartb))
