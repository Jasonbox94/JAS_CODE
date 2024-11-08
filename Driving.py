country = input("What's your nationality? ")
age = input('How old are you? ')
age = int(age)
if country == 'TW' :
    if age >= 18 :
        print('eligible to take a driving test!')
    else :
        print('not eligible to take a driving test')
elif country == 'US' :
    if age >= 16 :
        print('eligible to take a driving test!')
    else :
        print('not eligible to take a driving test')
