import sys
n = int(input())
num_list = list()
for _ in range(n):
    num_list.append(float(input()))

for i in range(1, sys.maxsize, 1):
    flag = 1
    for num in num_list:
        if num*i != int(num*i):
            flag = 0
            break
    if flag==1:
        print(i)
        exit()
    