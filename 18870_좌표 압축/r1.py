n = int(input())
num_list = list(map(int, input().split()))
set_list = sorted(list(set(num_list)))
order_dict = dict()

for idx,num in enumerate(set_list):
    order_dict[num]=idx
for num in num_list:
    print(order_dict[num], end=' ')