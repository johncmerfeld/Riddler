#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 22:33:37 2018

@author: johncmerfeld
"""

import numpy as np
import sys

# get number of trials
n_trials = int(sys.argv[1])

LEN = 100
        
def theres_a_square(grid, x, y):
    num = grid[x][y]
    for i in range(4):
        for j in range(4):
            if x + i >= LEN:
                return False
            elif y + j >= LEN:
                return False
            elif arr[x + i][y + j] != num:
                return False
    return True

def check_rug(grid):
    for i in range(LEN):
        for j in range(LEN):
            if theres_a_square(arr, i, j):
                return False
    return True

ILLEGAL_RUGS = 0
LEGAL_RUGS = 0

for n in range(n_trials):
    #print(n)
    arr = np.zeros((LEN, LEN), dtype = int)
    for i in range(LEN):
        for j in range(LEN):
            rand = np.random.random_sample() * 3
            if rand <= 1:
                arr[i][j] = 1
            elif rand <= 2:
                arr[i][j] = 3
            else:
                rand = 3
    if check_rug(arr):
        LEGAL_RUGS += 1
    else: 
        ILLEGAL_RUGS += 1
        
print("TRIALS: " + str(n_trials) + "; LEGAL RUGS: " + str(LEGAL_RUGS) + "; ILLEGAL RUGS: " + str(ILLEGAL_RUGS))
    
            