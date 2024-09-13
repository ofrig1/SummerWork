"""
author: Ofri Guz
Date: 13/09/24
description: Defines the Circle class, which is a subclass of Shape. It calculates
the area and perimeter of a circle
"""

from math import pi
import Shape


class Circle(Shape):
    """
    A class to represent a circle, inheriting from the Shape class
    """
    def __init__(self, color, radius):
        """
        Initializes a Circle instance with a specified color and radius
        :param color: (str) color of the circle
        :param radius: (float) the radius of the circle
        """
        super().__init__(color)
        self.radius = radius

    def get_area(self):
        """
        Calculates the area of the circle
        :return: (float) the area of the circle
        """
        return self.radius**2 * pi

    def get_perimeter(self):
        """
        Calculates the perimeter of the circle
        :return: (float)  the perimeter of the circle
        """
        return self.radius*2*pi


if __name__ == '__main__':
    # asserts
    # Create a circle with color "green" and radius 3
    circle = Circle("green", 3)
    assert circle.get_color() == "green", "Color should be 'green'"
    assert circle.radius == 3, "Radius should be 3"
    assert round(circle.get_area(), 2) == round(3 ** 2 * pi, 2), "Area should match the expected area"
    assert round(circle.get_perimeter(), 2) == round(2 * pi * 3, 2), "Perimeter should match the expected perimeter"

    # Create a circle with color "blue" and radius 5
    circle2 = Circle("blue", 5)
    assert circle2.get_color() == "blue", "Color should be 'blue'"
    assert circle2.radius == 5, "Radius should be 5"
    assert round(circle2.get_area(), 2) == round(5 ** 2 * pi, 2), "Area should match the expected area"
    assert round(circle2.get_perimeter(), 2) == round(2 * pi * 5, 2), "Perimeter should match the expected perimeter"

    # Test changing the color of the circle
    circle.set_color("yellow")
    assert circle.get_color() == "yellow", "Color should now be 'yellow'"
