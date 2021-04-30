"""
Base class for Video type representation.
"""
from src.archtypes.path import Archive

_REQUIRED = ["style", "type", "studio", "title", "genre", "year", "adult", "vr"]

VIDEOENUMS = {
    "style": ["Anime", "Cartoon", "CG", "Live-Action"],
    "type": ["Series", "Feature"]
}

class Video(Archive):
    """
    Archtype for video archiving.
    """
    def __init__(self, config):
        super().__init__(config)
        videoconfig = config["data"]
        Archive.validate(videoconfig, _REQUIRED, VIDEOENUMS)
        self.videostyle = videoconfig["style"]
        self.videotype = videoconfig["type"]
        self.studio = videoconfig["studio"]
        self.title = videoconfig["title"]
        self.genre = videoconfig["genre"]
        self.year = videoconfig["year"]
        self.adult = videoconfig["adult"]
        self.vr = videoconfig["vr"]
        self.id = videoconfig.get("id") or None
        self.url = videoconfig.get("url") or None
