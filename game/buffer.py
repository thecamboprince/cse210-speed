import random
from game.actor import Actor
from game.point import Point
from game.constants import constants

class Buffer(Actor):
    """Points earned. The responsibility of Buffer is to keep track of the player's text entry.
    Stereotype:
        Information Holder
    Attributes: 
        _text (string): The word that the user has typed in.
    """
    def __init__(self):
        """The class constructor. Invokes the superclass constructor, initializes points to zero, sets the position and updates the text.
        
        Args:
            self (Buffer): an instance of Buffer.
        """
        super().__init__()
        self._text = ""
        position = Point(1, constants.MAX_Y)
        self.set_position(position)
        self.set_text(f"Buffer: {self._text}")
    
    def add_letter(self, letter):
        """Adds the given letter unless it is an '*' which clears the word.
        
        Args:
            self (Buffer): An instance of Buffer.
            letter (char): The character to add.
        """
        self._text = "" if letter == "*" else self._text + letter
        self.set_text(f"Buffer: {self._text}")

    def get_buffer(self):
        """Gets whatever string is currently stored in the buffer.
        
        Args:
            self (Buffer): An instance of Buffer.
        """
        return self._text