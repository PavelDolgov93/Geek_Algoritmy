# 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
#
# На примере задания 3 урока 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы
#
# Windows 10 64-разрядная
# Python 3.7.1
#
# Использовать словарь было удобно, но заметный проигрыш по памяти

import random
import sys

def show_size(x):
    result_size = 0
    result_size += sys.getsizeof(x)

    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                result_size += show_size(key)
                result_size += show_size(value)
        elif not isinstance(x, str):
            for item in x:
                result_size += show_size(item)

    return result_size

def use_dict():

    SIZE = 10
    MIN_ = 10
    MAX_ = 99

    array = [random.randint(MIN_, MAX_) for _ in range(SIZE)]

    dict_index_value = {'max_index':0, 'min_index':0}
    #dict_index_value = {'max_value': array[0], 'max_index': 0, 'min_value': array[0], 'min_index': 0}

    for index in range(1, SIZE):

        if array[index] > array[dict_index_value['max_index']]:
            #dict_index_value['max_value'] = array[index]
            dict_index_value['max_index'] = index

        elif array[index] < array[dict_index_value['min_index']]:
            #dict_index_value['min_value'] = array[index]
            dict_index_value['min_index'] = index

    print(array)
    print(dict_index_value)

    array[dict_index_value['min_index']], array[dict_index_value['max_index']] = array[dict_index_value['max_index']], array[dict_index_value['min_index']]
    #array[dict_index_value['min_index']] = dict_index_value['max_value']
    #array[dict_index_value['max_index']] = dict_index_value['min_value']

    result_size = 0
    result_size += show_size(SIZE) # 14
    result_size += show_size(MIN_) # 14
    result_size += show_size(MAX_) # 14
    result_size += show_size(index) # 14
    result_size += show_size(array) # 240
    result_size += show_size(dict_index_value) # 232
    print(f'Размер: {result_size}') # 528

    return array


def use_var():
    SIZE = 10
    MIN_ = 10
    MAX_ = 99

    array = [random.randint(MIN_, MAX_) for _ in range(SIZE)]

    max_index = 0
    min_index = 0

    for index in range(1, SIZE):

        if array[index] > array[max_index]:
            #max_value = array[index]
            max_index = index

        elif array[index] < array[min_index]:
            #min_value = array[index]
            min_index = index

    print(array)
    print(f'max_value: {array[max_index]}, min_value: {array[min_index]}')

    array[min_index], array[max_index] = array[max_index], array[min_index]

    result_size = 0
    result_size += show_size(SIZE) # 14
    result_size += show_size(MIN_) # 14
    result_size += show_size(MAX_) # 14
    result_size += show_size(index) # 14
    result_size += show_size(array) # 240
    result_size += show_size(min_index) # 14
    result_size += show_size(max_index) # 14
    print(f'Размер: {result_size}') # 324

    return array


print(use_dict())
print("\n")
print(use_var())