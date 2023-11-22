# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def is_none_or_whitespace(input_str):

    return input_str is None or input_str.isspace() or ( len(input_str) <1)  

filestream = open ("sample.txt" ,"rt")
scores =  {0:0}
i =0

for currline in filestream :
   
    if is_none_or_whitespace(currline):
        i=i+1
        scores[i]=0
    else:
       scores[i]= scores[i] + int(currline)
       
   
    
    
print(scores.values)
    
        
    