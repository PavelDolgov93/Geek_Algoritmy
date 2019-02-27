#
#9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

COLUMNS = 3
ROWS = 4
MIN_ = 1
MAX_ = 9

matr = [[random.randint(MIN_, MAX_) for _ in range(COLUMNS)] for _ in range(ROWS)]

max_min_column = 0

for i_column in range(COLUMNS):

    min_column = matr[0][i_column]

    for i_row in range(1, ROWS):

        if min_column > matr[i_row][i_column]:
            min_column = matr[i_row][i_column]

    if max_min_column < min_column:
        max_min_column = min_column

for array in matr:
    print(array)

print(max_min_column)
