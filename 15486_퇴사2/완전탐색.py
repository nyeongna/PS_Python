from sys import stdin
import sys
sys.setrecursionlimit(150000)
n = int(input())
work_list = list()
work_list.append((None,None))
for _ in range(n):
    day, pay = map(int, stdin.readline().rstrip().split())
    work_list.append((day,pay))
record = [-1]*(n+2)

ans = float('-inf')
def DFS(level, profit):
    global ans
    if record[level] >= profit:
        return
    record[level] = max(record[level], profit)
    if level==n+1:
        ans = max(ans, profit)
        return
    nday, npay = work_list[level][0], work_list[level][1]
    if level + nday <= n+1:
        #record[level+work_list[level][0]] = max(record[level+work_list[level][0]], profit+work_list[level][1])
        DFS(level+nday, profit+npay)
    if level + 1 <= n+1:
        #record[level+1] = max(record[level+1], profit)
        DFS(level+1, profit)
        
DFS(1,0)
print(ans)
