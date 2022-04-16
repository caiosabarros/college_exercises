import math

def compute_area_square(side):
    area = side ** 2
    return area
def compute_area_rectangle(width, height):
    area = width * height
    return area
def compute_area_circle(radius):
    area = math.pi * (radius ** 2) 
    return area

willing = True
while willing:
    shape = input("Common, what's the shape? (C/R/S) ")
    if shape == "R":
        width = float(input("Whats is the width? "))
        height = float(input("Whats is the height? "))
        result = compute_area_rectangle(width, height)
        print(result)
    elif shape == "S":
        size = float(input("Whats is the size? "))
        result = compute_area_square(size)
        print(result)
    else:
        radius = float(input("Whats is the radius? "))
        result = compute_area_circle(radius)
        print(result)
    option = input("Do you want to continue? ")
    if option == "quit":
        willing = False