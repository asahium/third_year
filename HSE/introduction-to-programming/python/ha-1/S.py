"""
Даны два момента времени в пределах одних и тех же суток. Для каждого момента указан час, минута и секунда. Известно, что второй момент времени наступил не раньше первого.
Определите сколько секунд прошло между двумя моментами времени.

Формат ввода
Программа на вход получает шесть целых чисел через перевод строки. Первые три целых числа соответствуют часам, минутам и секундам первого момента, следующие три числа соответствуют второму моменту.
Часы задаются числом от 0 до 23 включительно. Минуты и секунды – от 0 до 59.

Формат вывода
Выведите число секунд между этими моментами времени.
"""



a, b, c = int(input()), int(input()), int(input())
x, y, z = int(input()), int(input()), int(input())
print((x-a)*3600 + (y-b)*60 + z - c)
