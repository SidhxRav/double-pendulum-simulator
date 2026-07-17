import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

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
dt = 0.01