#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""
    
    def __init__(self, size=0):
        """Initialize a new square.
        
        Args:
            size (int): The size of the new square (default 0).
        """
        self.size = size
    
    @property
    def size(self):
        """Get or set the size of the square."""
        return self.__size
    
    @size.setter
    def size(self, value):
        """Set the size of the square.
        
        Args:
            value (int): The size to set.
        
        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    
    def area(self):
        """Compute the area of the square."""
        return self.__size ** 2

