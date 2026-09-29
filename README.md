# CSPC Computer Science for Physics and Chemistry
My coursework repository. Each practical is under PW<n>/Lab <X>/.

## Setup
Create the environment for a given lab:
conda env create -f PW<n>/Lab\ <X>/environment.yml
conda activate cspc

## PW1
Lab A: Reproducible Foundations
**What I built:** Set up a reproducible Conda environment, structured the CSPC repository following course conventions, implemented radioactive decay simulation tests, and practiced Git version control with branching and merging.

**Speed comparison (loop vs NumPy):**
- loop: 1.718876 s
- numpy: 0.000206 s
- speed-up: 8331.8x faster

**Tests:** all passing? yes

**Conclusion:** 
The environment setup and simulation verification went smoothly. Writing the automated tests with pytest confirmed that the simulation correctly handles edge cases (like negative rates) and adheres to physical radioactive decay laws. The performance comparison dramatically highlights the efficiency of vectorized NumPy operations over pure-Python loops.
## PW2 Lab A - Motion from Tracking Data
- **Mean Acceleration**: -8.58 m/s^2 (close to the true free-fall acceleration -9.81 m/s^2)
- **Noise Observation**: The acceleration data is extremely noisy (standard deviation of 28.72) because differentiating twice (`np.gradient`) magnifies small measurement errors and noise from the position data.
- **Integration Result**: Integrating the noisy acceleration back up to velocity and position successfully suppresses the noise, recovering the original position within about 0.78 meters of the largest difference.

