# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого это цифры числа.
# Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

# Не придумал как использовать collections

# Вариант: "нормальный"

def plus_multip_16(lst_a, lst_b, action):

    dict_lett_num = {"A":10, "B":11, "C":12, "D":13, "E":14, "F":15,
                     10:"A", 11:"B", 12:"C", 13:"D", 14:"E", 15:"F"}


    def num_16_10_1(num16_1):
        if dict_lett_num.get(num16_1) is not None:
            return dict_lett_num[num16_1]
        return int(num16_1)

    def num_16_10(lst_num16):
        lst_num16 = lst_num16.copy()
        lst_num16.reverse()
        result1 = 0
        for i in range(len(lst_num16)):
            result1 = result1 + (num_16_10_1(lst_num16[i]) * (16 ** i))
        return result1


    def num_10_16_1(num10_1):
        if 9 < num10_1 < 16:
            return dict_lett_num[num10_1]
        else:
            return str(num10_1)

    def num_10_16(num10):
        result1 = []
        while num10 > 15:
            tmp = num10 // 16
            result1.append(num_10_16_1(num10 - (16 * tmp)))
            num10 = tmp

        result1.append(num_10_16_1(num10))
        result1.reverse()
        return result1


    if action == "+":
        return num_10_16(num_16_10(lst_a) + num_16_10(lst_b))
    elif action == "*":
        return num_10_16(num_16_10(lst_a) * num_16_10(lst_b))


a = list(input("Первое число (16): ").upper())
b = list(input("Второе число (16): ").upper())

print(f"Сложение: {plus_multip_16(a, b, '+')}")
print(f"Умножение: {plus_multip_16(a, b, '*')}")
