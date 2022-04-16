#Desired output of the simple program:
#
#How old are you? 25
#On your next birthday, you will be 26
#
#How many egg cartons do you have? 3
#You have 36 eggs
#
#How many cookies do you have? 18
#How many people are there? 8
#Each person may have 2.25 cookies

def birthday():
  age = int(input("How old are you? "))
  print(f"On your next birthday, you will be {age+1}\n")

def egg():
  eggs = int(input("How many egg cartons do you have? "))
  print(f"You  have {12*eggs}\n")

def people_and_cookies():
  cookies = input("How many cookies do you have? ")
  people = input(f"How many people are there? ")
  print(f"Each person may have {round(float(cookies)/float(people),2)} cookies\n")

birthday()
egg()
people_and_cookies()