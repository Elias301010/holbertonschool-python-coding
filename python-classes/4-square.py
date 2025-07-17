#!/usr/bin/python3
"""This module defines a Square class that can compute area and
print itself using '#' characters.
"""


class Square:
    """Defines a square with size validation and printable output."""

    def __init__(self, size=0):
        """Initialize the square with an optional size."""
        self.size = size  # Uses the setter for validation

    @property
    def size(self):
        """Get the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square using '#' characters. If size is 0, print an empty line."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
