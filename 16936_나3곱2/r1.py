'''
42: 84, 14
28: 56, X
84: 168, 28
126: 256, 42
'''

n = int(input())
num_list = list(map(int, input().split()))
d = dict()
for num in num_list:
    a = num*2
    b = num//3 if num%3==0 else None
    if num in d:
        d[num][0] += 1
    else:
        d[num] = [1,a,b]

# for key, val in d.items():
#     print(key, val)
rec = [0]*(n)
def dfs(num, level):
    if level==n:
        print(*rec)
        exit()
    # 리스트에 없는 숫자면 return
    if num not in d:
        return
    cnt, a, b = d[num]
    # 이미 쓰여진 숫자면 return
    if cnt == 0:
        return
        
    # 현재 숫자 level에 기록
    rec[level] = num
    d[num][0] -= 1
    for next in [a,b]:
        dfs(next, level+1)
    d[num][0] += 1
    rec[level] = 0

for start in num_list:
    dfs(start, 0)

