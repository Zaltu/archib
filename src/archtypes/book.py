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
        self.booktype = bookconfig["type"]
        self.author = bookconfig["author"]
        self.title = bookconfig["title"]
        self.genre = bookconfig["genre"]
        self.year = bookconfig["year"]
        self.adult = bookconfig["adult"]
        self.illus = bookconfig.get("illus") or None
        self.id = bookconfig.get("id") or None
        self.livemedia = bookconfig.get("livemedia") or False
