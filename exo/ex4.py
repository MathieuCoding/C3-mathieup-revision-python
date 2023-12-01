# Listes : Créez une liste de 10 nombres, trouvez le maximum, le minimum, et calculez la moyenne.
# Affichage de chaque opération

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def calculator(my_list):
    # print(f'Maximum: {max(my_list)}')
    if len(my_list) == 0:
        print('This list is empty')
    else:
        max = 0
        for i in my_list:
            if i > max:
                max = i
        # print(f'Minimum: {min(my_list)}')
        print(f'Maximum: {max}')
        min = max
        for i in my_list:
            if i < min:
                min = i
        print(f'Minimum: {min}')
        # print(f'Average: {sum(my_list)/len(my_list)}')
        sum = 0
        for i in my_list:
            sum += i
        print(f'Average: {sum/len(my_list)}')

calculator(my_list)