import sys

N, M, H = map(int, input().split())

graph = [[0]*(N+1) for _ in range(H+1)]

for _ in range(M):
    x, y = map(int, input().split())
    graph[x][y] = 1


possible = []
for i in range(1, H+1, 1):
    for j in range(1, N, 1):
        if graph[i][j] == 0 and graph[i][j-1] == 0 and graph[i][j+1] == 0:
            possible.append((i, j))


def game():
    for i in range(1, N+1, 1):
        col = i
        for j in range(1, H+1, 1):
            if graph[j][col] == 1:
                col = col + 1
            elif graph[j][col-1] == 1:
                col = col - 1
        if col != i:
            return 0
    return 1


ans = float('inf')


def DFS(idx, max_cnt, cnt):
    if max_cnt == cnt:
        if game() == 1:
            print(cnt)
            exit()
        return

    for cur in range(idx, len(possible), 1):
        x, y = possible[cur]
        if graph[x][y] == 0 and graph[x][y-1] == 0 and graph[x][y+1] == 0:
            graph[x][y] = 1
            DFS(cur+1, max_cnt, cnt+1)
            graph[x][y] = 0


for i in range(0, 4, 1):
    DFS(0, i, 0)

print(-1)
