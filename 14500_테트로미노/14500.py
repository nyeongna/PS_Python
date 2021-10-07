
n, m = map(int, input().split())

graph = list()
for _ in range(n):
    graph.append(list(map(int, input().split())))


''' 시간복잡도
19 * 500 * 500 * 3 = 1,200만
'''
shape_list = [
    [(0,1), (0,2), (0,3)],
    [(1,0), (1,1), (1,2)],
    [(0,1), (-1,1), (0,2)],
    [(0,1), (0,2), (-1,2)],
    [(1,0), (0,1), (0,2)],
    [(0,1), (0,2), (1,1)],
    [(0,1), (0,2), (1,2)],
    [(1,0), (2,0), (2,1)],
    [(0,1), (-1,1),(-2,1)],
    [(0,1), (1,0), (2,0)],
    [(0,1), (1,1), (2,1)],
    [(0,1), (1,0), (1,1)],
    [(1,0), (2,0), (3,0)],
    [(1,0), (1,1), (2,0)],
    [(1,0), (1,-1), (2,0)],
    [(0,1), (-1,1), (-1,2)],
    [(0,1), (1,1), (1,2)],
    [(1,0), (1,1), (2,1)],
    [(1,0), (0,1), (-1,1)]
]

ans = 0

def func(x, y):
    global ans

    for row in shape_list:
        sum = graph[x][y]
        for i in row:
            dx = x + i[0]
            dy = y + i[1]
            #print(x, y, dx, dy)
            if 0<=dx<n and 0<=dy<m:
                sum += graph[dx][dy]
            else:
                break
        ans = max(ans, sum)

for i in range(n):
    for j in range(m):
        func(i, j)
print(ans)