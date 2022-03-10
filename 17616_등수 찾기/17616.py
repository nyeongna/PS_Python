n, m, x = map(int, input().split())
from sys import stdin

# 1 보다 아래에 몇개 있는지 센다
# 세고나면 1의 최저등수가 정해진다
str_dict = { i:[] for i in range(1, n+1)}

# 1 보다 위에 몇개 있는지 센다
# 1의 최고등수가 정해진다
weak_dict = { i:[] for i in range(1, n+1)}
for _ in range(m):
    a, b = map(int, stdin.readline().strip().split())
    str_dict[a].append(b)
    weak_dict[b].append(a)

visited = None
def dfs(x, _set):
    global visited
    for num in str_dict[x]:
        if visited[num]==0:
            visited[num]=1
            _set.add(num)
            dfs(num, _set)
def dfs2(x, _set):
    global visited
    for num in weak_dict[x]:
        if visited[num]==0:
            visited[num]=1
            _set.add(num)
            dfs2(num, _set)

first, last = 1, n
# 1 보다 약한게 없다면 1은 꼴등이 될 수 있음
if len(str_dict[x])==0:
    last = n
else:
    _set = set()
    visited=[0]*(n+1)
    visited[x]=1
    dfs(x, _set)
    last = n - len(_set)

# 1 보다 센 게 없으면 1은 1등이 될 수 있음
if len(weak_dict[x])==0:
    first = 1
else:
    _set = set()
    visited=[0]*(n+1)
    visited[x]=1
    dfs2(x, _set)
    first = len(_set) + 1

print(first, last)