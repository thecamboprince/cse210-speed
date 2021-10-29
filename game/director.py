from time import sleep
from game import constants
from game.score import Score
from game import buffer
from game.word import Word

class Director:
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
        word (Word): gets words
    """

    def __init__(self, input_service, output_service):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self._input_service = input_service
        self._keep_playing = True
        self._output_service = output_service
        self._score = Score()
        self._buffer = buffer()
        self._word = word()
        
    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._keep_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
            self._add_word()
            sleep(constants.FRAME_LENGTH)

    def _get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means getting the input of the words.

        Args:
            self (Director): An instance of Director.
        """
        direction = self._input_service.get_key()
        if direction == 10:
            for word in words:
                if word.text == self._buffer.get_content():
                    self._score.add_points(points)
                    word.reset()
                    
        
    def _do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means checking if there are stones left and declaring 
        the winner.

        Args:
            self (Director): An instance of Director.
        """
        self._output_service.clear_screen()
        self._output_service.draw_actor(self._score)
        self._output_service.flush_buffer()
        self._output_service._get_word()

    
    def _check_for_correct_word(self):
        """Handles collisions between the snake's head and body. Stops the game 
        if there is one.
        Args:
            self (Director): An instance of Director.
        """
        for word in self._get_words():
            if word.get_word() == self._buffer.get_text():
                self._score.add_points(30)
                self._remove_word(word)
                self._create_new_word()
                self._buffer.clear_letters()
        

    def _kill_words(self):
        """Handles collisions between the snake's head and the food. Grows the 
        snake, updates the score and moves the food if there is one.
        Args:
            self (Director): An instance of Director.
        """
        for word in self._get_words():
            word_position = word.get_position()
            y = word_position.get_y()
            if y == constants.MAX_Y - 1:
                self._remove_word(word)
                self._score.add_points(-5)
                self._create_new_word()

    def _create_new_word(self):
        self._add_word(Word("doubt"))
        return
        with open("game/words.txt", "r") as f:
            word_list = f.readlines()
        self._add_word(Word(choice(word_list)))