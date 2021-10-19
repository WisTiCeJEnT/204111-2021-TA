# Ex1
i = 10
while i < 22:
    print(i)
    i += 3

# Ex2
i = 0
while i > -10:
    print(i)
    i -= 2

# Ex3
num = 10
while num < 12:
    print(f"{num:.2f}")
    num += 0.15

# Ex4
PASSWORD = "I love Python"
s = input("Enter password: ")
while s != PASSWORD:
    print("Incorrect password.  Access denied.")
    s = input("Enter password: ")
print("Correct password.  Access granted.")

# Ex5
# KeyboardInterrupt