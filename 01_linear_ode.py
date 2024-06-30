# First order ODE's: air friction while falling

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from scipy.integrate import solve_ivp
import scienceplots

plt.style.use(["science", "notebook", "grid"])


# Define the right side of the ODE when is written is the form "dv/dt = ax^2 + b"
def dvdt(t: float, v: float) -> float:
    beta = 5  # constant
    return 3*v**2 - beta


# Define the time range and the initial conditions

t = np.linspace(0, 1, 100)  # time range
v0 = 0  # Velocity initial condition -> At t = 0, v = 0

# Solve the ODE. The are two main solvers in scipy
# - odeint: Uses a particular solver called Isoda from the FORTRAN library odepack.
# - solve_ivp: More customizable, can choose from a list of possible solvers.

sol_m1 = odeint(dvdt, y0=v0, t=t, tfirst=True)
sol_m2 = solve_ivp(dvdt, t_span=(0, max(t)), y0=[v0], t_eval=t)

v_sol_m1 = sol_m1.T[0]
v_sol_m2 = sol_m2.y[0]

# print(sol_m1.T[0])
# print(sol_m2.y[0])

# Plot the solution
plt.scatter(t, v_sol_m1, s=7, c="r", label="odeint")
plt.plot(t, v_sol_m2, '--', label="solve_ivp")
plt.title("ODE solver comparison")
plt.ylabel(r"$v(t)\; (m/s)$")
plt.xlabel(r"$t\; (s)$")
plt.legend()
plt.show()
