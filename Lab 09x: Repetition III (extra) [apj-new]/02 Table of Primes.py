def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**(1/2))+1):
        if n%i == 0:
            return False
    return True

cur = int(input('Primes greater than? ')) + 1
p = int(input('How many primes? '))
if p > 0:
    print(f'{p} primes greater than {cur-1} are')
else:
    print('Nothing to do.')
for i in range(p):
    while(not is_prime(cur)):
        cur += 1
    print(f'{cur:6d}', end='')
    cur += 1
    if i % 10 == 9:
        print()