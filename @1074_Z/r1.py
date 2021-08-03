n, r, c = map(int, input().split())



cnt = 0

def dfs(x, y, size):
    global cnt
    if size==1:
        if x==r and y==c:
            print(cnt)
            exit()
        cnt = cnt + 1
        return
    n_size = size//2
    if x <= r < x + size and y <= c < y + size:
        dfs(x, y, n_size)
        dfs(x, y+n_size, n_size)
        dfs(x+n_size, y, n_size)
        dfs(x+n_size, y+n_size, n_size)
    else:
        cnt = cnt + size*size

dfs(0, 0, 2**n)