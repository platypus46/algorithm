from collections import deque

def solution(s):
    s = deque(list(s))

    cnt=0

    #첫번째 글자와 중복된 문자의 개수
    c_1=0
    #첫번째 글자와 중복되지않은 문자의 개수
    c_2=0
    #문자열에 문자가 하나도 없는 경우도 고려
    if len(s)!=0:
        cnt+=1
    while s:
        alphabet=s.popleft()
        c_1+=1
        while s:
            if c_1==c_2:
                cnt+=1
                break
            if alphabet==s[0]:
                c_1+=1
                s.popleft()
            elif alphabet!=s[0]:
                c_2+=1
                s.popleft()

    return cnt