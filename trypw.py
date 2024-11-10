pw = 'a123456'
counter = int(3)
in_pw = input('please input password')
while pw != pw:
    print('PW incorrect!')
    counter = counter - 1
    if counter<1:
        break

