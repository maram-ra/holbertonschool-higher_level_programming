#!/usr/bin/python3
"""
Module containing class FlyingFish.
"""


class Fish:
    """
    A class to define a fish.
    """
    def swim(self):
        print("the fish is swimming")

    def habitat(self):
        print("The fish lives in water")

class Bird:
    """
    A class to define a bird.
    """
    def fly(self):
        print("The flying fish is soaring!")

    def habitat(self):
        print("The bird lives in the sky")

class FlyingFish(Fish, Bird):
    """
    A class to define a flying fish.
    """
