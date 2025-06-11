#!/usr/bin/python3
""" the module"""


def append_write(filename="", text=""):
    """ Append to a file, and return length of characters """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
