# Ex1
len('1234567890123')
# Ex2
s1 = 'I--i-e--r'
# Ex3
s1 = 'g-e-t'
# Ex4
msg = input("Enter a message: ")
for i in range(len(msg)):
    print(f"Character {i+1} is {msg[i]}")
# Ex5
msg = input("Enter a message: ")

out = ""
for i in range(0, len(msg), 2):
    out = out+msg[i]
print(out)

out = ""
for i in range(1, len(msg), 2):
    out = out+msg[i]
print(out)