'''
MST: 최소 신장 스패닝 트리
크루스칼: union and find 사용해서 연결하려는 edge의 두 node 들이 같은 집합안에
        있는지 확인할 때 쓰임
'''
from itertools import combinations
import math
star_list = list()
n = int(input())
for i in range(n):
    x, y = map(float, input().split())
    star_list.append((x,y,i))
edge_list = list()
for comb in combinations(star_list, 2):
    a, b, star1 = comb[0]
    x, y, star2 = comb[1]
    dist=math.sqrt(pow((a-x),2) + pow((b-y),2))
    edge_list.append((dist, star1, star2))
edge_list.sort()

parent = [i for i in range(n+1)]
def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
        return parent[x]
    return parent[x]

def union(x,y):
    x = find(x)
    y = find(y)
    if x!=y:
        parent[x]=y
ans=0
for dist, e1, e2 in edge_list:
    x = find(e1)
    y = find(e2)
    if x != y:
        union(e1, e2)
        ans += dist
print('{:.2f}'.format(ans))



    
