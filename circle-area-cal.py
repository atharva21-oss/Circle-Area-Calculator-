# circle_area.py
import math

def calculate_area(radius):
    """Calculate the area of a circle given its radius."""
    if radius < 0:
        return "Radius cannot be negative."
    return math.pi * radius ** 2

if __name__ == "_main_":
    try:
        radius = float(input("Enter the radius of the circle: "))
        area = calculate_area(radius)
        print(f"The area of the circle with radius {radius} is {area:.2f}")
    except ValueError:
        print("Please enter a valid number for the radius.")