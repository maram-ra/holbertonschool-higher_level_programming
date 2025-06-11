#!/usr/bin/python3
""" The module """


import json


def from_json_string(my_str):
    """  function that returns an object"""
    return json.loads(my_str)
