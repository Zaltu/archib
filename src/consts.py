"""
Collection of archiver constants.
"""
ARCHIVE_FILENAME = "metis.archive"

DB_TABLE_MAP = {
    "Game": "games",
    "Audio": "audio",
    "Video": "videos",
    "Book": "books",
    "Software": "software",
    "ImageSet": "imageset"
}


SQL_INSERT = """
INSERT INTO {table}({fieldstr})
VALUES(%s) RETURNING uid;
"""


class SkipError(Exception):
    """
    An error occured, but continue processing other archives.
    """

class ConfigError(SkipError):
    """
    There is a missing required field for this config...
    """