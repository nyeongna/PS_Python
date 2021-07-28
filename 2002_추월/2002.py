from collections import deque

n, enter, exited= int(input()), deque(), deque()

for _ in range(n):
    enter.append(input())
for _ in range(n):
    exited.append(input())

ans = 0
alr_left_list = []
target = enter.popleft()

for idx in range(n):
    out = exited.popleft()
    # 현재 나와야할 차가 아니면 ans+1 하고 이미 나온 차 리스트에 추가
    if out != target:
        ans = ans + 1
        alr_left_list.append(out)
    # 현재 나와야할 차라면
    else:
        # 다음 나와야할 차로 target을 바꿔줌
        if len(enter) > 0:
            target = enter.popleft()
        # 다음 나와야 할 차가 이미 나왔다면 나음 나와야할 차로 바꿔줌
        while len(enter) > 0 and target in alr_left_list:
            target = enter.popleft()
        
print(ans)
