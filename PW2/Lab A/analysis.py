"""
PW2 Lab A -- Motion from tracking data.

Read noisy free-fall position measurements, then:
  - differentiate once  -> velocity
  - differentiate twice -> acceleration (should be ~ constant -g, but noisy!)
  - integrate the acceleration back up -> recover velocity and position

Complete the TODOs. Run:  python analysis.py
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumulative_trapezoid

# TODO 1: read freefall.csv into arrays t and y
data = np.loadtxt("PW2/Lab A/freefall.csv", delimiter=",", skiprows=1)
t = data[:, 0]
y = data[:, 1]

# TODO 2: compute velocity v = derivative of y w.r.t. t   (np.gradient)
#         and acceleration a = derivative of v w.r.t. t    (np.gradient again)
#         Print the mean acceleration and its standard deviation.
v = np.gradient(y, t)
a = np.gradient(v, t)

mean_a = np.mean(a)
std_a = np.std(a)
print(f"Mean acceleration: {mean_a:.2f}")
print(f"Acceleration std deviation: {std_a:.2f}")

# TODO 3: integrate a back up to recover velocity and position
v_recovered = cumulative_trapezoid(a, t, initial=0) + v[0]
y_recovered = cumulative_trapezoid(v_recovered, t, initial=0) + y[0]

max_diff = np.max(np.abs(y - y_recovered))
print(f"Largest position difference: {max_diff:.2f} meters")

# TODO 4: make a figure with 3 stacked panels: position, velocity, acceleration
fig, axes = plt.subplots(3, 1, figsize=(8, 10), sharex=True)

axes[0].plot(t, y, label="Original Position", color="blue")
axes[0].set_ylabel("Position (m)")
axes[0].legend()
axes[0].grid(True)

axes[1].plot(t, v, label="Velocity", color="orange")
axes[1].set_ylabel("Velocity (m/s)")
axes[1].legend()
axes[1].grid(True)

axes[2].plot(t, a, label="Acceleration", color="green", alpha=0.6)
axes[2].axhline(-9.81, color="red", linestyle="--", label="True -9.81")
axes[2].set_ylabel("Acceleration (m/s^2)")
axes[2].set_xlabel("Time (s)")
axes[2].legend()
axes[2].grid(True)

plt.tight_layout()
plt.savefig("PW2/Lab A/motion.png")
print("Figure saved as motion.png successfully!")
