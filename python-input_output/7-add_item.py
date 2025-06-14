#!/usr/bin/python3
""" Script that adds command-line arguments to a list and saves them in a JSON file"""


from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


try:
    new_list = load_from_json_file("add_item.json")
except FileNotFoundError:
    new_list = list()

new_list.extend(argv[1:])

save_to_json_file(new_list, "add_item.json")
