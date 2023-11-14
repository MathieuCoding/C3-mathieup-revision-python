# Dictionnaires : Créez un dictionnaire avec des noms d'élèves et leurs notes. Trouvez l'élève avec la meilleure note.
# ex : si Homonyme 1ᵉʳ élève par ordre alphabétique en se basant sur le nom et ensuite le prénom

students_marks = {
    "Dupont Alice": 17,
    "Dubois Bob": 14,
    "Martin Claire": 18,
    "Smith David": 11,
    "Johnson Emma": 16,
    "Garcia Franck": 14,
    "Brown Grace": 19,
    "Wilson Hugo": 15,
    "Anderson Iris": 16,
    "Thomas Jack": 13,
    "Evans Kelly": 18,
    "Perez Louis": 15,
    "Nguyen Mia": 16,
    "Gonzalez Noah": 14,
    "Lee Olivia": 17,
    "Rodriguez Paul": 16,
    "Martinez Quentin": 19,
    "Harris Rose": 15,
    "Dujardin Jean": 19,
    "Dupont Michel": 20
}

def best_student(students_marks):
    if len(students_marks) == 0:
        print('There are no students in this class')
    else:
        best_mark = 0
        best_student = ''
        for i in students_marks:
            if students_marks[i] > best_mark:
                best_mark = students_marks[i]
                best_student = i
        print(f'The best student is {best_student} with a mark of {best_mark}')

best_student(students_marks)