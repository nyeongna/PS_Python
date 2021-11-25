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
        return
    cnt, a, b = d[num]
    for next in [a,b]:
        if (next!= None) and (next in d) and (d[next][0]>0):
            rec[level] = next
            d[next][0] -= 1
            dfs(next, level+1)
            d[next][0] += 1
            rec[level] = 0

for start in num_list:
    rec[0]=start
    d[start][0] -= 1
    dfs(start, 1)
    d[start][0] += 1

