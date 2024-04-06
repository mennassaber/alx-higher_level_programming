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
        """Set the size of the square."""
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    
    def area(self):
        """Compute the area of the square."""
        return self.__size ** 2
    
    def __eq__(self, other):
        """Check if two squares are equal in area."""
        return self.area() == other.area()
    
    def __ne__(self, other):
        """Check if two squares are not equal in area."""
        return not self == other
    
    def __lt__(self, other):
        """Check if one square is smaller than the other in area."""
        return self.area() < other.area()
    
    def __le__(self, other):
        """Check if one square is smaller than or equal to the other in area."""
        return self.area() <= other.area()
    
    def __gt__(self, other):
        """Check if one square is greater than the other in area."""
        return self.area() > other.area()
    
    def __ge__(self, other):
        """Check if one square is greater than or equal to the other in area."""
        return self.area() >= other.area() 
