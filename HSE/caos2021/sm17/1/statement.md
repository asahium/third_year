|                      |          |
|----------------------|----------|
| **Time limit:**      | `200 ms` |
| **Real time limit:** | `2 s`    |
| **Memory limit:**    | `256M`   |


### Problem sm17-1: unix/pthread/create-10-1

Функция `main` должна создать 10 нитей. Каждая нить должна напечатать на стандартный поток вывода
свой порядковый номер (целое число от 0 до 9) на отдельной строке.

Функция `main` должна ждать не более одной нити (делать не более одного вызова `pthread_join`).
Например, не допускается вариант, когда в цикле функция `main` создает нить и сразу же дожидается ее
завершения.

Нити должны работать в таком порядке, чтобы порядковые номера нитей всегда выводились в возрастающем
порядке. Таким образом, программа всегда должна выводить:

    
    
    0
    1
    2
    3
    4
    5
    6
    7
    8
    9
    

Разрешается использовать только функции `pthread_create` и `pthread_join`. Не используйте активное
ожидание.

В этой задаче решение может получить статус Presentation error, если оно не соответствует условию.

