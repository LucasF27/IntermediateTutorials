# i = range(99999999999999999999999999999)
# print(i[1])

# list
# faster to use, bot slower to initiate
# xyz = [i for i in range(50000000)]
# print('done')

# generator
# slower to use, but faster to initiate
# xyz = (i for i in range(50000000))
# print(xyz)

input_list = [5,6,2,10,15,20,5,2,1,3]

def div_by_five(num):
    if num % 5 == 0:
        return True
    else:
        return False

# generator
# xyz = (i for i in input_list if div_by_five(i))
# print(xyz)

# for i in xyz:
    # print(i)
# or...
# (print(i) for i in xyz)

# list comprehension
xyz = [i for i in input_list if div_by_five(i)]
# print(xyz)
# (print(i) for i in xyz)

# xyz = [[[i,ii] for ii in range(5)] for i in range(3)]
#
# print(xyz[2][4][1])

xyz = (print(i) for i in range(5))
for i in xyz:
    i
