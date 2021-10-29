import random
from game.actor import Actor
from game.point import Point

class word:
    
    def __init__(self):
        with open('words.txt') as words:
            words = open('words.txt', 'r')
            list_of_words = words.readlines()
            words.close()
        super().__init__()
        new_word = random.choice(list_of_words)
        self._points = 0
        self.set_text(new_word)
        self.reset()
    
    def get_points(self):
        return self._points

    def reset(self):
        num_words = random.randint(1, 10)
        count =0
        while  count != num_words:
            self._points = random.randint(1,5)
            x = random.randint(1, 20 -2)
            y = random.randint(1, 20, -2)
            position = Point(x,y)
            self.set_position(position)