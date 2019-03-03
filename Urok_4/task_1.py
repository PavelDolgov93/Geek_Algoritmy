#1. Проанализировать скорость и сложность одного любого алгоритма,
# разработанных в рамках домашнего задания первых трех уроков.
# На примере задания 4 урока 3: Определить, какое число в массиве встречается чаще всего.

import random
import cProfile

def ver_dict(size):
    MIN_ = 10
    MAX_ = 99

    array = [random.randint(MIN_, MAX_) for _ in range(size)]

    dict_count = {array[0]:0}
    max_count = 0
    max_item = 0

    for item in array:

        if dict_count.get(item) is None:
            dict_count[item] = 0

        dict_count[item] += 1

        if dict_count[item] > max_count:
            max_count = dict_count[item]
            max_item = item

    # python -m timeit -n 20 -s "import task_1" "task_1.ver_dict(1000)"
    # 20 loops, best of 5: 3.18 msec per loop

    # python -m timeit -n 20 -s "import task_1" "task_1.ver_dict(10000)"
    # 20 loops, best of 5: 32.9 msec per loop

    # python -m timeit -n 20 -s "import task_1" "task_1.ver_dict(100000)"
    # 20 loops, best of 5: 337 msec per loop

    # Увеличение количества элементов массива в 10 раз
    # привело к увеличению времени выполнения в 10 раз
    # То есть, сложность алгоритма O(n)


def ver_cycle(size):
    MIN_ = 10
    MAX_ = 99

    array = [random.randint(MIN_, MAX_) for _ in range(size)]

    max_count = 0
    max_item = 0

    for i in range(size):
        curr_count = 1

        for j in range(i+1, size):
            if array[i] == array[j]:
                curr_count += 1

        if curr_count > max_count:
            max_count = curr_count
            max_item = array[i]

    # python - m timeit - n 20 - s "import task_1" "task_1.ver_cycle(100)"
    # 20 loops, best of 5: 1.19 msec per loop

    # python -m timeit -n 20 -s "import task_1" "task_1.ver_cycle(1000)"
    # 20 loops, best of 5: 111 msec per loop

    # python -m timeit -n 20 -s "import task_1" "task_1.ver_cycle(5000)"
    # 20 loops, best of 5: 2.79 sec per loop

    # Увеличение количества элементов массива в 10 раз
    # привело к увелечению времени выполнения в 100 раз
    # Увеличение количества элементов массива в 5 раз
    # привело к увелечению времени выполнения в 25 раз
    # То есть, сложность алгоритма O(n**2)

# ver_dict(10)
# ver_cycle(10)

#cProfile.run('ver_cycle(1000)')

