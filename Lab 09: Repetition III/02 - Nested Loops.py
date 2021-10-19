# Ex1
for i in range(5,10):
    print(f"i = {i}")
    for j in [1,2]:
        print(f"  j = {j}")

# Ex2
for i in range(1,6):
    print(f"i = {i}")
    for j in range(i,0,-1):
        print(f"  j = {j}")

# Ex3
for i in range(3):
    for j in range(4):
        nspaces = 4-j-1
        nstars = j*2+1
        print((' ' * nspaces) + ('*' * nstars))

# Ex4
def f(n):
    sum = 0
    for i in range(1,n+1):
        for j in range(1,i+1):
           sum = sum + i+j
    return sum
f(2)
f(5)
f(10)