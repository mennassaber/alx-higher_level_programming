#!/usr/bin/python3

"""Defines a Python class-to-JSON function."""


def class_to_json(obj):
    """Return the dictionary representation of a simple data structure.

    Args:
        obj: The object to be converted to a dictionary.

    Returns:
        dict: The dictionary representation of the input object.
    """
    return obj.__dict__
