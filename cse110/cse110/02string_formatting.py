#Let's do another game called "Bond, James Bond."
#Please, tell me your first name:
first_name = input("Please, tell me your first name:")
#Please, tell me your last  name:
last_name = input("Please, tell me your last name:")
#Now, let me tell you your Bond-version name:
print(f"Your last name is {last_name}, {first_name} {last_name}.")

# Be aware that there are many ways to do the formatting of that line, such as:
# print("Your name is " + last + ", " + first + " " + last + ".")
# print("Your name is {}, {} {}.".format(last, first, last))
# print("Your name is {0}, {1} {0}.".format(last, first))