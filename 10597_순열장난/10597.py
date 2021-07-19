import sys

visited = [0] * 101

n = input()
n_len = len(n)
ans = list()

# level = indicate the 'i-th' index of input 'n'
# cnt = indicate the number of number
# if n='12345678910'
# then level=n_len=11, but cnt = 10 cuz 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ----> total 10 numbers
def DFS(level,cnt):
    if level==n_len:
        for i in range(1,cnt+1):
            if visited[i]==0:
                return
        for i in ans:
            print(i, end=' ')
        exit()
        return

    f = int(n[level])
    if visited[f] == 0:
        visited[f] = 1
        ans.append(f)
        DFS(level+len(str(f)), cnt+1)
        visited[f] = 0
        ans.pop()
    
    s = int(n[level:level+2])
    if visited[s] == 0:
        visited[s] = 1
        ans.append(s)
        DFS(level+len(str(s)), cnt+1)
        visited[s]=0
        ans.pop()

    
DFS(0,0)