"""
author: Ofri Guz
Date: 13/09/24
description: This module defines the ShapeFactor class, responsible for generating random shapes
(Square, Rect, Circle), calculating their total areas and perimeters, and counting the frequency
of each shape color
"""

import random
import Shape
import Square
import Rect
import Circle

# Constants for available colors and shapes
COLOR_LIST = ["red", "green", "blue", "yellow", "black", "white"]
SHAPE_LIST = ["square", "rect", "circle"]


class ShapeFactor:
    """
    A class to generate random geometric shapes and perform calculations on them
    """
    def __init__(self):
        """
        Initializes the ShapeFactor with an empty list of shapes
        """
        self.num = 0
        self.shapes = []

    def generate(self, num):
        """
        Generates a specified number of random shapes (Rect, Square, Circle) with random colors
        and dimensions
        :param num: (int) The number of random shapes to generate
        """
        self.num = num
        for i in range(num):
            shape = Shape.Shape()
            shape_type = random.choice(SHAPE_LIST)
            color = random.choice(COLOR_LIST)
            if shape_type == "rect":
                length = random.uniform(1, 10)
                width = random.uniform(1, 10)
                shape = Rect.Rect(color, length, width)
            elif shape_type == "square":
                side = random.uniform(1, 10)
                shape = Square.Square(color, side)
            elif shape_type == "circle":
                radius = random.uniform(1, 10)
                shape = Circle.Circle(color, radius)
            self.shapes.append(shape)

    def sum_areas(self):
        """
        Calculates the total area of all the shapes
        :return: (float) The sum of the areas of all generated shapes
        """
        return sum([shape.get_area() for shape in self.shapes])

    def sum_perimeter(self):
        """
        Calculates the total perimeter of all the shapes
        :return: (float) The sum of the perimeters of all generated shapes
        """
        return sum([shape.get_perimeter() for shape in self.shapes])

    def count_colors(self):
        """
        Counts the number of shapes for each color
        :return: A dictionary where the keys are colors and the values are the count of shapes of that color
        """
        color_count = {}
        for shape in self.shapes:
            color = shape.get_color()
            if color in color_count:
                color_count[color] += 1
            else:
                color_count[color] = 1
        return color_count


if __name__ == '__main__':
    # asserts
    shape_factor = ShapeFactor()

    # Generate 10 random shapes
    shape_factor.generate(10)
    assert len(shape_factor.shapes) == 10, "The number of shapes generated should be 10"

    total_area = shape_factor.sum_areas()
    total_perimeter = shape_factor.sum_perimeter()
    assert isinstance(total_area, float), "The total area should be a float"
    assert isinstance(total_perimeter, float), "The total perimeter should be a float"

    # Validate that count_colors returns a dictionary with the correct keys
    color_counts = shape_factor.count_colors()
    assert isinstance(color_counts, dict), "The color count should be a dictionary"
    assert all(isinstance(count, int) for count in color_counts.values()), "Color counts should be integers"
    assert all(isinstance(color, str) for color in color_counts.keys()), "Color keys should be strings"

    print("All tests passed!")
