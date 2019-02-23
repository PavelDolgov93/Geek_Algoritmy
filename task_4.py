#
#4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125...
# Количество элементов (n) вводится с клавиатуры.

n = int(input("Кол-во элементов: "))
q = -0.5

i = 0
tekushee = -2
summa = 0

while i < n:

    tekushee = tekushee * q
    summa = summa + tekushee

    i = i + 1

print(summa)


#for i in range(1, n+1):
#    print( q**(i - 1) )
#print( (q**n - 1) / (q - 1) )