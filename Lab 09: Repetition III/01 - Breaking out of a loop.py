# Ex1
PASSWORD = "I love Python"
while True:
    s = input("Enter password: ")
    if s == PASSWORD:
      break
    print("Incorrect password.  Access denied.")
print("Correct password.  Access granted.")

# Ex2
n = 1001
while True:
  if n % 33 == 0 and n % 273 == 0:
    break
  n += 1
print(f"The value of n is {n}")