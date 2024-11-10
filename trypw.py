pw = 'a123456'
counter = int(3)

while counter > 0 :
    in_pw = input('please input password:')
    
    if pw == in_pw:
        print('Login Successful.')
        break
    else:
        print('Incorrect!')
        counter = counter - 1
        if counter < 1:        
            print('Bye Bye')

            



