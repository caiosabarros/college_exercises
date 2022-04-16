grade = float(input('What was your grade percentage? '))

if grade >= 90:
    letter = 'A'
elif grade >=80:
    letter = 'B'
elif grade >=70:
    letter = 'C'
elif grade >=60:
    letter = 'D'    
else:
    letter = 'F'
    
print(f'Your grade is {letter}\n')

if grade >=70:
    print('You are approved! Congratulations!')
else:
    print('You are not approved. Try more the next time.')
