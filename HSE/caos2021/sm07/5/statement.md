|                      |        |
|----------------------|--------|
| **Time limit:**      | `2 s`  |
| **Real time limit:** | `5 s`  |
| **Memory limit:**    | `512M` |


### Problem sm07-5: c/mem/gc

Напишите mark-and-sweep garbage collector (сборщик мусора), который находит динамически выделенные
области памяти, которые более не достижимы, и освобождает их.

Как известно, большой сложностью при программировании на языках с явным управлением памятью является
необходимость явно управлять памятью. Она приводит к таким проблемам, как утечки памяти (memory
leaks), использование ранее освобождённой динамической памяти (use after free), повторное
освобождение области памяти (double free) и другие способы испортить кучу (heap corruption).
Хотелось бы, чтобы компьютер как-нибудь сам следил, какие области динамической памяти нам ещё нужны,
а какие не нужны и могут быть освобождены.

Будем называть _аллокацией_ область памяти, полученную в результате вызова `malloc`. Для каждой
аллокации будем хранить такие сведения:

    
    
    typedef void (*finalizer_t)(void *ptr, size_t size);
    
    struct allocation {
        void *ptr; // указатель на область памяти
        size_t size; // размер
        finalizer_t finalizer; // функция, которую следует вызвать перед free
        bool alive; // достижимость
    };

Указатель `ptr` считается указателем на аллокацию `A`, если содержит адрес любого байта внутри
аллокации или байта сразу после аллокации:

    
    
    bool points_to(void *ptr, struct allocation *A) {
        uintptr_t uptr = (uintptr_t)ptr, aptr = (uintptr_t)A->ptr;
        return (uptr >= aptr) && (uptr - aptr <= A->size);
    }

Аллокация считается достижимой, если указатель на неё есть в стеке либо в другой достижимой
аллокации. Учитываются только правильно выровненные указатели (хранящиеся в памяти по адресам,
кратным `alignof(void *)`).

Сдаваемый файл должен содержать реализации функций `gc_init`, `gc_malloc` и `gc_collect_impl`,
[объявленных](https://caos.myltsev.ru/cgi-bin/new-
client?SID=0dec847c8597efd6&prob_id=46&action=194&file=gc.h) таким образом:

    
    
    void gc_init(char **argv);
    void *gc_malloc(size_t size, finalizer_t finalizer);
    void gc_collect_impl(uintptr_t stack_top);

Программа, которая использует ваш сборщик мусора, обязана в функции main вызвать `gc_init` с
параметром argv. Известно, что массив аргументов командной строки лежит внизу стека (по адресу,
большему, чем адреса любых автоматических переменных), так что argv можно использовать как указатель
на дно стека.

Функция `gc_malloc` вызывает `malloc` с переданным ей параметром `size` и в случае успешной
аллокации (когда malloc вернул не NULL) записывает сведения об этой аллокации в свои структуры
данных (которые вам предстоит определить).

Функция `gc_collect_impl` работает следующим образом.

* Помечает все известные ей аллокации как недостижимые.
* Проходит по стеку от `stack_top` (указатель на верхушку стека) до `stack_bottom` (указатель на дно стека) и пытается интерпретировать каждые `sizeof(void *)` байт из стека как указатель. Если это указатель на некоторую известную аллокацию A, то она помечается как достижимая.
* Таким же образом проходит по всем достижимым аллокациям, находя в них указатели и помечая достижимые аллокации.
* Для каждой недостижимой аллокации `A` вызывает `A.finalizer(A.ptr, A.size)` (если finalizer не NULL) и `free(A.ptr)`, а затем удаляет сведения об аллокации. Недостижимые аллокации можно удалять в любом порядке.

`gc_collect_impl` будет вызываться с помощью ассемблерной обёртки
[`gc_collect`](https://caos.myltsev.ru/cgi-bin/new-
client?SID=0dec847c8597efd6&prob_id=46&action=194&file=wrapper.S), которая сохраняет в стек значения
callee-saved регистров и передаёт корректный указатель на верхушку стека `stack_top`. Таким образом,
искать указатели в регистрах не придётся.

Программе запрещено вызывать realloc и free для тех областей памяти, которые были получены с помощью
`gc_malloc`. Программа может хранить указатели на такие области памяти в глобальных и статических
переменных (т. е. не в стеке), но сборщик мусора не будет учитывать такие указатели (не будет
считать достижимой область памяти, указатель на которую есть только в глобальной переменной).

