|                      |       |
|----------------------|-------|
| **Time limit:**      | `1 s` |
| **Real time limit:** | `5 s` |
| **Memory limit:**    | `64M` |


### Problem sm08-1: c/floats/fpclass-1

Дан следующий перечислимый тип, описывающий классификацию значений типа float:

    
    
    typedef enum FPClass
    {
        FFP_ZERO,         // нули
        FFP_DENORMALIZED, // числа в денормализованной форме
        FFP_NORMALIZED,   // числа в нормализованной форме
        FFP_INF,          // бесконечности
        FFP_NAN           // NaN-ы
    } FPClass;
    

Напишите следующую функцию:

    
    
    FPClass fpclassf(float value, int *psign);
    

Функция на вход принимает число `value` типа `float` и возвращает значение, соответствующее классу
этого числа. Если число не является `NaN`, то в переменную `psign` возвращается знак числа (0 для
неотрицательных чисел, любое ненулевое значение для отрицательных). Для чисел `NaN` знак всегда
должен быть 0.

При сдаче функции на проверку должно присутствовать только тело функции. Ни определение
перечислимого типа `FPClass`, ни функция `main` присутствовать не должна.

Запрещается использовать стандартные функции и расширения gcc для классификации чисел.

Запрещается использовать значения вещественных типов как аргументы любых операторов, кроме оператора
присваивания `=` и оператора взятия адреса `&`. Например:

    
    
    float copy_f = value;            // можно
    float *ptr = &value;         // можно
    bool small = (value < 1e-38); // нельзя использовать оператор < с вещественными аргументами
    

