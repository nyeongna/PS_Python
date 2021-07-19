import sys
from collections import deque
import copy

n, target = map(int, input().split())
sequence = list(map(int, input().split()))
rec = [0] * n
dict=dict()
ans=0
cnt=0
def DFS(level):
    if level==n:

        global cnt
        cnt = cnt + 1
        if 1 not in rec:
            return
        sum_num=0
        for i in range(n):
            if rec[i]==1:
                sum_num = sum_num + sequence[i]
        if sum_num == target:
            global ans
            ans = ans + 1
        return
    rec[level]=1
    DFS(level+1)
    rec[level]=0
    DFS(level+1)
    
DFS(0)
print(ans)
