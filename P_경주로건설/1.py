from collections import deque
def solution(board):
    ans = float('inf')
    n = len(board)
    
    Q = deque()
    Q.append((0, 0, 0, 4))
    visited = [ [float('inf')]*n for _ in range(n) ]
    visited[0][0] = 0
    x_dir = [-1,0,1,0]
    y_dir = [0,1,0,-1]
    
    while len(Q) > 0:
        x, y, cost, dir = Q.popleft()
        # if x==n-1 and y==n-1:
        #     ans = min(ans, cost)
        #     continue
        for i in range(4):
            dx, dy = x + x_dir[i], y + y_dir[i]
            if 0<=dx<n and 0<=dy<n and board[dx][dy]==0:
                if dir==4 and visited[dx][dy] >= cost+100:
                    visited[dx][dy] = cost+100
                    Q.append((dx,dy,cost+100, i))  
                elif dir%2 == i%2 and visited[dx][dy] >= cost+100:
                    visited[dx][dy] = cost+100
                    Q.append((dx,dy,cost+100, i))
                elif dir%2 != i%2 and visited[dx][dy] >= cost+100+500:
                    visited[dx][dy] = cost+100+500
                    Q.append((dx,dy,cost+100+500, i))
    print(visited[n-1][n-1])
    for i in visited:
        print(i)
    return ans
solution([[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0]])