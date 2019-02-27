#
#4. Определить, какое число в массиве встречается чаще всего.

import random

SIZE = 10
MIN_ = 1
MAX_ = 5

array = [random.randint(MIN_, MAX_) for _ in range(SIZE)]

dict_count = {array[0]:0}
max_count = 0
max_item = 0

for item in array:

    if dict_count.get(item) == None:
        dict_count[item] = 0

    dict_count[item] += 1

    if dict_count[item] > max_count:
        max_count = dict_count[item]
        max_item = item

print(array)
print(max_item)
