n = int(input())

# 완전탐색
energy = [0]*n
for idx in range(n-1):
    s, l = map(int, input().split())
    energy[idx+1] = (s,l)
k = int(input())


ans = float('inf')
def dfs(level, sum, flag):
    global ans
    if level > n:
        return
    if sum >= ans:
        return
    elif level == n:
        ans = min(ans, sum)
    else:
        if flag==0:
            dfs(level+3, sum+k, 1)
        dfs(level+1, sum+energy[level][0], flag)
        dfs(level+2, sum+energy[level][1], flag)
dfs(1, 0, 0)
print(ans)