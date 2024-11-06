"""
Topic: Префиксные суммы

Description: Дана последовательность чисел. Необходимо найти количество отрезков с нулевой суммой.

Input: В первой строке дано целое число n  — количество элементов в последовательности.
       Во второй строке дано n целых чисел — элементы последовательности.

Output: Выведите n целое число — количество отрезков с нулевой суммой.

Time complexity: O(n)

Example:
    :Test_1:
    Input:  5
            2 -1 0 -2 1

    Output: 3

    :Test_2:
    Input:  5
            1 2 3 4 5

    Output: 0

"""


k = int(input())
arr = list(map(int, input().split()))


def countprefixsum(arr: list) -> dict:
    prefixsumbyvalue = {0: 1}
    nowsum = 0
    for el in arr:
        nowsum += el
        if nowsum not in prefixsumbyvalue:
            prefixsumbyvalue[nowsum] = 0
        prefixsumbyvalue[nowsum] += 1
    return prefixsumbyvalue

def count_zero_sum_segments(prefixsum: dict) -> int:
    # Идея состоит в том, чтобы посчитать префиксные суммы.
    # Одинаковые префиксные суммы  означают, что сумма на отрезке с началом и концом в позициях,
    # на которых достигаются префиксные суммы, будет равна нулю.
    count = 0
    for nowsum in prefixsum:
        cntsum = prefixsum[nowsum]
        count += cntsum*(cntsum-1)//2
    return count


answer = count_zero_sum_segments(countprefixsum(arr))
print(answer)