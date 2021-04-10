# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 04:56:01 2020

@author: grego
"""

import numpy as np

inputFile = 'e1.in'
READ_FROM_FILE = False

if READ_FROM_FILE:
    f = open(inputFile)

def readNextLine():
    if READ_FROM_FILE:
        return f.readline().rstrip()
    else:
        return input()


def findCommonString(N, Ps):
    commonString = []
    
    Is = [len(word) - 1 for word in Ps]
    
    idxToWorkWith = list(range(N))
    
    while len(idxToWorkWith) > 0:
        delIdxs = []
        letter = ''
        
        for wordIdx in idxToWorkWith:
            thisLetter = Ps[wordIdx][Is[wordIdx]]
            
            if thisLetter == "*":
                delIdxs.append(wordIdx)
            else:
                if letter == '':
                    letter = thisLetter
                elif letter != thisLetter:
                    return "*"
                
                Is[wordIdx] -= 1
                
                if Is[wordIdx] < 0:
                    delIdxs.append(wordIdx)
                
        commonString.append(letter)
                
        for delIdx in delIdxs:
            idxToWorkWith.remove(delIdx)
    
    commonString.reverse()
    
    return "".join(commonString)
        

# Read input
T = int(readNextLine()) # nr Testcases

Ns = [None] * T # dimension of squares
Pss = [None] * T # latin squares

for i in range(T):
    Ns[i] = int(readNextLine())
    
    Pss[i] = []
    
    for j in range(Ns[i]):
        Pss[i].append(readNextLine())
    

# Solve problem and output
for i in range(T):
    s = findCommonString(Ns[i], Pss[i])
    print("Case #{}: {}".format(i + 1, s))


if READ_FROM_FILE:
    f.close()