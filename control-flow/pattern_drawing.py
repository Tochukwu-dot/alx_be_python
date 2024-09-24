# Prompt the user to enter a positive integer
size = int(input("Enter the size of the pattern: "))

# Initialize row counter for the while loop
row = 0

# Use while loop to iterate through each row
while row < size:
    # Use a for loop to print asterisks (*) for each row
    for col in range(size):
        print("*", end="")  # Print * without a newline
    print()  # Move to the next line after each row is complete
    row += 1  # Move to the next row