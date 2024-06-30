# Numerically solved ordinary differential equations

## 1. First order ODE's

The example ODE model air friction while falling. The ODE is the following:

$$\displaystyle \frac{dv}{dt} - \alpha v^2 + \beta = 0\\; \mathrm{with\\;initial\\; condition}\\; v(0) = 0$$

where $v$ is velocity, $t$ is time, and $\alpha,\\, \beta$ are constants.

First, we write the ODE in the following form:

$$\displaystyle \frac{dv}{dt} = f(t\\, v)$$

In other words, "the derivative of $v$ equals a function that depends on the velocity $v$ and time $t$". For this case, we can write it as:

$$\displaystyle \frac{dv}{dt} = \alpha v^2 - \beta$$

see the file "01_ode_linear.py". The ODE solution with the solvers "odeint" and "solve_ivp":

<figure>
    <img src="images/01_ode_linear.png" alt="ode_linear" width="400" height="auto"/>
    <figcaption>Figure 1. Velocity as a function of time considering air friction while falling.</figcaption>
</figure>


## 2. Coupled first order ODE's

The following are the two coupled fist-order linear differential equations. The are coupled because the two equations depend on each other,
with the terms $y_1,\\,y_2$.

$$y_1' = y_1 + y_2^2 + 3x,\\; y_1(0) = 0$$

$$y_2' = 3y_1 + y_2^3 - \cos(x),\\; y_2(0) = 0$$

The equation system can be rewritten as a vector. Letting $S = (y_1,\\; y_2)$ we need to write a function that returns $dS/dx = (dy_1/dx,\\; dy_2/dx)$.
The function $dS/dx$ can take in $S = y_1,\\; y_2$ and $x$. In vector form we then have:

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


## 3. Second order ODE's

**Python does not have functions to directly solve second or higher order ODE's**

**However, any second order ODE can be converted into two first order ODE's**

Consider the following second order ODE:

$$\ddot{x} = -\dot{x}^2 + \sin(x)$$

We can convert this into a system of two first order ODE's as follows:

- Take $x$, which is what we're trying to solve for. Then, define $\dot{x} = v$, so that $v$ becomes a new variable.
- Note that $\dot{x} = v$ is one differential equation.
- Since $\dot{v} = \ddot{x} = -\dot{x}^2 + \sin(x) = -v^2 + \sin(x)$, we get another differential equation.

Then, the system of two first order coupled ODE's is:

$$\dot{x} = v$$

$$\dot{v} = -v^2 + \sin(x)$$

For this system of ODE's, we are solving for $v$ and $x$. Additionally, it requires initial conditions of $x_0\\; \mathrm{and}\\; v_0$. For example,
$x(0) = 0$ and $v(0) = 5$.

See the file "03_second_order_ode.py" for the programming of this problem.

<figure>
    <img src="images/03_second_order_ode.png" alt="second_order_ode" width="400" height="auto"/>
    <figcaption>Figure 3. Solution of a second order ODE divided into two first oder ODE's.</figcaption>
</figure>


## 4. Two coupled third order ODE's

For this we have a two-coupled third-order ODE's system:

$$\dddot{x}_2 = -\ddot{x}_1^3 + \dot{x}_2 + x_1 + \sin(t)$$

$$\dddot{x}_1 = -2\ddot{x}_2^2 + x_2$$

Because each differential equation is of third order, there will be a system of **six** linear first order ODE's.
For this, we need to define the following:

1. $v_1 = \dot{x}_1$
2. $v_2 = \dot{x}_2$
3. $a_1 = \ddot{x}_1 = \dot{v}_1$
4. $a_2 = \ddot{x}_2 = \dot{v}_2$

These last ones make up for four differential equations. We need two more. For this, we note that $\dot{a}_1 = \dddot{x}_1$
and $\dot{a}_2 = \dddot{x}_2$, then we get:

5. $\dot{a}_2 = -a_1^3 + v_2 + x_1 + \sin(t)$
6. $\dot{a}_1 = -2v_2^2 + x_2$

Now, we have six coupled first order ODE's. We want to solve for $x_1,\\; v_1,\\; a_1$ and $x_2,\\; v_2,\\; a_2$.
Rewriting them in vector form we have the following:

$$
\vec{S} = \begin{bmatrix}
x_1 \\
v_1 \\
a_1 \\
x_2 \\
v_2 \\
a_2
\end{bmatrix} \Longrightarrow
\displaystyle \frac{d\vec{S}}{dt} = \begin{bmatrix}
\dot{x_1} \\
\dot{v_1} \\
\dot{a_1} \\
\dot{x_2} \\
\dot{v_2} \\
\dot{a_2}
\end{bmatrix} = \begin{bmatrix}
v_1 \\
a_1 \\
-2v_2^2 + x_2 \\
v_2 \\
a_2 \\
-a_1^3 + v_2 + x_1 + \sin(t)
\end{bmatrix}
$$

There will be needed six initial conditions. For this example, the initial conditions are:

$$x_1(0) = 0$$

$$v_1(0) = 0$$

$$a_1(0) = 0$$

$$x_2(0) = 0$$

$$v_2(0) = 0$$

$$a_2(0) = 0$$

See the file "04_third_order_coupled_ode.py" for the programming of this problem. The solutions are:

<figure>
    <img src="images/04_third_order_coupled_odes.png" alt="04_third_order_coupled_odes" width="400" height="auto"/>
    <figcaption>Figure 4. Solution for the two coupled third order linear ODE's.</figcaption>
</figure>


# Damped pendulum (No drive force)

The motion of a damped pendulum is modeled by a second-order non-linear differential equation as follows:

$$\ddot{\theta} + C\dot{\theta} + \displaystyle \frac{g}{L}\sin(\theta) = 0$$

where $\theta$ is the pendulum angle, $C = k/mL$ is the damping coefficient, $k$ the friction coefficient, $m$ the
pendulum mass, $g$ the gravitational constant, and $L$ the distance from the pivoting point to the mass center.

We want to rewrite the ODE using the state-space representation to create a two-coupled first-order equation system:

- $x_1 = \theta$
- $x_2 = \dot{\theta}$

Then, the two coupled ODE's are:

$$\dot{x}_1 = x_2$$

$$\dot{x}_2 = -C\dot{x}_2 - k\sin{x_1}$$

where,

$C = \displaystyle \frac{k}{mL}$.

$k = \displaystyle \frac{g}{L}$
