#!/usr/bin/python3
"""
Module providing a method to lookup object attributes and methods.
"""

def lookup(obj):
    """
    Looks up object attributes and methods.

    Args:
        obj (object): The object to inspect.

    Returns:
        list: The list of attributes and methods.
    """
    return dir(obj)
