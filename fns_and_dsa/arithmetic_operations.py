# arithmetic_operations.py

def perform_operation(num1, num2, operation):
    """
    Perform basic arithmetic operations based on the 'operation' parameter.
    
    Parameters:
    num1 (float): The first number.
    num2 (float): The second number.
    operation (str): A string specifying the operation ('add', 'subtract', 'multiply', 'divide').

    Returns:
    float or str: The result of the arithmetic operation or an error message in case of division by zero.
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return "Error: Invalid operation"
