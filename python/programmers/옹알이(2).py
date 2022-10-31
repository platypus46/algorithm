def solution(babbling):
    say = ['aya', 'ye', 'woo', 'ma']

    for i in range(len(babbling)):
        for word in say:
            if word * 2 not in babbling[i]:
                babbling[i] = babbling[i].replace(word, ' ')
        babbling[i] = babbling[i].strip()

    return babbling.count('')