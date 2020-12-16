
import numpy as np
import scipy as sp

c = [9,-1]
A = [[6,1,1], [-1,0,-1]]
b = [0,1,-6]
x0_bounds = (0, None)
x1_bounds = (0, None)

from scipy.optimize import linprog
# Solve the problem by Simplex method in Optimization
res = linprog(c, A_ub=A, b_ub=b)
print(res)


input()

