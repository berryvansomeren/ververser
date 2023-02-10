import logging

from hot_reloading.file_watcher import FileWatcher


class ReloadingAsset:

    def __init__(self, f_load_asset, file_path, backup = None ):
        self.f_load_asset = f_load_asset
        self.file_watcher = FileWatcher(file_path)
        self.backup_asset = backup
        self.reload()

    def reload( self ):
        if self.backup_asset:
            try:
                self.asset = self.f_load_asset( self.file_watcher.file_path )
            except Exception as e:
                logging.error(e)
                self.asset = self.backup_asset
        else:
            self.asset = self.f_load_asset( self.file_watcher.file_path )

    def update( self ):
        self._was_reloaded = False
        if self.file_watcher.is_updated():
            self.reload()
            self._was_reloaded = True

    def get( self ):
        return self.asset

    def was_reloaded( self ):
        return self._was_reloaded
