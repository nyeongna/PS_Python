n, m, k = map(int, input().split())
graph = [ list(map(int,input().split())) for _ in range(n) ]
'''
-행은 round마다 [n-round-1] 이하까지
-열은 round마다 [m-round-1] 이하까지
-다음 라운드는 'min(m,n) // 2' 번
-반시계방향의 반대인 시계방향순으로 역으로 업데이트 해주면 또다른 tmp 배열 만들필요 X

1 1
1 1

1 1 1
1 1 1
1 1 1

1 1 1 1
1 1 1 1
1 1 1 1
1 1 1 1

1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1

1 1 1 1 1 1
1 1 1 1 1 1
1 1 1 1 1 1
1 1 1 1 1 1
1 1 1 1 1 1 

1 1 1 1 1 1 1
1 1 1 1 1 1 1
1 1 1 1 1 1 1
1 1 1 1 1 1 1
1 1 1 1 1 1 1
1 1 1 1 1 1 1

1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1

2:1
3:1
4:2
5:2
6:3
7:3
8:4
1000 * 90000
'''
import copy
for kk in range(k):
    for round in range(min(m,n)//2):
        n_max = n-round-1
        m_max = m-round-1
        store = graph[round][round]
        # 윗변 [오른쪽 -> 왼쪽]으로 꼴고옴
        for i in range(round, m_max):
            graph[round][i] = graph[round][i+1]

        # 오른쪽변 [밑쪽 -> 위쪽] 으로 끌고옴
        for i in range(round, n_max):
            graph[i][m_max] = graph[i+1][m_max]

        # 밑변 [오른쪽 -> 왼쪽] 으로 끌고옴
        for i in range(m_max, round, -1):
            graph[n_max][i] = graph[n_max][i-1]

        # 왼변 [위쪽 -> 아랫쪽] 으로 끌고옴
        for i in range(n_max,round,-1):
            graph[i][round] = graph[i-1][round]
        graph[round+1][round] = store

for i in graph:
    print(*i)