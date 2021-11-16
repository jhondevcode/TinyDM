"""
This module is specially designed to configure and start the event logger.

The wind recorder will be used throughout the program to capture exceptions in a
detailed way in plain text files so that they can later be analyzed in detail.

Internally, the registers module that is included with the python SDK is used,
with which this module reuses that register by preconfiguring it for immediate use.
"""

import logging

from datetime import datetime
from os import mkdir
from os.path import isdir, join
from src.homedir import get_home_path

__logger__ = None
log_dir = join(get_home_path(), "logs")
log_file_name = f"log-{datetime.now().date()}.log"
log_file_path = join(log_dir, log_file_name)


def __create_log_dir__():
    """
        This function specializes in creating the directory of the records in case of not existing.
    """
    if not isdir(log_dir):
        mkdir(log_dir)


def __initialize_logger__():
    """
        This function is in charge of initializing the event logger.

        filemode:
            a: append   Add the content below the last line of the log file
            w: write    Completely overwrite the log file
    """
    print("Initializing new logger")
    global __logger__
    __create_log_dir__()
    format_style = "%(asctime)s [%(threadName)s] %(name)-5s %(levelname)-8s: %(message)s"
    logging.basicConfig(filename=log_file_path, datefmt="%H:%M:%S", format=format_style, filemode="w")
    __logger__ = logging.getLogger()
    __logger__.setLevel(logging.DEBUG)
    return __logger__


def get_logger():
    """
        This function returns the initialized and preconfigured instance of the event logger.
    """
    if __logger__ is None:
        return __initialize_logger__()
    return __logger__
