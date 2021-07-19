import sys
from collections import deque

n = int(input())
cost = [0] * (n+1)
graph = [ [] for _ in range(n+1) ]
degree = [0] * (n+1)

for i in range(n):
    line = list(map(int, input().split()))
    cost[i+1] = line[0]
    for j in range(1,len(line)-1):
        graph[line[j]].append(i+1)
        degree[i+1] = degree[i+1]+1

Q = deque()
ans = [0] * (n+1)

for i in range(1,n+1):
    if degree[i]==0:
        Q.append(i)
        ans[i]=cost[i]

order = list()


while len(Q) > 0:
    cur = Q.popleft()
    order.append(cur)

    for i in graph[cur]:
        ans[i] = max(ans[i], cost[i] + ans[cur])
    for i in graph[cur]:
        degree[i] = degree[i]-1
        if degree[i] == 0:
            Q.append(i)

for i in range(1, n+1):
    print(ans[i])
