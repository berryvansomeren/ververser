from enum import Enum, auto
import logging

from file_watcher import FileWatcher


class ReloadStatus(Enum):
    NOT_CHANGED = auto()
    RELOADED = auto()
    FAILED = auto()


class ReloadingAsset:

    def __init__(self, f_load_asset, file_path):
        self.f_load_asset = f_load_asset
        self.file_watcher = FileWatcher(file_path)

    def try_reload( self ) -> ReloadStatus:
        if not self.file_watcher.is_file_updated():
            self.reload_status = ReloadStatus.NOT_CHANGED
            return self.reload_status
        asset_path = self.file_watcher.file_path
        try:
            self.asset = self.f_load_asset( asset_path )
        except Exception as e :
            logging.error( f'Encountered an error during loading of asset from file "{asset_path}"' )
            logging.error( e )
            self.reload_status = ReloadStatus.FAILED
            return self.reload_status
        self.reload_status =  ReloadStatus.RELOADED
        return self.reload_status

    def get( self ):
        return self.asset