"""
An application to show off coroutine animation

This purpose of this lab is to understand how to use coroutines to animate an
a rolling ball.

<YOUR NAME HERE>
<DATE HERE>
"""
from game2d import *

#### CONSTANTS ####

# The initial width of the game display
GAME_WIDTH  = 840
# The initial height of the game display
GAME_HEIGHT = 630

# The height of the "plank" to roll on
PLANK_HEIGHT = 10

# The ball width
BALL_WIDTH  = 64
# The ball height
BALL_HEIGHT = 64

# How far to move the ball (left or right) in pixels
BALL_STEP = 64
# The number of seconds to move the ball
BALL_SPEED = 0.5


class LabApp(GameApp):
    """
    The application class for this lab.

    We have broken this up into helpers.  Your work will be done inside of these
    helpers.
    """
    # HIDDEN ATTRIBUTES
    # Attribute _plank: The rectangle to roll the ball on top of.
    # Invariant: _plank is a GRectangle; its top is center of window
    #
    # Attribute _ball: The ball to roll.
    # Invariant: _ball is a GRectangle; its bottom is center of window
    #
    # Attribute _animator: The animation coroutine.
    # Invariant: _animator is either None or a coroutine

    def start(self):
        """
        Initializes the application.

        This method is distinct from the built-in initializer __init__ (which
        you should not override or change). This method is called once the
        game is running.
        """
        self._plank = GRectangle(x=self.width/2,width=self.width,height=PLANK_HEIGHT,fillcolor='black')
        self._ball  = GImage(source='beach-ball.png',x=self.width/2,width=BALL_WIDTH,height=BALL_HEIGHT)

        # One on top of the other
        self._plank.top=self.height/2
        self._ball.bottom = self.height/2

        # The animator
        self._animator = None

    def update(self,dt):
        """
        Updates the game objects each frame.

        This method is used when we want to change the objects (change the positions or
        add new objects) AFTER the application is initialized.  In this lab, we have
        written this method for you. You just need to complete the two helpers.

        Parameter dt: The number of seconds since the last animation frame
        Precondition: dt is an number >= 0
        """
        if not self._animator  is None:
            self.runAnimator(dt)
        elif self.input.is_key_down('left'):
            # Create animator and start it up
            self._animator = self.makeAnimator(-BALL_STEP,BALL_SPEED)
            next(self._animator)
        elif self.input.is_key_down('right'):
            # Create animator and start it up
            self._animator = self.makeAnimator(BALL_STEP,BALL_SPEED)
            next(self._animator)

    def draw(self):
        """
        Draws the game objects to the view.

        Every single thing you want to draw in this game is a GObject. To draw a
        GObject g, simply use the method g.draw(self.view). It is that easy!
        """
        self._plank.draw(self.view)
        self._ball.draw(self.view)

    # The two methods to implement
    def runAnimator(self,dt):
        """
        The driver for the animation coroutine

        Parameter dt: The number of seconds since the last animation frame
        Precondition: dt is an number >= 0
        """
        # Send the dt to the animator
        try:
            self._animator.send(dt)
        except:
            self._animator = None
        # If you crash, it is done, so set animator to None


    def makeAnimator(self,dx,speed):
        """
        The animation coroutine.

        This should have a yield expression that receives the dt (and does NOT yield
        anything back the parent).  It only moves the ball left and right.  In the
        optional, optional exercise, it will rotate the ball as well.

        Parameter dx: The amount to move the ball
        Precondition: dx is a number (int or float)

        Paramter speed: The number of seconds to animate the ball
        Precondition: speed is a number > 0
        """
        # Compute the amount to move per-second
        move = dx/speed
        # Also keep track of the number of seconds animated so far
        time = 0
        currentpos = self._ball.x
        # While we have not animated all the seconds
            # Wait for the latest dt value
            # Use this to determine the amount to move this frame
            # Update the ball position and the total number of seconds
        while time < speed:
            dt = (yield)
            time = time + dt
            self._ball.x = self._ball.x + move * dt

        # Snap the ball into its correct final position (in case we went over)
        self._ball.x = currentpos + dx

# Application code
if __name__ == '__main__':
    # Create and run the lab application
    LabApp(width=GAME_WIDTH,height=GAME_HEIGHT).run()
