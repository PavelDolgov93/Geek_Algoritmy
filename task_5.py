#
#5. Вывести на экран коды и символы таблицы ASCII,
# начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.

stroka = ''
nomer = 0
i = 32

while i < 128:

    if nomer == 10:
        print(stroka)
        stroka = ''
        nomer = 0

    stroka = stroka + str(i) + ' - ' + chr(i) + '\t\t'

    nomer = nomer + 1
    i = i + 1

print(stroka)