|                      |       |
|----------------------|-------|
| **Time limit:**      | `1 s` |
| **Real time limit:** | `5 s` |
| **Memory limit:**    | `64M` |


### Problem sm02-2: asm/data-structures/list-reverse

Напишите подпрограмму list_reverse, которая разворачивает односвязный список. На проверку следует
сдать только файл с подпрограммой, без функции main.

Элемент списка хранится в памяти в виде трёх 32-битных машинных слов: (1-2) произвольные 64-битные
данные, (3) адрес следующего элемента списка или 0. В программе определена глобальная переменная
head, в которой хранится адрес начала списка. Подпрограмма должна развернуть список inplace и
записать в head новый адрес его начала.

