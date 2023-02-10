from pathlib import Path
from time import time, sleep

import pyglet

from fps_counter import FPSCounter


class GameWindow(pyglet.window.Window):

    def __init__(self, recording = False, throttle_fps = 30 ):
        super().__init__(vsync = False)

        self.recording = recording
        if self.recording:
            self.out_directory = Path(__file__).parent / 'rec'
            if self.out_directory.exists():
                self.out_directory.rmdir()
            self.out_directory.mkdir()

        self.throttle_fps = throttle_fps

        self.alive = True
        self.pause = False
        self.frame_count = 0
        self.last_update = time()
        self.fps_counter = FPSCounter()
        self.init()

        pyglet.graphics.get_default_shader()

    def on_close(self):
        self.alive = False

    def run(self):
        while self.alive:
            self.dispatch_events()

            if self.pause:
                continue

            now = time()
            dt = now - self.last_update
            self.last_update = now

            if self.throttle_fps:
                sleep_time = ( 1 / self.throttle_fps ) - dt
                sleep( max( sleep_time, 0 ) )

            # TODO:
            # we do not want the framerate to affect physics
            # easiest way to do that is fix the dt here for now
            dt = 1/60

            self._update(dt)
            self.update(dt)

            self._draw_start()
            self.draw()
            self._draw_end()



    def _update( self, dt ):
        self.fps_counter.update()

    def _draw_start( self ):
        self.clear()

    def _draw_end( self ):
        self.fps_counter.draw()
        self.flip()
        self.frame_count += 1
        if self.recording :
            pyglet.image.get_buffer_manager().get_color_buffer().save( f'{self.out_directory}/frame_{self.frame_count}.png' )

    # ================ End of standard boilerplate ================
    # ================ Overload the methods below! ================

    def init( self ):
        pass

    def update( self, dt ):
        pass

    def draw( self ):
        pass