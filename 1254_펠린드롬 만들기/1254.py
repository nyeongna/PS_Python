'''
핵심 알고리즘:
1. 몇개를 추가해야 할까?
- 몇 글자를 추가해야 palindrome이 되는지 확인하려면, 앞에서부터 "몇 글자"를 제거해서 palindrome을 만들 수 있는지 확인하면 된다.
- 앞에서 x개를 제거해서 나부지 부분으로 palindrome이 될수 있다면, 전체 문자열에 앞 x개를 더하면 palindrome이 완성되기 때문.

2. 펠린드롬 확인방법
- python의 [::-1] reverse 함수를 이용해서 순서대로 1~n까지 확인
- manachar 알고리즘 활용

'''

'''
e e f f e
'''
s = input()
for idx in range(len(s)):
    # palindrome 확인부분
    if s[idx:] == s[idx:][::-1]:
        print(len(s)+idx)
        exit()

