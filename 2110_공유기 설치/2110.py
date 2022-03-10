from sys import stdin
n, m = map(int, input().split())
home_list = [ int(stdin.readline().rstrip()) for _ in range(n) ]
home_list.sort()

# left에는 정답이 가능한 숫자 중 가장 작은 숫자
left = 1
# right에는 정답이 안되는 숫자 중 가장 큰 숫자
right = 2000000000

def check(mid):
    pivot = home_list[0]
    cnt=1
    for idx in range(1, n):
        if home_list[idx] - pivot >= mid:
            cnt += 1
            pivot = home_list[idx]
    return cnt

ans=1
while left <= right:
    # mid 숫자를 넣어보고 배치 가능하다면 left= mid+1
    # mid 숫자를 넣어보고 배치 불가능하면 right= mid-1
    mid = (left + right) // 2
    ch = check(mid)
    if ch >= m:
        left = mid+1
        ans = mid
    else:
        right = mid-1
print(ans) # or left-1 or right

