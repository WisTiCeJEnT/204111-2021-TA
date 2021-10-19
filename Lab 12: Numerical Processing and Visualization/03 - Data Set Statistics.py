import numpy as np
data = np.loadtxt(input('Enter file name: '))
print(f'Size of the data set is {len(data)}')
print(f'Minimum is {min(data):.2f}')
print(f'Maximum is {max(data):.2f}')
print(f'Mean is {sum(data)/len(data):.2f}')
print(f'Standard deviation is {(sum([(x - sum(data)/len(data))**2 for x in data])/(len(data)-1))**(1/2):.2f}')
