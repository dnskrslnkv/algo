"""
Topic: Линейный поиск

Description: Дана последовательность слов.
             Найти все самые короткие слова.

Input: В первой строке массив слов разной длины.

Output: Вывести через пробел все самые короткие слова.

Time complexity: O(n)

Example:
    :Test_1:
    Input: [abc, ab, zx, sfasr, yt, srsatdtsdyd]


    Output: ab zx yt



"""

words = list(map(str, input().split()))

def shortwords(words):
    ans = []
    min_len = len(words[0])
    for word in words:
        if len(word) < min_len:
            min_len = len(word)

    for word in words:
        if len(word) == min_len:
            ans.append(word)

    return ' '.join(ans)

answer = shortwords(words)
print(answer)
