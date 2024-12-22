"""
Topic: Линейный поиск

Description: Дана cтрока (возможно пустая), состоящая из букв A-Z. Необходимо написать функцию RLE.
             Если симол встречается 1 раз, он остается без изменений. Если символ встречается более одного раза, к нему
             добавляется количество повторений.

Input: В первой строке подается строка (возможно пустая).

Output: Вывести строку сжатую по RLE алгоритму.

Time complexity: O(n)

Example:
    :Test_1:
    Input: aaaaAAdfcccEW


    Output: a4A2dfc3EW

"""

some_str = input()

#Упростим задачу. Напишем функцию которая оставляет уникальные буквы.

def func_one_level(some_str):
    last_sym=some_str[0]
    ans = []
    for i in range(1,len(some_str)):
        if some_str[i] != last_sym:
            ans.append(last_sym)
            last_sym = some_str[i]
    ans.append(last_sym)
    return " ".join(ans)


# Основываясь на упрощенную задачу. Отмасштабируем ее на основую задачу

def rle(some_str):
    def pack(some_str, cnt):
        if cnt > 1:
            return some_str+str(cnt)
        return some_str

    last_sym = some_str[0]
    last_pos = 0
    ans = []

    for i in range(1, len(some_str)):
        if some_str[i] != last_sym:
            ans.append(pack(last_sym, i-last_pos))
            last_sym = some_str[i]
            last_pos = i
    ans.append(pack(some_str[last_pos], len(some_str)-last_pos))
    return "".join(ans)


answer = rle(some_str)
print(answer)