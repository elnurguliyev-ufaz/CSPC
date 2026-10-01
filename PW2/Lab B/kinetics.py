import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# 1. Read kinetics.csv (time, concentration)
data = np.loadtxt("PW2/Lab B/kinetics.csv", delimiter=",", skiprows=1)
t = data[:, 0]
C_measured = data[:, 1]

# 2. Set C0 to the first value of concentration
C0 = C_measured[0]

# 3. Define total error function to minimize
def total_error(k):
    # k is passed as an array [k_val] in scipy minimize
    k_val = k[0]
    C_model = C0 * np.exp(-k_val * t)
    error = np.sum((C_measured - C_model)**2)
    return error

# 4. Minimise error with SLSQP, bounds=[(0, 5)], x0=[0.5]
result = minimize(total_error, x0=[0.5], method="SLSQP", bounds=[(0, 5)])
k_fitted = result.x[0]
print(f"Fitted rate constant k = {k_fitted:.4f}")

# 5. Plot the data with fitted curve and save as kinetics.png
t_smooth = np.linspace(t.min(), t.max(), 200)
C_smooth = C0 * np.exp(-k_fitted * t_smooth)

plt.figure(figsize=(8, 5))
plt.scatter(t, C_measured, color='red', label='Measured Data', zorder=5)
plt.plot(t_smooth, C_smooth, color='blue', label=f'Fitted Curve (k = {k_fitted:.4f})', linewidth=2)
plt.xlabel("Time")
plt.ylabel("Concentration C(t)")
plt.title("Reaction Kinetics Fitting")
plt.legend()
plt.grid(True)
plt.savefig("PW2/Lab B/kinetics.png")
plt.close()
print("Plot saved as kinetics.png")
