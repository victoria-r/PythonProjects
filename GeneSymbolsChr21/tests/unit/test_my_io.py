#!/usr/bin/env python3.9
# test_my_io.py

""" Test suite for my_io.py"""

import os
import pytest

from assignment4.my_io import get_fh

# ignore all "Missing function or method docstring" since this is a unit test
# pylint: disable=C0116
# ignore all "Function name "test_get_fh_4_OSError" doesn't conform to snake_case naming style"
# pylint: disable=C0103

FILE_2_TEST = "chr21_genes.txt"
FILE_2_TEST_INPUT = ""

def test_existing_get_fh_4_reading():
    # does it open a file for reading
    # test
    test = get_fh(FILE_2_TEST, "r")
    assert hasattr(test, "readline") is True, "Not able to open for reading"
    test.close()


def test_existing_get_fh_4_writing():
    # does it open a file for writing
    #test
    test = get_fh(file='test_file.txt', mode="w")
    assert hasattr(test, "write") is True, "Not able to open for writing"
    test.close()
    os.remove('test_file.txt')


def test_get_fh_4_OSError():
    # does it raise OSError 
    # this should exit
    with pytest.raises(OSError):
        get_fh("does_not_exist.txt", "r")


def test_get_fh_4_ValueError():
    # does it raise ValueError
    # this should exit
    with pytest.raises(ValueError):
        get_fh("does_not_exist.txt", "rrr")
