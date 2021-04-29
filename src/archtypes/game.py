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
        self.publisher = gameconfig.get("publisher") or None
        self.dlc = gameconfig.get("DLC") or None
        self.id = gameconfig.get("id") or None
        self.drm = gameconfig.get("DRM") or None
        self.url = gameconfig.get("url") or None
