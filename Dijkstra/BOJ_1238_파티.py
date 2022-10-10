import heapq
import sys

inf=sys.maxsize

N,M,X=map(int,input().split())

graph=[[] for _ in range(N+1)]

for _ in range(M):
    a,b,c=map(int,input().split())

    graph[a].append((b,c))

def dijkstra(s):
    distance = [inf] * (N + 1)
    q=[]
    heapq.heappush(q,(0,s))
    distance[s]=0

    while q:
        dist,now=heapq.heappop(q)

        if distance[now]<dist:
            continue
        for i in graph[now]:
            cost=dist+i[1]

            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))

    return distance

start=[]
for i in range(1,N+1):
    start.append(dijkstra(i)[X])

end=dijkstra(X)[1:]

res=0

for a,b in zip(start,end):
    res=max(a+b,res)

print(res)