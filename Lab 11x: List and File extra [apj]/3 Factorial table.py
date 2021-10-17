n = int(input('Enter a number: '))
if n < 0:
    print('Invalid input, program terminates.')
else:
    print('0! = 1 = 1')
    fac = 1
    for i in range(1, n+1):
        fac *= i
        print(f'{i}! =', ' x '.join([str(j) for j in range(i, 0, -1)]), '=', fac)
