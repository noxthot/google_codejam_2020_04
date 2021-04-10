# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 04:56:01 2020

@author: grego
"""

import numpy as np

inputFile = 'e3.in'
READ_FROM_FILE = True

if READ_FROM_FILE:
    f = open(inputFile)

def readNextLine():
    if READ_FROM_FILE:
        return f.readline()
    else:
        return input()


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
        

# Read input
T = int(readNextLine()) # nr Testcases

Ns = [None] * T
Ss = [None] * T
Es = [None] * T

for i in range(T):
    Ns[i] = int(readNextLine())
    
    Ss[i] = np.empty((Ns[i]), int)
    Es[i] = np.empty(( Ns[i]), int)
        
    for j in range(Ns[i]):
        Ss[i][j], Es[i][j] = [int(s) for s in readNextLine().split(" ")]

# Solve problem and output
for i in range(T):
    schedule = genSchedule(Ss[i], Es[i], Ns[i])
    print("Case #{}: {}".format(i + 1, schedule))


if READ_FROM_FILE:
    f.close()