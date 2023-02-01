# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 13:16:01 2023

@author: DiyaSa
"""

'''
The first column is what your opponent is going to play: A for Rock, B for Paper, and C for Scissors.
The second column, you reason, must be what you should play in response: X for Rock, Y for Paper, and Z for Scissors.

Your total score is the sum of your scores for each round
The score for a single round is the score for the shape you selected:
(1 for Rock, 2 for Paper, and 3 for Scissors)
 plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won)
 
 
 
 Rock defeats Scissors, Scissors defeats Paper, 
 and Paper defeats Rock. If both players choose the same shape, 
 the round instead ends in a draw.
'''

strategy = open('q2input.txt', 'r').readlines()

codings = {
    "rock":['A','X'],
    "paper":['B','Y'], 
    "scissors":['C','Z']
}

def findCoding(code):   
    for key in codings.keys():
        if code in codings[key]:
            return key

def findWinner(player1, player2):
    if player1 == 'rock' and player2 == 'scissors':
        return 0
    if player1 == 'scissors' and player2 == 'rock':
        return 1
    if player1 == 'paper' and player2 == 'rock':
        return 0
    if player1 == 'rock' and player2 == 'paper':
        return 1
    if player1 == 'scissors' and player2 == 'paper':
        return 0
    if player1 == 'paper' and player2 == 'scissors':
        return 1
    elif player1 == player2:
        return 'draw'
    
def getShapeScore(eachRound, index):

    if findCoding(eachRound[index]) == 'rock':
        shapeScore = 1
    if findCoding(eachRound[index]) == 'paper':
        shapeScore = 2
    if findCoding(eachRound[index]) == 'scissors':
        shapeScore = 3
    return shapeScore

def getYourScoreEachRound(eachRound, winner):
    if winner == 1: #which means you are the winner 
        roundScore = 6
        shapeScore = getShapeScore(eachRound, winner)

    if winner == 0: #which means you lost
        roundScore = 0
        shapeScore = getShapeScore(eachRound, 1)
        
    if winner == 'draw':
        roundScore = 3
        shapeScore = getShapeScore(eachRound, 0) #doesn't matter of index as both same
    return shapeScore + roundScore
        
scoresList = []
for line in strategy:
    eachRound = line.strip().split(' ')
    winner = findWinner(findCoding(eachRound[0]), findCoding(eachRound[1]))
    scoresList.append(getYourScoreEachRound(eachRound, winner))
    
    
print(sum(scoresList)) #parta


#part b, second column now means how the round should end. X = you lose, Y = draw, Z = you win 

def yourHand(opponent, outcome):
    if outcome == 'X':
        for hand in ['rock', 'paper', 'scissors']:
            if findWinner(opponent, hand) == 0:
                return hand 
    if outcome == 'Y':
        return opponent
    if outcome == 'Z':
        for hand in ['rock', 'paper', 'scissors']:
            if findWinner(opponent, hand) == 1:
                return hand 

def getYourScoreEachRoundPartB(yourHand, winner):
    if yourHand == 'rock':
        shapeScore = 1
    if yourHand == 'paper':
        shapeScore = 2
    if yourHand == 'scissors':
        shapeScore = 3
        
    if winner == 1: #which means you are the winner 
        roundScore = 6
    if winner == 0: #which means you lost
        roundScore = 0
    if winner == 'draw':
        roundScore = 3

    return shapeScore + roundScore
    
scoresListPartB = []
for line in strategy:
    eachRound = line.strip().split(' ')
    opponent = findCoding(eachRound[0])
    myHand = yourHand(findCoding(eachRound[0]), eachRound[1])
    winner = findWinner(opponent, myHand)
    scoresListPartB.append(getYourScoreEachRoundPartB(myHand, winner))
     
print(sum(scoresListPartB)) #partb
    
