import random
from game.actor import Actor
from game.point import Point
from game import constants

class Word(Actor):
    
    def __init__(self):
        super().__init__()
        self._points = 0
        self.reset()
    
    def get_points(self):
        return self._points

    def reset(self):
        self._points = random.randint(1,5)
        x = random.randint(1, constants.MAX_X)
        y = random.randint(2, constants.MAX_Y - 1)
        position = Point(x, y)
        self.set_position(position)
        self.set_text(random.choice(constants.LIBRARY))
        self.set_velocity(Point(random.randint(-2, 2),random.randint(-2, 2)))