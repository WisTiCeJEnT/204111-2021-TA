inp = open(input('Enter score file: ')).read().splitlines()
inp = [int(l) for l in inp if l != '']
for i in range(len(inp)):
    print(f'Student #{i+1} score: {inp[i]}')
print(f'Average score is {sum(inp)/len(inp):.2f}')
print('Minimum score is', min(inp))
print('Maximum score is', max(inp))