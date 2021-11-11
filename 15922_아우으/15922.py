n = int(input())
ans = 0
left, right = map(int, input().split())

for _ in range(n-1):
    x, y = map(int, input().split())
    # 다음 선분이 전에 있던 선분과 이어지지 않는다면, 전에 있던 선분의 길이를 ans에 누적
    if x <= right:
        right = max(right, y)
    else:
        ans += right-left
        left=x
        right=y
# 마지막 선분의 길이까지 고려해서 출력
print(ans+right-left)

        
    