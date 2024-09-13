"""
author: Ofri Guz
Date: 13/09/24
description: Defines the Rect class, a subclass of Shape. It calculates the area and perimeter of a rectangle
"""

import Shape


class Rect(Shape):
    """
    A class to represent a rectangle, inheriting from the Shape class
    """
    def __init__(self, color, length, width):
        """
        Initializes a Rect instance with a specified color, length, and width
        :param color: (str) the color of the rectangle
        :param length: (float) The length of the rectangle
        :param width: (float) The width of the rectangle
        """
        super().__init__(color)
        self.length = length
        self.width = width

    def get_area(self):
        """
        Calculates the area of the rectangle
        :return: (float) the area of the rectangle
        """
        return self.length*self.width

    def get_perimeter(self):
        """
        Calculates the perimeter of the rectangle
        :return: (float) the perimeter of the rectangle
        """
        return self.length*2 + self.width*2


if __name__ == '__main__':
    # asserts
    # Create a rectangle with color "red", length 4, and width 6
    rect = Rect("red", 4, 6)
    assert rect.get_color() == "red", "Color should be 'red'"
    assert rect.length == 4, "Length should be 4"
    assert rect.width == 6, "Width should be 6"
    assert rect.get_area() == 24, "Area should be 24"
    assert rect.get_perimeter() == 20, "Perimeter should be 20"

    # Create a rectangle with color "blue", length 5, and width 7
    rect2 = Rect("blue", 5, 7)
    assert rect2.get_color() == "blue", "Color should be 'blue'"
    assert rect2.length == 5, "Length should be 5"
    assert rect2.width == 7, "Width should be 7"
    assert rect2.get_area() == 35, "Area should be 35"
    assert rect2.get_perimeter() == 24, "Perimeter should be 24"

    # Test changing the color of the rectangle
    rect.set_color("green")
    assert rect.get_color() == "green", "Color should now be 'green'"
