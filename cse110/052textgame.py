from random import random 
import hashlib

print("You're moving to a new city. THere you're able to choose wether you'd like to live ALONE or ACCOMPANIED")

living_choice = input()

if living_choice.upper() == 'ALONE':
    print("Awesome! There are two places then for you to live. One with people are KNOWN and the other with people that are UNKONW to you")
    alone_with = input()
    if alone_with.upper() == 'KNOWN':
        print("Awesome! So, they'll be right there waiting to have a party with you and they're thinking what you'd rather do first:EAT or DRINK or DANCE? ")
        partying = input()
        if partying.upper() == "EAT":
            print("That's is amazing! They're bringing your favorite food - but that's a secret, OK? ")
        elif partying.upper() == "DRINK":
            print("Incredible! Your must be thirsty after a long move, right? Don't worry, they'll take care of that for you!")
        elif partying.upper() == "DANCE":
            print("Excellent! Sounds like someone is really happy for moving out! Come on, let's dance!")
        else:
            print("It seems like you just wanna get a rest then!")
    elif alone_with.upper() == 'UNKNOWN':
        print("Cool! Unkown people are full of surprises. Of course, you'll get to know them. What method do you prefer to do that: PHISICALLY or VIRTUALLY?")
        meeting = input()
        if meeting.upper() == "PHISICALLY":
            print("I know, virtually has no comparison when it comes to meeting a person face to face in person ;)")
        elif meeting.upper() == "VIRTUALLY":
            print("Cool! We've seen many forms to do that lately, right? Metaverse sounds like a good place for this to happen!")
        else:
            print("Ok, it looks like you wanna to have some time by yourself.")
    else:
        print("It seems like you don't wanna interactions right nonw!")
elif living_choice.upper() == 'ACCOMPANIED':
    print("Awesome. Now you can decide who is going to live with you: your best FRIEND or your FAMILY.")
    living_with = input()
    if living_with.upper() == 'FRIEND':
        print("Uhhhh! You didn't want to be with your family. Would you like to say anything at all to them like SORRY or would you say NOTHING? ")
        what_to_say = input()
        if what_to_say.upper() == "SORRY":
            print("Your family is disappointed at you. But they're glad that at least you decided to live out of your commfort zone!")
        elif what_to_say.upper() == "NOTHING":
            print("Your family is not happy with you. They don't know what's been happening to you lately.")
        else:
            print("It looks like you'd rather say something else to them, right?")
    elif living_with.upper() == 'FAMILY':
        print("Awesome! Of course, your friend is sad, but he understands how much you love your family!")
    else: 
        print("Wait a moment! It seems like you've got an eternal partner! Uhu!")
else:
    print("It seems like you don't wanna move to a new place!")
print("Thanks for being here today. Because you participated, you'll receive a lucky hash!")
print(f"Your lucky hash is {hashlib.sha256(bytes(str(random() * 10), encoding = 'utf-8')).hexdigest()}")