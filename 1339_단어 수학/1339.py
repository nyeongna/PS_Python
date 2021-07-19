#-*-coding:utf-8 -*-
import sys

n = int(input())
graph = [ list(map(str,input())) for _ in range(n) ]
visited = [0] * 10
alpha = [0] * 100
ans = 0

# 사용된 unique한 알파벳이 들어갈 리스트
num_list = list()

for i in graph:
    for j in i:
        if j not in num_list:
            num_list.append(j)

# unique한 알파벳의 갯수
nn = len(num_list)

def DFS(level):
    global ans
    # 만약 모든 알파벳에 0~9까지 숫자가 assgin됐으면 ans값을 갱신할지 말지 검사한다.
    if level==nn:
        total=0
        # 이렇게 numm*10 + alpha[ord(j)] 방식으로해야 time out이 안걸린다
        # numm = numm + alpha[ord(j)] 를 string 방식으로 처리하면 O(M+N)이므로 time out이 걸린다.
        for i in graph:
            numm= 0
            for j in i:
                numm= numm*10 + alpha[ord(j)]
            total = total + numm
        if total > ans:
            ans = total
        return

    for i in range(9,-1,-1):
        if visited[i]==0:
            visited[i]=1
            alpha[ord(num_list[level])] = i
            DFS(level+1)
            visited[i]=0
            alpha[ord(num_list[level])] = 0
            
DFS(0)
print(ans)
