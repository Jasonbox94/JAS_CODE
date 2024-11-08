#else if your school
age=input('Input your age: ')
age=int(age)
if age < 13:
    print('Elementary School')
elif age >= 13 and age <16:
    print('Junior High School')
elif age >= 16 and age <18:
    print('High School')
elif age >=18 and age < 22:
    print('University')
else:
    print('Adult')