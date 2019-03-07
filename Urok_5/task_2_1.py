# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого это цифры числа.
# Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

# Не придумал как использовать collections

# Вариант: "в столбик"

def plus_16(lst_a, lst_b):

    dict_lett_num = {"A":10, "B":11, "C":12, "D":13, "E":14, "F":15,
                     10:"A", 11:"B", 12:"C", 13:"D", 14:"E", 15:"F"}

    def num_10_16_1(num10_1):
        if 9 < num10_1 < 16:
            return dict_lett_num[num10_1]
        return str(num10_1)

    def num_16_10_1(num16_1):
        if dict_lett_num.get(num16_1) is not None:
            return dict_lett_num[num16_1]
        return int(num16_1)


    def plus_16_1(a1, b1, addition):
        if addition == True:
            addition, a1 = plus_16_1(a1, 1, False)

        result1 = num_16_10_1(a1) + num_16_10_1(b1)
        if result1 >= 16:
            return True, num_10_16_1(result1 - 16)
        else:
            return addition, num_10_16_1(result1)


    lst_a = lst_a.copy()
    lst_a.reverse()
    lst_b = lst_b.copy()
    lst_b.reverse()

    len_a = len(lst_a)
    len_b = len(lst_b)

    if len_a < len_b:
        lst_a.extend([0 for _ in range(len_b - len_a)])
        len_a = len_b
    else:
        lst_b.extend([0 for _ in range(len_a - len_b)])

    result = [False for _ in range(len_a + 1)]
    for i in range(len_a):
        result[i + 1], result[i] = plus_16_1(lst_a[i], lst_b[i], result[i])

    if result[i + 1] == False:
        result.pop()
    else:
        result[i + 1] = "1"

    result.reverse()
    return result


def multip_16(lst_a, lst_b):

    dict_lett_num = {"A":10, "B":11, "C":12, "D":13, "E":14, "F":15,
                     10:"A", 11:"B", 12:"C", 13:"D", 14:"E", 15:"F"}

    def num_16_10(lst_num16):
        lst_num16 = lst_num16.copy()
        lst_num16.reverse()
        result1 = 0
        for i in range(len(lst_num16)):
            if dict_lett_num.get(lst_num16[i]) is not None:
                lst_num16[i] = dict_lett_num[lst_num16[i]]

            result1 = result1 + (int(lst_num16[i]) * (16 ** i))

        return result1

    a10 = num_16_10(lst_a)
    b10 = num_16_10(lst_b)

    if a10 < b10:
        lst_a, lst_b = lst_b, lst_a
        a10, b10 = b10, a10

    result = lst_a.copy()
    for _ in range(b10 - 1):
        result = plus_16(result, lst_a)

    return result


a = list(input("Первое число (16): ").upper())
b = list(input("Второе число (16): ").upper())

print(f"Сложение: {plus_16(a, b)}")
print(f"Умножение: {multip_16(a, b)}")
