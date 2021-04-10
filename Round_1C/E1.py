# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 04:56:01 2020

@author: grego
"""

import numpy as np

inputFile = 'e1.in'
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
    
    
def findShortestTour(startX, startY, tour):
    time = 0
    currPos = [startX, startY]
    
    for step in tour:
        time += 1
        
        if step == 'S':
            currPos[1] -= 1
        elif step == 'N':
            currPos[1] += 1
        elif step == 'W':
            currPos[0] -= 1
        elif step == 'E':
            currPos[0] += 1
            
        tourLength = findTour(currPos, time)
        
        if tourLength >= 0:
            return tourLength
        
    return "IMPOSSIBLE"
        

# Read input
T = int(readNextLine()) # nr Testcases

Xs = [None] * T
Ys = [None] * T
Ms = [None] * T

for i in range(T):
    Xs[i], Ys[i], Ms[i] = readNextLine().split(" ")
    Xs[i] = int(Xs[i])
    Ys[i] = int(Ys[i])
    

# Solve problem and output
for i in range(T):
    tourLength = findShortestTour(Xs[i], Ys[i], Ms[i])
    print("Case #{}: {}".format(i + 1, tourLength))


if READ_FROM_FILE:
    f.close()