"""
author: Ofri Guz
Date: 13/09/24
description: Defines a Shape class that represents a general shape, allowing for setting and retrieving the color, as
well as providing default methods for calculating area and perimeter
"""


class Shape:
    """
    A class to represent a generic geometric shape
    """
    def __init__(self, color1=None):
        """
        Constructs a new Shape instance with a specified color
        :param color1: The color of the shape. Defaults to None
        """
        self.color = color1

    def set_color(self, color):
        """
        Sets the color of the shape
        :param color : (str) the color of the shape
        """
        self.color = color

    def get_color(self):
        """
        retrieves the color of the shape
        :return: (str) the color of the shape
        """
        return self.color

    def get_area(self):
        """
        Computes the area of the shape
        :return: (int) The area of the shape (default is 0 for the base Shape class).
        """
        return 0

    def get_perimeter(self):
        """
        Computes the perimeter of the shape
        :return: (int) The perimeter of the shape (default is 0 for the base Shape class)
        """
        return 0


if __name__ == '__main__':
    # Asserts:
    # Create a shape object with color "red"
    shape = Shape("red")
    assert shape.get_color() == "red", "Color should be 'red'"
    assert shape.get_area() == 0, "Area should be 0 for the base Shape class"
    assert shape.get_perimeter() == 0, "Perimeter should be 0 for the base Shape class"

    # Change the color of the shape
    shape.set_color("blue")
    assert shape.get_color() == "blue", "Color should now be 'blue'"

    # Test a shape without a color
    shape_with_no_color = Shape()
    assert shape_with_no_color.get_color() is None, "Color should be None by default"
