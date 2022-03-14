print("Enter a list of numbers, type 0 when finished.")

numbers = []

def get_number():
    number = float(input("Enter a number: "))
    if number != 0 :
        numbers.append(number)
        get_number()
    else:
        print(f"The sum is: {sum(numbers)}")
        print(f"The average is: {sum(numbers)/len(numbers)}")
        print(f"The largest number is: {max(numbers)}")

get_number()
