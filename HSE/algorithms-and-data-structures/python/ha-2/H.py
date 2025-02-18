"""
Большой Музей скоро открывает новую выставку, и в связи с этим принято решение сделать апгрейд системы безопасности. Вас назначили ответственным за установку камер видеонаблюдения.
Пространство, отведённое для выставки, представляет собой прямоугольник размера H × W, разделённый на отдельные зоны размера 1 × 1. В каждой зоне планируется разместить ровно один экспонат; ценность экспоната, расположенного в зоне с координатами (i; j), равна Pij. Вы заметили, что все экспонаты имеют различные ценности.
Руководство музея планирует разместить видеокамеры над каждым из экспонатов; для этой цели уже закупили (H ⋅ W) видеокамер, k-я из которых имеет надёжность Qk. Вы заметили, что надёжности всех камер также являются различными.
Разумеется, над более ценными экспонатами следует разместить более надёжные камеры. Более формально, над самым дорогим экспонатом должна быть самая надёжная камера, над вторым по ценности экспонатом — вторая по надёжности камера, и так далее.
Составьте план размещения камер, аналогичный плану размещения экспонатов.

Формат ввода
Первая строка содержит целые числа H и W (1 ≤ H, W ≤ 100) — соответственно высоту и ширину плана выставки.
Следующие H строк описывают план размещения экспонатов. Каждая из них содержит W чисел Pij (1 ≤ Pij ≤ 109) — ценности экспонатов. Все числа Pij различны.
Следующая строка содержит (H ⋅ W) целых чисел Qk (1 ≤ Qk ≤ 109) — величины надёжности купленных камер. Все числа Qk различны.

Формат вывода
Выведите H строк, каждая из которых содержит W чисел — величины надёжности камер, размещаемых над каждым из экспонатов. 
"""



import random


def qsort(a, L, R):
    if R - L <= 1:
        return
    median = a[random.randrange(L, R)]
    m = L
    for i in range(L, R):
        if a[i] < median:
            (a[i], a[m]) = (a[m], a[i])
            m += 1
    qsort(a, L, m)
    qsort(a, m, R)


def qsort_l(a, L, R):
    if R - L <= 1:
        return
    median = a[random.randrange(L, R)][0]
    m = L
    for i in range(L, R):
        if a[i][0] < median:
            (a[i], a[m]) = (a[m], a[i])
            m += 1
    qsort_l(a, L, m)
    qsort_l(a, m, R)


h, w = map(int, input().split())
arr = []
for i in range(h):
    string = list(map(int, input().split()))
    for j in range(w):
        arr.append([string[j], i * w + j])
weight = list(map(int, input().split()))
qsort_l(arr, 0, len(arr))
qsort(weight, 0, len(weight))

for i in range(len(weight)):
    arr[i] = [arr[i][1], weight[i]]
qsort_l(arr, 0, len(arr))

for i in range(h):
    for j in range(w):
        print(arr[i * w + j][1], end=" ")
    print()
