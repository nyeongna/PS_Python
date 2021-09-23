n = int(input())
target = int(input())
graph = [ [ 0 for _ in range(n) ] for _ in range(n) ]

num, d = n**2, 0
dir = [ 
    [1, 0],
    [0, 1],
    [-1, 0],
    [0, -1]
]
row, col = 0, 0
while num != 0:
    graph[row][col] = num
    num -= 1
    r, c = row+dir[d][0], col+dir[d][1]
    
    # 0, n 범위를 넘거나 벽(graph[r][c]!=0) 을 만났다면 방향을 바꾼다.
    if r < 0 or r >=n or c < 0 or c >= n or graph[r][c] != 0:
        d = (d+1) % 4
    row, col = row+dir[d][0], col+dir[d][1]

x, y = 0, 0
for i in range(n):
    for j in range(n):
        print(graph[i][j], end=' ')
        if graph[i][j] == target:
            x, y = i+1, j+1
    print()
print(f'{x} {y}')