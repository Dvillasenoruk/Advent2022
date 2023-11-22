# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 15:02:36 2023

@author: David
"""
def scoreMove(move):

    # PAPER
    if (move == "PAPER"):
        return 2
    
    # ROCK
    if move == "ROCK":
        return 1
    
    # SCISSORS
    if move == "SCISSORS":
        return 3
    
def PlayRelative (theirMove, wld):
    if (wld == "DRAW") :
        return theirMove
    
    if theirMove =="PAPER":
        if wld == "WIN":
            return "SCISSORS"
        return "ROCK"
    
    if theirMove == "ROCK":
        if wld== "WIN":
            return "PAPER"
        return "SCISSORS"
    
    if theirMove == "SCISSORS":
        if wld == "WIN":
            return "ROCK"
        return "PAPER"
    
    

def WLD (q):
    if q== "X":
        return "LOSE"
    if q=="Y":
        return "DRAW"
    return "WIN"

def scoreWin (opp, ours):
       # ROCK
    if opp == "ROCK": 
        if ours =="ROCK":
           return 3
        if ours == "PAPER":
            return 6
        return 0
    
    # PAPER
    if opp == "PAPER":
       if ours =="ROCK":
          return 0      
       if ours == "PAPER":
          return 3     
       return 6
   
    # scissors
    if ours == "ROCK" :
       return 6
    if ours == "PAPER" :
       return 0
    return 3

def TranslateMove(m):
    if m =="A" or m == "X" :
       return "ROCK"
    if m== "B" or m == "Y" : 
        return "PAPER"
    return "SCISSORS"

        
Totalscore = 0
for line in open("input.txt"):
    print(line)
    play = line.strip().split(' ')
    
    theirMove = TranslateMove(play[0])
    #ourMove = TranslateMove(play[1])
    ourMove = PlayRelative (theirMove, WLD(play[1]))
    print (theirMove , ourMove)
    score = scoreMove(ourMove)
    score = score + scoreWin(theirMove, ourMove)
    Totalscore = Totalscore + score
    print(score)
    
print(Totalscore)



