# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


def AddIfTop3 (mylist, candidate):
        elements = 0
        bigger = False
        smallest = 999999999
        
        for existing in mylist:
            elements = elements + 1 
            bigger = bigger or (candidate > existing)
            if existing < smallest :
               smallest = existing

        if elements < 3 :
                mylist.append(candidate)                
        else : 
            if bigger :
              mylist.remove (smallest)              
              mylist.append (candidate)
       
def is_none_or_whitespace(input_str):

    return input_str is None or input_str.isspace() or ( len(input_str) <1)  

filestream = open ("sample.txt" ,"rt")
scores =  {0:0}
results = []
cur = 0
for currline in filestream :
   
    if is_none_or_whitespace(currline):
        # if (cur > max ) :
        #   max = cur
        print (cur)
        AddIfTop3(results, cur)
        print (results)
        cur = 0
    else:
       cur = cur + int(currline)
       
   
    
    
print(results)

totalCalories =0
for cal in results :
    totalCalories = totalCalories + cal
    
print (totalCalories)
    
        
    