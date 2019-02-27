#
#3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы

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

print(array)
print(dict_index_value)

array[dict_index_value['min_index']] = dict_index_value['max_value']
array[dict_index_value['max_index']] = dict_index_value['min_value']

print(array)
