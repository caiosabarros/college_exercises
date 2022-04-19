"""
You work for a retail store that wants to increase sales on Tuesday
and Wednesday, which are the store's slowest sales days. On Tuesday
and Wednesday, if a customer's subtotal is greater than $50, the
store will discount the customer's purchase by 10%.
"""

from datetime import datetime

current = datetime.now()

weekday = current.weekday()
print(f"Weekday {weekday}")

subtotal = float(input("Please enter the subtotal: "))


if subtotal >= 50: 
    if weekday == 1 or weekday == 2:
        print(f"Discount amount: {subtotal * 0.1:.2f}")
        print(f"Sales tax amount: {subtotal * 0.9 * 6 / 100:.2f}")
        print(f"Total {subtotal * 0.9 + (subtotal * 0.9 * 6 / 100):.2f}")
    else:
        print(f"Sales tax amount: {subtotal * 6 / 100:.2f}")
        print(f"Total {(subtotal + (subtotal * 6 / 100)):.2f}")
else:
    print(f"Sales tax amount: {subtotal * 6 / 100:.2f}")
    print(f"Total {(subtotal + (subtotal * 6 / 100)):.2f}")