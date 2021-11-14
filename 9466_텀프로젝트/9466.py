import sys
sys.setrecursionlimit(120000)
t = int(input())
visited = None
finished = None
graph = None
cnt = None

# cycle에 해당하는 정점의 갯수 구함
def count_cyclonize(node):
    global cnt,graph
    local_cnt = 1
    next_node = graph[node]
    while next_node != node:
        local_cnt += 1
        next_node = graph[next_node]
    cnt -= local_cnt
    #print(f'node:{node}, cnt:{local_cnt}')

def DFS(node):
    global visited, finished, graph
    next_node = graph[node]
    if visited[next_node]==0:
        visited[next_node]=1
        DFS(next_node)
    # elif에 도달했다면 cycle이 발견됐다는뜻
    # count_cyclonize를 통해 cycle에 속하는 정점의 갯수 구함
    elif visited[next_node]==1 and finished[next_node]==0:
        count_cyclonize(node)
    finished[node]=1

for _ in range(t):
    ## 초기화 시작
    n = int(input())
    graph = [0] + list(map(int, input().split()))
    visited = [0]*(n+1)
    finished = [0]*(n+1)
    cnt = n
    ## 초기화 끝
    for i in range(1, n+1):
        if visited[i]==0:
            visited[i]=1
            DFS(i)
    # 전체 n 정점에서 cycle에 해당하는 정점의 갯수를 빼면 '그룹을 못정한 정점개수가 구해짐'
    print(cnt)
