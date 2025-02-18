"""
Петрович часто пользуется услугами ломбарда. Вот и сегодня он понёс туда тёщины часы.
По правилам ломбарда, выкупать заложенные вещи можно только в обратном порядке. Это значит, что принесённый на прошлой неделе канделябр Петрович сможет выкупить только тогда, когда выкупит заложенные сегодня часы.
Петрович пытается вести хоть какой-то учёт отданных вещей, поэтому он попросил вас написать для него программу-помощника.

Формат ввода
Первая строка содержит целое число N (1 ≤ N ≤ 106) — количество запросов.
Следующие N строк описывают запросы:
    Запрос «1 X» означает, что Петрович отдаёт в ломбард вещь стоимостью X (1 ≤ X ≤ 1000, стоимости всех вещей целочисленны);
    Запрос «2» означает, что Петрович выкупает вещь, которую заложил последней. При этом гарантируется, что в ломбарде есть хотя бы одна вещь Петровича;
    Запрос «3» означает, что Петрович хочет узнать суммарную стоимость всех сданных им в ломбард предметов;
    Запрос «4» означает, что Петрович хочет узнать стоимость самой дорогой из вещей, сданных им в ломбард. Если таких вещей несколько, рассматривается стоимость любой из них;
    Запрос «5» означает, что Петрович хочет узнать количество предметов, которые нужно выкупить, чтобы вернуть самую дорогую из вещей в ломбарде. Если таких вещей несколько, рассматривается ближайшая из них (та, возврат которой потребует наименьшего числа выкупов).
Например, если Петрович сдал канделябр за 100 рублей, потом часы за 200 рублей, а затем портсигар за 50 рублей, то:
    Суммарная стоимость заложенных вещей равна 350 рублей;
    Наиболее дорогая заложенная вещь (часы) имеет стоимость 200 рублей;
    Чтобы вернуть самую дорогую вещь, нужно выкупить 2 предмета (портсигар и часы).

Формат вывода
Для каждого из запросов «3», «4» или «5» выведите в отдельной строке одно целое число — соответствующий ответ. Если в некоторый момент времени в ломбарде нет вещей Петровича, то ответом на любой из запросов является число 0. 
"""



import sys


class Lombard:
    def __init__(self):
        self.Stack = []
        self.Max = []
        self.MaxInd = []
        self.summa = 0

    def push(self, x):
        self.Stack.append(x)
        self.summa += x
        if (len(self.Stack) == 1):
            self.Max.append(x)
            self.MaxInd.append(len(self.Stack))
            return
        if (x >= self.Max[-1]):
            self.Max.append(x)
            self.MaxInd.append(len(self.Stack))
        else:
            self.Max.append(self.Max[-1])
            self.MaxInd.append(self.MaxInd[-1])

    def pop(self):
        self.summa -= self.Stack[-1]
        self.Stack.pop()
        self.Max.pop()
        self.MaxInd.pop()

    def isEmpty(self):
        if len(self.Stack) == 0:
            return True
        return False

    def getMostExp(self):
        return self.Max[-1]

    def toGetExp(self):
        return len(self.Stack) - self.MaxInd[-1] + 1

    def getSum(self):
        return self.summa


lom = Lombard()
n = int(sys.stdin.readline())
for i in range(n):
    info = sys.stdin.readline()
    if info == '3\n' or info == '4\n' or info == '5\n':
        if lom.isEmpty():
            print('0')
        else:
            if info == '3\n':
                print(lom.getSum())
            if info == '4\n':
                print(lom.getMostExp())
            if info == '5\n':
                print(lom.toGetExp())
    else:
        lst = info.split()
        if lst[0] == '1':
            lom.push(int(lst[1]))
        else:
            lom.pop()
