number = int(input("Enter a number to see its multiplication table: "))
our_range = range(1, 11)
for x in our_range:
    result = number * x
    print(number, "*", x, "=", result)