# Calculatrice simple : Écrivez un programme qui prend deux nombres et effectue les opérations de base : addition, soustraction, multiplication, division.
# ex : “3+1-4x4”
#
# def calculator(user_input):
#     print(eval(user_input))
#     count = 0
#     for i, x in enumerate(user_input):
#         if x == '*':
#             count += int(user_input[i - 1]) * int(user_input[i + 1])
#             user_input.replace(user_input[i], str(int(user_input[i - 1]) * int(user_input[i + 1])))
#             user_input.replace(user_input[i - 1], '')
#             user_input.replace(user_input[i + 1], '')
#             print(count)
#         if x == '/':
#             count += int(user_input[i - 1]) / int(user_input[i + 1])
#             user_input.replace(user_input[i], str(int(user_input[i - 1]) / int(user_input[i + 1])))
#             user_input.replace(user_input[i - 1], '')
#             user_input.replace(user_input[i + 1], '')
#         if x == '+':
#             count += int(user_input[i - 1]) + int(user_input[i + 1])
#             user_input.replace(user_input[i], str(int(user_input[i - 1]) + int(user_input[i + 1])))
#             user_input.replace(user_input[i - 1], '')
#             user_input.replace(user_input[i + 1], '')
#             print(count)
#         if x == '-':
#             count += int(user_input[i - 1]) - int(user_input[i + 1])
#             user_input.replace(user_input[i], str(int(user_input[i - 1]) - int(user_input[i + 1])))
#             user_input.replace(user_input[i - 1], '')
#             user_input.replace(user_input[i + 1], '')
#     print(count)
#
#
# calculator(input('Enter an operation with numbers from 0 to 9: '))
