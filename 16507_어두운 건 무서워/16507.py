import sys

r, c, k = map(int, input().split())

graph = []
for _ in range(r):
    graph.append(list(map(int, input().split())))

psum = [[0]*(c+1) for _ in range(r+1)]
for i in range(r):
    for j in range(c):
        # 여기가 핵심파트!
        # 2차원 psum을 어떻게 업데이트 하는지....
        psum[i+1][j+1] = psum[i][j+1] + psum[i+1][j] - psum[i][j] + graph[i][j]


for i in range(k):
    r1, c1, r2, c2 = map(int, input().split())
    area = psum[r2][c2] - psum[r2][c1-1] - psum[r1-1][c2] + psum[r1-1][c1-1]
    area = area // ((r2-r1+1) * (c2-c1+1))
    print(area)
