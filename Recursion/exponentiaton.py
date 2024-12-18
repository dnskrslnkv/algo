"""
Topic: Рекурсия

Description: Рекурсивный подход к алгоритму возвведения числа в степень. По сути применение рекуретного соотношения:
             a^(n) = a*a^(n-1).

Input: Строкой передается число a и степень n, в которую необходимо возвести число a .

Output: Необходимо вывести a^n.

Time complexity: O(log(n)).

Example:
    :Test_1:
    Input: 8 3

    Output: 512

"""

a, n = map(int, input().split())

def exponentiaton(a, n):
    if n == 0:
        return 1
    else:
        return a*exponentiaton(a, n-1)

answer = exponentiaton(a, n)
print(answer)
