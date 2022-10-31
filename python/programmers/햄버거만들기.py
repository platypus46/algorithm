def solution(ingredient):
    cnt=0

    if len(ingredient)<4:
        return 0
    else:
        ls=[]
        for i in range(len(ingredient)):
            if ls[-4:]==[1,2,3,1]:
                cnt+=1
                for _ in range(4):
                    ls.pop()
            ls.append(ingredient[i])
        if len(ingredient)>=4:
            if ls[-4:]==[1,2,3,1]:
                cnt+=1
    return cnt


