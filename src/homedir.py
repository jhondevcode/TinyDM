"""
This module is designed to work on the home directory. It provides functions to
manipulate temporary directories and work with plain text files as well as binary.
"""

from os import mkdir
from os.path import isdir, join
from pathlib import Path
from shutil import rmtree
from src.log import get_logger as logger


__home_path__ = None
if __home_path__ is None:
    __home_path__ = join(Path.home(), ".tinyDM")


def get_home_path() -> str:
    """This function returns the path of the working directory"""
    if not isdir(__home_path__):
        mkdir(__home_path__)
    return __home_path__


def __prepare_temp_dir__() -> str:
    """This function creates the temporary directory and returns the path"""
    temp_dir = join(get_home_path(), "temp")
    if not isdir(temp_dir):
        mkdir(temp_dir)
    return temp_dir


def create_temp_dir(name: str) -> str:
    """
        This function is responsible for creating a temporary folder within
        the temporary directory and returning the path.
    """
    temp_parent = __prepare_temp_dir__()
    temp_child = join(temp_parent, name)
    if not isdir(temp_child):
        mkdir(temp_child)
    return temp_child


def clean_temp_dirs() -> bool:
    """This function deletes the entire temp folder"""
    try:
        temp_dir = join(get_home_path(), "temp")
        if isdir(temp_dir):
            rmtree(temp_dir)
        return True
    except Exception as ex:
        logger().error(ex)
        return False


def delete_temp_dir(dirname: str) -> bool:
    """This function removes a specific temporary directory"""
    try:
        temp_dir = join(join(get_home_path(), "temp"), dirname)
        if isdir(temp_dir):
            rmtree(temp_dir)
        return True
    except Exception as ex:
        logger().error(ex)
        return False
