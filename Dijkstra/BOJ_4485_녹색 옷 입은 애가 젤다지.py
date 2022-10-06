import sys
inf=sys.maxsize

v,e=map(int,input().split())

graph=[[inf]*(v+1) for _ in range(v+1)]

for _ in range(e):
    a,b,c=map(int,input().split())
    graph[a][b]=c

for k in range(1,v+1):
    for a in range(1,v+1):
        for b in range(1,v+1):
            graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b])

answer=inf

for i in range(1,v+1):
    answer=min(answer,graph[i][i])

if answer==inf:
    print(-1)
else:
    print(answer)