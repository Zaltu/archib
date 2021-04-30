import os
import sys
import glob

from src import archiver
from src.consts import ARCHIVE_FILENAME, SkipError

def _checkrecusriveconfig(path, top=True):
    """
    Recursively go through a filetree and make sure that metis.archive exists only at the top level.

    :param str path: filepath to start with
    :param bool top: whether this is the start, where the archive file can exist

    :return: True if the filetree from this point is valid. Kills the program otherwise.
    :rtype: bool
    """
    paths = glob.glob(os.path.join(path, "*"))
    foundConfig = False
    for checking in paths:
        if os.path.isdir(checking):
            _checkrecusriveconfig(checking, False)
        elif os.path.basename(checking) == ARCHIVE_FILENAME and not top:
            print(f"ERROR: Config file found deeper than expected. Aborting all operations.\n{checking}")
            sys.exit(1)
        elif os.path.basename(checking) == ARCHIVE_FILENAME and top:
            foundConfig = True
    if not foundConfig and top:
        print("ERROR: No config file found for this archive. Expecting\n%s" % os.path.join(path, ARCHIVE_FILENAME))
        sys.exit(1)


def _getarchives(path):
    """
    Check all the folders at the path. They should all be archives.

    :return: individual folders to archive
    :rtype: list[str]
    """
    tocheck = glob.glob(os.path.join(path, "*"))
    checked = []
    for checking in tocheck:
        if os.path.isfile(checking):
            print(f"ERROR: Directory should be clear of any superfluous files for maximum sanitation. Found\n{checking}")
            sys.exit(1)
        elif os.path.isdir(checking):
            _checkrecusriveconfig(checking)
            print(f"Found archive folder\n{checking}\n")
            checked.append(checking)
        else:
            print(f"ERROR: Unknown bit tag that the OS does not recognize as a file or folder. Terminating.")
            sys.exit(1)
    return checked


def _getpath():
    """
    Get the path from the parameters.
    Halts execution if path is invalid or there are too many arguments.

    :returns: top path to archive
    :rtype: str
    """
    if len(sys.argv) != 2:
        print(f"ERROR: Too many arguments given. Only one taken.\n{sys.argv[1:]}")
        sys.exit(1)
    path = os.path.abspath(sys.argv[1])
    if not os.path.exists(path):
        print(f"ERROR: Path provided cannot be found. Halting.\n{path}")
        sys.exit(1)
    return path


def archive():
    """
    Attempt to archive all datasets at the given location.
    - Validate parameter
    - Validate directory
    - Validate archives
    - Process archives
    This program will forcibly exit if it detects incorrectly configured paths to avoid errors.
    """
    path = _getpath()
    print(f"Beginning archive from\n{path}\n")

    print("Checking directory contents...")
    archives = _getarchives(path)
    
    for archive in archives:
        try:
            archiver.processarchive(archive)
            print(f"Archive processed successfully. It can be safely remove from the staging area.\n{archive}\n")
        except SkipError:
            print(f"ERROR: A fatal error has occured while processing an archive. It has been skipped.\n{archive}\n")


if __name__ == "__main__":
    archive()
