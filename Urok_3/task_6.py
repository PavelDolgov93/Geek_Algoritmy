#
#6. В одномерном массиве найти сумму элементов,
# находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

SIZE = 10
MIN_ = 10
MAX_ = 99

array = [random.randint(MIN_, MAX_) for _ in range(SIZE)]

dict_index_value = {'max_value':array[0], 'max_index':0, 'min_value':array[0], 'min_index':0}

for index in range(1, SIZE):

    if array[index] > dict_index_value['max_value']:
        dict_index_value['max_value'] = array[index]
        dict_index_value['max_index'] = index

    elif array[index] < dict_index_value['min_value']:
        dict_index_value['min_value'] = array[index]
        dict_index_value['min_index'] = index

sum_between = 0
diff = dict_index_value['min_index'] - dict_index_value['max_index']

if abs(diff) == 1 or diff == 0:
    pass

else:
    if diff < 0:
        start = dict_index_value['min_index'] + 1
        stop = dict_index_value['max_index']

    else:
        start = dict_index_value['max_index'] + 1
        stop = dict_index_value['min_index']


    for index in range(start, stop):
        sum_between += array[index]

print(array)
print(dict_index_value)
print(sum_between)
