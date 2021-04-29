"""
Base class for Software type representation.
"""
from src.archtypes.path import Path

_REQUIRED = ["developer", "title", "type", "version"]

class Software(Archive):
    """
    Archtype for software archiving.
    """
    def __init__(self, config):
        super(config)
        softconfig = config["data"]
        Archive.validate(softconfig, _REQUIRED)
        self.developer = softconfig["developer"]
        self.title = softconfig["title"]
        self.type = softconfig["type"]
        self.version = softconfig["version"]
        self.format = softconfig.get("format")
        self.drm = softconfig.get("DRM")
        self.url = softconfig.get("url")
