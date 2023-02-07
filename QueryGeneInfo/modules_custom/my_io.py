#!/usr/bin/env python3
# my_io.py

"""Submodule for gene_information_query.py"""

import os
from assignment5 import config


def get_fh(file=None, mode=None):
    """
    filehandle: get_fh(file, "r")
    Takes 2 arguments: file name and mode
    This function opens the file based on the mode passed in the argument
    and returns a filehandle.
    @param file: The file to open for the mode
    @param mode: The way to open the file ("r" or "w")
    @return: filehandle
    """
    try:
        handle = open(file, mode)
        return handle
    except OSError:
        config.get_error_string_4_opening_file_OSError(file, mode)
        raise
    except ValueError:
        config.get_error_string_4_ValueError()
        raise
    except TypeError:
        config.get_error_string_4_TypeError()
        raise


def is_valid_gene_file_name(file):
    """
    Takes 1 argument: file/directory to open
    Returns boolean if file/directory path exists or not
    """
    if os.path.exists(file):
       return True
    else:
       return False


