"""
author: Ofri Guz
Date: 13/09/24
description: Defines the Square class, a subclass of Shape. It calculates the area and perimeter of a square
"""

import Shape


class Square(Shape):
    """
    A class to represent a square, inheriting from the Shape class
    """
    def __init__(self, color, side):
        """
        Initializes a Square instance with a specified color, length, and width
        :param color: (str) the color of the square
        :param side: (float) The length of the sides
        """
        super().__init__(color)
        self.side = side

    def get_area(self):
        """
        Calculates the area of the square
        :return: (float) the area of the square
        """
        return self.side**2

    def get_perimeter(self):
        """
        Calculates the perimeter of the square
        :return: (float) the area of the square
        """
        return self.side*4


if __name__ == '__main__':
    # asserts
    # Create a square with color "yellow" and side 5
    square = Square("yellow", 5)
    assert square.get_color() == "yellow", "Color should be 'yellow'"
    assert square.side == 5, "Side length should be 5"
    assert square.get_area() == 25, "Area should be 25"
    assert square.get_perimeter() == 20, "Perimeter should be 20"

    # Create a square with color "purple" and side 10
    square2 = Square("purple", 10)
    assert square2.get_color() == "purple", "Color should be 'purple'"
    assert square2.side == 10, "Side length should be 10"
    assert square2.get_area() == 100, "Area should be 100"
    assert square2.get_perimeter() == 40, "Perimeter should be 40"

    # Test changing the color of the square
    square.set_color("orange")
    assert square.get_color() == "orange", "Color should now be 'orange'"
