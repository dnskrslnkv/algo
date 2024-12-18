"""
Topic: Рекурсия

Description: Алгоритм Евклида — это эффективный метод нахождения наилучшего общего делителя (НОД) двух целых чисел.

Input: Строкой передается два целых числа (через пробел).

Output: Необходимо вывести НОД(целое число) этих чисел.

Time complexity: O(n)=log(min(a,b)), где a, b - целые числа.

Example:
    :Test_1:
    Input: 30 18

    Output: 6

"""

a, b= map(int, input().split())

def gcd(a: int,b:int) -> int:
    if b==0:
        return a
    else:
        return gcd(b, a%b)

answer = gcd(a, b)
print(answer)
