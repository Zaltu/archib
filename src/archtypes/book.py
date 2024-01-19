"""
Base class for Book type representation.
"""
from src.archtypes.path import Archive

_REQUIRED = ["type", "author", "title", "genre", "year", "adult"]

BOOKENUMS = {
    "type": ["Artbook", "Comic", "Doujinshi", "Manga", "Novel", "Magazine"]
}

class Book(Archive):
    """
    Archtype for Book archiving.
    """
    def __init__(self, config):
        super().__init__(config)
        bookconfig = config["data"]
        Archive.validate(bookconfig, _REQUIRED, BOOKENUMS)
        self.book_type = bookconfig["type"]
        self.author = bookconfig["author"]
        self.title = bookconfig["title"]
        self.genres = bookconfig["genre"]
        self.year = bookconfig["year"]
        self.adult = bookconfig["adult"]
        self.illus = bookconfig.get("illus") or None
        self.product_id = bookconfig.get("id") or None
        self.live_media = bookconfig.get("livemedia") or False
