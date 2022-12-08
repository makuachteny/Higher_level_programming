#!/usr/bin/python3
"A module that defines a class named MyList"

class MyList(list):
    """ MyList attributes:
    attr1(print_sorted):
    prints sorted list
    """
    def print_sorted(self):
        """Prints the instance"""
        print(sorted(self))
