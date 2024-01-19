"""
Collection of archiver constants.
"""
ARCHIVE_FILENAME = "metis.archive"
ARCHIVE_FILETYPES = ["zip", "tar", "rar", "7z", "iso", "exe", "gz"]

class SkipError(Exception):
    """
    An error occured, but continue processing other archives.
    """

class ConfigError(SkipError):
    """
    There is a missing required field for this config...
    """
