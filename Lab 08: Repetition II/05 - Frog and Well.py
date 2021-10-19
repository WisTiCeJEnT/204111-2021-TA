"""
How deep is the well? 5
Enter the height the frog can jump up: 3
Enter the height the frog slips down: 2
On day 1 the frog leaps to the depth of 2 meters.
At night he slips down to the depth of 4 meters.
On day 2 the frog leaps to the depth of 1 meters.
At night he slips down to the depth of 3 meters.
The frog is free on day 3.

How deep is the well? 10
Enter the height the frog can jump up: 5
Enter the height the frog slips down: 5
The frog will never escape from the well.
"""
h = int(input("How deep is the well? "))
p = int(input("Enter the height the frog can jump up: "))
s = int(input("Enter the height the frog slips down: "))
c = 0
d = 0
if s >= p and p < h:
    print('The frog will never escape from the well.')
else:
    while(h > 0):
        d += 1
        h -= p
        if h <= 0:
            break
        print(f'On day {d} the frog leaps to the depth of {h} meters.')
        h += s
        print(f'At night he slips down to the depth of {h} meters.')
    print(f'The frog is free on day {d}.')