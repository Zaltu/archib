"""
Base class for archive type representation.
"""
from src.consts import ConfigError

# Archive is an abstract type. "data" isn't required here, but it is required for every real archive type.
_REQUIRED = ["path", "type", "displayname", "data"]

class Archive():
    """
    Base class shared by all archive types.
    Holds only a few parameters essential to all types, which must all be set.
    """
    filepath = None
    archtype = None
    displayname = None
    def __init__(self, config):
        Archive.validate(config, _REQUIRED)
        self.filepath = config["path"]
        self.archtype = config["type"]
        self.displayname = config["displayname"]

    def parse(self):
        """
        Get all this object's properties.

        :return: iterator over *all* properties of this object
        :rtype: iterator[(key, value)]
        """
        for key, value in self.__dict__.items():
            yield key, value

    
    @staticmethod
    def validate(config, required):
        """
        Validate an archive according to it's required keys.
        Should be called in the constructor.

        :param dict config: config to validate
        :param list[str] required: list of required keys

        :raises SkipError: if a key is missing. This archive can't be processed.
        """
        if not all(key in config for key in required):
            # Kind of ugly, but lets us be more user friendly
            missing = []
            for key in required:
                if not config.get(key):
                    missing.append(key)
            print(f"ERROR: Missing required key(s) in config file:\n{missing}")
            raise ConfigError()