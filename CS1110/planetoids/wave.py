"""
Subcontroller module for Planetoids

This module contains the subcontroller to manage a single level (or wave) in the 
Planetoids game.  Instances of Wave represent a single level, and should correspond
to a JSON file in the Data directory. Whenever you move to a new level, you are 
expected to make a new instance of the class.

The subcontroller Wave manages the ship, the asteroids, and any bullets on screen. These 
are model objects. Their classes are defined in models.py.

Most of your work on this assignment will be in either this module or models.py.
Whether a helper method belongs in this module or models.py is often a complicated
issue.  If you do not know, ask on Ed Discussions and we will answer.

# YOUR NAME(S) AND NETID(S) HERE
# DATE COMPLETED HERE
"""
from game2d import *
from consts import *
from models import *
import random
import datetime

# PRIMARY RULE: Wave can only access attributes in models.py via getters/setters
# Level is NOT allowed to access anything in app.py (Subcontrollers are not permitted
# to access anything in their parent. To see why, take CS 3152)

class Wave(object):
    """
    This class controls a single level or wave of Planetoids.
    
    This subcontroller has a reference to the ship, asteroids, and any bullets on screen.
    It animates all of these by adding the velocity to the position at each step. It
    checks for collisions between bullets and asteroids or asteroids and the ship 
    (asteroids can safely pass through each other). A bullet collision either breaks
    up or removes a asteroid. A ship collision kills the player. 
    
    The player wins once all asteroids are destroyed.  The player loses if they run out
    of lives. When the wave is complete, you should create a NEW instance of Wave 
    (in Planetoids) if you want to make a new wave of asteroids.
    
    If you want to pause the game, tell this controller to draw, but do not update.  See
    subcontrollers.py from Lecture 25 for an example.  This class will be similar to
    than one in many ways.
    
    All attributes of this class are to be hidden. No attribute should be accessed 
    without going through a getter/setter first. However, just because you have an
    attribute does not mean that you have to have a getter for it. For example, the
    Planetoids app probably never needs to access the attribute for the bullets, so 
    there is no need for a getter there. But at a minimum, you need getters indicating
    whether you one or lost the game.
    """
    # LIST ANY ATTRIBUTES (AND THEIR INVARIANTS) HERE IF NECESSARY
    # THE ATTRIBUTES LISTED ARE SUGGESTIONS ONLY AND CAN BE CHANGED AS YOU SEE FIT
    # Attribute _data: The data from the wave JSON, for reloading 
    # Invariant: _data is a dict loaded from a JSON file
    #
    # Attribute _ship: The player ship to control 
    # Invariant: _ship is a Ship object
    #
    # Attribute _asteroids: the asteroids on screen 
    # Invariant: _asteroids is a list of Asteroid, possibly empty
    #
    # Attribute _bullets: the bullets currently on screen 
    # Invariant: _bullets is a list of Bullet, possibly empty
    #
    # Attribute _lives: the number of lives left 
    # Invariant: _lives is an int >= 0
    #
    # Attribute _firerate: the number of frames until the player can fire again 
    # Invariant: _firerate is an int >= 0
    
    # GETTERS AND SETTERS (ONLY ADD IF YOU NEED THEM)
    
    # INITIALIZER (standard form) TO CREATE SHIP AND ASTEROIDS
    
    # UPDATE METHOD TO MOVE THE SHIP, ASTEROIDS, AND BULLETS
    
    # DRAW METHOD TO DRAW THE SHIP, ASTEROIDS, AND BULLETS
    
    # RESET METHOD FOR CREATING A NEW LIFE
    
    # HELPER METHODS FOR PHYSICS AND COLLISION DETECTION
