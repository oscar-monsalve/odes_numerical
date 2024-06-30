# Coupled first order ODE's

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import scienceplots

plt.style.use(["science", "notebook", "grid"])


def dSdx(x: list, S: list) -> list:
    y1, y2 = S  # Extract the S vector components
    return [y1 + y2**2 + 3*x,
            3*y1 + y2**3 - np.cos(x)]


# Define the initial conditions
y1_0 = 0
y2_0 = 0
S_0 = (y1_0, y2_0)  # Group the initial condition in S

# Solve the coupled ODEs
x = np.linspace(0, 1, 100)
sol = odeint(dSdx, y0=S_0, t=x, tfirst=True)

# print(sol)

# Get the y1 and y2 solutions
y1_sol = sol.T[0]
y2_sol = sol.T[1]

# Plot y1 and y2
plt.plot(x, y1_sol, label="y1")
plt.plot(x, y2_sol, label="y2")
plt.title("Coupled linear ODE's solutions")
plt.ylabel(r"$y_{1,\;2}(x)$")
plt.xlabel(r"$x$")
plt.legend()
plt.show()
