SCORE = {
    'A': 4.0,
    'B+': 3.5,
    'B': 3.0,
    'C+': 2.5,
    'C': 2.0,
    'D+': 1.5,
    'D': 1.0,
    'F': 0.0
}
inp = open(input('Enter grade file: ')).read().splitlines()
inp = [l.split(',') for l in inp if l != '']
for i in range(len(inp)):
    print(f'subject: {inp[i][0]} credits: {inp[i][1]} grade: {inp[i][2]:2} point: {SCORE[inp[i][2]]}')
print('Total credits =', sum([int(c[1]) for c in inp]))
print(f'GPA = {sum([SCORE[s[2]] * int(s[1]) for s in inp]) / sum([int(c[1]) for c in inp]):.2f}')