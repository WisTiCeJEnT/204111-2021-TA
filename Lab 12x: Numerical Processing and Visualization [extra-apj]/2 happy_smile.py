n = int(input('Total number of days : '))
l = 0
ans = 0
for i in range(n):
    inp = int(input(f'Day {i+1} : '))
    if inp >= 80 or (inp >= 20 and inp - l >= 10):
        ans += 1
    l = inp
print(f'Happy Smile Days have {ans} days.')