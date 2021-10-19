arr = []
while(True):
    inp = input('Input score (or ENTER to finish): ')
    if inp == '':
        break
    arr.append(int(inp))
arr.sort(reverse=True)
for i in range(len(arr)):
    print(f'Rank #{i+1}: {arr[i]}')