from typing import Optional
from game_window import GameWindow
from pyglet.gl import glClearColor


_GAME : Optional[ GameWindow ] = None


def init( game_window : GameWindow ):
    global _GAME
    _GAME = game_window

    glClearColor( 255/255, 10/255, 10/255, 1.0 )  # red, green, blue, and alpha(transparency)


def update( dt ):
    ...

def draw():
    ...