import numpy as np
from scipy.optimize import linprog
import sympy as sym
x = sym.Symbol('x')
# primary function
c = [0.3, 0.9]
# constraints
A_ub = [
    [0.21, -0.35],
    [-0.03, 0.01],
    [-1.0, -1.0]
    ]
# constants
b_ub = [0, 0, -800]



x_bounds = [(0, None), (0, None)]

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
    print(f"x1 = {res.x[0]:.2f}, x2 = {res.x[1]:.2f}")
    print(f"Maximum value of y = {-res.fun:.2f}")
    # find shadow prices ineq constraints
    print(res.ineqlin)
    # find shadow prices eq constraints
    print(res.eqlin)
else:
    print("No solution found.")
