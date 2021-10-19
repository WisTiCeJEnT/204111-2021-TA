# Ex1
lines = open('planets.txt').read().splitlines()

# Ex2
lines = open('planets.txt').read().splitlines()
lines_noempty = [l for l in lines if l != '']

# Ex3
lines = open('numbers.txt').read().splitlines()
numbers = [float(s) for s in lines if s != '']
print("Numbers are:", numbers)
average = sum(numbers)/len(numbers)
print(f"Average is {average:.2f}")