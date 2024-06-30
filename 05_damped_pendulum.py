# Damped pendulum (No drive force)

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import scienceplots

plt.style.use(["science", "notebook", "grid"])


def dSdt(t, S):
    x1, x2 = S
    k = 0.2  # friction coefficient
    m = 0.5  # mass (kg)
    L = 0.2  # pendulum radius (m)
    g = 9.81  # gravitational constant (m^2/s)
    C1 = k / (m*L)
    C2 = g / L
    return [x2,
            -C1*x2 - C2*np.sin(x1)]


# Define the initial conditions
x1_0 = np.pi / 4  # pendulum angular position
x2_0 = 0  # pendulum angular velocity
S_0 = (x1_0, x2_0)

# Define the time range
t = np.linspace(0, 6, 1000)

# Solve the coupled ODE's
sol = odeint(dSdt, y0=S_0, t=t, tfirst=True)

# Extract the solutions for x1 and x2
x1_sol = sol.T[0]
x2_sol = sol.T[1]

# Plot x1 and x2
plt.plot(t, x1_sol, label=r"Angular position $\theta(t)$")
plt.plot(t, x2_sol, label=r"Angular velocity $\omega(t)$")
plt.title("Damped pendulum")
plt.ylabel(r"$\theta(t),\; \omega(t)$")
plt.xlabel(r"$t\; (s)$")
plt.legend()
plt.show()
