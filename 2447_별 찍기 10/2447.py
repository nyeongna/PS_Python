import sys

n = int(input())
graph = [ [0]*n for _ in range(n) ]

def DFS2(x, y, num):
    for i in range(x, x+num, 1):
        for j in range(y, y+num, 1):
            graph[i][j] = ' '

def DFS(x, y, num):
    if num==1:
        graph[x][y]='*'
        return
    val = num//3
    for i in range(3):
        for j in range(3):
            if i==1 and j==1:
                DFS2(x+i*val, y+j*val, val)
            else:
                DFS(x+i*val, y+j*val, val)

DFS(0, 0, n)
for i in range(n):
    for j in range(n):
        print(graph[i][j], end='')
    print()