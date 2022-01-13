n = int(input())
num_list = list(map(int, input().split()))
ans = float('inf')
def dfs(num_list, total):
    global ans
    if len(num_list)==1:
        ans=min(ans, total)
        return
    for i in range(len(num_list)-1):
        dfs(num_list[:i+1] + num_list[i+2:], total+abs(num_list[i]-num_list[i+1]))
        dfs(num_list[:i] + num_list[i+1:], total+abs(num_list[i]-num_list[i+1]))
dfs(num_list, 0)
print(ans)