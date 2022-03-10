num, e, w, s, n = map(int, input().split())
e,w,s,n = e/100, w/100, s/100, n/100
prob_list = [n,e,s,w]
'''
4^14 = 2억 6천...1초 통과 가능..?!
'''

visited =  [ [0]*100 for _ in range(100) ]
visited[15][15]=1
ans=0
x_dir=[-1,0,1,0]
y_dir=[0,1,0,-1]

def dfs(x,y,level, prob):
    global ans, visited
    if level==num:
        ans = ans + prob
        return
        
    for i in range(4):
        dx = x + x_dir[i]
        dy = y + y_dir[i]
        if visited[dx][dy]==0:
            visited[dx][dy]=1
            dfs(dx, dy, level+1, prob * prob_list[i])
            visited[dx][dy]=0

dfs(15,15,0, 1)
print(ans)