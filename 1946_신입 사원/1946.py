from sys import stdin

t = int(input())
for _ in range(t):
    n = int(input())
    cand = list()
    cand.append((0,0))
    for _ in range(n):
        a, b = map(int, stdin.readline().strip().split())
        cand.append((a,b))
    a_list, b_list = sorted(cand, key=lambda x:x[0]), sorted(cand, key=lambda x:x[1])
    a_visited, b_visited = [0]*(n+1), [0]*(n+1)
    a_visited[0], b_visited[0] = 1, 1
    ans = 0
    for a, b in a_list:
        if a_visited[a]==0:
            a_visited[a] = 1
            ans = ans + 1
            for i in range(b, n+1, 1):
                if b_visited[i]==1:
                    break
                b_visited[i]=1
                a_visited[b_list[i][0]]=1
    print(ans)
            
                
    