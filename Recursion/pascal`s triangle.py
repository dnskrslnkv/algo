"""
Topic: Рекурсия

Description: Треугольник Паскаля — это метод определения биномиальных коэффициентов членов биномиального выражения (x + y)^n,
             где n может быть любым положительным целым числом, а x и y — действительными числами.

Input: Передается n - число строк треугольника Паскаля.

Output: Необходимо вывести первые n биномиальных коэффициентов .

Time complexity: O(n^2).

Example:
    :Test_1:
    Input: 5

    Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

"""



from math import factorial


def getting_coeff(num):
    return [i for i in range(num+1)]

def pascal_triangle(number:int) -> list:
    answer = []
    for k in range(number):
        period = []
        coeff = getting_coeff(k)
        for el in coeff:
            num = int(factorial(k)/(factorial(k-el)*factorial(el)))
            period.append(num)
        answer.append(period)
    return answer



answer = pascal_triangle(5)
print(answer)



