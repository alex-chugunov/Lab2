# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 05:36:34 2020

@author: ПК
"""

import numpy as np
import scipy as sp

c = [4,1,9]
A = [[-1,-3,-1], [-2,1,-3], [-1,1,-5],[-6,-1,0],[-1,0,0]]
b = [-6,-1,1,1,0]
x0_bounds = (0, None)
x1_bounds = (0, None)

from scipy.optimize import linprog
# Solve the problem by Simplex method in Optimization
res = linprog(c, A_ub=A, b_ub=b)
print(res)


input()