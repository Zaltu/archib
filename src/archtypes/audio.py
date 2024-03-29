"""
Base class for Audio type representation.
"""
from src.archtypes.path import Archive

_REQUIRED = ["type", "artist", "title", "adult"]

AUDIOENUMS = {
    "type": ["ASMR", "Audiobook", "Audio Roleplay", "Music"]
}

class Audio(Archive):
    """
    Archtype for Audio archiving.
    """
    def __init__(self, config):
        super().__init__(config)
        audioconfig = config["data"]
        Archive.validate(audioconfig, _REQUIRED, AUDIOENUMS)
        self.audio_type = audioconfig["type"]
        self.artist = audioconfig["artist"]
        self.title = audioconfig["title"]
        self.adult = audioconfig["adult"]
        self.publisher = audioconfig.get("publisher") or None
        self.product_id = audioconfig.get("id") or None
        self.storefront = audioconfig.get("storefront") or None
        self.url = audioconfig.get("url") or None
        self.live_media = audioconfig.get("livemedia") or False
