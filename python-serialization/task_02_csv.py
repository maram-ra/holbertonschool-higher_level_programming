""" The module """

import csv
import json

def convert_csv_to_json(filename):
    """ Convert csv to json and save to file """

    try:
        with open(filename, "r") as csv_file:
            data = list(csv.DictReader(csv_file))

        with open('data.json', "w") as json_file:
            json.dump(data, json_file)
        return True
    except:
        return False
