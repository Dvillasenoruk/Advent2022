# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 15:17:47 2023

@author: David
"""
def Score(collection):
    totalscore =0
    for l in collection:
        i= ord (l[0])
        if i >= ord('a') and i<=ord('z'):
           totalscore = totalscore + i - ord('a') + 1 
          
        if i >=ord('A') and i <=ord('Z'):
           totalscore = totalscore + i - ord('A') + 27
    
    return totalscore

# version 1
#runningscore = 0

#for line in open("input.txt"):
#    load = line.strip()
#    part1= set(load[:int(len(load)/2)])
#    part2= set(load[int(len(load)/2):])
#    score = Score(part1.intersection(part2))
#    runningscore = runningscore + score
    
#print(runningscore)

#version 2#
def FindBadge (group):
    return set(group[0]).intersection(group[1]).intersection(group[2])

runningScore = 0
group = []
groupcount = 0

for line in open("input.txt"):
    load = line.strip()
    group.append(load)
    groupcount = groupcount + 1
    if groupcount == 3 :
        runningScore = runningScore+ Score(FindBadge(group))
        groupcount = 0
        group = []
        

print(runningScore)