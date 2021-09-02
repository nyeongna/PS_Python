
'''
다익스트라 문제 (Single-source, shortest path)
'''

import heapq
from sys import stdin

t = int(stdin.readline().strip())

for _ in range(t):
    n, d, c = map(int, stdin.readline().strip().split())
    dist = [float('inf')] * (n+1)
    graph = [ list() for _ in range(n+1)]

    for _ in range(d):
        t, f, d = map(int, stdin.readline().strip().split())
        graph[f].append((t, d))
    pQ, dist[c] = [], 0
    heapq.heappush(pQ, (0,c))

    # 다익스트라 시작
    while len(pQ) > 0:
        cost, now = heapq.heappop(pQ)
        if cost > dist[now]:
            continue
        for next,nextDis in graph[now]:
            nextCost = cost + nextDis
            if nextCost < dist[next]:
                dist[next] = nextCost
                heapq.heappush(pQ, (nextCost, next))
    cnt = 0
    ans = 0
    # print(dist)
    for i in dist:
        if i != float('inf'):
            cnt = cnt + 1
            ans = max(ans, i)
    print(cnt, ans)

        



