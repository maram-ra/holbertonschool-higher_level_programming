#!/usr/bin/python3
""" Module that returns the dictionary"""


def class_to_json(obj):
    """ Converts a class to a json object """

    return obj.__dict__
