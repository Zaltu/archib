"""
Base class for Video type representation.
"""
from src.archtypes.path import Archive

_REQUIRED = ["type", "studio", "title", "genre", "year", "adult"]

class Video(Archive):
    """
    Archtype for video archiving.
    """
    def __init__(self, config):
        super().__init__(config)
        videoconfig = config["data"]
        Archive.validate(videoconfig, _REQUIRED)
        self.videotype = videoconfig["type"]
        self.studio = videoconfig["studio"]
        self.title = videoconfig["title"]
        self.genre = videoconfig["genre"]
        self.year = videoconfig["year"]
        self.adult = videoconfig["adult"]
        self.id = videoconfig.get("id") or None
        self.url = videoconfig.get("url") or None
