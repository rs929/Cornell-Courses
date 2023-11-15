"""
Subcontroller module for Alien Invaders

This module contains the subcontroller to manage a single level or wave in
the Alien Invaders game.  Instances of Wave represent a single wave. Whenever
you move to a new level, you are expected to make a new instance of the class.

The subcontroller Wave manages the ship, the aliens and any laser bolts on
screen. These are model objects.  Their classes are defined in models.py.

Most of your work on this assignment will be in either this module or
models.py. Whether a helper method belongs in this module or models.py is
often a complicated issue.  If you do not know, ask on Piazza and we will
answer.

# Richie Sun(rs929) Noelle Pappous(ntp26)
# 12/09/21
"""
from game2d import *
from consts import *
from models import *
import random

# PRIMARY RULE: Wave can only access attributes in models.py via getters/setters
# Wave is NOT allowed to access anything in app.py (Subcontrollers are not
# permitted to access anything in their parent. To see why, take CS 3152)


class Wave(object):
    """
    This class controls a single level or wave of Alien Invaders.

    This subcontroller has a reference to the ship, aliens, and any laser bolts
    on screen. It animates the laser bolts, removing any aliens as necessary.
    It also marches the aliens back and forth across the screen until they are
    all destroyed or they reach the defense line (at which point the player
    loses). When the wave is complete, you  should create a NEW instance of
    Wave (in Invaders) if you want to make a new wave of aliens.

    If you want to pause the game, tell this controller to draw, but do not
    update.  See subcontrollers.py from Lecture 24 for an example.  This
    class will be similar to than one in how it interacts with the main class
    Invaders.

    All of the attributes of this class ar to be hidden. You may find that
    you want to access an attribute in class Invaders. It is okay if you do,
    but you MAY NOT ACCESS THE ATTRIBUTES DIRECTLY. You must use a getter
    and/or setter for any attribute that you need to access in Invaders.
    Only add the getters and setters that you need for Invaders. You can keep
    everything else hidden.

    """
    # HIDDEN ATTRIBUTES:
    # Attribute _ship: the player ship to control
    # Invariant: _ship is a Ship object or None
    #
    # Attribute _aliens: the 2d list of aliens in the wave
    # Invariant: _aliens is a rectangular 2d list containing Alien objects or None
    #
    # Attribute _bolt: the laser bolts currently on screen
    # Invariant: _bolt is a list of Bolt objects, possibly empty
    #
    # Attribute _dline: the defensive line being protected
    # Invariant : _dline is a GPath object
    #
    # Attribute _lives: the number of lives left
    # Invariant: _lives is an int >= 0
    #
    # Attribute _time: the amount of time since the last Alien "step"
    # Invariant: _time is a float >= 0s
    #
    # You may change any attribute above, as long as you update the invariant
    # You may also add any new attributes as long as you document them.
    # LIST MORE ATTRIBUTES (AND THEIR INVARIANTS) HERE IF NECESSARY
    #__________________________________________________________________________
    # Attribute _alienright: if the alien is moving right or left
    # Invariant: _alienright is a bool (True = right, False = left)
    #
    # Attribute _prevkey: the number of keys pressed last frame
    # Invariant: _prevkey is an int >= 0
    #
    # Attribute _prevkey2: the number of keys pressed last frame (separate)
    # Invariant: _prevkey2 is an int >= 0
    #
    # Attribute _Stype: stores the ship object selected by the player
    # Invariant: _Stype is a Ship Object
    #
    # Attribute _randbolt: the maximum number of alien steps before alien shoots
    # Invariant: _randbolt is an int >= 1 <= BOLT_RATE
    #
    # Attribute _stepcount: the number of steps taken by an alien object
    # Invariant: _stepcount is an int >= 0
    #
    # Attribute _animator: A coroutine for performing an animation
    # Invariant: _animator is a generator-based coroutine (or None)
    #
    # Attribute _aliendown: if the alien is moving down
    # Invariant: _aliendown is a bool (True = down, False = not down)
    #
    # Attribute _score: stores the player's _score
    # Invariant: _score is an int >= 0.
    #
    # Attribute _sounds: stores the possible game sounds in a list
    # Invariant: _sounds is a list of Sound objects

    # GETTERS AND SETTERS (ONLY ADD IF YOU NEED THEM)
    def getaliens(self):
        """
        Getter for _aliens attribute
        """
        return self._aliens

    def getship(self):
        """
        Getter for _ship attribute
        """
        return self._ship

    def setship(self, ship):
        """
        Setter for _ship attribute

        Parameter ship: the ship to be set
        Precondition: ship is a Ship object
        """
        self._ship = ship

    def getlives(self):
        """
        Getter for _lives attribute
        """
        return self._lives

    def setprevkey(self, key):
        """
        Setter for _prevkey attribute

        Parameter key: the number of keys pressed
        Precondition: key is an int >= 0
        """
        self._prevkey = key

    def gettime(self):
        """
        Getter for _time attribute
        """
        return self._time

    def getStype(self):
        """
        Getter for _Stype attribute
        """
        return self._Stype

    def getsounds(self):
        """
        Getter for _sounds attribute
        """
        return self._sounds

    def getscore(self):
        """
        Getter for _score attribute
        """
        return self._score

    # INITIALIZER (standard form) TO CREATE SHIP AND ALIENS
    def __init__(self, input, start, ship=None, score = 0):
        """
        Initializes the alien waves player ship, defense line, bolts, and
        sound effects

        Parameter input: input from app.py
        Precondition: input is a Ginput object

        Parameter start: If the game is still in the starting state
        Precondition: start is a bool

        Parameter ship: the player ship chosen by the player at the start
        Precondition: width is a number (int or float)

        Parameter score: the player score (saved from the previous wave)
        Precondition: width is an int >= 0
        """
        self._prevkey2 = 0
        if start:
            self._score = 0
            self._Stype = self.chooseshiptype(input)
        elif start == False:
            self._score = score
            self._Stype = ship
        self._aliens = self.alienlist()
        self._ship = Ship(format = (1,6), x=GAME_WIDTH/2,
            y=SHIP_BOTTOM+SHIP_HEIGHT/2, width=SHIP_WIDTH, height=SHIP_HEIGHT,
            source=self.getStype())
        self._ship.frame = 0
        self._dline = GPath(points=[0,DEFENSE_LINE,GAME_WIDTH,DEFENSE_LINE],
            linewidth=2, linecolor='white')
        self._bolt = []
        self._randbolt = self.randombolt()
        self._lives = SHIP_LIVES
        self._animator = None
        self._stepcount = 0
        self._prevkey = 0
        self._time = 0
        self._alienright = True
        self._aliendown = False
        self._sounds = [Sound('pop1.wav'),Sound('pop2.wav'),
        Sound('alienshoot.wav'),Sound('shoot.wav'),Sound('win.wav'),
        Sound('blast1.wav')]

    # UPDATE METHOD TO MOVE THE SHIP, ALIENS, AND LASER BOLTS
    def update(self, input, dt, speed):
        """
        Animates Alien Waves and Player Ship, bolt movement, and controls the
        generator for the ship death animation

        Parameter input: input fromt he player
        Precondition: input is a GInput object

        Parameter dt: The time in seconds since last update
        Precondition: dt is a number (int or float)

        Parameter speed: amount to change the speed for each wave
        Precondition: speed is a number >= 0 and <= 1 (int or float)
        """
        self.Moveship(input)
        self.Counttime(dt)
        if self.gettime() > ALIEN_SPEED*speed:
            if self._alienright == True: self.Movealiens('right')
            if self._alienright == False: self.Movealiens('left')
            if self._aliendown: self.Movealiens('down')
        self.Determinealienshoot()
        self.Boltcreation(input)
        if len(self._bolt) != 0:
            self.movebolt(dt)
        if self._animator is not None:
            try:
                self._animator.send(dt)
            except StopIteration:
                self._animator=None
                self._ship=None
                self._lives=self._lives-1
                self._bolt.clear()

    # DRAW METHOD TO DRAW THE SHIP, ALIENS, DEFENSIVE LINE AND BOLTS
    def draw(self, view):
        """
        Method to draw the the ship, alien waves, defensive line
        and bolts.

        Parameter view: the view
        Precondition: view is a the game view for things to be drawn on
        """
        for x in self.getaliens():
            for y in x:
                if y is not None:
                    y.draw(view)
        ship = self.getship()
        if ship is not None:
            ship.draw(view)
        defense = self._dline
        defense.draw(view)
        if len(self._bolt) != 0:
            for i in range(len(self._bolt)):
                bolt = self._bolt[i]
                bolt.draw(view)

    # HELPER METHODS FOR COLLISION DETECTION
    def alienlist(self):
        """
        Returns a 2d list of alien objects
        """
        list = []
        ycoord = GAME_HEIGHT - ALIEN_CEILING + ALIEN_V_SEP + ALIEN_HEIGHT*0.5
        xcoord = ALIEN_H_SEP-ALIEN_WIDTH*0.5
        for x in reversed(range(ALIEN_ROWS)):
            row = []
            if x % 6 <= 1:
                alientype = 'alien1.png'
            elif x % 6 >= 2 and x % 6 <= 3:
                alientype = 'alien2.png'
            else:
                alientype = 'alien3.png'
            ycoord = ycoord - ALIEN_V_SEP - ALIEN_HEIGHT
            for y in range(ALIENS_IN_ROW):
                xcoord = xcoord + ALIEN_H_SEP + ALIEN_WIDTH
                alien = Alien(x=xcoord,y=ycoord,width=ALIEN_WIDTH,
                height=ALIEN_HEIGHT,source=alientype)
                row.append(alien)
            xcoord = ALIEN_H_SEP-ALIEN_WIDTH*0.5
            list.append(row)
        return list

    def Moveship(self, input):
        """
        Moves the player ship by taking input from the keyboard

        Parameter input: the user key input
        Precondtion: input is a GInput object
        """
        if (self.getship() is not None and self._animator is None and
            input.is_key_down('left') and self.getship().x>0+SHIP_WIDTH*0.5):
            self.getship().x = self.getship().x - SHIP_MOVEMENT
        if (self.getship() is not None and self._animator is None and
            input.is_key_down('right') and
            self.getship().x < GAME_WIDTH-SHIP_WIDTH*0.5):
            self.getship().x = self.getship().x + SHIP_MOVEMENT

    def Counttime(self, dt):
        """
        Counts the number of seconds since the last alien step
        and alters the _time attribute

        Parameter dt: The time in seconds since last update
        Precondition: dt is a number (int or float)
        """
        self._time = self._time + dt

    def Movealiens(self, direction):
        """
        Moves Aliens

        Parameter direction: Direction that the alien is moving in
        (left, right, down)
        Precondtion: direction is a string indicating Direction
        ('left', 'right', 'down')
        """
        if direction == 'right':
            self.countsteps()
            move = ALIEN_H_WALK
            if self.rightmost()>GAME_WIDTH-ALIEN_WIDTH:
                move = 0
                self._aliendown = True
        elif direction == 'left':
            self.countsteps()
            move = -ALIEN_H_WALK
            if self.leftmost()<ALIEN_WIDTH:
                move = 0
                self._aliendown = True
        elif direction == 'down':
            self.countsteps()
            for i in range(len(self.getaliens())):
                for j in range(len(self.getaliens()[i])):
                    if self.getaliens()[i][j] is not None:
                        self._aliens[i][j].y=self._aliens[i][j].y-ALIEN_V_WALK
                self._aliendown = False
                move = 0
            if self.rightmost()>GAME_WIDTH-ALIEN_WIDTH:
                self._alienright = False
            elif self.leftmost()<ALIEN_WIDTH:
                self._alienright = True
        for i in range(len(self.getaliens())):
            for j in range(len(self.getaliens()[i])):
                if self.getaliens()[i][j] is not None:
                    self._aliens[i][j].x = self._aliens[i][j].x + move
        self._time = 0

    def rightmost(self):
        """
        Finds and returns x position of Rightmost Alien in the List
        """
        right = 0
        for i in range(len(self.getaliens())):
            for j in range(len(self.getaliens()[i])):
                if (self.getaliens()[i][j] is not None and
                self.getaliens()[i][j].x > right):
                    right = self.getaliens()[i][j].x
        return right

    def leftmost(self):
        """
        Finds and returns x position of Leftmost Alien in the List
        """
        left = GAME_WIDTH
        for i in range(len(self.getaliens())):
            for j in range(len(self.getaliens()[i])):
                if (self.getaliens()[i][j] is not None and
                self.getaliens()[i][j].x < left):
                    left = self.getaliens()[i][j].x
        return left

    def movebolt(self, dt):
        """
        Checks if the bolts are from the alien or the ships using the isPbolt()
        method and moves the bolt accordingly

        Checks for collision to the aliens and the ships and uses
        the aliencollion() and shipcollision() methods accordingly

        Parameter dt: The time in seconds since last update
        Precondition: dt is a number (int or float)
        """
        for i in self._bolt:
            if self.isPbolt(i):
                i.y = i.y + BOLT_SPEED
                if i.y > GAME_HEIGHT:
                    self._bolt.remove(i)
                    self._prevkey = 0
                self.aliencollision(i)
            else:
                i.y = i.y - BOLT_SPEED
                self.shipcollision(i, dt)

    def isPbolt(self, bolt):
        """
        Returns True if the bolt one that is shot from the player ship

        Parameter bolt: the bolt object being checked
        Precondition: bolt is a Bolt object
        """
        if bolt._velocity == BOLT_SPEED:
            return True
        else:
            return False

    def Determinealienshoot(self):
        """
        Determines if when an alien should shoot by comparing the number of
        steps take by the aliens and the random shooting interval generated
        by randombolt()
        """
        if self._stepcount > BOLT_RATE:
            self._stepcount = 0
        if self._stepcount == self._randbolt:
            choice = random.randint(0,len(self.getaliens()[0])-1)
            if self.isvalidcol(choice):
                self.alienshoot(choice)
                self._stepcount = 0
            else:
                choice = random.randint(0,len(self.getaliens()[0])-1)

    def randombolt(self):
        """
        Returns a randomly generated number from 1 to BOLT_RATE
        """
        return random.randint(1,BOLT_RATE)

    def countsteps(self):
        """
        Keeps track of the number of steps taken by the Aliens
        """
        self._stepcount = self._stepcount + 1

    def alienshoot(self, choice):
        """
        Selects a random alien column from _alien and creates a bolt object
        for the bottommost alien and appends it to the _bolt attribute

        Parameter choice: The valid column selected
        Precondition: choice is a valid column index (int >= 0)
        """
        if self.isvalidcol(choice) and self.getship() is not None:
            bottom = GAME_HEIGHT
            for j in range(len(self.getaliens())):
                if (self.getaliens()[j][choice] is not None and
                self.getaliens()[j][choice].y < bottom):
                    bottom = self.getaliens()[j][choice].y
                    bottomalien = self.getaliens()[j][choice]
            alienBolt = Bolt(x = bottomalien.x, y = bottomalien.y,
            width = BOLT_WIDTH, height = BOLT_HEIGHT,
            fillcolor = "red", linecolor = "black", velocity = -BOLT_SPEED)
            self._bolt.append(alienBolt)
            self.playsound(2).play()
        self._randbolt = self.randombolt()

    def isvalidcol(self, col):
        """
        Returns True if the alien column has at least
        one alien object

        Parameter col: the index of the alien column
        Precondition: col is an int >=0 and <= ALIENS_IN_ROW
        """
        accume = 0
        for i in range(len(self.getaliens())):
            if self.getaliens()[i][col] is not None:
                accume = accume + 1
        if accume == 0:
            return False
        else:
            return True

    def aliencollision(self, bolt):
        """
        Sets alien object that collides with player bolt equal to None
        ,deletes player bolt, and allows player to shoot again

        Parameter bolt: the bolt object being checked
        Precondition: bolt is a Bolt object
        """
        for a in range(len(self.getaliens())):
            for b in range(len(self.getaliens()[a])):
                if (self.getaliens()[a][b] is not None and
                self.getaliens()[a][b].acollides(bolt)):
                    self.getaliens()[a][b] = None
                    self.trackScore(a)
                    rando = random.randint(0,1)
                    self.playsound(rando).play()
                    self._bolt.remove(bolt)
                    self._prevkey = 0

    def shipcollision(self, bolt, dt):
        """
        Sets ship object that collides with alien bolt equal to None
        and deletes alien bolt.

        Parameter bolt: the bolt object being checked
        Precondition: bolt is a Bolt object

        Parameter dt: The time in seconds since last update
        Precondition: dt is a number (int or float)
        """
        if self.getship() is not None and self.getship().scollides(bolt):
            self._bolt.remove(bolt)
            self._animator = self.animatedeath()
            next(self._animator)

    def animatedeath(self):
        """
        Animates the death animation of the player ship over DEATH_SPEED time

        This method is a coroutine that keeps track of the time passed (as a
        fraction of the total time and use that to set the ship attributes.

        The coroutine takes the dt as periodic input so it knows how many
        (parts of) seconds to animate.
        """
        self.playsound(5).play()
        time = 0
        timeLapsed=0
        animating = True
        while animating:
            time = timeLapsed/DEATH_SPEED
            if timeLapsed <= DEATH_SPEED:
                dt = (yield)
                newframe = time*5
                timeLapsed = timeLapsed + dt
                self.getship().frame = int(newframe)
            else:
                animating = False

    def alienbegone(self):
        """
        Returns True if all of the aliens in the _aliens attribute list
        are of None value, meaning all aliens are dead
        """
        for i in range(len(self.getaliens())):
            for j in self.getaliens()[i]:
                if j is not None:
                    return False
        return True

    def defenselose(self):
        """
        Returns True if the bottom most alien(s) in _aliens attribute
        dips below the defense line
        """
        bottom = GAME_HEIGHT
        for j in range(len(self.getaliens())):
            for i in range(len(self.getaliens())):
                if (self.getaliens()[j][i] is not None and
                self.getaliens()[j][i].y < bottom):
                    bottom = self.getaliens()[j][i].y
                    if bottom-ALIEN_HEIGHT*0.5 < DEFENSE_LINE:
                        return True

    def Boltcreation(self, input):
        """
        Creates a bolt object for the player ship and postitions it
        at the front of the player ship

        Parameter input: the user key input
        Precondtion: input is a GInput object
        """
        if self.getship() is not None and input.is_key_down('up'):
            keydown = input.is_key_down('up')
            curr_keys = input.key_count
            change = curr_keys > 0 and self._prevkey == 0 and keydown
            if change:
                self.playsound(3).play()
                playerbolt = Bolt(x=self.getship().x,
                y=self.getship().y+SHIP_HEIGHT*0.5+BOLT_HEIGHT*0.5,
                width=BOLT_WIDTH,height=BOLT_HEIGHT, fillcolor='green',
                linecolor='white', velocity=BOLT_SPEED)
                self._bolt.append(playerbolt)
            self._prevkey = curr_keys

    def chooseshiptype(self, input):
        """
        Sets the source attribute of the ship to a different png file
        to allow the player to select their own player ship character

        This function detects if the player has pressed any of the number keys
        1, 2, 3, 4 and sets the source attrubute of the ship object accordingly

        Parameter input: the user key input
        Precondtion: input is a GInput object
        """
        if input.is_key_down('1'):
            keydown = input.is_key_down('1')
            curr_keys = input.key_count
            change = curr_keys > 0 and self._prevkey2 == 0 and keydown
            if change:
                ship = 's1.png'
            self._prevkey2 = curr_keys
        elif input.is_key_down('2'):
            keydown = input.is_key_down('2')
            curr_keys = input.key_count
            change = curr_keys > 0 and self._prevkey2 == 0 and keydown
            if change:
                ship = 's2.png'
            self._prevkey2 = curr_keys
        elif input.is_key_down('3'):
            keydown = input.is_key_down('3')
            curr_keys = input.key_count
            change = curr_keys > 0 and self._prevkey2 == 0 and keydown
            if change:
                ship = 's3.png'
            self._prevkey2 = curr_keys
        elif input.is_key_down('4'):
            keydown = input.is_key_down('4')
            curr_keys = input.key_count
            change = curr_keys > 0 and self._prevkey2 == 0 and keydown
            if change:
                ship = 's4.png'
            self._prevkey2 = curr_keys
        return ship

    def playsound(self, sound):
        """
        Plays the sound objects stored in the _sounds attribute
        0 = alien pop1
        1 = alien pop2
        2 = alien shoot
        3 = player shoot
        4 = win sound
        5 = ship explosion

        Paramter sound: The number of the index for the desired sound stored
        in the _sounds attribute
        Precondtion: sound is a valid index value, int >= 0 and <= 4
        """
        sound = self._sounds[sound]
        return sound

    def trackScore(self, index):
        """
        Adds the specified amount to the _score depending on the row index
        of the alien. Aliens higher up are worth more
        """
        self._score = self._score + (ALIEN_ROWS-index)*10
