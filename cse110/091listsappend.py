#Create a list to append names
names = []

#Get the first name
name = input("Type the name of a friend: ")

#Get names till the person types "end"
while name != "end":
    names.append(name)
    name = input("Type the name of a friend: ")

#Function for Displaying Item in List;
def display(e):
    for element in e:
        print(element)

#Display names on the list
display(names)