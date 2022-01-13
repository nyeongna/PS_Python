from collections import deque
'''
N 개의 node에 대해서 (N-1)개의 간선이 있고 모든 node가 연결되어 있으면
--> Spanning tree (cycle이 없는 tree)
모든 node에 대해서 BFS 돌려서 k값보다 높을때마다 cnt+=1
'''
n, q = map(int, input().split())
graph = [ list() for _ in range(n+5000) ]
for _ in range(n-1):
    f, t, v = map(int, input().split())
    graph[f].append((t,v))
    graph[t].append((f,v))

for _ in range(q):
    k, node = map(int, input().split())
    visited = [0]*(n+5000)
    visited[node]=1
    Q=deque()
    Q.append((node, float('inf')))
    cnt=0
    while len(Q) > 0:
        n, kk = Q.popleft()
        for nextNode,nextDist in graph[n]:
            if visited[nextNode] == 0:
                visited[nextNode]=1
                if  min(kk, nextDist) >= k:
                    cnt += 1
                Q.append((nextNode, min(kk,nextDist)))
    print(cnt)

                

                

    
    

