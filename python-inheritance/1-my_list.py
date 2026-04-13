#!/usr/bin/python3
"""MyList module"""


class MyList(list):
    """Custom list class"""

    def print_sorted(self):
        """Prints sorted list"""
        print(sorted(self))
