# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 04:56:01 2020

@author: grego
"""

import numpy as np

inputFile = 'e2.in'
READ_FROM_FILE = True

if READ_FROM_FILE:
    f = open(inputFile)

def readNextLine():
    if READ_FROM_FILE:
        return f.readline().rstrip()
    else:
        return input()


def findTour(pos, time):
    dist = abs(pos[0]) + abs(pos[1])
    
    #print(dist)
    if dist <= time:
        return time
    else:
        return -1
    
    
def findDigitString(U, Q, R):
    firstLetters = set()
    #firstTwoLetters = []
    evalLetters = []
    allLetters = set()
    
    for s in R:
        #firstTwoLetters.append(ord(s[0]))
        allLetters.add(s[-1])   
        evalLetters.append(ord(s[0]))
        
        if len(s) > 1:
            firstLetters.add(s[0])
        
        #if len(s) > 1:
        #    firstTwoLetters.append(ord(s[1]))
    
    uniqueLetters, counter = np.unique(evalLetters, return_counts=True)
    
    sortedLetters = uniqueLetters[np.flip(np.argsort(counter))]
    
    digitString = [chr(s) for s in sortedLetters]
    
    zeroLetter = (allLetters - firstLetters).pop()
    
    if zeroLetter in digitString:
        digitString.remove(zeroLetter)
    
    return zeroLetter + "".join(digitString)

    #return digitString[-1] + "".join(digitString[:9])
    
    #for s in digitString:
    #    allLetters.remove(s)
    #    
    #zeroLetter = allLetters.pop()
    #
    #return zeroLetter + "".join(digitString)
    
        

# Read input
T = int(readNextLine()) # nr Testcases

Us = [None] * T
Qs = [[None] * 10000] * T
Rs = [[None] * 10000] * T

for i in range(T):
    Us[i] = int(readNextLine())
    
    for idx in range(10000):
        q, r = [s for s in readNextLine().split(" ")]
        Qs[i][idx] = int(q)
        Rs[i][idx] = r
    

# Solve problem and output
for i in range(T):
    s = findDigitString(Us[i], Qs[i], Rs[i])
    print("Case #{}: {}".format(i + 1, s))


if READ_FROM_FILE:
    f.close()