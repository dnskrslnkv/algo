"""
Topic: Линейный поиск

Description: Дана последовательность чисел длиной N.
             Найти (первое) левое вхождение  положительного числа x нее или вывести -1.

Input: В первой строке массив целых чисел. Во второй строке число х.

Output: Если х существует в последовательности, то возвращает его индекс. В противном случае возвращает -1.

Time complexity: O(n)

Example:
    :Test_1:
    Input: [-1,0,3,9,9,12]
           9

    Output: 3

    :Test_2:
    Input: [-1,0,3,5,9,12]
           2

    Output: -1

"""

nums = list(map(int, input().split()))
target = int(input())

def find_left_x(seq: list, x:int):
    ans = -1
    for i in range(len(seq)):
        if seq[i] == x and ans == -1:
            ans = i
    return ans

answer = find_left_x(nums, target)
print(answer)