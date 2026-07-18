import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#initialise graph
fig, ax = plt.subplots(figsize=(6,6))
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_aspect('equal')
line, = ax.plot([], [], 'o-', lw=2)

#Set up inputs
gravity = input("What planet?")
gravties = {
    "Earth" : 9.8
}
g = gravties.get(gravity, 9.8)
m1 = int(input("Mass1 in kg?"))
m2 = int(input("Mass2 in kg?"))
r1 = int(input("Rope1 length in m?"))
r2 = int(input("Rope2 length in m?"))
theta1 = (int(input("Starting angle1 in degrees?")))*(np.pi/180)
theta2 = (int(input("Starting angle2 in degrees?")))*(np.pi/180)
#user chooses how fast animation plays
steps_per_frame = (int(input("Playback speed?"))) * 30
#This just means it starts at rest (no initial velocity)
thetadot1 = 0
thetadot2 = 0
dt = 0.001
#energy list to calculate percentage error
energies = []
# calculate energy function which i need to put up here cuz then i call it for the expected value
def Calculate_energy(g, m1, m2, r1, r2, theta1, theta2, thetadot1,thetadot2):
    # KE of mass 1
    ek1 = 0.5 * m1 * (r1 * thetadot1)**2

    # KE of mass 2 (has cross term because position depends on both angles)
    ek2 = 0.5 * m2 * ((r1 * thetadot1)**2 + (r2 * thetadot2)**2 + 2 * r1 * r2 * thetadot1 * thetadot2 * np.cos(theta1 - theta2))

    # PE of mass 1
    ep1 = m1 * g * r1 * np.cos(theta1)

    # PE of mass 2
    ep2 = m2 * g * (r1 * np.cos(theta1) + r2 * np.cos(theta2))

    total_energy = ek1 + ek2 - ep1 - ep2
    return total_energy
#expected value for error calc
expected_value = Calculate_energy(g,m1,m2,r1,r2,theta1,theta2,thetadot1,thetadot2)
def update(frame):
    global theta1, theta2, thetadot1, thetadot2

    #Calculate for the x and why values of the masses
    x1 = r1*np.sin(theta1)
    y1 = -r1*np.cos(theta1)
    x2 = r2* np.sin(theta2) + r1*np.sin(theta1)
    y2 = -r2*np.cos(theta2) - r1*np.cos(theta1)

    #Calculates every frame and then after this function is passed, only the nth frame will be played
    #This makes sure the calculation has less error (at dt is still kept high) and the speed is faster
    for i in range(steps_per_frame):
        #Set up the variables for solving theta double dots
        a = -(m1 +m2)*g*r1*np.sin(theta1) - m2*r1*r2*(thetadot2**2)*np.sin(theta1-theta2)
        b = (m1+m2)* (r1**2)
        c = m2*r1*r2*np.cos(theta1-theta2)
        e = -m2*g*r2*np.sin(theta2) + m2*r1*r2*(thetadot1**2)*np.sin(theta1-theta2)
        f = m2*(r2**2)
        h = m2*r1*r2*np.cos(theta1-theta2)

        #Set up theta double dots
        thetaddot2 = (e-((a*h)/b))/(f-((c*h)/b))

        thetaddot1 = (a/b) - ((c/b)*thetaddot2)
        
        #Use euler integration to find theta dots
        thetadot2 += thetaddot2*dt
        thetadot1 += thetaddot1*dt

        #Use euler integration again to find theta dots
        theta2 += thetadot2*dt
        theta1 += thetadot1*dt
    # Ensure that energies is constant
    total_energy = Calculate_energy(g,m1,m2,r1,r2,theta1,theta2,thetadot1,thetadot2 )
    print(total_energy)
    energies.append(total_energy)

    #return pivot, m1,m2 positions
    line.set_data([0, x1, x2], [0, y1, y2])
    return line,


def on_close(event):
    #error clac
    if energies:
        error1 = ((max(energies) - expected_value)) / abs(expected_value) * 100
        error2 = ((min(energies) - expected_value)) / abs(expected_value) * 100
        print(f"Expected value: {expected_value:.6f}")
        print(f"Energy error: +{abs(error1):.4f}% and -{abs(error2):.4f}%")
        print(f"Max energy: {max(energies):.4f}")
        print(f"Min energy: {min(energies):.4f}")
        print(f"Samples collected: {len(energies)}")
        print(f"Playback Speed: x{steps_per_frame/30}")

fig.canvas.mpl_connect('close_event', on_close)
ani = animation.FuncAnimation(fig, update, interval=10, blit=True)
plt.show()