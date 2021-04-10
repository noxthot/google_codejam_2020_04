# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 04:56:01 2020

@author: grego
"""

import numpy as np

inputFile = 'e5.in'
READ_FROM_FILE = True

if READ_FROM_FILE:
    f = open(inputFile)


def readNextLine():
    if READ_FROM_FILE:
        return f.readline()
    else:
        return input()


def createLatinSquare(N, K):
    outMat = None
    
    if N == 2:
        if K == 2:
            outMat = np.array([[1, 2], [2, 1]])
        elif K == 4:
            outMat = np.array([[2, 1], [1, 2]])
    elif N == 3:
        if K == 3:
            outMat = np.array([[1, 2, 3], [3, 1, 2], [2, 3, 1]])
        if K == 6:
            outMat = np.array([[2, 3, 1], [1, 2, 3], [3, 1, 2]])
        if K == 9:
            outMat = np.array([[3, 1, 2], [2, 3, 1], [1, 2, 3]])
        pass
    else:
        A = np.zeros((N, N), int)
        ktemp = K
        
        for i in range(N):
            A[i, i] = ktemp // (N - i)
            ktemp -= ktemp // (N - i)
            
        uni = [A[i, i] for i in range(N)]
        
        if 
            
        np.fill_diagonal(a, 5)
    
    return outMat
        

# Read input
T = int(readNextLine()) # nr Testcases

Ns = [None] * T # dimension of squares
Ks = [None] * T

for i in range(T):
    Ns[i], Ks[i] = [int(s) for s in readNextLine().split(" ")]    

# Solve problem and output
for i in range(T):
    outMat = createLatinSquare(Ns[i], Ks[i])
    
    s = "POSSIBLE" if outMat is not None else "IMPOSSIBLE"
    
    print("Case #{}: {}".format(i + 1, s))
    
    if outMat is not None:
        for j in range(outMat.shape[0]):
            print(" ".join([str(x) for x in outMat[j,:]]))


if READ_FROM_FILE:
    f.close()