from collections import deque
s = input()
pattern = input()
target = pattern[-1]

res = list()
for idx,ch in enumerate(s):
    # 먼저 정답 list에 문자 추가
    res.append(ch)
    # 만약 현재 문자가 pattern의 마지막 문자라면
    if ch==target:
        # 정답 list의 마지막 문자열들이 pattern과 같다면 pattern 길이만큼 pop
        if ''.join(res[-len(pattern):]) == pattern:
            for _ in range(len(pattern)):
                res.pop()
if len(res)==0:
    print("FRULA")
else:
    print(''.join(res))
