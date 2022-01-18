#What the program should look like:

#What is the price of a child's meal? 2.25
#What is the price of an adult's meal? 6.99
#How many children are there? 2
#How many adults are there? 1
#What is the sales tax rate? 4
#
#Subtotal: $11.49
#Sales Tax: $0.46
#Total: $11.95
#
#What is the payment amount? 20
#Change: $8.05

child_meal = round(float(input("What is the price of a child's meal? ")), 2) 
adult_meal = round(float(input("What is the price of an adult's meal? ")), 2)
children = int(input("How many children are there? ")) 
adults = int(input("How many adults are there? ")) 
tax_rate = round(float(input("What is the sales tax rate? ")), 2) 

subtotal = child_meal*children + adult_meal*adults
print(f"\nSubtotal: ${subtotal}") 
sales_tax = round(tax_rate*float(subtotal)/100, 2)
print(f"Sales Tax: ${sales_tax}") 
tip = float(input("Do you want to give a tip? If not, type 0. If so, type in the value: "))
total = round(sales_tax+subtotal+tip, 2)
print(f"Total: ${total}") 

payment_amount = round(float(input(f"\nWhat is the payment amount? ")), 2) 
print(f"Change: ${payment_amount-total}") 