#!/usr/bin/python3
"""Define a class MagicClass."""


class MagicClass:
    """Represent a class that performs magic."""
    
    def __init__(self, radius=0):
        """Initialize a new MagicClass.
        
        Args:
            radius (int): The radius of the magic circle (default 0).
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius
    
    def area(self):
        """Compute the area of the magic circle."""
        return self.__radius ** 2 * math.pi
    
    def circumference(self):
        """Compute the circumference of the magic circle."""
        return 2 * math.pi * self.__radius 
