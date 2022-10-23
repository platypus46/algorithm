def solution(survey, choices):
    answer = ""
    personality = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}

    for i, j in zip(survey, choices):
        if j > 4:
            personality[i[1]] += (j - 4)
        elif j < 4:
            personality[i[0]] += (4 - j)

    if personality['R'] >= personality['T']:
        answer += 'R'
    else:
        answer += 'T'

    if personality['C'] >= personality['F']:
        answer += 'C'
    else:
        answer += 'F'

    if personality['J'] >= personality['M']:
        answer += 'J'
    else:
        answer += 'M'

    if personality['A'] >= personality['N']:
        answer += 'A'
    else:
        answer += 'N'

    return answer