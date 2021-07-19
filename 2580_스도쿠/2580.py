import sys
limit_number = 300000
sys.setrecursionlimit(limit_number)


graph = [ list(map(int,input().split())) for _ in range(9) ]

zeros = []

rows = [
    dict() for _ in range(9)
]
cols = [
    dict() for _ in range(9)
]
square = [
    dict() for _ in range(9)
]

for i in range(9):
    for j in range(9):
        num = graph[i][j]
        if num == 0:
            zeros.append((i,j))
        else:
            rows[i][num] = True
            cols[j][num] = True
            # Main Point
            q = i//3 * 3 + j//3
            square[q][num] = True

n = len(zeros)

def Check(x, y, num):
    if num in rows[x]:
        return 0
    if num in cols[y]:
        return 0
    if num in square[x//3 * 3 + y // 3]:
        return 0
    return 1

def DFS(cnt):
    if cnt==n:
        for i in range(9):
            for j in range(9):
                print(graph[i][j], end=' ')
            print()
        exit()

    x, y = zeros[cnt]
    for j in range(1,10,1):
        flag = Check(x,y,j)
        if flag:
            graph[x][y] = j
            rows[x][j] = True
            cols[y][j] = True
            square[x//3 * 3 + y // 3][j] = True

            DFS(cnt+1)  
            del rows[x][j]
            del cols[y][j]
            del square[x//3 * 3 + y // 3][j]
            graph[x][y] = 0

DFS(0)