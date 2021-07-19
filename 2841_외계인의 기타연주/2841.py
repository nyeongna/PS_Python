from sys import stdin
from collections import deque

n, p = map(int, stdin.readline().rstrip().split())
graph = [ deque() for _ in range(7) ]

ans = 0
for _ in range(n):
    line, flat = map(int, stdin.readline().rstrip().split())

    # 해당 줄에 이미 플랫에 손이 있고 AND 음에 해당하는 플랫보다 큰 숫자가 나오면 계속 뺀다. 빼면서 손가락 움직임 +1
    while len(graph[line]) > 0 and graph[line][-1] > flat:
        graph[line].pop()
        ans = ans + 1
    # 해당 줄에 이미 플랫에 손이 있고 AND 해당 줄의 제일 높은 플랫이 치려는 플랫이면 아무 손가락 움직임 없이 continue
    if len(graph[line]) > 0 and graph[line][-1] == flat:
        continue
    # 치려는 플랫을 치고 queue에 넣고 손가락 움직임 +1
    graph[line].append(flat)
    ans = ans+1

print(ans)


