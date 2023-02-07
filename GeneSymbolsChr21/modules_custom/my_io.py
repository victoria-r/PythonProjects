#!/usr/bin/env python3.9
# my_io.py

def get_fh(file=None, mode=None):
    """
    filehandle: get_fh(infile, "r")
    Takes 2 arguments: file name and mode 
    This function opens the file based on the mode passed in the argument and returns a filehandle. 
    @param file: The file to open for the mode
    @param mode: The way to open the file ("r" or "w")
    @retuen: filehandle
    """

    try:
        handle = open(file, mode)
        return handle
    except OSError:
        print("OSError: Could not open the file.")
        raise
    except ValueError:
        print("ValueError: Could not open the file.")
        raise

