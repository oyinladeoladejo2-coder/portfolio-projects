# Implement safe_calculator(a, operator, b). 
# Return the result of applying the operator to the two numbers. 
# Supported operators are "+", "-", "*", "/", "%", and "**". 
# If the operator is unknown, return "Invalid operator". 
# If the operator is "/" or "%" and b is 0, return "Cannot divide by zero".
# Round division results to 2 decimal places.


def safe_calculator(a, operator, b):
    if operator == "+" :
        return a+b 
    elif operator == "-":
        return a-b
    elif operator == "*":
        return a*b
    elif operator == "/":
        if b == 0:
            return("Cannot divide by zero")
        return round (a/b, 2)
    elif operator == "%":
        if b == 0:
            return "Cannot divide by zero"
        return a%b
    elif operator == "**":
        return a**b
    else:
        return "Invalid operator"

