# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 17:00:47 2023

@author: David
"""

def IsUnique(seq):
    for i in range(len(seq)):
        for  j in range (i):
            if seq[i]==seq[j]:
                return False
    
    return True
    


def findUnique (seq, markerLen):
    stop = len(seq) - markerLen
    for i in range (stop):
        if (IsUnique(seq[i:i+markerLen])):
            return i+markerLen
        
    return None



def run6a():
    runningTotal = 0
    for line in open("input.txt"):
        print(line)
        start = findUnique(line.strip(),4)
        print ('Found sig at ' + str(start))
        runningTotal = runningTotal + start
 
    print('6a running total ' + str(runningTotal))        


def  run6b():
    for line in open("input.txt"):   
        print('6b running total ' + str( findUnique(line.strip(),14)))        


run6a()    

run6b()