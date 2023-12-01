# Calculatrice simple : Écrivez un programme qui prend deux nombres et effectue les opérations de base : addition, soustraction, multiplication, division.
# ex : “3+1-4x4”

def calculator(input):

    # Check if a character is an operator
    def is_operator(char):
        return char in ['+', '-', '*', '/']
    # Perform an operation
    def operations(operator, a, b):
        if operator == '+':
            return a + b
        elif operator == '-':
            return a - b
        elif operator == '*':
            return a * b
        elif operator == '/':
            if b == 0:
                raise ValueError("Cannot divide by 0!")
            return a / b

    operators = []
    numbers = []

    i = 0
    while i < len(input):
        # Check if the character is a digit
        if input[i].isdigit():
            number_start = i
            # Extract the number and convert it to float, add it to the list of numbers
            while i < len(input) and (input[i].isdigit() or input[i] == '.'):
                i += 1
            numbers.append(float(input[number_start:i]))
            i -= 1
        # Check if the character is an operator
        elif is_operator(input[i]):
            # Evaluate operations according to the priority of the operators
            while (len(operators) > 0 and is_operator(operators[-1]) and
                   (input[i] in ['*', '/'] or input[operators[-1]] in ['+', '-'])):
                numbers.append(operations(operators.pop(), numbers.pop(-2), numbers.pop()))
            # Add the index of the operator to the list of operators
            operators.append(i)
        i += 1
    # Evaluate the remaining operations with the remaining operators
    while len(operators) > 0:
        numbers.append(operations(input[operators.pop()], numbers.pop(-2), numbers.pop()))

    return int(numbers[0])


print(calculator(input('Enter an operation: ')))
