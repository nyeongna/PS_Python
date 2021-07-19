import sys
from collections import deque
sys.setrecursionlimit(30000)

n = int(input())
stack_list = [ deque() for _ in range(4) ]
where = 1
nums = list(map(int, input().split()))

for num in nums:
    stack_list[1].append(num)

# 정답을 기록한 배열
seq = []

for target in range(n, 0, -1):
    # 뽑아야 할 숫자가 1에 있으면 1에 있다고 기록
    if target in stack_list[1]:
        where = 1

    # 뽑아야 할 숫자가 2에 있으면 2 에 있다고 기록
    elif target in stack_list[2]:
        where = 2

    # 뽑아야 할 숫자가 나올때까지 계속 stack[where]에서 pop해서 다른쪽으로 옮김
    while len(stack_list[where]) > 0 and stack_list[where][-1] != target:
        pop = stack_list[where].pop()
        if where==1:
            stack_list[2].append(pop)
            seq.append((where, 2))
        elif where==2:
            stack_list[1].append(pop)
            seq.append((where, 1))

    # 뽑아야 할 숫자를 where -> 3으로 옮김
    stack_list[3].append(stack_list[where].pop())
    seq.append((where, 3))

        
print(len(seq))
for i in seq:
    print(i[0], i[1])
    
'''
시간 복잡도: O(n^2)
n=123 이므로 최대 123^2
'''