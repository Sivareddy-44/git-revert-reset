# Get a number from the user and convert it to an integer
num = int(input("Enter a number to check: "))

# Check if the remainder is 0 when divided by 2
if num % 3 == 0:
    print(f"{num} is an Even number.")
else:
    print(f"{num} is an Odd number.")
