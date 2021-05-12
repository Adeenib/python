students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]
# iterateDictionary(students)
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel


# def iterateDictionary(students):
#     for student in students:
#         print(
#             f"first name -{student['first_name']} and the last name :{student['last_name']}", end="\n")


# iterateDictionary(students)

def iterateDictionary(students):
    for student in students:
        for key, value in student.items():
            print(f"{key} -{value} ", end=", ")
        print("")


iterateDictionary(students)
