|                      |       |
|----------------------|-------|
| **Time limit:**      | `1 s` |
| **Real time limit:** | `1 s` |
| **Memory limit:**    | `64M` |


### Problem sm14-3: unix/signal/signal-9

Программа должна напечатать на стандартный поток вывода свой PID и перейти в режим ожидания
поступления сигналов.

При поступлении сигнала SIGUSR2 программа должна увеличивать счетчик поступления сигнала SIGUSR2.

При поступлении сигнала SIGUSR1 программа должна вывести на стандартный поток вывода счетчик
поступлений сигнала SIGUSR1 и счетчик поступления сигнала SIGUSR2, затем увеличить счетчик
поступления сигнала SIGUSR1.

При поступлении сигнала SIGTERM программа не должна ничего выводить и должна завершить работу с
кодом завершения 0.

Обработчики сигналов не должны выполнять никаких действий, кроме изменения значений глобальных
переменных. Ожидание поступления сигналов выполняйте с помощью `sigsuspend`.

Стандартный поток вывода вашей программы будет перенаправлен в канал. Не забывайте выводить
разделитель после вывода чисел и сбрасывать буфер вывода.

