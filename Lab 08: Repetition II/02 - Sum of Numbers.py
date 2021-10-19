inp = -1
pos = 0
neg = 0
while (inp != 0):
  inp = float(input('Enter a number (or just 0 to exit): '))
  if inp > 0:
    pos += inp
  else:
    neg += inp
print(f'The sum of positive numbers is {pos:.2f}')
print(f'The sum of negative numbers is {neg:.2f}')