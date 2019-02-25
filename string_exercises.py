names = ['Lucas', 'Carol', 'Ana', 'Carla']

# for name in names:
    # print('Hello there, ' + name + '!')
    # print(''.join(['Hello there, ', name, '!']))

# print(', '.join(names))

import os

location_of_files = '/Users/lucasfonseca/PycharmProjects/IntermediateTutorials/'
file_name = 'my_file.txt'

# print(location_of_files + '/' + file_name)

# with open(os.path.join(location_of_files, file_name)) as f:
#     print(f.read())

who = 'Lucas'
how_many = 12

# Lucas bought 12 apples today!

# sentence = {}

print('{} bought {} apples today!'.format(who, how_many))