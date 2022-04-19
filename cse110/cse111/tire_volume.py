"""
Author: Caio Sa
"""
import math

width = int(input("Enter the width of the tire in mm (ex 205): "))
aspect_ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))

denominator = 10000000000

v = math.pi * aspect_ratio * (width) ** 2 * (width * aspect_ratio + 2540 * diameter) / denominator

print(f"The approximate volume is {v:.2f} liters")