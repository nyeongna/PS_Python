n, k = map(int, input().split())
num_list = list(map(int,input()))
idx=0
ans_list = list()
time = 0
while k != 0:
    max_num = max(num_list[idx:idx+k+1])
    max_idx = num_list[idx:idx+k+1].index(max_num) + idx
    #print(num_list[idx:idx+k+1], num_list[idx:idx+k+1].index(max_num) )
    ans_list.append(max_num)
    k = k - (max_idx - idx)
    idx = max_idx+1
    #print(max_num, max_idx, idx, ans_list, k)

ans_list.extend( num_list[idx:] )
#print(ans_list)
print(''.join(list(map(str,ans_list))))
#print(''.join(ans_list))