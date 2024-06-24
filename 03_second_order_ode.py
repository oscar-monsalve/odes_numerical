# Second order ODE's

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


def dSdx(x: list, S: list) -> list:
    x, v = S
    return [v,
            -v**2 + np.sin(x)]


# Define the initial conditions and the solution range for the time t
x_0 = 0
v_0 = 5
t = np.linspace(0, 1, 100)

# Group the initial condtion into S_0
S_0 = (x_0, v_0)

# Solve the system
sol = odeint(dSdx, y0=S_0, t=t, tfirst=True)

# Extract the solutions for x and v
x_sol = sol.T[0]
v_sol = sol.T[1]

# Plot the solutions for x and v
plt.plot(t, x_sol, label="x")
plt.plot(t, v_sol, label="v")
plt.title("Second order linear ODE's solutions")
plt.ylabel(r"$x,\; v$")
plt.xlabel(r"$t,\; (s)$")
plt.legend()
plt.show()
