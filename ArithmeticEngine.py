# Implement arithmetic_engine(a, b). 
# Return a dictionary with three keys: "sum", "product", and "power". 
# The sum is a + b, the product is a * b, and the power is a ** b.


def arithmetic_engine(a, b):
    sum = a + b
    product = a * b
    power = a ** b

    return{
    "sum": sum,
    "product": product,
    "power": power
    }
