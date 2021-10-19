inp = [line.split(',') for line in open(input('Enter age file: ')).read().splitlines()]
maxx = str(max([int(p[1]) for p in inp]))
print(f'Oldest person(s) with the age of {maxx}:')
for p in inp:
    if p[1] == maxx:
        print('-', p[0])