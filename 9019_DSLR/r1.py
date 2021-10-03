from collections import deque

for _ in range(int(input())):
    A, B = map(int, input().split())
    Q = deque()
    Q.append((A, 0, ""))
    visited = { A:1 }

    while len(Q) > 0:
        num, dist, order = Q.popleft()
        if num == B:
            print(order)
            break
        # D
        D_num = num*2 if num*2 <=9999 else num*2%10000
        if D_num not in visited:
            Q.append((D_num, dist+1, order+"D"))
            visited[D_num]=1
        # S
        S_num = num-1 if num > 0 else 9999
        if S_num not in visited:
            Q.append((S_num, dist+1, order+"S"))
            visited[S_num]=1
        # L
        L_num = num % 1000 * 10 + num//1000
        if L_num not in visited:
            Q.append((L_num, dist+1, order+"L"))
            visited[L_num]=1
        # R
        R_num = num%10 * 1000 + num//10
        if R_num not in visited:
            Q.append((R_num, dist+1, order+"R"))
            visited[R_num]=1
    

