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
        return f.readline()
    else:
        return input()


def analyseMatrix(M, N):
    k = np.trace(M)
    r = 0
    c = 0
    
    for i in range(N):        
        if len(np.unique(M[:, i])) != N:
            c += 1
    
        if len(np.unique(M[i, :])) != N:
            r += 1
        
    return [k, r, c]
        

# Read input
T = int(readNextLine()) # nr Testcases

Ns = [None] * T # dimension of squares
Ms = [None] * T # latin squares

for i in range(T):
    Ns[i] = int(readNextLine())
    
    Ms[i] = np.empty((0, Ns[i]), int)
    
    for j in range(Ns[i]):
        Mrow = np.array([[int(s) for s in readNextLine().split(" ")]])
        Ms[i] = np.append(Ms[i], Mrow, axis=0)
    

# Solve problem and output
for i in range(T):
    k, r, c = analyseMatrix(Ms[i], Ns[i])
    print("Case #{}: {} {} {}".format(i + 1, k, r, c))


if READ_FROM_FILE:
    f.close()