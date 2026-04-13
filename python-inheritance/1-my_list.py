#!/usr/bin/python3
"""MyList module"""


class MyList(list):
    """Custom list class that inherits from list"""

    def print_sorted(self):
        """Prints the list, but sorted (ascending sort)"""
        print(sorted(self))
