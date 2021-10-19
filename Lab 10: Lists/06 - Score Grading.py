def grader(x, avr, sd):
    if x >= avr + 1.5 * sd:
        return 'A'
    elif x >= avr + sd:
        return 'B+'
    elif x >= avr + 0.5 * sd:
        return 'B'
    elif x >= avr:
        return 'C+'
    elif x >= avr - 0.5 * sd:
        return 'C'
    elif x >= avr - 1.0 * sd:
        return 'D+'
    elif x >= avr - 1.5 * sd:
        return 'D'
    else:
        return 'F'


arr = []
while(True):
    inp = input('Input score (or ENTER to finish): ')
    if inp == '':
        break
    arr.append(int(inp))

avr = sum(arr)/len(arr)
sd = (sum([(x - avr)**2 for x in arr])/(len(arr)-1))**(1/2)
print(f'Average score is {avr:.2f}')
print(f'Standard deviation is {sd:.2f}')
for i in range(len(arr)):
    print(f'Score #{i+1}: {arr[i]} grade: {grader(x=arr[i], avr=avr, sd=sd)}')