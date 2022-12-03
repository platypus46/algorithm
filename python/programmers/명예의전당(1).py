def solution(k, score):
    answer = []

    for i in range(len(score)):
        ls = score[:i + 1]
        if len(ls) <= k:
            ls.sort()
            answer.append(ls[0])
        else:
            ls.sort()
            answer.append(ls[-k])

    return answer