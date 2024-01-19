"""
Base class for ImageSet type representation.
"""
from src.archtypes.path import Archive

_REQUIRED = ["type", "title", "filetype", "adult"]

IMAGESETENUMS = {
    "type": ["2D", "CG", "Photo"]
}

class ImageSet(Archive):
    """
    Archtype for ImageSet archiving.
    """
    def __init__(self, config):
        super().__init__(config)
        imageconfig = config["data"]
        Archive.validate(imageconfig, _REQUIRED, IMAGESETENUMS)
        self.image_type = imageconfig["type"]
        self.artist = imageconfig["artist"]
        self.title = imageconfig["title"]
        self.file_type = imageconfig["filetype"]
        self.adult = imageconfig["adult"]
        self.moving = imageconfig.get("moving") or False
        self.live_media = imageconfig.get("livemedia") or False
