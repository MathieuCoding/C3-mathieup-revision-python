# Compréhension de liste : Utilisez la compréhension de liste de 10 éléments dans laquelle il faudra calculer le nombre élevé au carré de chaque élément

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def square(my_list):
    if len(my_list) == 0:
        print('This list is empty')
    for i in my_list:
        print(i * i)

square(my_list)