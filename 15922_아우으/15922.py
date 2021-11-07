n = int(input())
ans = 0
left, right = map(int, input().split())

for _ in range(n-1):
    x, y = map(int, input().split())
    if x <= right:
        right = max(right, y)
    else:
        ans += right-left
        left=x
        right=y
print(ans+right-left)

        
    