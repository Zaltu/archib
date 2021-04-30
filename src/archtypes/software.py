"""
Base class for Software type representation.
"""
from src.archtypes.path import Archive

_REQUIRED = ["developer", "title", "type", "version"]

class Software(Archive):
    """
    Archtype for software archiving.
    """
    def __init__(self, config):
        super().__init__(config)
        softconfig = config["data"]
        Archive.validate(softconfig, _REQUIRED)
        self.developer = softconfig["developer"]
        self.title = softconfig["title"]
        self.softtype = softconfig["type"]
        self.version = softconfig["version"]
        self.format = softconfig.get("format") or None
        self.drm = softconfig.get("DRM") or None
        self.url = softconfig.get("url") or None
