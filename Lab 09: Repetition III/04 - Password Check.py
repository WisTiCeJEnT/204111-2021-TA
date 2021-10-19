PASSWORD = 'Python is fun'
count = 0
while True:
    inp = input('Enter password please: ')
    if inp == PASSWORD:
        print('Correct password\nAccess granted')
        break
    else:
        count += 1
        print(f'Wrong password, attempt #{count}\nAccess not allowed')
    if count == 3:
        print('Maximum attempts exceeded')
        break