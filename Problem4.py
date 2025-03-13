import numpy as np
from scipy.optimize import linprog
import sympy as sym
x = sym.Symbol('x')
# primary function
c = [19.0, 12.0, 34.0]

# constraints matrix
A_ub = [
    [1.0, 0.0, 0.0],
    [0.0, 1.0, 0.0],
    [0.0, 0.0, 1.0],
    [-1.0, -1.0, -1.0]
    ]
# constants equal to constraints
b_ub = [5, 20, 15, -18]



x_bounds = [(0, None), (0, None), (0, None)]

res = linprog(
    c=c,
    A_ub=A_ub,
    b_ub=b_ub,
    bounds=x_bounds,
    method='highs'
)

if res.success:
    # Since we minimized -y, the maximum of y is -res.fun:
    print("Solution found!")
    # print values for primary function that achieve maximum
    print(f"x1 = {res.x[0]:.2f}, x2 = {res.x[1]:.2f}, x3 = {res.x[2]:.2f}")
    # print found max
    print(f"Maximum value of y = {res.fun:.2f}")
    # print shadow prices for ineql constraints
    print(res.ineqlin)
    # print shadow prices for equality constraints
    print(res.eqlin)
else:
    print("No solution found.")
