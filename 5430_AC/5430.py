from collections import deque

for _ in range(int(input())):
    function = input()
    n = int(input())
    num_list = deque(input()[1:-1].split(','))

    # 어차피 앞뒤로만 짤라낸다
    idx = 0
    for ch in function:
        error = 0
        # R때는 방향만 바꿔준다
        if ch=='R':
            idx = 1 if idx==0 else 0
        elif ch=='D':
            # 배열 길이가 0이거나, 맨첫번쨰 원소가 ''이면(즉 처음 받은 배열이 '[]' 라면 error)
            if len(num_list) <= 0 or num_list[0]=='':
                print('error')
                error=1
                break
            else:
                # 처음원소 없애거나
                if idx==0:
                    num_list.popleft()
                # 뒤에 원소 없앰
                elif idx==1:
                    num_list.pop()
    if error==0:
        # 정방향 출력
        if idx==0:
            print('['+','.join(num_list)+']')
        # 거꾸로 출력
        else:
            print('['+','.join(list(num_list)[::-1])+']')


    