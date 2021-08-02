from collections import deque
t = int(input())

# 에라토스테네스의 체
# O(Nlog(logN))
prime_list = [0]*10000
for i in range(2, 10000, 1):
    if prime_list[i] == 0:
        for j in range(i+i, 10000, i):
            prime_list[j] = 1

# t만큼 반복
for _ in range(t):
    A, B = map(int, input().split())
    Q = deque()
    Q.append((A,0 ))
    visited = [0]*10000
    visited[A] = 1
    
    flag=0
    # BFS를 통해 최소 거리를 구한다
    while len(Q) > 0:
        num, dist = Q.popleft()
        if num==B:
            print(dist)
            #print(route)
            flag=1
            break
        # pos 는 자릿수, pos=0이면 천의자리, pos=1이면 백의자리, ...
        for pos in range(4):
            str_num = list(map(str, str(num)))
            for i in range(0, 10, 1):
                str_num[pos] = str(i)
                d1 = int(''.join(str_num))
                if visited[d1]==0 and prime_list[d1]==0 and 1000 <= d1 <= 9999:
                    visited[d1]=1
                    Q.append((d1,dist+1 ))
    if flag == 0:
        print('Impossible')
            
'''
시간복잡도 10,000 * 40 = 400,000  통과
'''