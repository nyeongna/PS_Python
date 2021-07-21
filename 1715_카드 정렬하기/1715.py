import sys

n = int(input())
card_list = sorted( [ int(input()) for _ in range(n) ] )
ans = 0
for idx, num in enumerate(card_list):
    if idx <= 1:
        ans = ans + num
    else:
        ans = ans + card_list[idx-2] + card_list[idx-1] + num
print(ans)

