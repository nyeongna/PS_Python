import sys
from itertools import combinations

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

people = [x for x in range(n)]
ans = float('inf')


def Solve():
    global ans
    for comb in combinations(people, n//2):
        start = list(comb)
        link = list(set(people) - set(start))
        sum1 = 0
        sum2 = 0
        for (x, y) in combinations(start, 2):
            sum1 = sum1 + graph[x][y] + graph[y][x]
        for (x, y) in combinations(link, 2):
            sum2 = sum2 + graph[x][y] + graph[y][x]
        ans = min(ans, abs(sum1-sum2))
    print(ans)


Solve()
