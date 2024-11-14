#Guess Number
import random
r = random.randint(1 , 100)
#print(str(r))
switch = True
while switch == True :

    number = int(input('Guess a number: '))
    if r == number:
        print('Bingo')
        switch = False
    else:
        print('Missed!')
        if number < r:
            print('Go Higher')
        else:
            print('Go Lower')
