"""
Topic: Бинарный поиск

Description: Учитывая массив целых чисел nums, отсортированный в порядке возрастания, и целочисленный целевой объект,
             напишите функцию для поиска целевого объекта в nums.

Input: В первой строке массив целых чисел. Во второй строке целевой объект.

Output: Если целевой объект существует, то возвращает его индекс. В противном случае возвращает -1.

Time complexity: O(log(n))

Example:
    :Test_1:
    Input: [-1,0,3,5,9,12]
           9

    Output: 4

    :Test_2:
    Input: [-1,0,3,5,9,12]
           2

    Output: -1

"""

nums = list(map(int, input().split()))
target = int(input())

def binary_search(nums: list, target: int):
    low = 0
    high = len(nums)-1


    while low <= high:
        mid = (low+high) // 2
        if nums[mid] < target:
            low = mid + 1

        elif nums[mid] > target:
            high = mid - 1

        else:
            return mid

    return -1

answer = binary_search(nums, target)
print(answer)

