|                      |       |
|----------------------|-------|
| **Time limit:**      | `2 s` |
| **Real time limit:** | `5 s` |
| **Memory limit:**    | `64M` |


### Problem sm09-5: asm/floats/dot-product-1

На языке ассемблера напишите подпрограмму `dot_product` со следующим прототипом (на Си):

    
    
    void dot_product(int n, const float *x, const float *y, float *result);

Подпрограмма должна вычислить скалярное произведение векторов x и y, каждый из которых имеет размер
n, и сохранить его по указателю result.

Гарантируется, что n ≥ 0. При n == 0 скалярное произведение полагается равным 0. Указатели x и y не
равны NULL.

Подпрограмма должна соблюдать стандартные соглашения о вызовах. Должен использоваться стандартный
пролог и эпилог функции. Для вычислений используйте векторные операции SSE.

Например, скалярное произведение векторов { 1.5, 3.5 } и { -3.5, 1.0 } равно -1.75.

