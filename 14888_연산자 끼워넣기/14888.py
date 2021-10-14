n = int(input())
num_list = list(map(int, input().split()))
# +, -, *, /
opr_list = list(map(int, input().split()))

max_num = float('-inf')
min_num = float('inf')

def DFS(level, total):
    global max_num, min_num
    if level==n-1:
        max_num = max(max_num, total)
        min_num = min(min_num, total)
        return
    # +
    if opr_list[0] > 0:
        opr_list[0] -= 1
        DFS(level+1, total + num_list[level+1])
        opr_list[0] += 1
    # -
    if opr_list[1] > 0:
        opr_list[1] -= 1
        DFS(level+1, total - num_list[level+1])
        opr_list[1] += 1
    # *
    if opr_list[2] > 0:
        opr_list[2] -= 1
        DFS(level+1, total * num_list[level+1])
        opr_list[2] += 1
    # /
    if opr_list[3] > 0:
        opr_list[3] -= 1
        DFS(level+1, int(total / num_list[level+1]))
        opr_list[3] += 1

DFS(0, num_list[0])
print(max_num)
print(min_num)
