#
#9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

def summa_cifr (chislo):
    summa = 0

    while chislo != 0:
        summa = summa + (chislo % 10)
        chislo = chislo // 10

    return summa

max_summa = 0
max_chislo = 0
print('Натуральные числа:')
n = int(input())
while n != 0:
    summa = summa_cifr(n)
    if max_summa < summa:
        max_summa = summa
        max_chislo = n

    n = int(input())

print(f'Число: {max_chislo} | Сумма цифр: {max_summa}')