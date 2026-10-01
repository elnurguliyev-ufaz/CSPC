import numpy as np
from scipy.optimize import newton, minimize

# Part 2A: Easy convex function f(x) = (x - 3)**2 + 1
def f(x):
    return (x - 3)**2 + 1

def f_prime(x):
    return 2 * (x - 3)

print("--- Part 2A: Easy Function ---")
x = 0.0
lr = 0.1
for _ in range(100):
    x = x - lr * f_prime(x)
print(f"Gradient Descent result: x = {x:.4f}")

x_newton = newton(f_prime, x0=0.0)
print(f"Newton's method result: x = {x_newton:.4f}")

res = minimize(f, x0=0.0, method="SLSQP")
print(f"SLSQP result: x = {res.x[0]:.4f}")


# Part 2B: Harder landscape g(x) = x**4 - 3*x**2 + x + 5
def g(x):
    return x**4 - 3*x**2 + x + 5

def g_prime(x):
    return 4*x**3 - 6*x + 1

def g_double_prime(x):
    return 12*x**2 - 6

print("\n--- Part 2B: Harder Landscape ---")
for x0 in [0.0, 2.0]:
    print(f"\nStarting from x0 = {x0}:")
    
    # 1. Gradient descent
    x = x0
    lr = 0.05
    for _ in range(1000):
        x = x - lr * g_prime(x)
    print(f"  Gradient Descent: x = {x:.4f}, g(x) = {g(x):.4f}")
    
    # 2. Newton's method on g_prime(x) = 0
    try:
        x_n = newton(g_prime, x0=x0)
        g2 = g_double_prime(x_n)
        status = "Minimum (g'' > 0)" if g2 > 0 else "Maximum/Saddle (g'' < 0)"
        print(f"  Newton's method:  x = {x_n:.4f}, g''(x) = {g2:.2f} -> {status}")
    except Exception as e:
        print(f"  Newton's method:  Failed to converge ({e})")
        
    # 3. SLSQP minimize
    res_g = minimize(g, x0=x0, method="SLSQP")
    print(f"  SLSQP minimize:   x = {res_g.x[0]:.4f}, g(x) = {res_g.fun:.4f}")
