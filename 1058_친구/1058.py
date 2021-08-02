

n = int(input())
graph = [ list(map(str, input())) for _ in range(n) ]

visited = [ [0]*n for _ in range(n) ]

# n^3. 2-친구까지 다 검사해본다
for i in range(n):
    for j in range(n):
        if graph[i][j]=='Y':
            visited[i][j] = 1
            for k in range(n):
                if graph[j][k] == 'Y' and i != k:
                    visited[i][k] = 1

ans = float('-inf')
for i in range(n):
    sum = 0
    for j in range(n):
        if visited[i][j]==1:
            sum += 1
    ans = max(ans, sum)

print(ans)

'''시간 복잡도
O(n^3) n이 50이므로 가능
'''
