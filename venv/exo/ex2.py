# Manipulation de chaînes : Demandez à l'utilisateur de saisir une phrase, puis affichez la phrase en majuscules, en minuscules et le nombre de mots.
def display_input(user_input):
    print(user_input.upper())
    print(user_input.lower())
    print('There are ', user_input.count(' ') + 1, ' words in your sentence.')

display_input(input("Enter a sentence: "))