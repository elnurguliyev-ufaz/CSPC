import time
from decay import simulate, simulate_loop

N0 = 200000
lam = 0.4
dt = 0.05
steps = 50

# Time the pure-Python loop version
start_time = time.perf_counter()
simulate_loop(N0, lam, dt=dt, steps=steps)
loop_time = time.perf_counter() - start_time

# Time the NumPy vectorized version
start_time = time.perf_counter()
simulate(N0, lam, dt=dt, steps=steps)
numpy_time = time.perf_counter() - start_time

speedup = loop_time / numpy_time

print(f"Loop version time: {loop_time:.6f} s")
print(f"NumPy version time: {numpy_time:.6f} s")
print(f"Speed-up: {speedup:.1f}x faster")
