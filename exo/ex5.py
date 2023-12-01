# Fonctions : Écrivez une fonction qui calcule le factoriel d'un nombre.

def factorial(n):
    if n is not int:
        return 'Please enter an integer'
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))