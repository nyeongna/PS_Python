import sys
from collections import deque

n, m = map(int, input().split())

graph = [ [] for _ in range(n+1) ]
degree = [ 0 for _ in range(n+1) ]

for i in range(m):
    line = list(map(int, input().split()))
    num = line[0]
    for j in range(1, num):
        graph[line[j]].append(line[j+1])
        degree[line[j+1]] = degree[line[j+1]] + 1

Q = deque()

for i in range(1,n+1):
    if degree[i]==0:
        Q.append(i)

ans = list()
cnt=0

while len(Q) > 0:
    cur = Q.popleft()
    ans.append(cur)
    cnt=cnt+1
    for i in graph[cur]:
        degree[i] = degree[i]-1
        if degree[i] ==0:
            Q.append(i)
if cnt < n:
    print(0)
else:
    for i in ans:
        print(i)