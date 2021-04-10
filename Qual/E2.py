# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 04:56:01 2020

@author: grego
"""

import numpy as np

inputFile = 'e2.in'
READ_FROM_FILE = False


if READ_FROM_FILE:
    f = open(inputFile)
    

def readNextLine():
    if READ_FROM_FILE:
        return f.readline()
    else:
        return input()


def getParenthesesString(S):
    nrChars = len(S)
    
    currOpen = 0
    idx = 0
    Sprime = ""
    
    while idx < nrChars:
        currChar = int(S[idx])
        
        if currOpen > currChar:
            Sprime += ')'
            currOpen -= 1
        elif currOpen == currChar:
            Sprime += str(currChar)
            idx += 1
        else:
            Sprime += '('
            currOpen += 1
            
    for _ in range(currOpen):
        Sprime += ')'    
        
    return Sprime
        

# Read input
T = int(readNextLine()) # nr Testcases

Ss = [None] * T # strings

for i in range(T):
    Ss[i] = readNextLine().strip()
    
    
# Solve problem and output
for i in range(T):
    Sprime = getParenthesesString(Ss[i])
    print("Case #{}: {}".format(i + 1, Sprime))


if READ_FROM_FILE:
    f.close()