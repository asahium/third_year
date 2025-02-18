"""
Электронные часы показывают время в формате h:mm:ss, то есть сначала записывается количество часов, потом обязательно двузначное количество минут, затем обязательно двузначное количество секунд. Количество минут и секунд при необходимости дополняются до двузначного числа нулями.
С начала суток прошло N секунд. Выведите, что покажут часы.

Формат ввода
Вводится число N — целое, положительное, не превышает 107.

Формат вывода
Выведите показания часов, соблюдая формат.
"""



t = int(input())
print((t // 3600) % 24, ":",
      t // 60 % 60 // 10, t //
      60 % 60 % 10, ":",
      t % 60 // 10, t % 10, sep="")
