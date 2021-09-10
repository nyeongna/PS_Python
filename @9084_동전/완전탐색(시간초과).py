
import sys
sys.setrecursionlimit(30000)
t = int(input())


n = None
coin_list = None
target = None
ans = 0

def DFS(idx, total):
    global ans, target, n
    if total > target:
        return
    if total == target:
        ans = ans + 1
        return
    for i in range(idx, n, 1):
        DFS(i, total+coin_list[i])
    
for _ in range(t):
    n = int(input())
    coin_list = list(map(int, input().split()))
    target = int(input())
    ans = 0
    DFS(0, 0)
    print(ans)