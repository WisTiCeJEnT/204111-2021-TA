# Ex1
list(range(10))
# Ex2
list(range(100, 108))
# Ex3
list(range(-30, -20))
# Ex4
list(range(5, 101, 5))
# Ex5
list(range(20, 0, -1))
# Ex6
list(range(0, 19, 3))
# Ex7
for i in [30, 28, 26, 24, 22]:
    print(f"i = {i}")
# Ex8
import math

def f(n):
    return 15 + 10*math.sin(n/10)

print("  n | f(n)")
print("----+-------------------------------------------------")
for n in range(0, 100, 5):
    spaces = " " * round(f(n))
    print(f" {n:2} | {spaces}*")
