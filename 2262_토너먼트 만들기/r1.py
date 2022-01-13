n = int(input())
num_list = list(map(int, input().split()))
visited = [0]*num_list
ans = float('inf')

def dfs(level, total):
    if level==1:
        return
    
dfs(num_list, 0)