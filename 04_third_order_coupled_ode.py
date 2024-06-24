# two coupled third order linear ode's

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


def dSdt(t, S):
    x1, v1, a1, x2, v2, a2 = S
    return [v1,
            a1,
            -2*v2**2 + x2,
            v2,
            a2,
            -a1**3 + v2 + x1 + np.sin(t)]


# Define the six initial conditions
x1_0 = 0
v1_0 = 0
a1_0 = 0
x2_0 = 0
v2_0 = 0
a2_0 = 0

# Group all initial conditions into an S vector
S_0 = (x1_0, v1_0, a1_0, x2_0, v2_0, a2_0)

# Define the time range for the solution
t = np.linspace(0, 1, 100)

# Solve the ODE system
sol = odeint(dSdt, y0=S_0, t=t, tfirst=True)

# Extract the solutions
x1_sol = sol.T[0]
v1_sol = sol.T[1]
a1_sol = sol.T[2]
x2_sol = sol.T[3]
v2_sol = sol.T[4]
a2_sol = sol.T[5]

# Plot the solutions for x and v
plt.plot(t, x1_sol, label=r"$x_1$")
plt.plot(t, v1_sol, label=r"$v_1$")
plt.plot(t, a1_sol, label=r"$a_1$")
plt.plot(t, x2_sol, label=r"$x_2$")
plt.plot(t, v2_sol, label=r"$v_2$")
plt.plot(t, a2_sol, label=r"$a_2$")
plt.title("Solution for the two coupled third order linear ODE's")
plt.ylabel("ODE system solutions")
plt.xlabel(r"$t\; (s)$")
plt.legend()
plt.show()
