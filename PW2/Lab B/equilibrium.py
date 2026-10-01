import numpy as np
from scipy.optimize import minimize

K = 50.0

def objective(x):
    val = (2 * x[0])**2 / ((1 - x[0]) * (1 - x[0])) - K
    return val**2

res = minimize(objective, x0=[0.5], method="SLSQP", bounds=[(0.01, 0.99)])
x_eq = res.x[0]
print(f"Equilibrium extent x = {x_eq:.4f}")

H2_eq = 1 - x_eq
I2_eq = 1 - x_eq
HI_eq = 2 * x_eq
print(f"Equilibrium amounts: [H2] = {H2_eq:.4f}, [I2] = {I2_eq:.4f}, [HI] = {HI_eq:.4f}")
