def solution(dartResult):
    score=[]
    num=0
    res=0
    for i in range(len(dartResult)):
        if ord(dartResult[i])==0 or 48<=ord(dartResult[i])<=57:
            num=int(dartResult[i])
            if i>0:
                if dartResult[i-1]=='1' and dartResult[i]=='0':
                    num=10
        elif dartResult[i]=='S':
            score.append(num**1)
            num=0
        elif dartResult[i]=='D':
            score.append(num**2)
            Num=0
        elif dartResult[i]=='T':
            score.append(num**3)
            Num=0
        elif dartResult[i] == '*':
            if len(score) > 1:
                score[-2] *= 2
            score[-1] *= 2
        elif dartResult[i]=='#':
            score[-1] *= -1
        res=sum(score)
    return res

