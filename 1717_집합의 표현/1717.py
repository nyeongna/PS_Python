n, m = map(int, input().split())

parent = [ i for i in range(n+1) ]

def find(x):
    if x == parent[x]:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]
def union(a, b):
    x, y = find(a), find(b)
    if x != y:
        parent[x] = y

for _ in range(m):
    op, a, b = map(int, input().split())
    if op==0:
        union(a,b)
    elif op==1:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')

    