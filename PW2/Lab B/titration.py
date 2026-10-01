import numpy as np
import matplotlib.pyplot as plt

# 1. Read titration.csv (volume, pH)
data = np.loadtxt("PW2/Lab B/titration.csv", delimiter=",", skiprows=1)
V = data[:, 0]
pH = data[:, 1]

# 2. Find equivalence point using numerical derivative (dpH/dV max)
dpH = np.gradient(pH)
dV = np.gradient(V)
derivative = dpH / dV

max_idx = np.argmax(derivative)
V_eq = V[max_idx]
print(f"Equivalence point Volume V_eq = {V_eq:.2f}")

# 3. Plot the titration curve and save as titration.png
plt.figure(figsize=(8, 5))
plt.plot(V, pH, label='Titration Curve', color='purple', linewidth=2)
plt.axvline(V_eq, color='red', linestyle='--', label=f'Equivalence Point (V = {V_eq:.2f})')
plt.xlabel("Volume")
plt.ylabel("pH")
plt.title("Titration Curve Analysis")
plt.legend()
plt.grid(True)
plt.savefig("PW2/Lab B/titration.png")
plt.close()
print("Plot saved as titration.png")
