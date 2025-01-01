"""
Topic: Рекурсия

Description: Факториал — это положительное целое число n, обозначаемое n!.
             Тогда произведение всех положительных целых чисел, меньших или равных n.

Input: Передается n - число факториал которого надо найти.

Output: Необходимо вывести факториал этого числа.

Time complexity: O(n).

Example:
    :Test_1:
    Input: 5

    Output: 120

"""

n = int(input())



def func_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


answer = factorial(n)
print(answer)