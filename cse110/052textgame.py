print("You're moving to a new city. THere you're able to choose wether you'd like to live ALONE or ACCOMPANIED")

living_choice = input()

if living_choice.upper() == 'ALONE':
    print("Awesome! There are two places then for you to live. One with people are KNOWN and the other with people that are UNKONW to you")
    alone_with = input()
    if alone_with == 'KNOWN':
        print('Story continues')
    elif alone_with == 'UNKNOWN':
        print('Story continues')
    else:
        print('Story continues')
elif living_choice.upper() == 'ACCOMPANIED':
    print("Awesome. Now you can decide who is going to live with you: your best FRIEND or your FAMILY.")
    living_with = input()
    if living_with.upper() == 'FRIEND':
        print('Story continues')
    elif living_with.upper() == 'FAMILY':
        print('Story continues')
    else: 
        print('Story continues')
else:
    print("It seems like you don't wanna move to a new place!")