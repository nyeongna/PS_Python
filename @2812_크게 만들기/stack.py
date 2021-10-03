from collections import deque
from sys import stdin
n, k = map(int, input().split())
num_list = list(map(int, stdin.readline().strip()))
kk = k
dQ = deque()

# k개를 무조건 뺴야하므로, 어떻게 정답을 도출해도 자리수는 같다
# 따라서 앞에서부터 가장 큰 수만 넣어서 greedy하게 구한다

for i in range(n):
    # stack[-1] 보다 크면 pop 해준다
    # stack[-1] 보다 작으면 append 해준다
    while len(dQ) > 0 and k != 0:
        if dQ[-1] < num_list[i]:
            dQ.pop()
            k -= 1
        else:
            break
    dQ.append(num_list[i])

for num in range(n-kk):
    print(dQ[num],end='')
        