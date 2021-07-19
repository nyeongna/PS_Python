from itertools import permutations
from itertools import combinations
from sys import stdin
from collections import deque
import sys
sys.getrecursionlimit()

x_dir = [-1, 0, 1, 0, 0, 0]
y_dir = [0, 1, 0, -1, 0, 0]
z_dir = [0, 0, 0,  0, 1, -1]
while True:
    L, R, C = map(int, stdin.readline().split())
    if L == 0 and R == 0 and C == 0:
        exit()
    graph = []
    visited = [[[0]*C for _ in range(R)] for _ in range(L)]
    start = ()
    end = ()
    for l in range(L):
        floor = [stdin.readline() for _ in range(R)]
        graph.append(floor)
        stdin.readline()
        for i in range(R):
            for j in range(C):
                if graph[l][i][j] == 'S':
                    start = (l, i, j, 0)
                if graph[l][i][j] == 'E':
                    end = (l, i, j, 0)
    Q = deque()
    Q.append(start)
    visited[start[0]][start[1]][start[2]] = 1
    flag = 1
    while len(Q) > 0:
        z, x, y, dist = Q.popleft()
        if z == end[0] and x == end[1] and y == end[2]:
            print(f'Escaped in {dist} minute(s).')
            flag = 0
            break
        for i in range(6):
            dz = z + z_dir[i]
            dx = x + x_dir[i]
            dy = y + y_dir[i]
            if dx >= 0 and dx < R and dy >= 0 and dy < C and dz >= 0 and dz < L and graph[dz][dx][dy] != '#' and visited[dz][dx][dy] == 0:
                visited[dz][dx][dy] = 1
                Q.append((dz, dx, dy, dist+1))
    if flag == 1:
        print('Trapped!')
