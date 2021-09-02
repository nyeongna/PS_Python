from collections import deque

n, m, start = map(int, input().split())
graph = [ list() for _ in range(n+1) ]
for _ in range(m):
    f, t = map(int, input().split())
    graph[f].append(t)
    graph[t].append(f)

for idx in range(1, n+1):
    graph[idx] = sorted(graph[idx])

visited = [0]*(n+1)        
def DFS(v):
    visited[v]=1
    print(v, end = ' ')
    for next in graph[v]:
        if visited[next]==0:
            DFS(next)
    return

def BFS(v):
    visited = [0]*(n+1)
    visited[v]=1
    Q = deque()
    Q.append(v)
    while len(Q) > 0:
        now = Q.popleft()
        print(now, end= ' ')
        for next in graph[now]:
            if visited[next]==0:
                visited[next]=1
                Q.append(next)
DFS(start)
print()
BFS(start)