print("Please enter the following:\n")

adjective = input("adjective: ")
animal = input("animal: ")
verb = input("verb: ")
exclamation = input("exclamation: ")
verb_second = input("verb: ")
verb_third = input("verb: ")

print("\nYour story is:\n")

story = f'The other day, I was really in trouble. It all started when I saw a very\n {adjective} {animal} {verb} down the hallway. "{exclamation.capitalize()}!" I yelled. But all\n I could think to do was to {verb_second} over and over. Miraculously,\n that caused it to stop, but not before it tried to {verb_third}\n right in front of my family.'
print(f"{story}\n")

given_input = input("Do you want to see a cool thing? type in exactly 'yes' or 'no'\n")

if given_input == 'yes':
  print(f"\n{story.swapcase()}\n")
  print("Yes, I swapped the case of your story ;)")
else: 
  print("\nAlright! That's it for today :)")
