def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**(1/2))+1):
        if n%i == 0:
            return False
    return True

while True:
    inp = input('Enter an integer (or [Enter] to quit): ')
    if inp == '':
        break
    print(f'{inp} is{"" if is_prime(int(inp)) else " not"} prime.')
print('Bye!')
