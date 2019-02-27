#
#7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

import random

SIZE = 10
MIN_ = 10
MAX_ = 99

array = [random.randint(MIN_, MAX_) for _ in range(SIZE)]

if array[0] < array[1]:
    dict_index_value = {'min_value': array[0], 'min_value2': array[1]}
else:
    dict_index_value = {'min_value': array[1], 'min_value2': array[0]}

for index in range(2, SIZE):

    if array[index] <= dict_index_value['min_value']:
        dict_index_value['min_value2'] = dict_index_value['min_value']
        dict_index_value['min_value'] = array[index]

    elif array[index] <= dict_index_value['min_value2']:
        dict_index_value['min_value2'] = array[index]

print(array)
print(dict_index_value)