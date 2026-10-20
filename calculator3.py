# Problem
# Build a continuous calculator that maintains a running total. The user inputs an operator and a number repeatedly (e.g., + 5, then * 2). 
# Examples
# Input: + 5 → Result: 5
# Input: * 2 → Result: 10
# Input: undo → Result: 5 
# Constraints
# Must handle floating-point numbers.
# Implement an undo feature that reverts the calculation to the previous state.
# Strictly forbid the use of eval().
# Must handle division by zero and invalid operators without crashing the program.
# Do not import libraries.





def calculator(current_total, new_number, operators):
    if operators == '+':
        current_total += new_number
    elif operators == '-':
        current_total -= new_number
    elif operators == '*':
        current_total *= new_number
    elif operators == '/':
        if new_number == 0:
            return 'Error: cannot divide by zero'
        current_total /= new_number
    else:
        return 'Error: Invalid operator'

    return current_total


current_total = float(input("Enter starting number: "))
history = [current_total]

while True:
    user_input = input("Enter operation (+ 5, - 2, undo, or quit): ").strip()

    if user_input == 'undo':
        if len(history) > 1:
            history.pop()
            current_total = history[-1]
            print(f"Current total: {current_total}")
        else:
            print("Nothing to undo yet.")

    elif user_input == 'quit':
        print("Calculator closed.")
        break

    else:
        try:
            operators, number = user_input.split()
            new_number = float(number)

            result = calculator(current_total, new_number, operators)

            if isinstance(result, str):
                print(result)
            else:
                current_total = result
                history.append(current_total)
                print(f"Current total: {current_total}")

        except ValueError:
            print("Invalid input. Try something like + 5 or * 2.")
        except (TypeError, AttributeError):
            print("Invalid input. Try something like + 5 or * 2.")
