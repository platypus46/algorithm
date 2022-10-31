def solution(X, Y):
    s=''
    for i in range(9,-1,-1):
        n=min(X.count(f'{i}'),Y.count(f'{i}'))
        s+=str(i)*n

    if len(s)==0:
        return '-1'
    elif s[0]=='0':
        return '0'
    else:
        return "".join(s)