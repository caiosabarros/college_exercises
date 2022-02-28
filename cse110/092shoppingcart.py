"""
Author: Caio Sa

Purpose: Simple Supermarket Cart
Exceeds in Using a Funcitonal Programming Approach 
"""


print("Welcome to the Shopping Cart Program!")

items = []
prices = []

def select_action():
    print("Please select one of the following:") 
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")
    action = int(input("Please enter an action: ")) 

    if action == 1:
        add_item()
    elif action == 2:
        view_cart()
    elif action == 3:
        remove_item()
    elif action == 4:
        compute_total()
    else:
        terminate()

def add_item():
    item = input("What item would you like to add? ")    
    price = input(f"What is the price of {item}? ")
    #Add to the list
    items.append(item)
    prices.append(price)
    print(f"{item} has been added to the cart. ")
    select_action()

def view_cart():
    print("The contents of the shopping cart are: ")
    #Show each item in the list
    i = 1
    for item in items:
        print(f"{i}. {items[i-1]} - ${prices[i-1]}")
        i += 1
    select_action()

def remove_item():
    item_to_remove = input("Which item would you like to remove? ")
    #remove item from the list
    item_index = items.index(item_to_remove)
    items.remove(items[item_index])
    prices.remove(prices[item_index])
    print("Item removed.")
    select_action()

def compute_total():
    #compute total
    total = 0
    for price in prices:
        total += int(price)
    print(f"The total price of the items in the shopping cart is ${total}")
    select_action()

def terminate():
    print("Thank you.\nGoodbye.")

select_action()