"""
Base class for Audio type representation.
"""
from src.archtypes.path import Archive

_REQUIRED = ["type", "artist", "title", "adult"]

class Audio(Archive):
    """
    Archtype for Audio archiving.
    """
    def __init__(self, config):
        super().__init__(config)
        audioconfig = config["data"]
        Archive.validate(audioconfig, _REQUIRED)
        self.audiotype = audioconfig["type"]
        self.artist = audioconfig["artist"]
        self.title = audioconfig["title"]
        self.adult = audioconfig["adult"]
        self.publisher = audioconfig.get("publisher") or None
        self.id = audioconfig.get("id") or None
        self.drm = audioconfig.get("DRM") or None
        self.url = audioconfig.get("url") or None
