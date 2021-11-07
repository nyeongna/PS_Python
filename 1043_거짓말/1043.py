n, m = map(int, input().split())
true_list = list(map(int, input().split()))
true_num, true_list = true_list[0], true_list[1:]

# UNION & FIND 초기화
parent = [i for i in range(n+1)]
def find(x):
    if x==parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]
def union(a,b):
    x, y = find(a), find(b)
    if x != y:
        parent[x]=y
# 진실을 아는 사람끼리 다 묶어줌
for i in range(len(true_list)-1):
    union(true_list[i], true_list[i+1])

# 파티 정보 입력 받음
party_list = list()
for _ in range(m):
    party = list(map(int, input().split()))
    party_num, party = party[0], party[1:]
    party_list.append(party)

# 같은 파티내에 있는 사람끼리 다 묶어줌
for party in party_list:
    for i in range(len(party)-1):
        union(party[i], party[i+1])

# 진실을 아는 사람이 없으면 m이 정답
if true_num==0:
    print(m)
    exit()

# 각 파티에 있는 사람들에 대해서 진실된 사람과 접점이 있으면 (find(p) == find(true_list[0])) 그 파티는 진실만 말해야함
ans=0
for party in party_list:
    flag=0
    for p in party:
        if find(p) == find(true_list[0]):
            flag=1
    if flag==0:
        ans+=1
print(ans)

'''
좋은 예시
4 5
1 1

1 1
1 2
1 3
2 4 2
2 4 1
답: 1
'''