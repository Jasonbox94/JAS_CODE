pw = 'a123456'
counter = int(3)

while counter > 0 :
    in_pw = input('please input password:')
    counter = counter - 1
    if pw == in_pw:
        print('Login Successful.')
        break
    else:
        if counter < 1:        
            print('Account Locked!')
        else:
            print('Incorrect! '+ str(counter) + ' times rested')

            



