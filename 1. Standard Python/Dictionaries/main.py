# Traditional Dictionaries
traditional_dict = {'name': 'Superman', 'secret': 'Clark Kent'}

for k in traditional_dict:  # Iterates over the keys only
    print(k)

for k, v in traditional_dict.items():  # Iterates over the keys (k) and values (v)
    print(f'The value of {k} is {v}.')


# Nested Dictionaries
nested_dict = {
    'name': 'Superman',
    'secret': 'Clark Kent',
    'background': {
        'place_of_origin': 'Krypton',
        'currently_resides': 'Metropolis',
    },
    'allies': [
        {
            'name': 'Batman',
            'secret': 'Bruce Wayne',
        },
        {
            'name': 'Wonder Woman',
            'secret': 'Diana Prince',
        }
    ],
}


# Copying and adding to a dictionary
expanded_dict = {'team': 'Justice League', **traditional_dict}


# Making a dictionary from a list of tuples
dict_from_list = dict([('name': 'Superman'), ('secret': 'Clark Kent')])
