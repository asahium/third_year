|                      |       |
|----------------------|-------|
| **Time limit:**      | `1 s` |
| **Real time limit:** | `5 s` |
| **Memory limit:**    | `64M` |


### Problem sm08-2: c/floats/float-split-1

На стандартном потоке ввода задается последовательность вещественных чисел типа float.
Последовательность заканчивается с концом файла.

Для каждого числа на стандартный поток вывода на отдельной строке напечатайте три беззнаковых числа,
выделенных из двоичного представления вещественного числа `float`: бит знака, биты порядка (8 бит),
биты мантиссы (23 бита). Мантиссу выводите в шестнадцатеричном виде.

### Examples

#### Input

    
    
    -6.1235

#### Output

    
    
    1 129 43f3b6

