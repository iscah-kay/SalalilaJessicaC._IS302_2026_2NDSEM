import math

class Shape_jcs:
    def area_jcs(self_jcs):
        pass  # Placeholder for polymorphism

class Rectangle_jcs(Shape_jcs):
    def __init__(self_jcs, width_jcs, height_jcs):
        self_jcs.width_jcs = width_jcs
        self_jcs.height_jcs = height_jcs

    def area_jcs(self_jcs):
        return self_jcs.width_jcs * self_jcs.height_jcs

class Circle_jcs(Shape_jcs):
    def __init__(self_jcs, radius_jcs):
        self_jcs.radius_jcs = radius_jcs

    def area_jcs(self_jcs):
        return math.pi * self_jcs.radius_jcs ** 2

class Triangle_jcs(Shape_jcs):
    def __init__(self_jcs, base_jcs, height_jcs):
        self_jcs.base_jcs = base_jcs
        self_jcs.height_jcs = height_jcs

    def area_jcs(self_jcs):
        return 0.5 * self_jcs.base_jcs * self_jcs.height_jcs

# Example usage
rectangle_jcs = Rectangle_jcs(10, 5)
circle_jcs = Circle_jcs(5)
triangle_jcs = Triangle_jcs(8, 6)

print(f"Rectangle Area: {rectangle_jcs.area_jcs()}")
print(f"Circle Area: {circle_jcs.area_jcs():.1f}")
print(f"Triangle Area: {triangle_jcs.area_jcs()}")
