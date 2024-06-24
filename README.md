# Numerically solved ordinary differential equations

## 1. First order ODE's (see 01_ode_linear.py)

The example ODE model air friction while falling. The ODE is the following:

$$\displaystyle \frac{dv}{dt} - \alpha v^2 + \beta = 0\\; \mathrm{with\\;initial\\; condition}\\; v(0) = 0$$

where $v$ is velocity, $t$ is time, and $\alpha,\\, \beta$ are constants.

First, we write the ODE in the following form:

$$\displaystyle \frac{dv}{dt} = f(t\\, v)$"$

In other words, "the derivative of $v$ equals a function that depends on the velocity $v$ and time $t$". For this case, we can write it as:

$$\displaystyle \frac{dv}{dt} = \alpha v^2 - \beta$$

ODE solution with the solvers "odeint" and "solve_ivp":

<figure>
    <img src="images/01_ode_linear.png" alt="ode_linear" width="400" height="auto"/>
    <figcaption>Figure 1. Velocity as a function of time considering air friction while falling.</figcaption>
</figure>


## 2. Coupled first order ODE's

The following are the two coupled fist-order linear differential equations. The are coupled because the two equations depend on each other,
with the terms $y_1,\\,y_2$.

$$y_1' = y_1 + y_2^2 + 3x,\\; y_1(0) = 0$$

$$y_2' = 3y_1 + y_2^3 - \cos(x),\\; y_2(0) = 0$$

The equation system can be rewritten as a vector. Letting $S = (y_1,\\; y_2$ we need to write a function that returns $dS/dx = dy_1/dx,\\; dy_2/dx$.
The function $dS/dx$ can take in $S = (y_1,\\; y_2$ and $x$. In vector form we then have:

$$
\vec{S} = \begin{bmatrix}
y_1 \\
y_2
\end{bmatrix} \Longrightarrow
\displaystyle \frac{d\vec{S}}{dx} = \vec{f}(x,\\;\vec{S}) = \vec{f}(x,\\;y_1,\\; y_2) = \begin{bmatrix}
y_1' \\
y_2'
\end{bmatrix} = \begin{bmatrix}
y_1 + y_2^2 + 3x \\
3y_1 + y_2^3 - \cos(x)
\end{bmatrix}
$$

Now, the vector function $d\vec{S}/dx$ can be programmed defining a function for "dSdx" as $\vec{f}(x,\\; \vec{S})$. See the file "02_coupled_ode.py".

<figure>
    <img src="images/02_coupled_linear_ode.png" alt="coupled_linear_linear" width="400" height="auto"/>
    <figcaption>Figure 2. y1 and y2 solutions for the coupled linear ODE's.</figcaption>
</figure>


## 3. Higher order ODE's
