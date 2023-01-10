#!/usr/bin/python3
"""
MyList Class
"""


class MyList(list):
    """class MyList that inherits fro list"""

    def print_sorted(self):
        """prints the list, but sorted"""
        print(sorted(self))
