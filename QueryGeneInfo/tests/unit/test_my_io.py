#!/usr/bin/env python3
# test_my_io.py

""" Test suite for my-io.py """

import os
import pytest
from assignment5.my_io import get_fh

# ignore all "Missing function or method docstring" since this is a unit test
# pylint: disable=C0116
# ignore all "Function name "test_get_fh_4_OSError" doesn't conform to snake_case_naming_style"
# pylint: disable=C0103

FILE_2_TEST = "test.txt"


def test_existing_get_fh_4_reading():
    # does it open a file for reading
    # create a test file
    _create_test_file(FILE_2_TEST) 
    # test
    test = get_fh(FILE_2_TEST, "r")
    assert hasattr(test, "readline") is True, "Not able to open for reading"
    test.close()
    os.remove(FILE_2_TEST)


def test_existing_get_fh_4_writing():
    # does it open a file for writing
    # test
    test = get_fh(file=FILE_2_TEST, mode="w")
    assert hasattr(test, "write") is True, "Not able to open for writing"
    test.close()
    os.remove(FILE_2_TEST)


def test_get_fh_4_OSError():
    # does it raise OSError
    # this should exit
    with pytest.raises(OSError):
        get_fh("does_not_exist.txt", "r")


def test_get_fh_4_ValueError():
    # does it raise ValueError
    # this should exit
    _create_test_file(FILE_2_TEST)
    with pytest.raises(ValueError):
        get_fh("does_not_exist.txt", "rrr")
    os.remove(FILE_2_TEST)


def test_get_fh_4_TypeError():
    # does it raise on TypeError
    # this should exit
    _create_test_file(FILE_2_TEST)
    with pytest.raises(TypeError):
        get_fh([], "r")
    os.remove(FILE_2_TEST)


def _create_test_file(file):
    # not actually run, just a helper function for the test script
    # create a test file
    open(file, "w").close()

