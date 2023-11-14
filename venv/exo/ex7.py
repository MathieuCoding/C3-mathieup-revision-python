# Fichiers : Écrivez un programme qui lit un fichier texte, compte le nombre de mots et écrit le résultat dans un autre fichier.

with open('file.txt', 'r') as file:
    file_content = file.read()
    result = len(file_content.split(' '))

with open('result.txt', 'w') as file:
    file.write(str(result))
