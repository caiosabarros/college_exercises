#simpler example of 075guessumber.py
magic_number = int(input("What is the magic number? "))
guess = int(input("What is your guess? "))
if magic_number == guess:
    print("You guessed it!")
elif magic_number > guess:
    print("Higher")
else:
    print("Lower")