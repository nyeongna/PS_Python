import sys
sys.setrecursionlimit(300000)
n, r, c = map(int, input().split())
cnt = 0

def dfs(x, y, num):
    print(f'{x} {y} {num} called')
    global cnt
    if num==1:
        if x==r and y==c:
            print(cnt)
            exit()
        cnt += 1
        return
    divided = num // 2
    # 핵심 조건.
    # 조건의 r,c가 안들어 있는 4사분면은 그냥 (num * num) 크기만큼 더해버리면된다. 재귀할필요없음.
    if x + num > r and y + num > c:
        dfs(x, y, divided)
        dfs(x, y+divided, divided)
        dfs(x+divided, y, divided)
        dfs(x+divided, y+divided, divided)
    else:
        cnt += num*num

dfs(0, 0, 2**n)

