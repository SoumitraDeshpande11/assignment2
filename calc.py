def add(a, b):
    """Return the sum of two numbers."""
    return a + b

def subtract(a, b):
    """Return the difference of two numbers."""
    return a - b

def multiply(a, b):
    """Return the product of two numbers."""
    return a * b

def divide(a, b):
    """Return the quotient of two numbers."""
    if b == 0:
        return "Error: Division by zero."
    return a / b
add(10,20)
