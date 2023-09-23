import math


def print_circum(radius):
    # The formula for calculating the circumference is 2 * pi * r(radius)
    circumference = 2 * math.pi * radius
    print(
        f"The circumference of a circle of radius {radius} is {circumference:.5f}")


# Here is the function with three different radius values
print_circum(5)
print_circum(3)
print_circum(10.6)
