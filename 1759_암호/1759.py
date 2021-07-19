import sys
sys.setrecursionlimit(1000000)

l, c = map(int, input().split())
seq = input().split()
seq = sorted(seq)

rec = [0] * l
ch = ['a', 'e', 'i', 'o', 'u']
def DFS(s, level):
    if level==l:
        m=0
        j=0
        for i in rec:
            if i in ch:
                m=m+1
            else:
                j=j+1
        if m and j>=2:
            print(''.join(rec))
        return
    for i in range(s, c, 1):
        rec[level] = seq[i]
        DFS(i+1, level+1)
DFS(0,0)

