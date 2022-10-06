import sys,heapq

def dijkstra(a,b):
    dx,dy=[-1,1,0,0],[0,0,-1,1]
    q=[]
    heapq.heappush(q,(graph[a][b],a,b))

    while q:
        cost,x,y=heapq.heappop(q)
        if x == n - 1 and y == n - 1:
            print(f'Problem {cnt}: {distance[x][y]}')
            break

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<n and 0<=ny<n:
                ncost=cost+graph[nx][ny]

                if ncost<distance[nx][ny]:
                    distance[nx][ny]=ncost
                    heapq.heappush(q,(ncost,nx,ny))

cnt=1

while True:
    inf=sys.maxsize
    n=int(input())

    if n==0:
        break

    graph=[]
    distance=[[inf]*n for _ in range(n)]

    for _ in range(n):
        graph.append(list(map(int,input().split())))

    dijkstra(0,0)
    cnt+=1