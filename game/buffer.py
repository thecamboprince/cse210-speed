import random
from game.actor import Actor
from game.point import Point
from game import constants

class Buffer(Actor):
    """Points earned. The responsibility of Buffer is to keep track of the player's text entry.
    Stereotype:
        Information Holder
    Attributes: 
        _text (string): The word that the user has typed in.
    """
    def __init__(self):
        """The class constructor. Invokes the superclass constructor, initializes points to zero, sets the position and updates the _entry.
        
        Args:
            self (Buffer): an instance of Buffer.
        """
        super().__init__()
        self._entry = ""
        position = Point(1, constants.MAX_Y)
        self.set_position(position)
        self.set_text(f"Buffer: {self._entry}")
    
    def add_letter(self, letter):
        """Adds the given letter unless it is an '*' which returns the word.
        
        Args:
            self (Buffer): An instance of Buffer.
            letter (char): The character to add.
        """
        self._entry = '' if letter == '*' else self._entry + letter
        self.set_text(f"Buffer: {self._entry}")

    def clear_buffer(self):
        self._entry = ""

    def get_content(self):
        """Gets whatever string is currently stored in the buffer.
        
        Args:
            self (Buffer): An instance of Buffer.
        """
        return self._entry