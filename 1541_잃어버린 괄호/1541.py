
num = input()

'''
핵심 포인트
첫번쨰 (-)를 만나기 전까진 모두 더해야하고,
첫번쨰 (-)를 만난 이후는 모두 뺄 수 있다. (괄호를 적절히 넣으면 모두 빼기 가능)
'''
minus_split = num.split('-')
sum=0
# 첫번쨰 (-)를 만나기 전까진 모두 더해야하고,
for num in minus_split[0].split('+'):
    sum = sum + int(num)

# 첫번쨰 (-)를 만난 이후는 모두 뺄 수 있다.
for minus in minus_split[1:]:
    for num in minus.split('+'):
        sum = sum - int(num)
print(sum)