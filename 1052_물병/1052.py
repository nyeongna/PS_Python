from sys import stdin

n, k = map(int, input().split())

def num_to_bin(num):
    return list(map(int, bin(num)[2:]))

# n을 binary list 형식으로 바꿔줌    
bin_n = num_to_bin(n)

# 현재 가지고 있는 물병을 다 합치면 필요한 물병의 갯수
num_bottles = bin_n.count(1)
if k>=num_bottles:
    print(0)
    exit()

# idxK 에는 기준점이 되는 물병 liter의 idx가 들어감
idxK = 0
for idx, num in enumerate(bin_n):
    if num==1:
        idxK = idxK+ 1
    if idxK == k:
        idxK = idx
        break
# 총 필요한 물병 liter
requireK = 2**(len(bin_n)-1-idxK)

# 기준이 되는 물병 말고 현재 가지고 있는 물병 liter
alreadyHave=0
for i in range(idxK+1, len(bin_n), 1):
    if bin_n[i] == 1:
        alreadyHave = alreadyHave + 2**(len(bin_n)-1-i)

# 총 필요한 물병 liter 에서 현재 가지고 있는 물병 liter 빼면
# '새로 사야하는 물병의 갯수'가 나옴
ans = requireK - alreadyHave
print(ans)



