# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 04:56:01 2020

@author: grego
"""

import numpy as np
import math as m

inputFile = 'e1.in'
READ_FROM_FILE = True

if READ_FROM_FILE:
    f = open(inputFile)

def readNextLine():
    if READ_FROM_FILE:
        return f.readline().rstrip()
    else:
        return input()


def findSol(X, Y):
    def decToBinRev(n):
        binaryList = []
        tempVal = n
    
        while tempVal >= 1:
            binaryList.append(str(tempVal % 2))
            tempVal //= 2
                    
        return binaryList
    
    
    def findPathToLargerDir(valToReach, templLowerDir):
        currPos = 0
        pathToLowerDir = []
        
        for idx, val in enumerate(templLowerDir):
            coeff = 2**(len(templLowerDir) - idx - 1) if val == '1' else 0
            
            if coeff == 0:
                pathToLowerDir.append('0')
            elif currPos < valToReach:
                currPos += coeff
                pathToLowerDir.append('1')
            else:
                currPos -= coeff
                pathToLowerDir.append('-1')
                
        if currPos != valToReach:
            return "ERROR"
        else:
            return pathToLowerDir
            
    
    Xsign = np.sign(X)
    Ysign = np.sign(Y)
    
    X = abs(X)
    Y = abs(Y)
    
    moveToSmallerDir = min(X, Y)
    
    moveXfirst = (X < Y)
    
    pathSmallerDir = decToBinRev(moveToSmallerDir)
    
    templateLargerDir = ['0' if val == '1' else '1' for val in pathSmallerDir]
    
    while 2 ** (len(templateLargerDir)) < max(X, Y):
        templateLargerDir.append('1')        
        
    templateLargerDir.reverse()
    
    pathLargerDir = findPathToLargerDir(max(X, Y), templateLargerDir)
    
    if pathLargerDir == "ERROR":
        newTemplateLargerDir = ['1']
        newTemplateLargerDir.extend(templateLargerDir)
        pathLargerDir = findPathToLargerDir(max(X, Y), newTemplateLargerDir)
    
    if pathLargerDir == "ERROR":
        newnewTemplateLargerDir = ['1']
        newnewTemplateLargerDir.extend(newTemplateLargerDir)
        pathLargerDir = findPathToLargerDir(max(X, Y), newnewTemplateLargerDir)
    
    if pathLargerDir == "ERROR":
        return "IMPOSSIBLE"
    else:
        # valid solution, but we have to decode now
        pathLargerDir.reverse()
        newWay = ''
        
        dictDirections = dict()
        
        if moveXfirst:        
            dictDirections['0'] = 'E' if Xsign > 0 else 'W'
            dictDirections['1'] = 'N' if Ysign > 0 else 'S'
            dictDirections['-1'] = 'S' if Ysign > 0 else 'N'
        else:
            dictDirections['0'] = 'N' if Ysign > 0 else 'S'
            dictDirections['1'] = 'E' if Xsign > 0 else 'W'
            dictDirections['-1'] = 'W' if Xsign > 0 else 'E'
        
        return "".join([dictDirections[s] for s in pathLargerDir])
        

# Read input
T = int(readNextLine()) # nr Testcases

Xs = [None] * T
Ys = [None] * T

for i in range(T):
    Xs[i], Ys[i] = [int(s) for s in readNextLine().split(" ")]
    

# Solve problem and output
for i in range(T):
    s = findSol(Xs[i], Ys[i])
    print("Case #{}: {}".format(i + 1, s))


if READ_FROM_FILE:
    f.close()