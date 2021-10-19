msg = input("What do you want me to say? ")
num = int(input("How many times you want me to say it? "))
# BEGIN
print(((msg+'\n')*num).strip())
# END


msg = input("What do you want me to say? ")
num = int(input("How many times you want me to say it? "))
# BEGIN
print('\n'.join([msg+' #'+str(x+1) for x in range(num)]))
# END


# BEGIN
def g(x):
    return x*x

print(" x | g(x)")
print("---+---------------------------------")
for x in range(5):
    bars = "#" * round(g(x+1))
    print(f" {x+1} | {bars} ({g(x+1)})")
# END