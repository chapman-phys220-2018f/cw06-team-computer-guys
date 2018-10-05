#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import elementary
from scipy import constants
import math

"""elementary.py Test Module

Verifies that the implementations for the particle classes are correct.
"""

def test_instantiation():
    """Verify that particles are created with correct attributes.
    """
    p = elementary.Particle(1.0, 2.0, 3.0)
    assert math.isclose(p.mass, 1.0)
    assert all(math.isclose(*pos) for pos in zip(p.position, (1.0, 2.0, 3.0)) )
    assert all(math.isclose(*mom) for mom in zip(p.momentum, (0.0, 0.0, 0.0)) )

def test_impulse():
    """Verify that an impulse changes the momentum.
    """
    p = elementary.Particle(1.0, 2.0, 3.0)
    p.impulse(1.0, 2.0, 3.0)
    assert all(math.isclose(*mom) for mom in zip(p.momentum, (1.0, 2.0, 3.0)) )
    
def test_move():
    """Verify that motion proceeds as expected.
    """
    p = elementary.Particle(1.0, 2.0, 3.0)
    p.mass = 2.0  # Change mass so motion is nontrivial
    p.impulse(1.0, 2.0, 3.0)
    p.move(0.1)
    assert all(math.isclose(*pos) for pos in zip(p.position, (1.0 + 0.1*1.0/2.0, 2.0 + 0.1*2.0/2.0, 3.0 + 0.1*3.0/2.0)) )

def test_electron():
    """Verify the electron implementation.
    """
    e = elementary.Electron(1.0, 2.0, 3.0)
    assert math.isclose(e.mass, constants.m_e)
    assert math.isclose(e.charge, -constants.e)

def test_proton():
    """Verify the positron implementation.
    """
    p = elementary.Proton(1.0, 2.0, 3.0)
    assert math.isclose(p.mass, constants.m_p)
    assert math.isclose(p.charge, constants.e)
    
