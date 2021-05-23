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
        raise SkipError("ERROR: Unrecognised or missing archive type: %s" % archiveconfig["type"])
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
        raise SkipError(f"ERROR: Config file we *just* confirm existed appears to have moved. Expecting\n{configpath}")
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


def _validatedestination(config):
    """
    Validate if the target directory exists, and whether this file has already been archived.

    :param dict config: this archive's config

    :raises SkipError: if the target directory doesn't exist, or the data has already been archived.
    """
    # If the directory where we intend to put the archive doesn't exist, it should be created manually.
    if not os.path.exists(os.path.dirname(config["path"])):
        raise SkipError("ERROR: Destination path does not exist\n%s" % os.path.dirname(config["path"]))

    # If the full destination path already exists, this dataset has already been archived.
    if os.path.exists(config["path"]):
        raise SkipError("ERROR: Archive appears to already exist:\n%s" % config["path"])


def _finalizeandupload(compressedlocation, config, archiveobj):
    """
    Validate compressed file, move to expected location, and update DB.

    :param str compressedlocation: expected location to the compressed file to archive
    :param dict config: this archive's config
    :param Archive archiveobj: validated archive object for DB update

    :raises SkipError: if compressed file cannot be found, or cannot be moved
    """
    # If the compressed file does not exist, we have a problem...
    if not os.path.exists(compressedlocation):
        raise SkipError("ERROR: Compression has not generated the expected file. Could not find:\n%s" % compressedlocation)

    # Move compressed files to location
    try:
        _movefile(compressedlocation, config["path"])
    except:
        raise SkipError("ERROR: Unable to move compressed file... Manual intervention required.")

    # Update DB
    dbupdater.insertarchive(archiveobj)


def processonearchive(archive, config):
    """
    Archive the folder to the correct location, and update the DB with the information on this dataset.

    :param str archive: path to the archive top dir
    :param dict config: the loaded archive config

    :raises SkipError: in a lot of places
    """
    # Create the archive-type object, which will validate the config.
    archiveobj = makearchive(config)

    # Validate check for destination path and existing archive
    _validatedestination(config)

    compressedlocation = detectcompressed(archive)
    if not compressedlocation:
        # Get the name of the archive file to store
        try:
            archivename = os.path.basename(config["path"]).split(".")[0]
        except:
            raise SkipError("ERROR: Cannot determine intended archive name from config:\n%s" % config["path"])

        # Compress folder
        _compress(archive, archivename)
        compressedlocation = os.path.join(os.path.dirname(archive), os.path.basename(config["path"]))

    # Validate compressed file, move to archive location, and update DB
    _finalizeandupload(compressedlocation, config, archiveobj)


def processarchiveset(archivepath, config):
    """
    Process an archive that was defined in a multi archive set. Multiple aspects of the validation logic are
    different in this situation, so the whole thing is separated.

    :param str archivepath: path to the compressed file or single directory of this archive.
    :param dict config: the config for this particular archive
    """
    # Create the archive-type object, which will validate the config.
    archiveobj = makearchive(config)

    # Validate check for destination path and existing archive
    _validatedestination(config)

    if os.path.isdir(archivepath):
        # Get the name of the archive file to store
        try:
            archivename = os.path.basename(config["path"]).split(".")[0]
        except:
            raise SkipError("ERROR: Cannot determine intended archive name from config:\n%s" % config["path"])
        # Compress folder
        _compress(archivepath, archivename)
        compressedlocation = os.path.join(os.path.dirname(archivepath), os.path.basename(config["path"]))
    elif archivepath.split(".")[-1] in ARCHIVE_FILETYPES:
        compressedlocation = archivepath
    else:
        raise SkipError("Multi-Archive Sets expect pre-compressed files, or folders. Received:\n%s" % archivepath)

    # Validate compressed file, move to archive location, and update DB
    _finalizeandupload(compressedlocation, config, archiveobj)


def processarchive(directory):
    """
    Process a folder, which may have multiple archives prepared in it.

    :param str directory: path to the directory which contains the archive(s)
    """
    # Read config
    config = readconfig(directory)

    if "type" in config and config["type"] in TYPEMAP:
        processonearchive(directory, config)
    else:
        for archive in config:
            processarchiveset(archive, config[archive])
