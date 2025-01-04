def sum_of_squares(n):
    """Calculate the sum of squares of the first n natural numbers."""
    total = 0
    for i in range(1, n + 1):
        total += i**2
    return total

# Prompt the user to enter a positive integer
while True:
    try:
        n = int(input("Enter a positive integer: "))
        if n > 0:
            break
        else:
            print("Please enter a positive integer.")
    except ValueError:
        print("That's not an integer! Please enter a valid positive integer.")

# Calculate the sum of squares
result = sum_of_squares(n)

# Display the result
print(f"The sum of squares of the first {n} natural numbers is: {result}")