#!/usr/bin/env python3
# config.py

_UNIGENE_DIR = "/data/PROGRAMMING/assignment5"
_UNIGENE_FILE_ENDING = "unigene"


def get_unigene_directory():
    """
    Returns the variable _UNIGENE_DIR that will be found in
    assignment5.config.py
    Absolute path to the data on Defiance
    """
    return _UNIGENE_DIR


def get_unigene_extension():
    """
    Returns the variable _UNIGEN_FILE_ENDING that will be found in 
    assignment5.config.py
    Extension for the files that will be used 
    """
    return _UNIGENE_FILE_ENDING


def get_host_keywords():
    """
    Returns a dictionary of hosts (species) that will be found in 
    assignment5.config.py
    Maps common names with scientific names
    """
    bos_taurus = "Bos_taurus"
    homo_sapiens = "Homo_sapiens"
    equus_caballus = "Equus_caballus"
    mus_musculus = "Mus_musculus"
    ovis_aries = "Ovis_aries"
    rattus_norvegicus = "Rattus_norvegicus"

    host_keywords = {
            "bos_taurus" : bos_taurus,
            "Bos_taurus" : bos_taurus,
            "bos taurus" : bos_taurus,
            "cow" : bos_taurus,
            "cows" : bos_taurus,
            "homo_sapiens" : homo_sapiens,
            "Homo_sapiens" : homo_sapiens,
            "homo sapiens" : homo_sapiens,
            "human" : homo_sapiens,
            "humans" : homo_sapiens,
            "equus_caballus" : equus_caballus,
            "Equus_caballus" : equus_caballus,
            "equus caballus" : equus_caballus,
            "horse" : equus_caballus,
            "horses" : equus_caballus,
            "mus_musculus" : mus_musculus,
            "Mus_musculus" : mus_musculus,
            "mus musculus" : mus_musculus,
            "mouse" : mus_musculus,
            "mice" : mus_musculus,
            "ovis_aries" : ovis_aries,
            "Ovis_aries" : ovis_aries,
            "ovis aries" : ovis_aries,
            "sheep" : ovis_aries,
            "sheeps" : ovis_aries,
            "rattus_norvegicus" : rattus_norvegicus,
            "Rattus_norvegicus" : rattus_norvegicus,
            "rattus norvegicus" : rattus_norvegicus,
            "rat" : rattus_norvegicus,
            "rats" : rattus_norvegicus
    }
    return host_keywords


def get_error_string_4_ValueError():
    """
    Error when used get_fh(file, "1234")
    Print the invalid argument message for ValueError
    """
    print("Invalid argument Value for opening a file for reading or writing")


def get_error_string_4_TypeError():
    """
    Error when used get_fh(file, "r", "w")
    Print the invalid argument message for TypeError
    """
    print("Invalid argument Type passed in: ")


def get_error_string_4_FileNotFoundError(file=None):
    """
    Print the invalid argument message for FileNotFoundError
    Takes 1 argument: file name
    """
    print(f"Could not Could not find file {file}")



def get_error_string_4_opening_file_OSError(file=None, mode=None):
    """
    Takes 2 arguments: The file name and mode to open the file
    Print the invalid argument message for OSError
    """
    print(f"OSError: Could not open {file} with mode {mode}")

