'''
1. 처음에는 숫자버튼만 이용하여 최대한 target 채널에 가까워진다
2. 그 다음에는 (+, -) 버튼만을 이용하여 접근한다

num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
out = [                  6, 7  8   ]

5 6 1 0

100의 자리에서 6이 불가하여 내려갔다면, 그 다음부터는 계속 제일 큰 수를 받아야함
5 5 9 9
100의 자리에서 6이 불가하여 올라갔다면, 그 다음부터는 게속 제일 작은 수를 받아야함
5 7 2 2
100의 자리에서 6이 가능하여 그대로라면, 그 다음부터도 최대한 찾으려고 한다.
5 6 1 0

1. 중요점: 처음에는 neutral-policy, 그 후 up-policy인지, down-policy인지 결정나면 계속 따라야함.
'''

target = list(map(int,input()))
n = int(input())
num_list = [ i for i in range(10) ]
off_list = list(map(int, input().split()))

if int(''.join(list(map(str,target)))) == 100:
    print(0)
    exit()
# neutral:0, pos:1, neg:1
policy = 0

smallest_possible = 0
biggest_possible = 9
while smallest_possible in off_list:
    smallest_possible += 1
while biggest_possible in off_list:
    biggest_possible -= 1
print(smallest_possible, biggest_possible)

ans = float('inf')
order_list = list()
for idx in range(len(target)):
    if policy==0:
        if target[idx] not in off_list:
            order_list.append(str(target[idx]))
        elif target[idx] in off_list:
            num = target[idx]
            if idx==0:
                while True:
                    num = num + 1
                    for i in list(map(int, str(num))):
                        if i in off_list:
                            continue
                    break
                order_list.extend(list(map(str,str(num))))
            else:
                while num in off_list:
                    num = num + 1
                if num == 10:
                    order_list.append(float('inf'))
                    break
                else:
                    order_list.append(str(num))
            policy=1
    elif policy==1:
        order_list.append(str(smallest_possible))
ans = min(ans, len(order_list) + abs( int(''.join(list(map(str,target))  )) -int(''.join(order_list)  )))
print(order_list, ans)

order_list_2 = list()
policy = 0
for idx in range(len(target)):
    if policy==0:
        if target[idx] not in off_list:
            order_list_2.append(str(target[idx]))
        elif target[idx] in off_list:
            num = target[idx]
            if idx==0:
                while True:
                    num = num - 1
                    if num in off_list:
                        continue
                    if num == -1:
                        num = 0
                    break
                order_list_2.append(str(num))
            else:
                while num in off_list:
                    num = num - 1
                if num == -1:
                    order_list_2.append(float('inf'))
                    break
                else:
                    order_list_2.append(str(num))
            policy=2
    elif policy==2:
        order_list_2.append(str(biggest_possible))

ans = min(ans, len(order_list_2) + abs( int(''.join(list(map(str,target))  )) -int(''.join(order_list_2)  )))
print(order_list_2, ans)

if ans == float('inf'):
    print(target-100)
else:
    print(ans)