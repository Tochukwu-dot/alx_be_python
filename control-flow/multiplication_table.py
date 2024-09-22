number = int(input("Enter a number to see its multiplication table: "))
range = range(1, 11)
for x in range:
    result = number * x
    print(number, "*", x, "=", result)