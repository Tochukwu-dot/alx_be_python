number = int(input("Enter a number to see its multiplication table: "))
# range = range(1, 11)
for x in range(1, 11):
    result = number * x
    print(f"{number} * {x} = {result}")