'''
.split(':') 할때 ':'가 맨앞이나 뒤에 존재하면, ['', '', '1'] 이런식으로 3개생성됨을 주의
'''

n = input().split(':')
for idx in range(len(n)):
    if n[idx] != '':
        n[idx] = n[idx].zfill(4)
if len(n) < 8:
    fill_cnt = 8 - len(n)
    for _ in range(fill_cnt):
        n.insert(n.index(''),'0000')
if len(n) > 8:
    fill_cnt = len(n) - 8
    for _ in range(fill_cnt):
        n.remove('')
for i in range(8):
    if n[i]=='':
        n[i]='0000'

print(':'.join(n))

