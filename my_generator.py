# def simple_gen():
#     yield 'Oh'
#     yield 'Hello'
#     yield 'there!'
#
#
# [print(i) for i in simple_gen()]

import timeit


CORRECT_COMBO = (5, 3, 7)
found_combo = False
for c1 in range(10):
    if found_combo:
        break
    for c2 in range(10):
        if found_combo:
            break
        for c3 in range(10):
            if (c1, c2, c3) == CORRECT_COMBO:
                #print('Found the combo: {}'.format((c1, c2, c3)))
                found_combo = True
                break

# below is a code that does the same thing. It finds the code and stops. But this one is slower.
CORRECT_COMBO = (5, 3, 7)
def combo_gen():
    for c1 in range(10):
        for c2 in range(10):
            for c3 in range(10):
                yield (c1, c2, c3)

for (c1, c2, c3) in combo_gen():
    if (c1, c2, c3) == CORRECT_COMBO:
        #print('Found the combo: {}'.format((c1, c2, c3)))
        break

# print(timeit.timeit(code1, number=10000))
# print(timeit.timeit(code2, number=10000))