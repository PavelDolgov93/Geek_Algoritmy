#2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования «Решета Эратосфена»;
# Используя алгоритм «Решето Эратосфена»

import math

def no_sieve(i):

    curr_prime = 2
    curr_i = 1
    curr_num = 3

    while curr_i < i:

        is_prime = True
        for num in range(2, math.trunc(math.sqrt(curr_num))+1):
            if curr_num % num == 0:
                is_prime = False
                break

        if is_prime == True:
            curr_prime = curr_num
            curr_i += 1

        curr_num += 2

    return curr_prime

    # python -m timeit -n 20 -s "import task_2" "task_2.no_sieve(1000)"
    # 20 loops, best of 5: 9.08 msec per loop

    # python -m timeit -n 20 -s "import task_2" "task_2.no_sieve(2000)"
    # 20 loops, best of 5: 24.1 msec per loop

    # python -m timeit -n 20 -s "import task_2" "task_2.no_sieve(5000)"
    # 20 loops, best of 5: 109 msec per loop

    # python -m timeit -n 20 -s "import task_2" "task_2.no_sieve(10000)"
    # 20 loops, best of 5: 365 msec per loop

    # Время выполнения возрастает заметней, чем при использовании "решета"
    # Использование "решета" считаю предпочтительней


def sieve(i):

    # Вероятность, что число будет простым в диапозоне [1; n] = 1 / ln(n)
    # Значит количество простых чисел (i) в диапозоне [1; n] = n / ln(n)
    # Не смог придумать как высчитать n из n / ln(n) = i, зная i
    # поэтому перебираю n

    n = 10
    max_i = 4
    while max_i < i:
        max_i = math.trunc(n / math.log(n))
        n *= 2

    curr_i = 1
    array = [num for num in range(n)]
    array[1] = 0
    for num in range(2, n):
        if array[num] != 0:

            if curr_i == i:
                return num

            curr_i += 1

            j = num + num

            while j < n:
                array[j] = 0
                j += num

    # python -m timeit -n 20 -s "import task_2" "task_2.sieve(1000)"
    # 20 loops, best of 5: 7.71 msec per loop

    # python -m timeit -n 20 -s "import task_2" "task_2.sieve(2000)"
    # 20 loops, best of 5: 16.5 msec per loop

    # python -m timeit -n 20 -s "import task_2" "task_2.sieve(5000)"
    # 20 loops, best of 5: 76.8 msec per loop

    # python -m timeit -n 20 -s "import task_2" "task_2.sieve(10000)"
    # 20 loops, best of 5: 162 msec per loop


#print(no_sieve(1000))
#print(sieve(1000))

# for i in range(1, 1001):
#     if no_sieve(i) != sieve(i):
#         print(i)
