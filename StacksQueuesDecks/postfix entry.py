"""
Topic: Дэк

Description: В постфиксной записи (или обратной польской записи) операция записывается после двух операндов.
             Например, сумма двух чисел A и B записывается как A B +. Запись B C + D * обозначает привычное нам (B + C) * D,
             а запись A B C + D * + означает A + (B + C) * D. Достоинство постфиксной записи в том,
             что она не требует скобок и дополнительных соглашений о приоритете операторов для своего чтения.

Input: В единственной строке записано выражение в постфиксной записи, содержащее цифры и операции +, -, *.
       Цифры и операции разделяются пробелами. В конце строки может быть произвольное количество пробелов.

Output: Необходимо вывести значение записанного выражения.

Time complexity: O(n)

Example:
    :Test_1:
    Input: 8 9 + 1 7 - *

    Output: -102

"""

from collections import deque

some_str = (input())


def postfix_entry(some_str: str) -> int:
    my_stack = deque()

    for i in range(len(some_str)):
        if some_str[i] == ' ' and some_str[i + 1] == ' ':
            break
        else:
            if some_str[i] == '+':
                result = int(my_stack[0]) + int(my_stack[1])
                my_stack.popleft()
                my_stack.popleft()
                my_stack.appendleft(result)
            elif some_str[i] == '*':
                result = int(my_stack[0]) * int(my_stack[1])
                my_stack.popleft()
                my_stack.popleft()
                my_stack.appendleft(result)
            elif some_str[i] == '-':
                result = int(my_stack[1]) - int(my_stack[0])
                my_stack.popleft()
                my_stack.popleft()
                my_stack.appendleft(result)
            elif some_str[i] == ' ':
                pass
            else:
                my_stack.appendleft(int(some_str[i]))
    return int(my_stack.popleft())


answer = postfix_entry(some_str)
print(answer)
