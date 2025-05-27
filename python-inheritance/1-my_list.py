#!/usr/bin/python3
""" MyList module """


class MyList(list):
    """ A subclass of list """

    def print_sorted(self):
        new_list = sorted(self)
        print(new_list)
        return new_list
