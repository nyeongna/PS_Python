#-*-coding:utf-8 -*-
import sys

n = int(input())
graph = [ list(map(str,input())) for _ in range(n) ]
visited = [0] * 10
alpha = [0] * 100
ans = 0

# ���� unique�� ���ĺ��� �� ����Ʈ
num_list = list()

for i in graph:
    for j in i:
        if j not in num_list:
            num_list.append(j)

# unique�� ���ĺ��� ����
nn = len(num_list)

def DFS(level):
    global ans
    # ���� ��� ���ĺ��� 0~9���� ���ڰ� assgin������ ans���� �������� ���� �˻��Ѵ�.
    if level==nn:
        total=0
        # �̷��� numm*10 + alpha[ord(j)] ��������ؾ� time out�� �Ȱɸ���
        # numm = numm + alpha[ord(j)] �� string ������� ó���ϸ� O(M+N)�̹Ƿ� time out�� �ɸ���.
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
