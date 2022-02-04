first_number = input("What is the first number? ")
second_number = input("What is the second number? ")
if(first_number > second_number):
    print("The first number is greater")
    print(f"The numbers are not equal")
    print(f"The second number is not greater\n")
elif(first_number < second_number):
    print("The first number is not greater")
    print(f"The numbers are not equal")
    print(f"The second number is greater\n")
else:
    print("The first number is not greater")
    print(f"The numbers are equal")
    print(f"The second number is not greater\n")

my_favorite_animal = "bear"
animal = input("What is your favorite animal? ")
if(animal.lower() == my_favorite_animal):
    print("That's my favorite animal too!")
else:
    print("That one is not my favorite.")