l, r = input().split()

ans = 0
# 자릿수 다르면 0 출력, 언제나 8이 없는 수를 만들어낼수 있다.
if len(l) != len(r):
    print(0)
# 자릿수 같다면
else:
    for idx in range(len(l)):
        # 제일 큰 자릿수부터 비교해서 서로 같고 8이 아니면 continue
        if l[idx] == r[idx] and l[idx] != '8':
            continue
        # 서로 같고 8이라면 ans +1
        elif l[idx] == '8' and r[idx] == '8':
            ans = ans + 1
        # 같은 자릿수 숫자가 안맞으면 break
        else:
            break
    print(ans)
