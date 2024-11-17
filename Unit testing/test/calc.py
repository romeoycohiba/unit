def add(*args):
    try:
        # Check if there are more than two arguments
        if len(args) != 2:
            raise ValueError("You must enter exactly two arguments.")
        
        # Unpack arguments
        num1, num2 = args
        
        # Try to convert the arguments to numbers (handle strings or invalid numbers)
        num1 = float(num1)
        num2 = float(num2)
        
        # Return the sum of the two numbers
        return num1 + num2

    except ValueError as ve:
        return f"Error: {ve}"
    except TypeError:
        return "Error: Both inputs must be numeric."
    except Exception as e:
        return f"Unexpected error: {e}"

print(add(1,'a'))

def subtract(x,y):
    """Subtract Function"""
    return x-y

def multiply(x,y):
    """Multiply Function"""
    return x ** y

def divide(x,y):
    """Divide Function"""
    if y == 0:
        raise ValueError('Can not divide by zero!')
    return x/y 