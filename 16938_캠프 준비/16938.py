from itertools import combinations

n, l, r, x = map(int, input().split())
diff = list(map(int, input().split()))
ans=0
for p_num in range(2, n+1):
    for comb in combinations(diff, p_num):
        min_num = min(comb)
        max_num = max(comb)
        sum_num = sum(comb)
        if l <= sum_num <= r and max_num-min_num >= x:
            ans+=1
print(ans)