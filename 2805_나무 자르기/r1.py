n, m = map(int, input().split())
tree_list = list(map(int, input().split()))

left = 0
right = int(1e9)

def f(height):
    total = 0
    for tree in tree_list:
        cut = tree - height if tree >= height else 0
        total += cut
    return total
ans = float('-inf')
while left <= right:
    mid = (left+right) // 2
    
    if f(mid) >= m:
        ans=max(ans,mid)
        left = mid + 1
    else:
        right = mid -1

print(ans)