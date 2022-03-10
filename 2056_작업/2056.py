'''
N: 3 <= N <= 10,000
각 작업의 선핵작업 갯수 : <= 100
O(1,000,000)

-'n' 번쨰 작업의 전체 시간을 구하려고 할 때 선행작업은 무조건 'n-1'만 존재하고
 'n' 번째 작업의 전체 시간을 구하려고 할 떄 'n-1' 작업들의 전체시간은 무조건 구할 수 있다 (이미 끝나있으므로)
-'n'번 쨰 작업을 구하려고 할 때 선행작업들 중 가장 늦게 끝나는 작업을 구하고 + 'n'작업의 시간을 더해주면 됨
'''

n = int(input())
work_time = [0]*(10002)
for idx in range(1, n+1, 1):
    row = list(map(int, input().split()))
    idx_time, pre_num = row[0], row[1]
    pre_list = row[2:]
    # 가장 늦게 끝나는 선행작업의 시간을 구함
    max_pre_time = 0
    for pre in pre_list:
        max_pre_time = max(max_pre_time, work_time[pre])
    # 'idx' 작업의 끝나는 시간 = 'idx'작업시간 + 선행작업 중 가장 늦게 끝나는 작업 시간
    work_time[idx] = max_pre_time + idx_time

print(max(work_time))

