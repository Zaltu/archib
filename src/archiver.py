"""
All utilities related to actually archiving a set of data.
"""
import os
import json
import glob
import shutil

from src.archtypes import TYPEMAP
from src.consts import ARCHIVE_FILENAME, ARCHIVE_FILETYPES, SkipError
from src.db import dbupdater


def detectcompressed(archivepath):
    """
    Checks whether the requested archivation data is already compressed.

    :param str archivepath: the path to the archive detected by the initial scan.

    :return: the path to an existing set of compressed data, or False
    :rtype: str|bool
    """
    filesthere = glob.glob(os.path.join(archivepath, "*"))
    if len(filesthere) > 2:  # There needs to be only one archive and one config in this case...
        return False
    filesthere.remove(os.path.join(archivepath, ARCHIVE_FILENAME))
    if len(filesthere) == 2:  # This would mean there's no config...
        return False
    if len(filesthere) == 0:  # This would mean there was only a config in the folder...
        raise SkipError(f"ERROR: No files to archive found at path:\n{archivepath}")
    if filesthere[0].split(".")[-1] not in ARCHIVE_FILETYPES:  # Not a valid compressed file. Maybe an exe or a single image or something...
        return False
    return filesthere[0]


def makearchive(archiveconfig):
    """
    Transform the config into a python type, which will validate it.

    :param dict archiveconfig: the archive config read from disk

    :raises SkipError: if the archive type in the config is not valid, or is missing

    :return: the python archive subclass of this archive
    :rtype: Archive
    """
    if not archiveconfig["type"] or archiveconfig["type"] not in TYPEMAP:
        print("ERROR: Unrecognised or missing archive type: %s" % archiveconfig["type"])
        raise SkipError()
    return TYPEMAP[archiveconfig["type"]](archiveconfig)


def readconfig(archive):
    """
    Load the config file.

    :param str archive: path to archive dir.

    :raises SkipError: if config file cannot be found

    :return: archive config
    :rtype: dict
    """
    configpath = os.path.join(archive, ARCHIVE_FILENAME)
    try:
        with open(configpath, 'r') as configfile:
            config = json.load(configfile)
    except FileNotFoundError:
        print(f"ERROR: Config file we *just* confirm existed appears to have moved. Expecting\n{configpath}")
        raise SkipError()
    return config


def _compress(archive, archivename):
    """
    Compress the archive to a single tarball.

    :param str archive: archive path
    :param str archivename: name of the archive file
    """
    shutil.make_archive(os.path.join(os.path.dirname(archive), archivename), "tar", os.path.dirname(archive), os.path.basename(archive))


def _movefile(source, destination):
    """
    Move the compressed archive from the local location to the expected destination.
    Primary source of failure...

    :param str source: path to compressed archive to move
    :param str destination: path to moveto destination
    """
    shutil.move(source, destination)


def processarchive(archive):
    """
    Archive the folder to the correct location, and update the DB with the information on this dataset.

    :param str archive: path to the archive top dir

    :raises SkipError: in a lot of places
    """
    # Read config
    config = readconfig(archive)

    # Create the archive-type object, which will validate the config.
    archiveobj = makearchive(config)

    # If the directory where we intend to put the archive doesn't exist, it should be created manually.
    if not os.path.exists(os.path.dirname(config["path"])):
        print("ERROR: Destination path does not exist\n%s" % os.path.dirname(config["path"]))
        raise SkipError()

    # If the full destination path already exists, this dataset has already been archived.
    if os.path.exists(config["path"]):
        print("ERROR: Archive appears to already exist:\n%s" % config["path"])
        raise SkipError()

    compressedlocation = detectcompressed(archive)
    if not compressedlocation:
        # Get the name of the archive file to store
        try:
            archivename = os.path.basename(config["path"]).split(".")[0]
        except:
            print("ERROR: Cannot determine intended archive name from config:\n%s" % config["path"])
            raise SkipError()

        # Compress folder
        _compress(archive, archivename)
        compressedlocation = os.path.join(os.path.dirname(archive), os.path.basename(config["path"]))

    # If the compressed file does not exist, we have a problem...
    if not os.path.exists(compressedlocation):
        print("ERROR: Compression has not generated the expected file. Skipping.")
        raise SkipError()

    # Move compressed files to location
    try:
        _movefile(compressedlocation, config["path"])
    except:
        print("ERROR: Unable to move compressed file... Manual intervention required.")
        raise SkipError()

    # Update DB
    dbupdater.insertarchive(archiveobj)
