arr = []
while(True):
    inp = input('Input score (or ENTER to finish): ')
    if inp == '':
        break
    arr.append(int(inp))
for i in range(len(arr)):
    print(f'Score #{i+1}: {arr[i]}')
print(f'Average score is {sum(arr)/len(arr):.2f}',)
print(f'Minimum score is {min(arr)}',)
print(f'Maximum score is {max(arr)}',)
