#!/usr/bin/python3
"""the module"""



def read_file(filename=""):
    """opens the file and prints its content"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
