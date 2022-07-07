#!/usr/bin/python3
"""8-rectangle: class Rectangle from BaseGeomerty"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle inerits from BaseGeometry"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.integer_validator("height", height)
        self.integer_validator("height", height)
