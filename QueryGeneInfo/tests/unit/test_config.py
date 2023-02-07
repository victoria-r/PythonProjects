#!/usr/bin/env python3
# test_config.py

"""Test suite for config.py"""

import os
import pytest
from assignment5 import config

# ignore all "Missing function or method docstring" since this is a unit test
# pylint: disable=C0116
# ignore all "Function name "test_get_error_string_4_ValueError" doesn't conform to snake_case naming style"
# pylint: disable=C0103


def test_get_host_keywords():
    # does it get the host keywords and return them
    # test
    test = config.get_host_keywords()
    assert test.get("bos taurus") == "Bos_taurus"
    assert test.get("rats") == "Rattus_norvegicus"


def test_get_error_string_4_ValueError(capfd):
    # does it raise an error when invalid argument value is passed
    # test
    config.get_error_string_4_ValueError()
    out, err = capfd.readouterr()
    assert out == "Invalid argument Value for opening a file for reading or writing\n"


def test_get_error_string_4_TypeError(capfd):
    # does it raise an error when the wrong argument type is passed
    # test
    config.get_error_string_4_TypeError()
    out, err = capfd.readouterr()
    assert out == "Invalid argument Type passed in: \n"
