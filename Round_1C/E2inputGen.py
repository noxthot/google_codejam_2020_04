# -*- coding: utf-8 -*-
"""
Created on Sat May  2 12:02:17 2020

@author: grego
"""

import numpy as np

digitString = 'ABCDEFGHIJ'

T = 1000
U = 2

with open('E2sim.in', 'w') as f:
    f.write(str(T) + "\n")
    
    for _ in range(T):
        f.write(str(U) + "\n")
        
        for _ in range(10000):
            M = np.random.randint(10**U)
            
            Rnumb = np.random.randint(M + 1)
            
            R = [digitString[int(s)] for s in str(Rnumb)]
            
            f.write("-1 " + "".join(R) + "\n")