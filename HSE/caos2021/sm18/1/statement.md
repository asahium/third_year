|                      |       |
|----------------------|-------|
| **Time limit:**      | `1 s` |
| **Real time limit:** | `5 s` |
| **Memory limit:**    | `64M` |


### Problem sm18-1: asm/atomic/spinlock

Реализуйте спинлок.

Напишите на языке ассемблера x86 функции с такими сигнатурами:

    
    
    void spin_lock(volatile int *s);
    void spin_unlock(volatile int *s);

Пользователи будут вызывать эти функции, чтобы создать в коде критическую секцию с активным
ожиданием:

    
    
    int s = 0;
    ...
    spin_lock(&s);
    // critical section here
    spin_unlock(&s);

Тестирующая программа запускает с помощью `fork()` 10 процессов, которые конкурируют за спинлок в
общем участке памяти.

(Идея: попробуйте сделать две реализации, одну с помощью инструкции xchg, а другую с помощью
cmpxchg, и сравните ощущения.)

