#First requirement
print("Enter the names and balances of bank accounts (type: quit when done)")
accounts = []
balances = []
account = input("What is the name of this account? ")
while account != "quit":
    accounts.append(account)
    balance = float(input("What is the balance? "))
    balances.append(balance)
    account = input("What is the name of this account? ")
#Second Requirement
print()
print("Account Information:")
for i in range(len(accounts)):
    print(f"{accounts[i]} - ${balances[i]}")

#Third Requirement:
print()
print(f"Total: {sum(balances)}")
print(f"Average: {round(sum(balances)/len(balances),2)}")

