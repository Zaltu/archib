"""
Base class for ImageSet type representation.
"""
from src.archtypes.path import Archive

_REQUIRED = ["type", "subject", "title", "filetype", "adult"]

class Game(Archive):
    """
    Archtype for ImageSet archiving.
    """
    def __init__(self, config):
        super()__init__(config)
        imageconfig = config["data"]
        Archive.validate(imageconfig, _REQUIRED)
        self.imagetype = imageconfig["type"]
        self.subject = imageconfig["subject"]
        self.title = imageconfig["title"]
        self.filetype = imageconfig["filetype"]
        self.adult = imageconfig["adult"]
