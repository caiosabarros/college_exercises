print("For the next 4 questions, type in an integer in the range of 1 to 10")

loan = int(input("How large is the loan? "))
credit_history = int(input("How good is your credit history? "))
income = int(input("How high is your income? "))
down_payment = int(input("How large is your down payment? "))
can_loan = False

if loan >= 5: 
    if credit_history >= 7 and income >= 7:
        can_loan = True
    elif  credit_history >= 7 or income >= 7:
        if down_payment >= 5:
            can_loan = True
        else:
            pass
    else:
        pass
else:
    if credit_history < 4:
        pass
    else:
        if income >= 7 or down_payment >= 7:
            can_loan = True
        elif income >= 4 and down_payment >= 4:
            can_loan = True
        else:
            pass

if can_loan == True:
    print("Congrats, you can take a loan!")
else:
    print("Sorry, try improving your scores")