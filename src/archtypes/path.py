"""
Base class for archive type representation.
"""
from src.consts import ConfigError

# Archive is an abstract type. "data" isn't required here, but it is required for every real archive type.
_REQUIRED = ["path", "type", "displayname", "data"]

ARCHIVEENUMS = {
    "type": ["Audio", "Book", "Game", "ImageSet", "Software", "Video"]
}

class Archive():
    """
    Base class shared by all archive types.
    Holds only a few parameters essential to all types, which must all be set.
    """
    filepath = None
    archtype = None
    displayname = None
    def __init__(self, config):
        Archive.validate(config, _REQUIRED, ARCHIVEENUMS)
        self.filepath = config["path"]
        self.archtype = config["type"]
        self.displayname = config["displayname"]
        self.notes = config.get("notes")

    def parse(self):
        """
        Get all this object's properties.

        :return: iterator over *all* properties of this object
        :rtype: iterator[(key, value)]
        """
        for key, value in self.__dict__.items():
            yield key, value

    
    @staticmethod
    def validate(config, required, enums):
        """
        Validate an archive according to it's required keys.
        Should be called in the constructor.

        :param dict config: config to validate
        :param list[str] required: list of required keys
        :param dict enums: set of all fields that have a limited number of values {"field": ["values"]}

        :raises SkipError: if a key is missing. This archive can't be processed.
        """
        if not all(key in config and config[key] is not None for key in required):
            # Kind of ugly, but lets us be more user friendly
            missing = []
            for key in required:
                if not config.get(key):
                    missing.append(key)
            print(f"ERROR: Missing required key(s) in config file:\n{missing}")
            raise ConfigError()
        for enum in enums:
            if config.get(enum) and not config.get(enum) in enums[enum]:
                print(f"ERROR: value of {enum} should be restricted to {enums[enum]}, got {config[enum]}")
                raise ConfigError()
