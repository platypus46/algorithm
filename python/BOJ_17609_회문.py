T = int(input())

def Similar(word, start, end):
    while start < end:
        if word[start] == word[end]:
            start += 1
            end -= 1
        else:
            return 2
    return 1


def Palindrome(word, start, end):
    while start < end:
        if word[start] == word[end]:
            start += 1
            end -= 1
        else:
            sim1 = Similar(word, start + 1, end)
            sim2 = Similar(word, start, end - 1)
            if sim1 == 1 or sim2 == 1:
                return 1
            else:
                return 2
    return 0


for _ in range(T):
    word = list(input())
    res = Palindrome(word, 0, len(word) - 1)
    print(res)