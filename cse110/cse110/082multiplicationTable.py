#Ask the user for a number
table_size = int(input("How many columns and rows do you want in your multiplication table? "))

#Make two for loops so that each number in table_size is multipled by all the numbers 
#In the range of range(1,table_size+1)

max_number = table_size * table_size

number = max_number

#Core requirements 1:
for t in range(1, table_size + 1):
    print(t)

#Core requirements 2:
for k in range(1, table_size + 1):
    if k == table_size:
        print(k)
        break
    print(k, end=" ")

#counter measures how much is x in 10^x so that number/10^x is still more than 1.
counter = 0
while number > 1:
    number = number / 10
    counter += 1
   #print(number)

#Print all those numbers in a table.
for i in range(1, table_size + 1):
    for j in range (1, table_size + 1):
        if(j == table_size):
            print(f"{i * j:{counter}}")
        else:
            print(f"{i * j:{counter}}", end=" ")