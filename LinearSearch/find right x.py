"""
Topic: Линейный поиск

Description: Дана последовательность чисел длиной N.
             Найти (последнее) правое вхождение  положительного числа x нее или вывести -1.

Input: В первой строке массив целых чисел. Во второй строке число х.

Output: Если х существует в последовательности, то возвращает его индекс. В противном случае возвращает -1.

Time complexity: O(n)

Example:
    :Test_1:
    Input: [-1,0,3,9,9,12]
           9

    Output: 4

    :Test_2:
    Input: [-1,0,3,5,9,12]
           2

    Output: -1

"""

nums = list(map(int, input().split()))
target = int(input())

def find_right_x(seq: list, x:int):
    ans = -1
    for i in range(len(seq)):
        if seq[i] == x:
            ans = i
    return ans

answer = find_right_x(nums, target)
print(answer)