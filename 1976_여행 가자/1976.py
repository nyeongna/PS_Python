n = int(input())
m = int(input())

graph = list()
for _ in range(n):
    graph.append(list(map(int, input().split())))

parent = [i for i in range(n+1)]

def find(x):
    if x == parent[x]:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]
def union(a,b):
    x, y = find(a), find(b)
    if x!=y:
        parent[x] = y

# 연결된 것들은 연결표시를 Find & Union을 통해 만들어준다
for i in range(n):
    for j in range(n):
        if graph[i][j]==1:
            union(i+1,j+1)
#print(parent)
order_list = list(map(int, input().split()))
flag=1

# 가는 도중 못가는 곳이 생기면 find(a) != find(b) 면 NO
# 아무런 문제가 없다면 다 이어진 것이므로 YES
for i in range(len(order_list)-1):
    if find(order_list[i]) != find(order_list[i+1]):
        print('NO')
        exit()
print('YES')