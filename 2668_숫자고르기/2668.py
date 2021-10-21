import sys
sys.setrecursionlimit(30000)
n = int(input())
up_list = [i for i in range(n)]
down_list = []
for _ in range(n):
    down_list.append(int(input())-1)

'''
'i' 가 cycle을 이룰 수 있다면 정답에 속해있단 뜻이다.
'i' 가 cycle을 이룰 수 없다면 'i'를 넣고서는 up_set과 down_set이 다르다는 뜻이다.

'''

def dfs(cur, next,visited):
    if visited[next]==0:
        visited[next]=1
        return dfs(cur, down_list[next], visited)
    else:
        if cur == next:
            return 1
        else:
            return 0

ans_list = list()
for i in range(n): 
    visited = [0]*(n+1)
    if dfs(i,i,visited):
        ans_list.append(i)
print(len(ans_list))
for i in ans_list:
    print(i+1)

