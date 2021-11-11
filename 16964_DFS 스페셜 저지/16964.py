from sys import stdin
from functools import cmp_to_key
n = int(input())

graph = [ list() for _ in range(n+1) ]
visited = [ 0 for _ in range(n+1)]

for _ in range(n-1):
    f, s = map(int, stdin.readline().strip().split())
    graph[f].append(s)
    graph[s].append(f)
input_dfs = list(map(int,input().split()))


priority = [ 0 for _ in range(n+1) ]
def pri_comp(a,b):
    if priority[a] > priority[b]:
        return 1
    else:
        return -1

for i in range(len(input_dfs)):
    priority[input_dfs[i]] = i

# 핵심: 커스텀 정렬
# 각 노드의 인접 노드 리스트를, 입력받은 input_dfs를 기준으로 정렬한다
for i in range(len(graph)):
    graph[i] = sorted(graph[i], key=cmp_to_key(pri_comp))

# input_dfs기준으로 정렬한 전체 그래프를 dfs 때리면, 입력받은 input_dfs와 동일한 결과를 나타내야함
ans_list = list()
def dfs(x):
    if visited[x]==1:
        return
    visited[x]=1
    ans_list.append(x)
    for next in graph[x]:
        dfs(next)
dfs(1)

# 동일하면 1, 아니면 0
if ans_list == input_dfs:
    print(1)
else:
    print(0)

'''
1 4 3 6 5 2
'''
'''
      1
  4     2
 3 6 5

'''