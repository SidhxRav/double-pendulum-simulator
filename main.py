import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots(figsize=(6,6))
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_aspect('equal')
line, = ax.plot([], [], 'o-', lw=2)

gravity = input("What planet?")
gravties = {
    "Earth" : 9.8
}
g = gravties[gravity]
m1 = int(input("Mass1 in kg?"))
m2 = int(input("Mass2 in kg?"))
r1 = int(input("Rope1 length in m?"))
r2 = int(input("Rope2 length in m?"))
theta1 = (int(input("Starting angle1 in degrees?")))*(np.pi/180)
theta2 = (int(input("Starting angle2 in degrees?")))*(np.pi/180)
thetadot1 = 0
thetadot2 = 0
dt = 0.001

def update(frame):
    global theta1, theta2, thetadot1, thetadot2

    x1 = r1*np.sin(theta1)
    y1 = -r1*np.cos(theta1)
    x2 = r2* np.sin(theta2) + r1*np.sin(theta1)
    y2 = -r2*np.cos(theta2) - r1*np.cos(theta1)

    a = -(m1 +m2)*g*r1*np.sin(theta1) - m2*r1*r2*(thetadot2**2)*np.sin(theta1-theta2)
    b = (m1+m2)* (r1**2)
    c = m2*r1*r2*np.cos(theta1-theta2)
    e = -m2*g*r2*np.sin(theta2) + m2*r1*r2*(thetadot1**2)*np.sin(theta1-theta2)
    f = m2*(r2**2)
    h = m2*r1*r2*np.cos(theta1-theta2)

    thetaddot2 = (e-((a*h)/b))/(f-((c*h)/b))

    thetaddot1 = (a/b) - ((c/b)*thetaddot2)
    
    thetadot2 += thetaddot2*dt
    thetadot1 += thetaddot1*dt

    theta2 += thetadot2*dt
    theta1 += thetadot1*dt

    line.set_data([0, x1, x2], [0, y1, y2])
    return line,