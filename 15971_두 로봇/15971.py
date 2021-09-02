from sys import stdin
from collections import deque
import heapq

n, r1, r2 = map(int, stdin.readline().strip().split())

graph = [ list() for _ in range(n+1) ]

for _ in range(n-1):
    start, end, dist = map(int, stdin.readline().strip().split())
    graph[start].append((end,dist))
    graph[end].append((start,dist))

# 다익스트라를 r1, r2에 대해 2번 돌린다.
dist1 = [ float('inf') for _ in range(n+1) ]
dist1[r1]=0
Q = []
heapq.heappush(Q, (0, r1))

while len(Q) > 0:
    cost, now = heapq.heappop(Q)
    if dist1[now] < cost:
        continue
    for (next, nextDis) in graph[now]:
        nextCost = cost + nextDis
        if dist1[next] > nextCost:
            dist1[next] = nextCost
            heapq.heappush(Q, (nextCost, next))

dist2 = [ float('inf') for _ in range(n+1) ]
dist2[r2]=0
Q = []
heapq.heappush(Q, (0, r2))

while len(Q) > 0:
    cost, now = heapq.heappop(Q)
    if dist2[now] < cost:
        continue
    for (next, nextDis) in graph[now]:
        nextCost = cost + nextDis
        if dist2[next] > nextCost:
            dist2[next] = nextCost
            heapq.heappush(Q, (nextCost, next))

# 만약 두 로봇 시작 위치가 같다면 0 출력
if r1==r2:
    print(0)
    exit()

ans = float('inf')
# 최소거리를 찾는다
# r1에서의 최단거리와 r2에서의 최단거리의 합이 가장 짧은 vertex까지의 최단거리합을 찾는다.
for r1_idx in range(1, n+1):
    for r2_idx, cost in graph[r1_idx]:
        ans = min(ans, dist1[r1_idx] + dist2[r2_idx])
print(ans)



