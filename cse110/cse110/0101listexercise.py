print("Please enter the items of the shopping list (type: quit to finish):")

list_of_things = []
command = ''
while command != "quit":
    command = input("Item: ")
    if command == "quit":
        break
    list_of_things.append(command)

print("\nThe shopping list is: ")
for item in range(len(list_of_things)):
    print(list_of_things[item])

print(f"\nThe shopping list with indexes is: ")
for i in range(len(list_of_things)):
    print(f"{i}. {list_of_things[i]}")

change = int(input("\nWhich item would you like to change? "))
new_item = input("What is the new item? ")

list_of_things[change] = new_item

print(f"\nThe shopping list with indexes is: \n")
for i in range(len(list_of_things)):
    print(f"{i}. {list_of_things[i]}")