# Tri par insertion : Implémentez l'algorithme de tri par insertion, la fonction prendra en paramètre une liste.
# Sur une list contenant des number

my_list = [5, 2, 4, 50, 6, 1, 8, 22, 3, 1, 2, 6]


def insertion_sort(my_list):
    if len(my_list) == 0:
        print('This list is empty')
    else:
        for i in range(1, len(my_list)):
            while i > 0 and my_list[i] < my_list[i-1]:
                my_list[i], my_list[i-1] = my_list[i-1], my_list[i]
                i -= 1
        return my_list


print(insertion_sort(my_list))
