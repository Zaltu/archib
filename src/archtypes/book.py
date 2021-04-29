"""
Base class for Book type representation.
"""
from src.archtypes.path import Path

_REQUIRED = ["type", "author", "title", "genre", "year", "adult"]

class Book(Archive):
    """
    Archtype for Book archiving.
    """
    def __init__(self, config):
        super(config)
        bookconfig = config["data"]
        Archive.validate(bookconfig, _REQUIRED)
        self.type = bookconfig["type"]
        self.author = bookconfig["author"]
        self.title = bookconfig["title"]
        self.genre = bookconfig["genre"]
        self.year = bookconfig["year"]
        self.adult = bookconfig["adult"]
        self.illus = bookconfig.get("illus") or None
        self.id = bookconfig.get("id") or None
