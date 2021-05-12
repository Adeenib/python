students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]


# def iterateDictionary(key_name, other_list): same the next
#     for i in other_list:
#         print(i[key_name])


def iterateDictionary(key_name, students):
    for student in students:
        print(student[key_name])


iterateDictionary('first_name', students)
print("\n")
iterateDictionary('last_name', students)
