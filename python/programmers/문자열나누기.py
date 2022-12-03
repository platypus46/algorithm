from collections import deque

def solution(s):
    s = deque(list(s))

    cnt=0

    c_1=0
    c_2=0
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