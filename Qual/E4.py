# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 04:56:01 2020

@author: grego
"""

import numpy as np

def printfl(text):
    print(text, flush=True)


def genSchedule(S, E, N):
    cBusyUntil = -1
    jBusyUntil = -1
    
    scheduleList = [None] * N

    idxSort = np.argsort(S)
    
    for i in idxSort:
        if S[i] >= cBusyUntil:
            scheduleList[i] = 'C'
            cBusyUntil = E[i]
        elif S[i] >= jBusyUntil:
            scheduleList[i] = 'J'
            jBusyUntil = E[i]
        else:
            return 'IMPOSSIBLE'
        
    return "".join(scheduleList)


def findTwoPairs(guessedB, knownDigits):
    foundEqual = False
    foundUnequal = False
    idxFront = 0
    idxBack = B - 1
    neqIdxFront = -1
    eqIdxFront = -1
    
    while not (foundEqual and foundUnequal):
        if idxBack <= idxFront:
            break
        
        if knownDigits[idxBack] and knownDigits[idxFront]:
            if guessedB[idxBack] == guessedB[idxFront]:
                foundEqual = True
                eqIdxFront = idxFront
            else:
                foundUnequal = True
                neqIdxFront = idxFront
        else:
            knownDigits[idxBack]  = False
            knownDigits[idxFront] = False
                
        idxBack -= 1
        idxFront += 1
            
    return [foundEqual, foundUnequal, eqIdxFront, neqIdxFront]


def determineFluctuation(foundEqual, foundUnequal, eqNumberOld, eqNumberNew, neqNumberOld, neqNumberNew):
    # 1 = reverse, 2 = negate, 3 = negate and shift, 4 = nothing
    if foundEqual and foundUnequal:
        if eqNumberOld == eqNumberNew:
            if neqNumberOld == neqNumberNew:
                return 4
            else:
                return 1
        else:
            if neqNumberOld == neqNumberNew:
                return 3
            else:
                return 2
    elif foundEqual:
        if eqNumberOld == eqNumberNew:
            return 4
        else:
            return 2
    elif foundUnequal:
        if neqNumberOld == neqNumberNew:
            return 4
        else:
            return 1
    
    raise "NO!"
        
            
                

def isSpecialCase(queryNr):
    return (queryNr != 1) and (int(str(queryNr)[-1]) == 1) # first case does not matter
        

# Read input
T, B = [int(s) for s in input().split(" ")]


for i in range(T):
    guessedB = [9] * B
    knownDigits = [False] * B
    idxFront = 0
    idxBack = B - 1
    searchFront = True
    queryNr = 1
    
    while queryNr <= 150:
        if isSpecialCase(queryNr):
            foundEqual, foundUnequal, eqIdxFront, neqIdxFront = findTwoPairs(guessedB, knownDigits)
            
            eqNumberOld = 0
            eqNumberNew = 0
            neqNumberOld = 0
            neqNumberNew = 0            
            
            if foundEqual:
                printfl(eqIdxFront + 1)
                eqNumberOld = guessedB[eqIdxFront]
                eqNumberNew = int(input())
                queryNr += 1
            
            if foundUnequal:
                printfl(neqIdxFront + 1)
                neqNumberOld = guessedB[neqIdxFront]
                neqNumberNew = int(input())
                queryNr += 1
            
            caseFluct = determineFluctuation(foundEqual, foundUnequal, eqNumberOld, eqNumberNew, neqNumberOld, neqNumberNew)
                
            if caseFluct == 1 or caseFluct == 3:
                guessedB.reverse()
                knownDigits.reverse()
                searchFront = not searchFront
                
            if caseFluct == 2 or caseFluct == 3:
                for gIdx in range(len(guessedB)):
                    newVal = guessedB[gIdx]
                    
                    if newVal == 0:
                        newVal = 1
                    elif newVal == 1:
                        newVal = 0
                        
                    guessedB[gIdx] = newVal
                
        else:            
            if searchFront:
                idx = 0 
                
                while idx < B - 1 and knownDigits[idx]:
                    idx += 1 
            else: 
                idx = B - 1
                
                while idx > 0 and knownDigits[idx]:
                    idx -= 1
            
            printfl(idx + 1)
            
            guessedB[idx] = int(input())
            queryNr += 1
            knownDigits[idx] = True
                            
            searchFront = not searchFront                
        
    printfl("".join([str(digit) for digit in guessedB]))
    
    assert(all(knownDigits))
    
    judgement = input()
    
    
    if judgement == 'N':
        break