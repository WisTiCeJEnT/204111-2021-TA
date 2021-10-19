def print_tbl(m):
    for i in range(1, 13):
        print(f'{m} x {i} = {m*i}')

while True:
    n = input('Specify N (or just ENTER to quit): ')
    if n == '':
        break
    print_tbl(int(n))