# polymorphism_demo.py

import math

# Base class: Shape
class Shape:
    def area(self):
        """Method to calculate the area. Needs to be overridden by derived classes."""
        raise NotImplementedError("Subclasses must override this method.")

# Derived class: Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        """Initialize Rectangle with length and width."""
        self.length = length
        self.width = width

    def area(self):
        """Override area method to calculate the area of the rectangle."""
        return self.length * self.width

# Derived class: Circle
class Circle(Shape):
    def __init__(self, radius):
        """Initialize Circle with radius."""
        self.radius = radius

    def area(self):
        """Override area method to calculate the area of the circle."""
        return math.pi * self.radius ** 2

# Function to demonstrate polymorphism
def print_area(shape):
    """This function demonstrates polymorphic behavior by calling the area method."""
    print(f"The area is: {shape.area():.2f}")

# # Example usage
# if __name__ == "__main__":
#     rectangle = Rectangle(10, 5)
#     circle = Circle(7)

#     # Polymorphism: calling the area method on different objects
#     print_area(rectangle)  # Output: 50.00
#     print_area(circle)     # Output: 153.94
