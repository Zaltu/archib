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
        self.video_style = videoconfig["style"]
        self.video_type = videoconfig["type"]
        self.studio = videoconfig["studio"]
        self.title = videoconfig["title"]
        self.genres = videoconfig["genre"]
        self.year = videoconfig["year"]
        self.adult = videoconfig["adult"]
        self.vr = videoconfig["vr"]
        self.product_id = videoconfig.get("id") or None
        self.url = videoconfig.get("url") or None
        self.live_media = videoconfig.get("livemedia") or False
