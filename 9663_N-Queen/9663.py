import sys
from collections import deque

n = int(input())
graph = [ [0]*n for _ in range(n) ]

ans = 0
ch = deque()
num=0

def Check(row, col):
    for [x,y] in ch:
        if row == x:
            return 1
        if col == y:
            return 1
        if abs(row-x) == abs(col-y):
            return 1
    return 0

def DFS(row, cnt):
    if row==n and cnt==n:
        global ans
        ans = ans + 1
        return
    for col in range(n):
        flag=Check(row,col)
        if flag==0:
            ch.append([row,col])
            DFS(row+1, cnt+1)
            ch.pop()
            
DFS(0, 0)
print(ans)