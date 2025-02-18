|                      |       |
|----------------------|-------|
| **Time limit:**      | `1 s` |
| **Real time limit:** | `1 s` |
| **Memory limit:**    | `64M` |


### Problem sm12-5: unix/processes/parse-exec-1

Напишите функцию:

    
    
    int mysystem(const char *cmd);

В параметре `cmd` передается командная строка для запуска. Командная строка содержит аргументы,
разделенные произвольным количеством пробельных символов (см. функцию `isspace`). В начале и конце
строки также может находиться произвольное количество пробельных символов.

Разбейте командную строку на аргументы и запустите ее на выполнение. Запрещается вызывать какие-либо
другие команды (на- пример, интерпретатор командной строки), кроме заданной в командной строке.
Запрещается использовать высокоуровневые средства создания процессов, такие как `system`, `popen`.

Если в командной строке нет ни одного аргумента, функция должна вернуть -1. Если создать процесс не
удалось, функция должна вернуть -1. Если указанную команду запустить не удалось, функция должна
вернуть 1. Если созданный процесс завершился из-за сигнала, необходимо вернуть номер этого сигнала,
к которому прибавлено 1024. В противном случае необходимо вернуть код завершения созданного
процесса. В любом случае, только значение 0 может обозначать нормальное выполнение созданного
процесса.

Используйте системный вызов `execvp`.

Пример: `mysystem("ls .")` должна создать новый процесс, который выведет в stdout содержимое текущей
рвбочей директории.

