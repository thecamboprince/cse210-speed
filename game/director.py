import random
from time import sleep
from game import constants
from game.score import Score
from game.buffer import Buffer
from game.word import Word
from game.point import Point

class Director:
    # Chase
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        input_service (InputService): The input mechanism.
        keep_playing (boolean): Whether or not the game can continue.
        output_service (OutputService): The output mechanism.
        score (Score): The current score.
        buffer (Buffer): buffer the words typed in
        words ([Word]): an array of Word objects
    """

    def __init__(self, input_service, output_service):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
            input_service (InputService): an instance of InputService.
            output_service (output_service): an instance of output_service.
        """
        self._input_service = input_service
        self._keep_playing = True
        self._output_service = output_service
        self._score = Score()
        self._buffer = Buffer()
        self._words = []
        for _ in range(0, random.randint(5, 10)):
            self._add_word()
        
    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._keep_playing:
            self._get_inputs()
            self._update()
            self._do_outputs()
            sleep(constants.FRAME_LENGTH)

    def _get_inputs(self):
        newLetter = self._input_service.get_letter()
        self._buffer.add_letter(newLetter)

    def _update(self):
        """Update the position and velocity of the words. Updates the score. Clears the buffers as needed.

        Args:
            self (Director): An instance of Director.
        """
        for word in self._words:
            if word.get_text() == self._buffer.get_content():
                self._score.add_points(word.get_points())
                word.reset()
                self._buffer.clear_buffer()
            else:
                word.move_next()
                if not word.get_position().isInsideBox(Point(0,0), constants.MAX_X, constants.MAX_Y):
                    word.set_velocity(word.get_velocity().reverse())
        
    def _do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means printing out the HUD and Actors to the screen.

        Args:
            self (Director): An instance of Director.
        """
        self._output_service.clear_screen()
        for word in self._words:
            self._output_service.draw_actor(word)
        self._output_service.draw_actor(self._score)
        self._output_service.draw_actor(self._buffer)
        self._output_service.flush_buffer()

    def _add_word(self):
        """Adds a word to the _words array.

        Args:
            self (Director): An instance of Director.
        """
        self._words.append(Word())