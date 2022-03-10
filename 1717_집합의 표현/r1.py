from sys import stdin
import sys
sys.setrecursionlimit(1000000)
'''
집합끼리 합집합을 계속 해야함..
같은 set에 속해있는지 보기위해서는 union & find 가 속도최적화
-dict 로 구현하면 합집합 할 때마다 cost가 너무 큼
'''
n, m = map(int, input().split())
parent=[ i for i in range(n+1) ]

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
        return parent[x]
    return x

def union(a,b):
    aa = find(a)
    bb = find(b)
    if aa!=bb:
        parent[aa]=bb
        
for _ in range(m):
    op, a, b = map(int, stdin.readline().strip().split())
    if op==0:
        union(a,b)
    elif op==1:
        a = find(a)
        b = find(b)
        if a==b:
            print('YES')
        else:
            print('NO')