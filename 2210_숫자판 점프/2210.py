from sys import stdin
from collections import deque
import sys
sys.setrecursionlimit(10000)

graph = [ list(map(str, stdin.readline().rstrip().split())) for _ in range(5) ]

d = set()
record = ['0']*6
ans = 0

x_dir = [-1,0,1,0]
y_dir = [0,1,0,-1]

def DFS(x, y, dist):
    global ans
    if dist==6:
        combi = ''.join(record)
        if combi not in d:
            #print(combi, end=' ')
            d.add(combi)
            ans += 1
        return
    for i in range(4):

        dx = x + x_dir[i]
        dy = y + y_dir[i]
        if dx>=0 and dx<5 and dy>=0 and dy<5:
            record[dist]=graph[dx][dy]
            DFS(dx, dy, dist+1)

for i in range(5):
    for j in range(5):
        record[0] = graph[i][j]
        DFS(i,j,1)
print(ans)