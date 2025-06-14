#!/usr/bin/python3
"""Module to load object from a JSON file"""


import json


def load_from_json_file(filename):
    """Load an object from a JSON file"""

    with open(filename, 'r') as f:
        return json.load(f)
