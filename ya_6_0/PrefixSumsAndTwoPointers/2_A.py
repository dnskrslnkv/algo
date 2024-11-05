"""
Topic: Префиксные суммы

Description: Дана последовательность чисел. Вычислить последовательность ее префиксных сумм.

Input: В первой строке дано целое число n  — количество элементов в последовательности.
       Во второй строке дано n целых чисел — элементы последовательности.

Output: Выведите n целых чисел — последовательность префиксных сумм для последовательности.

Time complexity: O(n)

Example:
    :Test_1:
    Input:  5
            10 -4 5 0 2

    Output: 10 6 11 11 13

"""


k = int(input())
arr = list(map(int, input().split()))


def solution(arr: list, k: int) -> str:
    ans = [0]*k
    ans[0] = arr[0]
    for i in range(1, len(arr)):
        ans[i] = ans[i-1]+arr[i]
    return ' '.join(map(str, ans))



answer = solution(arr, k)
print(answer)