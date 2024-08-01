import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import matplotlib.animation as animation

# Defining the system parameters
m1 = 1.0
m2 = 1.0
L_1 = 2.0
L_2 = 1.0
g = 9.81

# Modelling the system
def double_pendulum(y, t):
    theta_1, theta_2, omega_1, omega_2 = y

    d_theta_1 = omega_1
    d_theta_2 = omega_2
    d_omega_1 = ((-g)*(2*m1+m2)*(np.sin(theta_1)) - m2 * g * np.sin(theta_1 - 2*theta_2) - 2*np.sin(theta_1-theta_2) * m2 * (omega_2**2 * L_2 + omega_1**2 * L_1 * np.cos(theta_1 - theta_2))) / (L_1 * (2*m1 + m2 - m2 * np.cos(2*theta_1 - 2*theta_2)))
    d_omega_2 = (2 * np.sin(theta_1 - theta_2) * (omega_1**2 * L_1 * (m1 + m2) + g * (m1 + m2) * np.cos(theta_1) + omega_2**2 * L_2 * m2 * np.cos(theta_1 - theta_2))) / (L_2 * (2*m1 + m2 - m2 * np.cos(2*theta_1 - 2*theta_2)))

    return [d_theta_1, d_theta_2, d_omega_1, d_omega_2]

# Defining the set of initial conditions parameter
theta_1_0 = 1
theta_2_0 = 1
omega_1_0 = 0.0
omega_2_0 = 0.0
y0 = [theta_1_0, theta_2_0, omega_1_0, omega_2_0]

# Defining the time array for the simulation
t = np.linspace(0, 10, 100)

# Solving the differential equations
y = odeint(double_pendulum, y0, t)

# Extracting the angles out of the solution set
theta_1 = y[:, 0]
theta_2 = y[:, 1]

# Plotting the angles
plt.plot(t, y[:, 0], label='theta_1')
plt.plot(t, y[:, 1], label='theta_2')
plt.xlabel('Time (s)')
plt.ylabel('Angle (rad)')
plt.title('Double Pendulum')
plt.legend()
plt.show()  # This will show the plot of the angles of the double pendulum

# Converting to cartesian coordinates for animation
x1 = L_1 * np.sin(theta_1)
y1 = -L_1 * np.cos(theta_1)
x2 = x1 + L_2 * np.sin(theta_2)
y2 = y1 - L_2 * np.cos(theta_2)

# Create figure and axes
fig, ax = plt.subplots()

# Create line objects for pendulum's rod and bob mass
line, = ax.plot([], [], 'o-', lw=2)

# Set limits for the axes
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)

# Defining an initialization function for animation
def init():
    line.set_data([], [])
    return line,

# The comma after return line is there 
# because the FuncAnimation expects the update function to 
# return an iterable of artists that will be redrawn for each frame of the animation. 

# Update function for animation
def update(n):
    line.set_data([0, x1[n], x2[n]], [0, y1[n], y2[n]])
    return line,

# Create animation using the matplotlib FuncAnimation function
ani = animation.FuncAnimation(fig, update, frames=len(t), init_func=init, blit=True, interval =65)

# Display the animation
plt.show()

