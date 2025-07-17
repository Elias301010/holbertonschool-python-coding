#!/usr/bin/python3
"""This module defines a Square class for representing squares."""

class Square:
    """Defines a square."""

    def __init__(self, size=0):
        """Initialize a new square with optional size."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size
