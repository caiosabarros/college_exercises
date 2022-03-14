"""
Author: Caio Sa

Purpose: Practice working with files.
"""

#Open the file and display data
with open("hr_system.txt") as data:
    for line in data:
        print(line)

with open("hr_system.txt") as data:
    for line in data:
        print(f"Name: {line.split(' ')[0]}")

with open("hr_system.txt") as data:
    for line in data:
        print(f"Name: {line.split(' ')[0]},", end=" ")
        print(f"Title: {line.split(' ')[2]}")
