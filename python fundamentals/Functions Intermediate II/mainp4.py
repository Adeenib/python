dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


def printInfo(some_dict):
    for key, valus in some_dict.items():
        print(f'{len(valus)} {key}')
        for valu in valus:
            print(valu, end="\n")
        print("")


printInfo(dojo)
