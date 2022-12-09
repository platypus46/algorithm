def solution(s):
    answer = [-1]

    for i in range(1, len(s)):
        check = False
        count = 0
        for j in range(i - 1, -1, -1):
            count += 1
            if s[i] == s[j]:
                answer.append(count)
                check = True
                break
        if not check:
            answer.append(-1)

    return answer