# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 04:56:01 2020

@author: grego
"""

import numpy as np
import scipy.linalg as sl

inputFile = 'e2.in'
READ_FROM_FILE = True
DEBUG = False

if READ_FROM_FILE:
    f = open(inputFile)

def readNextLine():
    if READ_FROM_FILE:
        return f.readline().rstrip()
    else:
        return input()


def findPath(N):
    cntBit = 0
    Ntemp = N
    
    while Ntemp > 0:
        cntBit += 1
        Ntemp //= 2
        
    pascal = sl.pascal(cntBit).astype(int)
    DEBUG and print(pascal)
    
    tempVal = 0
    
    path = []
    
    for idx in range(cntBit):        
        if tempVal + pascal[cntBit - 1 - idx, idx] > N - (cntBit - 1):
            break
        else:
            path.append((cntBit - 1 - idx, idx))
            tempVal += pascal[cntBit - 1 - idx, idx]
            
    path.reverse()
    DEBUG and print("Init ", path)
    
    tempVal = N - tempVal
    
    cntBit -= 1
    
    startfromleft = True
    
    while cntBit > 0:
        DEBUG and print("Check ", 2 ** (cntBit - 1) + (cntBit - 1), tempVal)
        
        if 2 ** (cntBit - 1) + (cntBit - 1) <= tempVal:
            tempPath = []
            tempVal -= 2 ** (cntBit - 1)
            
            for idx in range(cntBit):
                tempPath.append((cntBit - 1 - idx, idx))
                
                if not startfromleft:
                    tempPath.reverse()
                    
                startfromleft = not startfromleft
                
            path.extend(tempPath)
            DEBUG and print("Adding ", tempPath)
        else:
            if startfromleft:
                path.append((cntBit - 1, 0))
            else:
                path.append((0, cntBit - 1))
                
            DEBUG and print("Added ", path[-1])
                
            tempVal -= 1
            
        cntBit -= 1
        
    controlVal = 0
    
    for p in path:
        controlVal += pascal[p[0], p[1]]
        #print(pascal[p[0], p[1]])
        
    print(int(controlVal), N)
    
    return path
        

# Read input
T = int(readNextLine()) # nr Testcases

Ns = [None] * T

for i in range(T):
    Ns[i] = int(readNextLine())
    

# Solve problem and output
for i in range(T):
    path = findPath(Ns[i])
    #print(path)
    #print("Case #{}: {}".format(i + 1, s))


if READ_FROM_FILE:
    f.close()