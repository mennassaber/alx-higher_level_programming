#!/usr/bin/python3

"""Defines a JSON-to-object function."""
import json


def from_json_string(my_str):
    """Return the Python object representation of a JSON string.

    Args:
        my_str (str): The JSON string to be converted.

    Returns:
        obj: The Python object representation of the input JSON string.
    """
    return json.loads(my_str) 
