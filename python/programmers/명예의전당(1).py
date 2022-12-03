import math

def get_num(n):
    cnt=0

    for i in range(1,int(math.sqrt(n))+1):
        if n%i==0:
            cnt+=1
            if (i*i)<n:
                cnt+=1

    return cnt

def solution(number,limit,power):
    ans=0

    for i in range(1,number+1):
        if get_num(i)<=limit:
            ans+=get_num(i)
        else:
            ans+=power

    return ans
