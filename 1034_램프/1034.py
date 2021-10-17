n, m = map(int, input().split())
lamp_list = list()
for _ in range(n):
    lamp_list.append(list(map(int, input())))
k = int(input())
'''
완전탐색.
1. 행마다 0의 갯수를 찾는다.
2. k의 값이 행의 0의 갯수이상이면서 0의 개수의 홀/짝과 맞아야, 해당 행을 켤 수 있다.
3. 같은 모양의 행이 몇갠지 센다.
4. 마지막에 dict 중에서 가장 많은 value 값을 출력
'''
ch = dict()
for row in lamp_list:
    #print(row)
    zeros = row.count(0)
    # k 값이 0의 갯수 이상이면서 k와 0의 개수의 홀/짝이 맞을때
    if k >= zeros and k%2 == zeros%2:
        row = tuple(row)
        if row in ch:
            ch[row] += 1
        else:
            ch[row] = 1
#print(ch)
if ch:
    print(max(ch.values()))
else:
    print(0)