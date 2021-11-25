n = int(input())
p_list = list(map(int, input().split()))

left, right = 0, n-1
ans = float('-inf')
while left < right:
    val = p_list[left] + p_list[right]
    if abs(val) < abs(ans):
        ans = val
    if val >= 0:
        right -= 1
    elif val < 0:
        left += 1
print(ans)
