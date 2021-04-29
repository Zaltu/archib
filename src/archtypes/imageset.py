"""
Base class for ImageSet type representation.
"""
from src.archtypes.path import Path

_REQUIRED = ["type", "subject", "title", "filetype", "adult"]

class Game(Archive):
    """
    Archtype for ImageSet archiving.
    """
    def __init__(self, config):
        super(config)
        imageconfig = config["data"]
        Archive.validate(imageconfig, _REQUIRED)
        self.type = imageconfig["type"]
        self.subject = imageconfig["subject"]
        self.title = imageconfig["title"]
        self.filetype = imageconfig["filetype"]
        self.adult = imageconfig["adult"]
