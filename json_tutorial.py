# this tutorial is on https://www.learnpython.org/

import json

simple_string = 'hello world'
numbers = [1, 2, 3, 5]
number_and_chars = ['a', 1, 'b', 3]
my_dict = {'name' : 'Lucas', 'age' : 31}

json_data = json.dumps([simple_string, numbers, number_and_chars, my_dict])
# non_json = json.loads(json_data)


print(json_data)
print(json.loads(json_data)[3]['name'])
[print(data) for data in json.loads(json_data)]

# client
# import pickle
# dict = {...}
# tcp_send(pickle.dumps(dict))
#
# server
# import pickle
# dict = pickle.loads(tcp_recieve())
# If the other end is not written in python, you can use a data serialization format, like xml, json or yaml.