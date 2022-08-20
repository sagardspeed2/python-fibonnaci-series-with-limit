# take input from user
limit = int(input("Enter Number: "))

# initial values
a, b = 0, 1

# print fibonacci number until the condition match
while a <= limit:
    print(a)

    # increase values
    a, b = b, a + b
