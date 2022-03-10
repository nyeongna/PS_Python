import copy
n, m, k = map(int, input().split())
cost = list(map(int, input().split()))
cost.insert(0,None)
parent = [ i for i in range(n+1) ]
parent[0] = None
min_cost = copy.deepcopy(cost)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
        return parent[x]
    return x

def union(a,b):
    a, b = find(a), find(b)
    if a!=b:
        parent[a]=b
        # min_cost[a] 에는 a와 친구가 되려고할때 필요한 최소 친구비
        # a와 친구가 된다면 a를 대표번호로 갖고있는 다른 친구들과도 친구를 할 수 있음
        min_cost[b] = min(min_cost[a], min_cost[b])

for _ in range(m):
    a, b = map(int, input().split())
    union(a,b)

ans=0
friend_ch = dict()
for i in range(1,n+1):
    rep = find(i)
    # i 친구의 대표번호가 friend_ch 없다면
    # 아직 친구비를 안준 친구이므로 줘야함
    if rep not in friend_ch:
        ans += min_cost[rep]
        friend_ch[rep]=1
if ans <= k:
    print(ans)
else:
    print('Oh no')


