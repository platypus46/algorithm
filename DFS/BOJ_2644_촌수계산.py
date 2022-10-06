import sys

def binary_search(start,end,n,k):
    if start>=end:
        return start
    mid=(start+end)//2

    if mid*(mid+1)*k>=2*n:
        return binary_search(start,mid,n,k)
    else:
        return binary_search(mid+1,end,n,k)

T=int(input())

for _ in range(T):
    N,K=map(int,sys.stdin.readline().split())
    pos=0
    Sum=0
    idx=binary_search(0,5000,N,K)

    Sum = idx*(idx+1)//2

    if idx%2!=0:
        pos=K*(idx//2+1)
        pos+=(N-1)-Sum*K
        print(f"{pos} R")
    else:
        pos=-K*(idx//2)
        pos-=(N-1)-Sum*K
        print(f"{pos} L")