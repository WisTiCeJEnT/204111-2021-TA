arr = [0]
while(True):
    inp = input()
    if inp == '-1':
        break
    arr.append((arr[-1]*1.01+int(inp)))
print(f'Total = {arr[-1]:.3f}')

for i in range(1, len(arr)):
    print(f'{arr[i]:.3f}')