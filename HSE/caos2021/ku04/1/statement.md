|                      |       |
|----------------------|-------|
| **Time limit:**      | `1 s` |
| **Real time limit:** | `5 s` |
| **Memory limit:**    | `64M` |


### Problem ku04-1: kr04-1 (дореш)

Программе задаются три аргумента командной строки.

* Путь `path` к файлу.
* `rows` — число строк матрицы.
* `cols` — число столбцов матрицы.

Гарантируется, что программе передается ровно три аргумента. Гарантируется, что rows и cols —
корректные записи целых чисел от 1 до 1000 включительно.

Программа должна сформировать матрицу из rows строк и cols столбцов вещественных чисел типа double и
сохранить их в выходной файл `path` в бинарном виде точно в том виде, в котором в памяти
располагается двухмерный массив double[rows][cols]. Если выходной файл существует, он
перезаписывается, иначе создается. При создании указываются права на чтение и запись только для
владельца. Значение элемента [i][j] вычисляется по формуле 2*sin(i) + 4*cos(j/2), где i и j
рассматриваются как вещественные числа.

Для заполнения файла отображайте его в память. Запрещается использовать write и аналогичные. Для
изменения размера используйте (f)truncate.

Если выходной файл невозможно открыть или отобразить в память, программа должна завершится с кодом
1, в противном случае - с кодом 0.

Например, при числе строк rows == 2 и столбцов cols == 3 в выходной файл в бинарном виде должна быть
записана следующая последовательность чисел типа double:

    
    
    4
    3.510330247561491
    2.161209223472559
    5.682941969615793
    5.193272217177284
    3.844151193088352

