# NOT USING STRING.count()

s = input('Enter a string: ')
vo = 'aeiou'
no_of_vo = 0
d = {v: 0 for v in vo}
for c in s:
    if c in vo:
        d[c] += 1
        no_of_vo += 1
for v in vo:
    print(f"There are {d[v]} {v}'s.")
print(f'There are {len(s)-no_of_vo} non-vowels characters.')