"""
Topic: Рекурсия

Description: Последовательность Фибоначчи - это последовательность, в которой следующий член является суммой двух предыдущих членов.

Input: Передается n - номер числа в последовательности Фибоначчи .

Output: Необходимо вывести число последовательности Фибоначчи под номером n.

Time complexity: O(2^n).

Example:
    :Test_1:
    Input: 7

    Output: 13

"""

n = int(input())

def Fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)

answer = Fibonacci(n)
print(answer)