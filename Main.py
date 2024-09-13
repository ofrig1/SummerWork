"""
author: Ofri Guz
Date: 13/09/24
description: Defines a server that handles multiple clients by using the `select` module.
It includes functionality to combine two shapes, generate random shapes, and calculate the total
areas and perimeters of the shapes
"""

import Rect
import Circle
import ShapeFactor


def combine_two_shapes(shape1, shape2):
    """
    Combines two shapes by summing their areas and perimeters to create a new rectangle
    :param shape1: the first shape to combine
    :param shape2: the second shape to combine
    :return: (Rect) A new Rect object with combined area and perimeter of the input shapes
    """
    if isinstance(shape1, Circle.Circle) or isinstance(shape2, Circle.Circle):
        return "Error: One or both shapes are circles, which cannot be combined."
    total_area = shape1.get_area() + shape2.get_area()
    total_perimeter = shape1.get_perimeter() + shape2.get_perimeter()
    return Rect.Rect(shape1.color, total_perimeter / 4, total_area / (total_perimeter / 4))


def test_combine_two_shapes():
    """
    Tests the combine_two_shapes function with sample shapes
    Asserts
    """
    shape1 = Rect.Rect("red", 4, 5)
    shape2 = Rect.Rect("blue", 3, 4)

    combined_shape = combine_two_shapes(shape1, shape2)

    # Expected values
    expected_color = shape1.get_color()
    expected_area = shape1.get_area() + shape2.get_area()
    expected_perimeter = shape1.get_perimeter() + shape2.get_perimeter()
    expected_side = expected_perimeter / 4
    expected_length = expected_area / expected_side

    # Test the properties of the combined shape
    assert combined_shape.get_color() == expected_color, "Color of combined shape should match input shape1 color"
    assert combined_shape.get_area() == expected_area, "Area of combined shape should match the sum of areas"
    assert combined_shape.get_perimeter() == expected_perimeter, "Perimeter of combined shape should be perimeters sum"
    assert combined_shape.length == expected_length, "Length of combined shape should match expected value"
    assert combined_shape.width == expected_side, "Width of combined shape should match expected value"


def main():
    my_container = ShapeFactor.ShapeFactor()
    my_container.generate(100)
    print("total area:", my_container.sum_areas())
    print("total perimeter:", my_container.sum_perimeter())
    print("colors:", my_container.count_colors())


if __name__ == '__main__':
    test_combine_two_shapes()
    main()
