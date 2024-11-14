#Guess Number
import random
start = int(print('f'))
r = random.randint(1 , 100)
#print(str(r))
switch = True
count = 0
while switch == True :
    count += 1
    number = int(input('Guess a number: '))
    print('times' + str(count))
    if r == number:
        print('Bingo')
        switch = False
    else:
        print('Missed!')
        if number < r:
            print('Go Higher')
        else:
            print('Go Lower')
