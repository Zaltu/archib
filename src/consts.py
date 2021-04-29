"""
Collection of archiver constants.
"""
ARCHIVE_FILENAME = "metis.archive"


class SkipError(Exception):
    """
    An error occured, but continue processing other archives.
    """

class ConfigError(SkipError):
    """
    There is a missing required field for this config...
    """