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
