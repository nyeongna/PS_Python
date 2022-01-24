'''
어려운 수학문제..
'''

import math
n=int(input())
num_list = [ int(input()) for _ in range(n) ]
num_list = sorted(num_list)

# i+1 - i 숫자 리스트를 다 뽑아내서 gcd를 찾는다
gcd = num_list[1] - num_list[0]
minus_list = list()
for i in range(2, len(num_list)):
    gcd = math.gcd(gcd, num_list[i]-num_list[i-1])

# gcd로 나눴을 때 나머지가 같다면, gcd의 약수로 나눠도 나머지가 같다
ans_list = list([gcd])
for i in range(2, int(math.sqrt(gcd))+1, 1):
    if gcd % i == 0:
        ans_list.append(gcd//i)
        ans_list.append(i)
ans_list = sorted(list(set(ans_list)))
print(*ans_list, sep=' ')



