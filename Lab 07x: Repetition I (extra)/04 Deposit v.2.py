init = int(input('Enter cash in Baht: '))
y = int(input('Enter #years: '))
interest = float(input('Enter interest rate (%): '))
c = init
for i in range(1, y+1):
    c = c + c*interest/100
    print(f'You will get back {c:.2f} Baht in {i} years.')
print(f'At the end, you will earn {c-init:.2f} Baht of interest in {y} years.')