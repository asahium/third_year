|                      |       |
|----------------------|-------|
| **Time limit:**      | `1 s` |
| **Real time limit:** | `1 s` |
| **Memory limit:**    | `64M` |


### Problem sm19-5: test-exam/0x05

Программе в аргументах командной строки передаются два имени текстовых файлов. Текстовые файлы
содержат 32-битные знаковые целые числа.

Программа должна создать два процесса-сына, которые параллельно просуммируют числа в соответствующих
файлах. Процессы передают результат отцу, который сначала выводит сумму чисел, полученную от второго
процесса (то есть процесса, запущенного вторым), затем сумму чисел, полученную от первого процесса,
затем сумму этих двух чисел.

Все операции сложения выполняются с 32-битными целыми числами и дают 32-битный результат.
Переполнение игнорируется. Сумма чисел в пустом файле равна 0. Аргументы командной строки корректны,
то есть содержат имена двух файлов, доступных на чтение. Оба файла корректны, то есть все числа в
них представимы 32-битным целым типом, и в файле находятся только числа, разделенные пробельными
символами.

Родитель должен дождаться завершения всех процессов и завершиться сам с кодом 0.

Для пересылки данных и синхронизации разрешается использовать только неименованные каналы. В
программе не должны присутствовать синхронизационные ошибки (гонки, тупики, активное ожидание).
Файловые дескрипторы должны вовремя закрываться.

