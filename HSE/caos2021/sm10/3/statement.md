|                      |       |
|----------------------|-------|
| **Time limit:**      | `1 s` |
| **Real time limit:** | `5 s` |
| **Memory limit:**    | `64M` |


### Problem sm10-3: unix/filesystem/filter-dir-6

В аргументах командной строки задается путь к каталогу.

На стандартный поток вывода напечатайте суммарный размер всех файлов в заданном каталоге (без
подкаталогов), удовлетворяющих следующему условию:

* Файл регулярный (для символической ссылки - файл, на который указывает ссылка).
* Его владельцем является текущий пользователь (для символической ссылки нужно учитывать владельца того файла, на который указывает ссылка).
* Его имя начинается с заглавной латинской буквы (для символической ссылки - имя самой ссылки).

Для получения идентификатора пользователя процесса используйте системный вызов `getuid`.

Символические ссылки прослеживайте до соответствующих файлов (используйте соответствующий системный
вызов семейства *stat).

Не используйте системные вызовы, меняющие текущий каталог процесса.

Не используйте функции `readlink` и `realpath`, а также функции, напрямую работающие с файловыми
дескрипторами (`fdopendir`, `fstatat` и подобные).

