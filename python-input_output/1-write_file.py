#!/usr/bin/python3
"""the module"""


def write_file(filename="", text=""):
    """ Write to a file, and return length of characters """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
        return f.write(text)
