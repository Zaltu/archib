"""
Base class for Game type representation.
"""
from src.archtypes.path import Archive

_REQUIRED = ["developer", "title", "genre", "year", "adult"]

GAMEENUMS = {}

class Game(Archive):
    """
    Archtype for Game archiving.
    """
    def __init__(self, config):
        super().__init__(config)
        gameconfig = config["data"]
        Archive.validate(gameconfig, _REQUIRED, GAMEENUMS)
        self.developer = gameconfig["developer"]
        self.title = gameconfig["title"]
        self.genre = gameconfig["genre"]
        self.year = gameconfig["year"]
        self.adult = gameconfig["adult"]
        self.publisher = gameconfig.get("publisher") or None
        self.dlc = gameconfig.get("dlc") or None
        self.id = gameconfig.get("id") or None
        self.drm = gameconfig.get("drm") or None
        self.url = gameconfig.get("url") or None
        self.mod = gameconfig.get("mod") or None
