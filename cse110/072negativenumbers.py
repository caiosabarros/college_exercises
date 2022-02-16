number = -1

while number < 0:
    number = float(input("Please type a positive number: "))
    
    if(number<0):
        print("Sorry, that is not a positive number. Please try again")
    else:
        print("the number is {}".format(number))

