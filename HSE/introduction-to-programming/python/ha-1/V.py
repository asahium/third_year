"""
Напишите программу, которая считывает два целых числа A и B и выводит наибольшее значение из них. Числа — целые от 1 до 1000.
При решении задачи можно пользоваться только целочисленными арифметическими операциями. Нельзя пользоваться нелинейными конструкциями: ветвлениями, циклами, функциями.

Формат ввода
Вводятся два числа.

Формат вывода
Выведите ответ на задачу.
"""



a, b = int(input()), int(input())
print(int((a * (a // b) + b * (b // a)) / (b // a + a // b)))
