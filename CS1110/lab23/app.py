"""
A simple application displaying a text and an image.

The purpose of this lab is to familiarize you with the basics of the game2d package.
This will help you get started on the last assignment.

<Richie Sun>
<11/17/21>
"""
from game2d import *

#### CONSTANTS ####

# The initial width of the game display
GAME_WIDTH  = 840
# The initial height of the game display
GAME_HEIGHT = 630

# The initial state of the application
STATE_BEGIN  = 0
# After the font is loaded and initialized
STATE_FINISH = 1

# The number of steps between animation frames
FRAME_STEP = 5

class LabApp(GameApp):
    """
    The application class for this lab.

    In this lab, you will implement three hidden lab attributes.  Read the instructions
    and look at the constants above.
    """
    # HIDDEN ATTRIBUTES
    # Attribute _message: The message to display on the screen
    # Invariant: _message is a GLabel or None
    #
    # Attribute _image: The image to decorate the welcome message
    # Invariant: _image is a GTile, a GImage, or None
    #
    # Attribute _state: The current application state
    # Invariant: _state is one of STATE_BEGIN, STATE_FINISHED

    def start(self):
        """
        Initializes the application.

        This method is distinct from the built-in initializer __init__ (which
        you should not override or change). This method is called once the
        game is running.
        """
        message = GLabel(text = 'Hello World', font_size = 64, font_name = "CuteFrog.ttf", x = self.width/2, y = self.height/2)
        image = GSprite(width = 128, height = 128, source = 'heart-sprite.png', format = (2,4), x = self.width/2, y = self.height/2)
        self._message = message
        self._image = image
        self._state = STATE_BEGIN
        self._cool = FRAME_STEP
        self._image.top = self._message.bottom

    def update(self,dt):
        """
        Updates the game objects each frame.

        This method is used when we want to change the objects (change the positions or
        add new objects) AFTER the application is initialized.  In our case, we need it
        because fonts do not finish loading until after start() has completed.
        """
        if self._state == STATE_BEGIN:
            self._image.top = self._message.bottom
            self._state = STATE_FINISH

        
        if self._cool == 0:
            self._image.frame = (self._image.frame + 1) % self._image.count
            self._cool = FRAME_STEP
        else:
            self._cool = self._cool - 1

    def draw(self):
        """
        Draws the game objects to the view.

        Every single thing you want to draw in this game is a GObject. To draw a
        GObject g, simply use the method g.draw(self.view). It is that easy!
        """
        self._message.draw(self.view)
        self._image.draw(self.view)


# Application code
if __name__ == '__main__':
    # Create and run the lab application
    LabApp(width=GAME_WIDTH,height=GAME_HEIGHT).run()
