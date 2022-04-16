age_first = int(input("What is the age of the first rider? ")) 
height_first = int(input("What is the height of the first rider? "))
is_accompanied = input("Is there a second rider (yes/no)? ")

if height_first >= 36:    
    if is_accompanied.lower() == "yes":
        age_second = int(input("What is the age of the first rider? "))
        height_second = int(input("What is the height of the first rider? "))
        if height_second < 36:
            print("Sorry, you may not ride.")
        else:
            if age_first >= 18 or age_second >= 18:
                print("Welcome to the ride. Please be safe and have fun!")
            else:
                print("Sorry, you may not ride.")
    else: 
        if age_first >= 18 and height_first >= 62:
            print("Welcome to the ride. Please be safe and have fun!")
        else:
            print("Sorry, you may not ride.")
else:
    print("Sorry, you may not ride.")
