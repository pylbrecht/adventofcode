#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
"""

__author__ = "pylbrecht"
__contact__ = "pylbrecht@gmail.com"


from day4 import *


def test_get_md5_hash():
    """
    """
    data = b"test"
    assert get_hash(data) == "098f6bcd4621d373cade4e832627b4f6"
