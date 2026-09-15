def calculator(num1,num2, operators):
    if operators == "+":
        return num1 + num2
    elif operators == "-":
        return num1 - num2
    elif operators == "*":
        return num1 * num2
    elif operators == "/":
        if num1/num2 == 0:
            return "Error:cannot divide by zero"
        return num1/ num2
    else:
        return "Error: invalid operators"

while True:
        num1_input = input("Enter first number: ")
        operator = input("\nEnter operator (+, -, *, /): ")
        num2_input = input("Enter second number: ")
        

        try:
            num1 = int(num1_input)
            num2 = int(num2_input)
            result = calculator(num1, num2, operator)
            print(f"Result: {result}")
        except ValueError:
            print("Error: Please enter valid numbers")


