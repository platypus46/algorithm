def solution(food):
    answer=""
    s=""
    ls=[]

    for i in range(1,len(food)):
        ls.append(food[i]//2)

    for i in range(1,len(ls)+1):
        s+=str(i)*ls[i-1]

    s1="".join(list(reversed(s)))
    answer+=s+'0'+s1

    return answer



print(solution([1,7,1,2]))