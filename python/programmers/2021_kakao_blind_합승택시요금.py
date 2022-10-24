import sys
import heapq

inf = sys.maxsize
graph = [[]]

def dijkstra(s, e):
    global graph
    table = [inf]*(N+1)
    table[s] = 0
    queue = [[0, s]]

    while queue:
        cost, node = heapq.heappop(queue)

        if table[node] < cost:
            continue

        for n,c in graph[node]:
            c += cost
            if c < table[n]:
                table[n] = c
                heapq.heappush(queue, [c, n])

    return table[e]


def solution(n, s, a, b, fares):

    global graph,N
    N=n
    graph = [[] for _ in range(n + 1)]

    for i, j, k in fares:
        graph[i].append((j, k))
        graph[j].append((i, k))

    cost = inf

    for i in range(1,n+1):
        cost = min(cost, dijkstra(s, i) + dijkstra(i, a) + dijkstra(i, b))

    return cost