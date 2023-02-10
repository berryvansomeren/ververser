import logging
from pathlib import Path
from time import time

from full_screen_shader.screen_shader import load_screen_shader
from game_window import GameWindow
from hot_reloading.reloading_asset import ReloadingAsset


class Window(GameWindow):

    def init( self ):
        repo_root = Path(__file__).parent
        logging.info('Loading backup shader')
        backup_screen_shader = load_screen_shader( f'{repo_root}/screen_shader_backup.frag', self.width, self.height )
        logging.info( 'Loading reloading screen shader' )
        self.reloading_screen_shader = ReloadingAsset(
            f_load_asset = lambda path : load_screen_shader( path, self.width, self.height ),
            file_path = f'{repo_root}/screen_shader.frag',
            backup = backup_screen_shader
        )
        self.time_start = time()

    def _uniform( self, name: str, v ):
        # uniforms are only set if available
        # uniforms that are declared but not used are optimized out
        # so they are not available then.
        # Check the log to see what uniforms and attributes are available
        shader = self.reloading_screen_shader.get().shader
        if name in shader.uniforms :
            shader[ name ] = v

    def update( self, dt ):
        self.reloading_screen_shader.update()
        if self.reloading_screen_shader.was_reloaded():
            self.time_start = time()

        self._uniform( 'u_resolution', ( self.width, self.height ) )
        self._uniform( 'u_time_total_elapsed_s', time() - self.time_start )
        self._uniform( 'u_time_delta_s', dt )
        self._uniform( 'u_frames_total', self.fps_counter.total_frames )
        self._uniform( 'u_frames_per_second', self.fps_counter.fps )

    def draw( self ):
        self.reloading_screen_shader.get().draw()


if __name__ == '__main__':
    logging.basicConfig( level = logging.INFO )
    window = Window()
    window.run()
