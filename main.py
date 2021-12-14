import pygame as pg
import numpy as np

#96139초

timeAcceleration = 0.001

def gravity(A, B):
    G =  6.67384 * 10**(-11)
    r = np.abs(A.pos - B.pos)
    F = G * A.m * B.m / r ** 2
    return F

def unitVector(A, B):
    direction = B.pos - A.pos
    direction /= np.abs(direction)
    return direction

def accelation(A, B, F):
    return F / A.m * unitVector(A, B)

def velocity(A):
    return A.a * 1 * timeAcceleration

def position(A):
    return A.v * 1 * timeAcceleration

class Object():
    def __init__(self, x, y, m):
        self.pos = np.array([x, y])
        self.a = np.zeros(2)
        self.v = np.zeros(2)
        self.m = m

A = Object(0.5, 0., 1)
B = Object(-0.5, 0., 1)
t = 0
while True:
    A.pos[1] = 0
    B.pos[1] = 0

    F = gravity(A, B)

    A.a = accelation(A, B, F)
    A.v += velocity(A)
    A.pos += position(A)

    B.a = accelation(B, A, F)
    B.v += velocity(B)
    B.pos += position(B)

    t += 1

    if int(t)%10000 == 0:
        print(A.pos)
        print(B.pos)
        print()

    if A.pos[0] < B.pos[0]:
        print(t*timeAcceleration)
        break