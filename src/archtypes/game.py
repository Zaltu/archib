"""
Base class for Game type representation.
"""
from src.archtypes.path import Path

_REQUIRED = ["developer", "title", "genre", "year", "adult"]

class Game(Archive):
    """
    Archtype for Game archiving.
    """
    def __init__(self, config):
        super(config)
        gameconfig = config["data"]
        Archive.validate(gameconfig, _REQUIRED)
        self.developer = gameconfig["developer"]
        self.title = gameconfig["title"]
        self.genre = gameconfig["genre"]
        self.year = gameconfig["year"]
        self.adult = gameconfig["adult"]
        self.publisher = gameconfig.get("publisher")
        self.dlc = gameconfig.get("DLC")
        self.id = gameconfig.get("id")
        self.drm = gameconfig.get("DRM")
        self.url = gameconfig.get("url")
