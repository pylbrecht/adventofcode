#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Advent of Code - Day 4
======================

The Ideal Stocking Stuffer
"""

__author__ = "pylbrecht"
__contact__ = "pylbrecht@gmail.com"


import hashlib


def get_hash(data, algorithm="md5"):
    """
    Compute the hash of a byte string and return its value as a hex string.
    """
    h = hashlib.new(algorithm)
    h.update(data)
    return h.hexdigest()


if __name__ == '__main__':
    secret_key = "yzbqklnj"
    number = 0

    data = "{}{}".format(secret_key, number)

    checksum = get_hash(data.encode('utf-8'))

    while not checksum.startswith("00000"):
        number += 1
        data = "{}{}".format(secret_key, number)
        checksum = get_hash(data.encode('utf-8'))

    print("five zeroes: %d" % number)

    while not checksum.startswith("000000"):
        number += 1
        data = "{}{}".format(secret_key, number)
        checksum = get_hash(data.encode('utf-8'))

    print("six zeroes: %d" % number)
