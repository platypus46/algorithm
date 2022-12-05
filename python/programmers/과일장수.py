def solution(k, m, score):
    score=list(reversed(sorted(score)))

    #박스 전체가 담긴 리스트
    box_ls=[]
    #한 박스에 들어가는 원소
    ls=[]

    ans=0

    for i in range(len(score)):
        ls.append(score[i])
        if ((i+1)%m)==0:
            box_ls.append(ls)
            ls=[]

    for i in box_ls:
        ans+=min(i)*m

    return ans



print(solution(4,3,[4,1,2,2,4,4,4,4,1,2,4,2]))