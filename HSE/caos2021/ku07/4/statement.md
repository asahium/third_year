|                      |       |
|----------------------|-------|
| **Time limit:**      | `1 s` |
| **Real time limit:** | `1 s` |
| **Memory limit:**    | `64M` |


### Problem ku07-4: kr07-4 (дореш)

Напишите функцию `void fd_watcher(const struct file_t* files, size_t n) `, которая слушает указанные
дескрипторы на чтение и на каждые 2048 байт выводит результат функции `void some_hash(char* data,
size_t n, char* out) ` на стандартный вывод. Функция some_hash предоставляется извне. Указатель
`char* out` должен быть предоставлен вами. Количество памяти, необходимое указателю, вы должны
получить из функции `size_t get_hash_size()`.

Структура file_t определена так:

    
    
    struct file_t {
        int fd;
        char* filename;
    };

Программа должна для каждого отдельного блока вывести строку
`[{filename}]\t[{block_number}]\t{hash}`, где filename - имя файла, к которому относится блок,
block_number - номер блока в файле, hash - значение хэш-функции от этого блока.

После получения EOF из файла этот файл больше не нужно прослушивать. Функция должна работать до тех
пор, пока не получит сигнал на завершение. Особым образом сигнал обрабатывать не надо, закрывать
дескрипторы тоже.

Гарантируется, что все дескрипторы валидные, а имена файлов - null-terminated строки. Все
дескрипторы открыты в неблокирующем режиме. Гарантируется, что количество полученных из каждого
дескриптора байтов кратно 2048. Гарантируется, что file_t.filename - null-terminated строка.
Гарантируется, что char* out после вызова функции some_hash - null-terminated строка.

Вывод программы перенаправлен в канал. Сбрасывайте буфер после вывода каждого блока.

### Examples

#### Input

    
    
    fd_watcher({ {3, "some_file.bin"} }, 1);

#### Output

    
    
    [some_file.bin]\t[1]\tthis_block_is_even
    [some_file.bin]\t[2]\tthis_block_is_odd
    

