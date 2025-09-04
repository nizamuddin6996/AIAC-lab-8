def simple_calculator(a, b, operation):
    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    elif operation == 'divide':
        if b == 0:
            return "Error: Division by zero"
        return a / b
    else:
        return "Invalid operation"

#Example usage:
result = simple_calculator(10, 5, 'add')
print(result)  # Output: 15