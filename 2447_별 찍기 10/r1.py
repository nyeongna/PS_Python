n = int(input())
graph = [ [0]*(3**7+1) for _ in range(3**7+1) ]


def dfs(x, y, size, blank):
    if size==1:
        graph[x][y] = '*' if blank==0 else ' '
        return
    new_size = size // 3
    for i in range(3):
        for j in range(3):
            if (i==1 and j==1) or blank==1:
                dfs(x + new_size*i, y + new_size*j, new_size, 1)
            else:
                dfs(x + new_size*i, y + new_size*j, new_size, 0)

dfs(0, 0, n, 0)
for i in range(n):
    for j in range(n):
        print(graph[i][j], end='')
    print()