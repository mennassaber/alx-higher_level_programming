#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""
    
    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square.
        
        Args:
            size (int): The size of the new square (default 0).
            position (tuple): The position of the square (default (0, 0)).
        """
        self.size = size
        self.position = position
    
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
    
    @property
    def position(self):
        """Get or set the position of the square."""
        return self.__position
    
    @position.setter
    def position(self, value):
        """Set the position of the square.
        
        Args:
            value (tuple): The position to set.
        
        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
    
    def area(self):
        """Compute the area of the square."""
        return self.__size ** 2
    
    def my_print(self):
        """Print the square."""
        if self.__size == 0:
            print()
            return
        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size) 
