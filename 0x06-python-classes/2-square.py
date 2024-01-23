#!/usr/bin/python3
""" module that creates a class of Square """


class Square:
    """Square class with an attribute of size """
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
