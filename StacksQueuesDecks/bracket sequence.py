"""
Topic: Стэк

Description: Рассмотрим последовательность, состоящую из круглых, квадратных и фигурных скобок.
             Программа должна определить, является ли данная скобочная последовательность правильной.
             Пустая последовательность является правильной. Если A — правильная,
             то последовательности (A), [A], {A} — правильные.
             Если A и B — правильные последовательности, то последовательность AB — правильная

Input: В единственной строке записана скобочная последовательность, содержащая не более 100000 скобок.

Output: Если данная последовательность правильная, то программа должна вывести строку "yes", иначе строку "no".

Time complexity: O(n)

Example:
    :Test_1:
    Input: ()[]

    Output: yes

    :Test_2:
    Input:  ([)]

    Output: no

    :Test_3:
    Input:  (

    Output: no


"""



some_str = input()


def bracket_sequence(some_str: str) -> str:
    my_stack = []

    example = {
        ')': '(',
        '}': '{',
        ']': '[',
    }
    for el in some_str:
        if el == '(' or el == '{' or el == '[':
            my_stack.insert(0, el)
        elif el == ')' or el == '}' or el == ']':
            if len(my_stack) == 0:
                return 'no'
            else:
                if example[el] == my_stack[0]:
                    my_stack.pop(0)
                else:
                    return 'no'
    if len(my_stack) == 0:
        return 'yes'
    else:
        return 'no'

answer = bracket_sequence(some_str)
print(answer)
