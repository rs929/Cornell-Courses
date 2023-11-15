"""
Primary module for Alien Invaders

This module contains the main controller class for the Alien Invaders app.
There is no need for any additional classes in this module.  If you need
more classes, 99% of the time they belong in either the wave module or the
models module. If you are unsure about where a new class should go, post a
question on Piazza.

# Noelle Pappous(ntp26) Richie Sun(rs929)
# 12/09/21
"""
from consts import *
from game2d import *
from wave import *


# PRIMARY RULE: Invaders can only access attributes in wave.py via
# getters/setters
# Invaders is NOT allowed to access anything in models.py


class Invaders(GameApp):
    """
    The primary controller class for the Alien Invaders application

    This class extends GameApp and implements the various methods necessary
    for processing the player inputs and starting/running a game.

        Method start begins the application.

        Method update either changes the state or updates the Play object

        Method draw displays the Play object and any other elements on screen

    Because of some of the weird ways that Kivy works, you SHOULD NOT create
    an initializer __init__ for this class.  Any initialization should be done
    in the start method instead.  This is only for this class.  All other
    classes behave normally.

    Most of the work handling the game is actually provided in the class Wave.
    Wave should be modeled after subcontrollers.py from lecture, and will
    have its own update and draw method.

    The primary purpose of this class is to manage the game state: which is
    when the game started, paused, completed, etc. It keeps track of that in
    an internal (hidden) attribute.

    For a complete description of how the states work, see the specification
    for the method update.

    Attribute view: the game view, used in drawing
    Invariant: view is an instance of GView (inherited from GameApp)

    Attribute input: user input, used to control the ship or resume the game
    Invariant: input is an instance of GInput (inherited from GameApp)

    Attribute prevkey: the number of keys pressed last frame
    Invariant: prevkey is an int >= 0
    __________________________________________________________________________

    Attribute prevkey2: the number of keys pressed last frame (for continue)
    Invariant: prevkey2 is an int >= 0

    Attribute mcount: the number of 'm' keys pressed last frame
    Invariant: mcount is an int >= 0
    """
    # HIDDEN ATTRIBUTES:
    # Attribute _state: the current state of the game represented as an int
    # Invariant: _state is one of STATE_INACTIVE, STATE_NEWWAVE, STATE_ACTIVE,
    # STATE_PAUSED, STATE_CONTINUE, or STATE_COMPLETE
    #
    # Attribute _wave: the subcontroller for a single wave, managing aliens
    # Invariant: _wave is a Wave object, or None if there is no wave currently
    # active. It is only None if _state is STATE_INACTIVE.
    #
    # Attribute _text: the currently active message for display screen
    # Invariant: _text is a GLabel object, or None if there is no message to
    # display for the welcome screen. It is onl None if _state is STATE_ACTIVE.
    #
    # You may have new attributes if you wish (you might want an attribute to
    # store any score across multiple waves). But you must document them.
    # LIST MORE ATTRIBUTES (AND THEIR INVARIANTS) HERE IF NECESSARY
    #__________________________________________________________________________
    # Attribute _background1: background of starting screen
    # Invariant: _background1 is a GImage object
    #
    # Attribute _background2: background of game
    # Invariant: _background2 is a GImage object and is not None until state is
    # STATE_NEWWAVE
    #
    # Attribute _title: display of the game name: Alien Assassin
    # Invariant: _title a GLabel object when _state is STATE_INACTIVE and
    # is None in any other state
    #
    # Attribute _shiptypes: display of the types of ships availible
    # Invariant: _shiptypes a GImage object when _state is STATE_INACTIVE and
    # is None in any other state
    #
    # Attribute _hearts: representation of the number of lives remaining
    # Invariant: _hearts is None when _state is STATE_INACTIVE, and a GImage
    # object in any other state
    #
    # Attribute _numwaves: the number of alien waves
    # Invariant: _numwaves is an int >= 0
    #
    # Attribute _originalship: Stores the ship that the player chooses
    # Invariant: _originalship is None when _state is STATE_INACTIVE and is a
    # GImage object in any other state
    #
    # Attribute _textwaves: display of the current alien wave
    # Invariant: _textwaves is None when _state is STATE_INACTIVE and is a
    # GLabel object in any other state
    #
    # Attribute _win: status of game at completion
    # Invariant: _win is a boolean or None. True if player won the game and
    # False if the player lost. Is only not None when _state is STATE_COMPLETE
    #
    # Attribute _music: Epic background music
    # Invariant: _music is a Sound object
    #
    # Attribute _points: display of the number of points the player has earned
    # Invariant: _points is None when _state is STATE_INACTIVE and is a
    # GLabel object in any other state
    #
    # Attribute _savescore: stores the player score between waves
    # Invariant: _savescore is an int >= 0
    #
    # Attribute _mute: displays the directions to mute the game
    # Invariant: _mute is None when the game state is STATE_INACTIVE, and
    # becomes a GLabel Object in STATE_ACTIVE



    # THREE MAIN GAMEAPP METHODS
    def start(self):
        """
        Initializes the application.

        This method is distinct from the built-in initializer __init__ (which
        you should not override or change). This method is called once the
        game is running. You should use it to initialize any game specific
        attributes.

        This method should make sure that all of the attributes satisfy the
        given invariants. When done, it sets the _state to STATE_INACTIVE and
        create a message (in attribute _text) saying that the user should press
        to play a game.
        """
        self._background1 = GImage(x=GAME_WIDTH/2,y=GAME_HEIGHT/2,
        width=GAME_WIDTH,height=GAME_HEIGHT,source='space1.png')
        self._background2 = None
        self.prevkey = 0
        self.prevkey2 = 0
        self._state = STATE_INACTIVE
        if self._state == STATE_INACTIVE:
            title="Press 1, 2, 3, or 4 to Choose\na Ship and Play"
            self._text = GLabel(text=title, font_name = "RetroGame.ttf",
            linecolor='white', font_size=40,x=self.width/2, y = self.height/2)
            self._title=GLabel(text='Alien Assassin',font_name="RetroGame.ttf",
            linecolor='turquoise', font_size=65,x=self.width/2, y = 600)
            self._shiptypes=GImage(x=GAME_WIDTH/2, y=175, width=500, height=188,
            source='selection.png')
        if self._state == STATE_INACTIVE:
            self._wave = None
        self._hearts = None
        self._numwaves = 3
        self._originalship = None
        self._textwaves = None
        self._win = None
        self.mcount = 0
        self._music = Sound('music.wav')
        self._music.volume = 0.3
        self._music.play(loop = True)
        self._points = None
        self._savescore = 0
        self._mute = None

    def update(self,dt):
        """
        Animates a single frame in the game.

        It is the method that does most of the work. It is NOT in charge of
        playing the game.  That is the purpose of the class Wave. The primary
        purpose of this game is to determine the current state, and -- if the
        game is active -- pass the input to the Wave object _wave to play the
        game.

        As part of the assignment, you are allowed to add your own states.
        However, at a minimum you must support the following states:
        STATE_INACTIVE, STATE_NEWWAVE, STATE_ACTIVE, STATE_PAUSED,
        STATE_CONTINUE, and STATE_COMPLETE.  Each one of these does its own
        thing and might even needs its own helper.  We describe these below.

        STATE_INACTIVE: This is the state when the application first opens.
        It is a paused state, waiting for the player to start the game.  It
        displays a simple message on the screen. The application remains in
        this state so long as the player never presses a key.  In addition,
        this is the state the application returns to when the game is over
        (all lives are lost or all aliens are dead).

        STATE_NEWWAVE: This is the state creates a new wave and shows it on
        the screen. The application switches to this state if the state was
        STATE_INACTIVE in the previous frame, and the player pressed a key.
        This state only lasts one animation frame before switching to
        STATE_ACTIVE.

        STATE_ACTIVE: This is a session of normal gameplay.  The player can
        move the ship and fire laser bolts.  All of this should be handled
        inside of class Wave (NOT in this class).  Hence the Wave class
        should have an update() method, just like the subcontroller example
        in lecture.

        STATE_PAUSED: Like STATE_INACTIVE, this is a paused state. However,
        the game is still visible on the screen.

        STATE_CONTINUE: This state restores the ship after it was destroyed.
        The application switches to this state if the state was STATE_PAUSED
        in the previous frame, and the player pressed a key. This state only
        lasts one animation frame before switching to STATE_ACTIVE.

        STATE_COMPLETE: The wave is over, and is either won or lost.

        You are allowed to add more states if you wish. Should you do so, you
        should describe them here.

        Parameter dt: The time in seconds since last update
        Precondition: dt is a number (int or float)
        """
        self._NumKeyDown()
        self._CKeyDown()
        self.Hearts()
        self.Newwave()
        if self._state == STATE_ACTIVE:
            self._mute=GLabel(text='Press M to Mute',font_name="RetroGame.ttf",
            linecolor='white', font_size=10,x=60,y=10)
            if self._numwaves == 3:
                speed = 1
            if self._numwaves == 2:
                speed = 0.5
            if self._numwaves == 1:
                speed = 0.25
            self._wave.update(self.input, dt, speed)
            if self._wave.getship() is None:
                self._state = STATE_PAUSED
            self._points.text = "score: " + str(self._wave.getscore())
        self.PauseAndContinue()
        self.SelectEnding()
        self.StateCompletion()
        self.mute()

    def draw(self):
        """
        Draws the game objects to the view.

        Every single thing you want to draw in this game is a GObject.  To
        draw a GObject g, simply use the method g.draw(self.view).  It is
        that easy!

        Many of the GObjects (such as the ships, aliens, and bolts) are
        attributes in Wave. In order to draw them, you either need to add
        getters for these attributes or you need to add a draw method to
        class Wave.  We suggest the latter.  See the example subcontroller.py
        from class.
        """
        if self._background1 is not None:
            self._background1.draw(self.view)
        if self._shiptypes is not None:
            self._shiptypes.draw(self.view)
        if self._background2 is not None:
            self._background2.draw(self.view)
        if self._text is not None:
            self._background1.draw(self.view)
        if self._wave is not None:
            self._wave.draw(self.view)
        if self._hearts is not None:
            self._hearts.draw(self.view)
        if self._text is not None:
            self._text.draw(self.view)
        if self._textwaves is not None:
            self._textwaves.draw(self.view)
        if self._title is not None:
            self._title.draw(self.view)
        if self._points is not None:
            self._points.draw(self.view)
        if self._mute is not None:
            self._mute.draw(self.view)

    # HELPER METHODS FOR THE STATES GO HERE
    def Newwave(self):
        """
        Checks to see if the game state is in the NEW_WAVE state and looks
        for the number of alien waves remaing (_numwaves).

        If the _state attribute is in the state NEW_WAVE, this function:
        1. Removes all screen text except the score and the wave counter
        2. Changes the _textwaves display depending on _numwaves
        3. Sets _background2 to the game background
        4. Sets the ship image source to the ship chosen by the player on the
        5. Calls the constructor to initalize the alien waves
        6. After everything is created, the state is set to STATE_ACTIVE
        title screen
        """
        if self._state == STATE_NEWWAVE and self._numwaves == 3:
            self._text = None
            self._title = None
            self._directions = None
            self._points = GLabel(text= "score: 0", font_name = "RetroGame.ttf",
            linecolor='yellow', font_size=30,x=400, y = 675)
            self._textwaves = GLabel(text="Wave 1", font_name = "RetroGame.ttf",
            linecolor='white', font_size=40,x=700, y = 675)
            self._shiptypes = None
            self._wave = Wave(self.input, True)
            self._background2 = GImage(x=GAME_WIDTH/2,y=GAME_HEIGHT/2,
            width=GAME_WIDTH,height=GAME_HEIGHT,source='start.png')
            self._state = STATE_ACTIVE
        if self._state == STATE_NEWWAVE and self._numwaves == 2:
            self._originalship = self._wave.getStype()
            self._textwaves = GLabel(text="Wave 2", font_name = "RetroGame.ttf",
            linecolor='white', font_size=40,x=700, y =675)
            self._wave=Wave(self.input,False,self._originalship,self._savescore)
            self._state = STATE_ACTIVE
        if self._state == STATE_NEWWAVE and self._numwaves == 1:
            self._originalship = self._wave.getStype()
            self._textwaves = GLabel(text="Wave 3", font_name = "RetroGame.ttf",
            linecolor='white', font_size=40,x=700, y = 675)
            self._wave=Wave(self.input,False,self._originalship,self._savescore)
            self._state = STATE_ACTIVE

    def PauseAndContinue(self):
        """
        Checks whether or not the _state attribute has reached the state
        STATE_PAUSED or STATE_CONTINUE.

        If the state is STATE_PAUSED, a message is displayed to allow the
        player to continue so long as the player still has lives remaining

        If the state is STATE_CONTINUE, a new ship object is created, the
        text from STATE_PAUSED is removed and the player is allowed to shoot
        again before the state is set back to STATE_ACTIVE
        """
        if self._state == STATE_PAUSED and self._wave.getlives() > 0:
            self._text = GLabel(text = "Press 'C' to Continue",
            font_name = "RetroGame.ttf", linecolor = 'white', font_size = 40,
            x = self.width/2, y = self.height/2)
        if self._state == STATE_CONTINUE:
            self._wave.setship(Ship(format=(1,6),x=GAME_WIDTH/2,y=SHIP_BOTTOM+
            SHIP_HEIGHT/2,width=SHIP_WIDTH,height=SHIP_HEIGHT,
            source=self._wave.getStype()))
            self._wave.setprevkey(0)
            self._text = None
            self._state=  STATE_ACTIVE

    def SelectEnding(self):
        """
        Checks whether or not the _state attribute has reached the state
        STATE_PAUSED and determines the end status of the game

        The possible end statuses are when the player wins or loses, and
        the function changes the _win attribute accordingly

        If the player runs out of lives, _win is set to False
        If the aliens dip below the defense line _win is set to False
        If the player clears all the alien waves, _win is set to True
        If the player clears the wave and _numwaves is not 0, the next wave is
        initialized
        """
        if self._state == STATE_PAUSED and self._wave.getlives() <= 0:
            self._win = False
            self._state = STATE_COMPLETE
        if (self._wave is not None and self._wave.alienbegone() and
         self._numwaves > 0):
            self._savescore = self._wave.getscore()
            self._numwaves = self._numwaves - 1
            self._state = STATE_NEWWAVE
        if (self._wave is not None and self._wave.alienbegone() and
        self._numwaves == 0):
            self._win = True
            self._state = STATE_COMPLETE
        if self._wave is not None and self._wave.defenselose():
            self._win = False
            self._state = STATE_COMPLETE

    def StateCompletion(self):
        """
        Checks whether or not the _state attribute has reached the state
        STATE_COMPLETE and generates the respective ending message on screen by
        creating a GLabel object.

        If the attribute _win is True, a win messages is displayed
        If the attribute _win is False, a lose message is displayed
        """
        if self._state == STATE_COMPLETE and self._win:
            self._text = GLabel(text='VICTORY!',font_name="RetroGame.ttf",
            font_size = 80, x = self.width/2, y=self.height/2,linecolor='blue')
        if self._state == STATE_COMPLETE and self._win == False:
            self._text = GLabel(text='GAME OVER',font_name="RetroGame.ttf",
            font_size = 80, x = self.width/2, y = self.height/2,linecolor='red')

    def Hearts(self):
        """
        Creates PNG images for each life and keeps track of the number of Lives
        remaining. The number of hearts on the PNG drawn decreases with each
        life lost.

        Created GImage objects are stored in the _hearts attribute
        """
        if self._wave is not None and self._wave.getlives()==3:
            self._hearts=GImage(width=200,height=100,x=90,y=670,
            source="hearts1.png")
        elif self._wave is not None and self._wave.getlives()==2:
            self._hearts=GImage(width=200,height=100,x=90,y=670,
            source="hearts2.png")
        elif self._wave is not None and self._wave.getlives()==1:
            self._hearts=GImage(width=200,height=100,x=90,y=670,
            source="hearts3.png")
        elif self._wave is not None and self._wave.getlives()==0:
            self._hearts = None

    def mute(self):
        """
        Determines if the 'M' key is pressed, and if it is,
        it modifies the volumes of the sound objects in the list of sound
        objects in _sounds attribute in wave subcontroller

        Mutes the game when 'M' key is pressed once by setting the volume
        of every sound to 0, and back to its original volume if pressed again

        If the 'M' is pressed and the volume is >0, each of the volume
        attributes are set to 0

        If the 'M' is pressed and the volume is 0, each of the volume
        attributes are set to their original default volumes
        """
        # OR just press F10
        if self._wave is not None:
            keydown = self.input.is_key_down('m')
            curr_keys = self.input.key_count
            change = curr_keys > 0 and self.mcount == 0 and keydown
            if change:
                for i in self._wave.getsounds():
                    if i.volume > 0:
                        self._music.volume = 0
                        i.volume = 0
                    else:
                        self._music.volume = 0.3
                        i.volume = 1
            self.mcount = curr_keys

    def _NumKeyDown(self):
        """
        Determines if the '1' '2' '3' '4' key is pressed, and if it is,
        it modifies the _state and _text attributes so that the welcome screen
        is dismissed

        A key press is when the '1' '2' '3' '4' key is pressed for the
        FIRST TIME. We do not want the state to continue to change as
        we hold down the key. The user must release the
        key and press it again to change the state.

        If the current state is STATE_INACTIVE, a '1' '2' '3' '4' key press
        will result in the state to be changed to STATE_NEWWAVE
        """
        keydown = (self.input.is_key_down('1')or self.input.is_key_down('2')or
        self.input.is_key_down('3')or self.input.is_key_down('4'))
        curr_keys = self.input.key_count
        change = curr_keys > 0 and self.prevkey == 0 and keydown
        if change and self._state == STATE_INACTIVE:
            self._state = STATE_NEWWAVE
        self.prevkey= curr_keys

    def _CKeyDown(self):
        """
        Determines if the 'c' key is pressed, and if it is, it modifies
        the _state and _text attributes so that continue screen is dismissed

        A key press is when the 'c' key is pressed for the FIRST TIME.
        We do not want the state to continue to change as
        we hold down the key. The user must release the
        key and press it again to change the state.

        If the current state is STATE_PAUSED, a 'c' key press will result
        in the state to be changed to STATE_CONTINUE
        """
        keydown = self.input.is_key_down('c')
        curr_keys = self.input.key_count
        change = curr_keys > 0 and self.prevkey2 == 0 and keydown
        if change and self._state == STATE_PAUSED and self._wave.getlives()>0:
            self._state = STATE_CONTINUE
        self.prevkey2= curr_keys
