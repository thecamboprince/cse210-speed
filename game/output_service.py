import sys
from asciimatics.widgets import Frame

class OutputService:

    def __init__(self,screen):
        self._screen = screen

    def clear_screen(self):
        self._screen.clear_buffer(7,0,0)
        self._screen.print_at("-"* 60, 0, 0, 7)
        self._screen.print_at("-"* 60, 0, 20, 7)
    
    def draw_actor(self,actor):
        text = actor.get_text()
        position = actor.get_position()
        x = position.get_x()
        y = position.get_y()
        self._screen.print_at(text, x, y, 7)

    def draw_actors(self, actors):
        for actor in actors:
            self.draw_actor(actor)

    def flush_buffer(self):
        self._screen.refresh()