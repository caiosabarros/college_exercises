"""
File: 0121iterate.py
Author: Caio Sa

Purpose: Practice finding items in lists.
"""

people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

youngest_age = int(people[0].split(" ")[1])
youngest_person = people[0].split(" ")[0]

for information in people:
    person = information.split(" ")[0]
    age = int(information.split(" ")[1])

    if age < youngest_age:
        youngest_age = age
        youngest_person = person

print(f"The youngest person is {youngest_person} of age {youngest_age}")
        

