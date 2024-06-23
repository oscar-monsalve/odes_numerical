# First order ODE's: air friction while falling

import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from scipy.integrate import odeint
from scipy.integrate import solve_ivp


# Define the right side of the ODE when is written is the form "dv/dt = ax^2 + b"
def dvdt(t: float, v: float, beta: float) -> float:
    return 3*v**2 - beta


# Define the time range, the initial conditions, and the constant values

t = np.linspace(0, 1, 100)  # time range
v0 = 0  # Velocity initial condition -> At t = 0, the Velocity is 0
beta = 5

# Solve the ODE. The are two main solvers in scipy
# - odeint: Uses a particular solver called Isoda from the FORTRAN library odepack.
# - solve_ivp: More customizable, can choose from a list of possible solvers.

sol_m1 = odeint()

