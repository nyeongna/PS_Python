# -*- coding: utf-8 -*-

import sys

n, m = map(int, sys.stdin.readline().split())
graph = [ list(map(int, sys.stdin.readline().split())) for _ in range(n) ]
psum = [ [0]*(n+1) for _ in range(n+1) ]


# psum을 이제 채워야하는데 규칙은 이렇다.
# psum[i+1][j+1] = psum[i][j+1] + psum[i+1][j] - psum[i][j] + graph[i][j]
#
for i in range(n):
    for j in range(n):
        psum[i+1][j+1] = psum[i][j+1] + psum[i+1][j] - psum[i][j] + graph[i][j]

for _ in range(m):
    x1,y1,x2,y2 = map(int,sys.stdin.readline().split())
    x1,y1,x2,y2 = x1-1, y1-1, x2-1, y2-1
    
    #    (x1,y1) ~ (x2, y2) 사이의 넓이의 합은
    #   psum[x2+1][y2+1] - psum[x1][y2+1] - psum[x2+1][y1] + psum[x1][y1]

    #                      psum[x1][y2+1] 과 psum[x2+1][y1] 인것에 주의하자 (psum[x1][y1+1], psum[x2+1][y2]가 아니다)
    
    print(psum[x2+1][y2+1] - psum[x1][y2+1] - psum[x2+1][y1] + psum[x1][y1])
    
