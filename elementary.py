#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###
# Genral Notes: Elementary particle simulator. Needs to be extended to a charged particle and an electron.
###

###
# Name: Trevor Kling
# Student ID: 002270716
# Email: kling109@mail.chapman.edu
# Course: PHYS 220/CPSC 220/MATH 220 Fall 2018
# Assignment: CW05 Elementary Particle Class
###

"""
Contains a class for an elementarty particle.  Defines the particle's properties as mass, position, and momentum in tuples, as well as posessing seeral methods to change these properties.
"""

from scipy import constants as cs

class Particle(object):
    """
    Defines an elementary particle in terms of its mass, position, and momentum.  The particle can then be moved and given set values of momentum.

    Parameters:
    -----------
    mass : float > 0
        Indicates the mass of the particle.  The value is set at the beginning of the program, then is called for the later calculations with momentum.
    
    position: (float, float, float)
        Indicates the instantaneous location of the particle in an (x,y,z) tuple.

    momentum: (float, float, float)
        Indicates the direction and magnitude of the motion of the particle in 3-D space.  Each component of the momentum indicates the momentum in that direction.
    """

    def __init__(self, x=0, y=0, z=0):
        """
        Basic constructor for the elementary particle
        """
        self.mass = 1.0
        self.position = (x, y, z)
        self.momentum = (0.0, 0.0, 0.0)

    def impulse(self, px=0, py=0, pz=0):
        """
        Adds the given px, py, and pz values to the existing momentum.  px is the additional momentum in the x direction, py is the additional momentum in the y direction, and pz is the addtional momentum in the z direction.  The three values are placed in a tuple, and then iterated over to add each component.
        """
        newMomentum = (self.momentum[0] + px, self.momentum[1] + py, self.momentum[2] + pz)
        self.momentum = newMomentum

    def move(self, dt=0):
        """
        Shifts the particle by a distance equal to its momentum, divided by the mass, times the time increment dt.  This is accomplished by creating a new tuple of distance values based on this calculation, in the order (dx, dy, dz).  This tuple is then iterated over, and each component is added to its requisite component in the position.
        """
        additionalDistance = ((dt * (self.momentum[0] / self.mass)), (dt * (self.momentum[1] / self.mass)), (dt * (self.momentum[2] / self.mass)))
        newPosition = (self.position[0] + additionalDistance[0], self.position[1] + additionalDistance[1], self.position[2] + additionalDistance[2])
        self.position = newPosition

    def printParticle(self):
        """
        Basic printing method for debugging
        """
        print("Pos: " + repr(self.position) + " Momentum: " + repr(self.momentum) + " Mass: " + repr(self.mass))

class ChargedParticle(Particle):
    """
    Inherits all aspects of the particle class, then adds a charge attribute.
    
    Parameters:
    -----------
    Charge: (float)
        Indicates the particle's charge.  Can be either postiive or negative.
    """
    def __init__(self, x=0, y=0, z=0, c=0):
        Particle.__init__(self, x, y, z)
        self.charge = c

class Electron(ChargedParticle):
    """
    A class which extends the charged particle to specifically an electron.  The scipy constants are employed to attain exact values for the particle.
    """
    def __init__(self, x=0, y=0, z=0):
        ChargedParticle.__init__(self, x, y, z, -cs.e)
        self.mass = cs.m_e

class Proton(ChargedParticle):
    """
    A class which extends the charged particle to specifically a proton.  The scipy constants are used again to attain exact values.
    """
    def __init__(self, x=0, y=0, z=0):
        ChargedParticle.__init__(self, x, y, z, cs.e)
        self.mass = cs.m_p
