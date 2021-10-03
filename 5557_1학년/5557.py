n = int(input())
num_list = list(map(int, input().split()))
ans = 0

def DFS(level, sum):
    global ans
    # 마지막 숫자에 도달 했으면 cnt+1
    if level == len(num_list)-2:
        if sum == num_list[-1]:
            ans = ans + 1
        return
    # (+)
    if 0 <= sum + num_list[level+1] <= 20:
        DFS(level+1, sum+num_list[level+1])
    # (-)
    if 0 <= sum - num_list[level+1] <= 20:
        DFS(level+1, sum-num_list[level+1])
DFS(0, num_list[0])
print(ans)