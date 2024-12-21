"""
Topic: Линейный поиск

Description: Дана последовательность чисел длиной N (N>1).
             Найти максимальное число в последоательности и второе по величине число (такое, которое будет максимальным,
             если вычеркнуть из последовательности одно максимальное число).

Input: В первой строке массив целых чисел.

Output: Два максимальных числа в массиве.

Time complexity: O(n)

Example:
    :Test_1:
    Input: [-1,0,3,9,9,12]


    Output: 9, 12

"""

nums = list(map(int, input().split()))


def find_max_x(seq: list):
    max_1 = max(seq[0], seq[1])
    max_2 = min(seq[0], seq[1])

    for i in range(2,len(seq)):
        if seq[i] > max_1:
            max_2 = max_1
            max_1 = seq[i]
        elif (seq[i] > max_2 and seq[i] < max_1):
            max_2 = seq[i]
    return (max_2, max_1)

answer = find_max_x(nums)
print(answer)