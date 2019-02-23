#
#8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

def skolko_raz(chislo, cifra):
    kolvo_raz = 0

    while chislo != 0:
        if chislo % 10 == cifra:
            kolvo_raz = kolvo_raz + 1

        chislo = chislo // 10

    return kolvo_raz

kolvo_raz = 0

kolvo_chisel = int(input('Кол-во чисел: '))
cifra = int(input('Цифра поиска: '))
print('Натуральные числа:')

for i in range(kolvo_chisel):
    chislo = int(input(f'{i+1}) '))
    kolvo_raz = kolvo_raz + skolko_raz(chislo, cifra)

print(f'Встречается раз: {kolvo_raz}')