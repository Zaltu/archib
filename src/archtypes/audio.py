"""
Base class for Audio type representation.
"""
from src.archtypes.path import Path

_REQUIRED = ["type", "artist", "title", "adult"]

class Audio(Archive):
    """
    Archtype for Audio archiving.
    """
    def __init__(self, config):
        super(config)
        audioconfig = config["data"]
        Archive.validate(audioconfig, _REQUIRED)
        self.type = audioconfig["type"]
        self.artist = audioconfig["artist"]
        self.title = audioconfig["title"]
        self.adult = audioconfig["adult"]
        self.publisher = audioconfig.get("publisher")
        self.id = audioconfig.get("id")
        self.drm = audioconfig.get("DRM")
        self.url = audioconfig.get("url")
